"""Offline source/archive checks; run after building to check published assets too."""
from pathlib import Path
import hashlib
import json
import re
import zipfile
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SIMPLE_TYPES = {'note', 'archive', 'web', 'github', 'panelnote', 'paneltalk',
                'panelvideo', 'podcast', 'talk', 'lab', 'tutorial', 'notebook',
                'whiteboard', 'quiz'}


def main():
    manifest = json.loads((ROOT / 'exams/manifest.json').read_text())['documents']
    assert len(manifest) == 63
    assert len({d['local_path'] for d in manifest}) == 63
    assert {d['year'] for d in manifest} == set(range(2020, 2026))
    for doc in manifest:
        data = (ROOT / doc['local_path']).read_bytes()
        assert data.startswith(b'%PDF-'), doc['local_path']
        assert len(data) == doc['size'], doc['local_path']
        assert hashlib.sha256(data).hexdigest() == doc['sha256'], doc['local_path']
    coverage = json.loads((ROOT / 'exams/coverage.json').read_text())['questions']
    assert len(coverage) == 176
    for q in coverage:
        assert (ROOT / q['paper']).is_file()
        assert (ROOT / q['marking_scheme']).is_file()
        assert q['course_topics'] and all(1 <= t <= 16 for t in q['course_topics'])
    topics = sorted(ROOT.glob('topic-*'))
    assert len(topics) == 17, [p.name for p in topics]
    quiz_count = question_count = 0
    for topic in topics[:16]:
        assert (topic / 'topic.md').is_file(), topic
        assert list(topic.glob('note-01-*/*.md')), topic
        assert list(topic.glob('book-*/*.md')), f'{topic}: use book-* folders for reader-compatible labs'
        assert list(topic.glob('talk-*/*.marp')), topic
        route_panels = list(topic.glob('panelnote-*/*.md'))
        assert any(all(f'/{kind}/lc-cs/{topic.name}/' in p.read_text()
                       for kind in ('note', 'lab', 'quiz')) for p in route_panels), f'{topic}: missing visible study route'
        sequence = ['note-01-*', 'book-01-practice', 'quiz-01-check',
                    'note-02-feedback', 'note-03-exam-practice', 'talk-01-recap']
        for order, pattern in enumerate(sequence, 1):
            resource = next(topic.glob(pattern))
            metadata = sorted(resource.glob('*.md'))[0].read_text()
            assert metadata.startswith(f'---\norder: {order}\n---\n'), f'{resource}: missing study-route card order'
        for p in topic.glob('quiz-*/*.md'):
            text = p.read_text()
            assert f'/note/lc-cs/{topic.name}/note-02-feedback' in text, f'{p}: missing answer explanations link'
            assert len(re.findall(r'^`{3,}quiz\s*$', text, re.M)) == 1, p
            fence = re.search(r'^(`{3,})quiz\s*\n(.*?)^\1\s*$', text, re.M | re.S)
            assert fence, p
            blocks = re.findall(r'^question:.*?(?=^---\s*$|\Z)', fence[2], re.M | re.S)
            assert len(blocks) >= 8, p
            for block in blocks:
                answer = re.search(r'^correct:\s*(.+)$', block, re.M)
                assert answer, (p, block)
                if 'type: true-false' in block:
                    assert answer[1].strip().lower() in ('true', 'false', '0', '1'), p
                else:
                    options = re.findall(r'^\s+-\s+\S', block, re.M)
                    assert len(options) >= 2 and 0 <= int(answer[1]) < len(options), p
            quiz_count += 1
            question_count += len(blocks)
    for p in ROOT.glob('topic-*/notebook-*/*.ipynb'):
        notebook = json.loads(p.read_text())
        assert notebook['nbformat'] == 4
        env = {}
        for cell in notebook['cells']:
            if cell['cell_type'] == 'code':
                exec(compile(''.join(cell['source']), str(p), 'exec'), env)
    for p in ROOT.glob('topic-*/whiteboard-*/*.excalidraw'):
        board = json.loads(p.read_text())
        assert board['type'] == 'excalidraw' and board['elements'], p
    for p in ROOT.glob('topic-*/archive-*/*.zip'):
        with zipfile.ZipFile(p) as archive:
            assert archive.testzip() is None and archive.namelist(), p
            for name in archive.namelist():
                source = ROOT / name
                if name.startswith('code/'):
                    assert source.is_file() and archive.read(name) == source.read_bytes(), f'Stale practical download: {name}'
            for notebook_name in ('representation', 'simulation'):
                source = next(ROOT.glob(f'topic-*/notebook-*/{notebook_name}.ipynb'))
                assert archive.read(f'notebooks/{notebook_name}.ipynb') == source.read_bytes(), f'Stale notebook download: {notebook_name}'
    for p in ROOT.glob('topic-*/book-*/assets/*.zip'):
        with zipfile.ZipFile(p) as archive:
            assert archive.testzip() is None and archive.namelist(), p
            for name in archive.namelist():
                source = p.parent / name
                if name.endswith('.ipynb'):
                    source = next(p.parents[2].glob(f'notebook-*/{name}'))
                assert source.is_file() and archive.read(name) == source.read_bytes(), f'Stale starter pack: {p}/{name}'
    # Follow course-owned links without relying on an external site or a cached browser tab.
    for p in [ROOT / 'course.md', *ROOT.glob('panelnote-*/*.md'),
              *ROOT.glob('topic-*/**/*.md'), *ROOT.glob('side-reference/**/*.md')]:
        source_text = p.read_text()
        targets = re.findall(r'\]\((https?://[^\s)]+)\)', source_text)
        targets += re.findall(r'<a\s+href="(https?://[^"]+)"', source_text)
        assert not re.search(r'\]\(https://tutors\.dev/', source_text), f'{p}: internal Markdown links open a new tab; use an HTML anchor'
        for target in targets:
            url = urlsplit(target)
            parts = unquote(url.path).strip('/').split('/')
            if url.netloc == 'tutors.dev' and len(parts) >= 2 and parts[1] == 'lc-cs':
                if parts[0] == 'course':
                    continue
                source = ROOT.joinpath(*parts[2:])
                if parts[0] == 'lab' and not source.is_dir():
                    assert list(source.parent.glob(f'*.{source.name}.md')), (p, target)
                else:
                    assert source.is_dir(), (p, target)
            elif url.netloc == 'lc-cs.netlify.app':
                assert ROOT.joinpath(*parts).is_file(), (p, target)
            elif url.netloc == 'raw.githubusercontent.com' and parts[:3] == ['jouwdan', 'lc-cs', 'main']:
                assert ROOT.joinpath(*parts[3:]).is_file(), (p, target)
            elif url.netloc == 'github.com' and parts[:2] == ['jouwdan', 'lc-cs'] and len(parts) > 3 and parts[2] in ('blob', 'tree') and parts[3] == 'main':
                assert ROOT.joinpath(*parts[4:]).exists(), (p, target)
    if (ROOT / 'json/tutors.json').exists():
        course = json.loads((ROOT / 'json/tutors.json').read_text())
        nodes = []
        def walk(lo):
            nodes.append(lo)
            for child in lo.get('los', []):
                walk(child)
        walk(course)
        types = {lo['type'] for lo in nodes}
        assert SIMPLE_TYPES <= types, SIMPLE_TYPES - types
        assert all(lo.get('title', '').strip() for lo in nodes)
        card_types = {'topic', 'lab', 'note', 'web', 'github', 'archive',
                      'notebook', 'whiteboard', 'quiz', 'talk', 'tutorial'}
        for lo in nodes:
            if lo['type'] in card_types:
                assert len(lo['title'].strip()) <= 28, f'Card title too long: {lo["route"]}'
                assert len(lo.get('summary', '').strip()) <= 45, f'Card description too long: {lo["route"]}'
        for lo in nodes:
            if lo['type'] == 'lab':
                assert lo['id'].startswith('book-'), f"Reader requires a book-* lab root: {lo['route']}"
            if lo['type'] == 'topic' and lo['id'] != 'topic-17-past-papers':
                ordered = sorted((child for child in lo['los'] if 'order' in child.get('frontMatter', {})),
                                 key=lambda child: child['frontMatter']['order'])
                assert [child['frontMatter']['order'] for child in ordered] == list(range(1, 7)), lo['id']
                assert [child['title'].strip()[:2] for child in ordered] == [f'{n}.' for n in range(1, 7)], lo['id']
        internal = [lo['route'] for lo in nodes if lo['type'] not in {'unit', 'side', 'web', 'github'}]
        assert len(internal) == len(set(internal)), 'Duplicate navigable routes'
        assert sum(lo['type'] == 'quiz' for lo in nodes) == quiz_count
        for doc in manifest:
            assert (ROOT / 'json' / doc['local_path']).read_bytes() == (ROOT / doc['local_path']).read_bytes()
        print(f'Built course: {len(nodes)} objects/steps; all 14 simple object types present')
    print(f'PASS: {len(manifest)} PDFs, {len(coverage)} question groups, {quiz_count} quizzes/{question_count} questions')


if __name__ == '__main__':
    main()
