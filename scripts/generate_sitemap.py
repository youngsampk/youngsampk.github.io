#!/usr/bin/env python3
"""
Generate sitemap.xml for a static site based on an input directory (e.g. `docs/`).
Usage:
  python scripts/generate_sitemap.py --site-url https://example.com --input-dir docs --output docs/sitemap.xml
"""
import os
import argparse
from datetime import datetime

def iso_date(ts):
    return datetime.utcfromtimestamp(ts).date().isoformat()

parser = argparse.ArgumentParser()
parser.add_argument("--site-url", required=True)
parser.add_argument("--input-dir", default="docs")
parser.add_argument("--output", default="docs/sitemap.xml")
parser.add_argument("--exclude", nargs="*", default=["sitemap.xml", "feed.xml"])
args = parser.parse_args()

site_url = args.site_url.rstrip('/')
input_dir = args.input_dir
output = args.output
exclude = set(args.exclude)

# site_libs 등 라이브러리 디렉토리는 탐색에서 제외
SKIP_DIRS = {'site_libs'}

urls = []
for root, dirs, files in os.walk(input_dir):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for f in files:
        if not f.lower().endswith('.html'):
            continue
        rel = os.path.relpath(os.path.join(root, f), input_dir).replace('\\', '/')
        if rel in exclude:
            continue
        # index.html -> canonical trailing slash
        if rel == 'index.html':
            loc = site_url + '/'
        elif rel.endswith('/index.html'):
            loc = site_url + '/' + rel[:-len('index.html')]
        else:
            loc = site_url + '/' + rel
        path = os.path.join(root, f)
        lastmod = iso_date(os.path.getmtime(path))
        urls.append((loc, lastmod))

# 중복 제거 후 정렬
seen = set()
unique_urls = []
for loc, lastmod in sorted(urls):
    if loc not in seen:
        seen.add(loc)
        unique_urls.append((loc, lastmod))

lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for loc, lastmod in unique_urls:
    lines.append('  <url>')
    lines.append(f'    <loc>{loc}</loc>')
    lines.append(f'    <lastmod>{lastmod}</lastmod>')
    lines.append('  </url>')
lines.append('</urlset>')

out_dir = os.path.dirname(output)
if out_dir:
    os.makedirs(out_dir, exist_ok=True)
with open(output, 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines))

print(f'Wrote sitemap with {len(unique_urls)} entries to {output}')
