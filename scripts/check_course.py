"""Offline source/archive checks; run after building to check published assets too."""
from pathlib import Path
import hashlib
import json
import re
import zipfile

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
        assert list(topic.glob('lab-*/*.md')), topic
        assert list(topic.glob('talk-*/*.marp')), topic
        for p in topic.glob('quiz-*/*.md'):
            text = p.read_text()
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
        internal = [lo['route'] for lo in nodes if lo['type'] not in {'unit', 'side', 'web', 'github'}]
        assert len(internal) == len(set(internal)), 'Duplicate navigable routes'
        assert sum(lo['type'] == 'quiz' for lo in nodes) == quiz_count
        for doc in manifest:
            assert (ROOT / 'json' / doc['local_path']).read_bytes() == (ROOT / doc['local_path']).read_bytes()
        print(f'Built course: {len(nodes)} objects/steps; all 14 simple object types present')
    print(f'PASS: {len(manifest)} PDFs, {len(coverage)} question groups, {quiz_count} quizzes/{question_count} questions')


if __name__ == '__main__':
    main()
