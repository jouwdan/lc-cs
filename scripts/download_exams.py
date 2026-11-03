#!/usr/bin/env python3
"""Download every document listed by Better Exams for LC Computer Science 2020–2025."""
import argparse
import hashlib
import json
import time
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen

BASE = 'https://www.betterexams.ie'
EXPECTED = {2020: 5, 2021: 12, 2022: 12, 2023: 12, 2024: 11, 2025: 11}
ROOT = Path(__file__).resolve().parents[1]

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.current = None
    def handle_starttag(self, tag, attrs):
        href = dict(attrs).get('href', '')
        if tag == 'a' and href.endswith('.pdf'):
            self.current = [href, '']
    def handle_data(self, text):
        if self.current is not None:
            self.current[1] += text
    def handle_endtag(self, tag):
        if tag == 'a' and self.current is not None:
            self.links.append(self.current)
            self.current = None

def fetch(url):
    for attempt in range(4):
        try:
            with urlopen(Request(url, headers={'User-Agent': 'LC-CS-Educational-Archive/1.0'}), timeout=60) as response:
                return response.read()
        except Exception:
            if attempt == 3:
                raise
            time.sleep(attempt + 1)

def download(row):
    path = ROOT / row['local_path']
    data = path.read_bytes() if path.exists() else fetch(row['url'])
    if not data.startswith(b'%PDF-'):
        raise ValueError(f"Not a PDF: {row['url']}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    row.update(sha256=hashlib.sha256(data).hexdigest(), size=len(data))
    return row

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--evidence-dir', type=Path)
    args = parser.parse_args()
    previous_path = ROOT / 'exams/manifest.json'
    previous = json.loads(previous_path.read_text()) if previous_path.exists() else {}
    old_documents = {row['url']: row for row in previous.get('documents', [])}
    rows = []
    for year, expected in EXPECTED.items():
        landing = f'{BASE}/leaving-cert/computer-science/{year}'
        html = fetch(landing)
        if args.evidence_dir:
            args.evidence_dir.mkdir(parents=True, exist_ok=True)
            (args.evidence_dir / f'listing-{year}.html').write_bytes(html)
        links = Links()
        links.feed(html.decode())
        if len(links.links) != expected:
            raise ValueError(f'{year}: expected {expected} documents, found {len(links.links)}; inspect the source listing')
        for href, label in links.links:
            stem = Path(href).stem
            kind = 'marking-scheme' if '/marking-schemes/' in href else 'exam-paper'
            rows.append(dict(year=year, level='Higher' if 'higher-level' in stem else 'Ordinary',
                language='English' if stem.endswith('-ev') else 'Irish',
                language_code='EV' if stem.endswith('-ev') else 'IV',
                section='A and B' if 'section-aandb' in stem else 'C' if 'section-c' in stem else 'All',
                kind=kind, title=' '.join(label.split()), url=urljoin(BASE, href), landing_page=landing,
                local_path=f'topic-17-past-papers/unit-{year}/tutorial-{kind}-{stem}/{kind}-{stem}.pdf'))
    assert len(rows) == 63 and len({row['url'] for row in rows}) == 63
    with ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(download, rows))
    for row in rows:
        old = old_documents.get(row['url'])
        if old and old['sha256'] != row['sha256']:
            raise ValueError(f"Archived content changed: {row['local_path']}; inspect before updating provenance")
        if old and 'pages' in old:
            row['pages'] = old['pages']
    manifest = {'source': f'{BASE}/leaving-cert/computer-science',
        'retrieved': previous.get('retrieved', '2026-11-03'), 'scope': 'Every PDF listed for 2020–2025, all available levels and languages',
        'documents': rows}
    (ROOT / 'exams').mkdir(exist_ok=True)
    (ROOT / 'exams/manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(f'Verified {len(rows)} PDFs, {sum(r["size"] for r in rows):,} bytes')

if __name__ == '__main__':
    main()
