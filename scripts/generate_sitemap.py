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

urls = []
for root, dirs, files in os.walk(input_dir):
    for f in files:
        if not f.lower().endswith('.html'):
            continue
        rel = os.path.relpath(os.path.join(root, f), input_dir).replace('\\', '/')
        if rel in exclude:
            continue
        # skip index.html at top-level mapping to root
        loc = site_url + '/' + rel
        path = os.path.join(root, f)
        lastmod = iso_date(os.path.getmtime(path))
        urls.append((loc, lastmod))

# sort URLs to keep output stable
urls.sort()

xml = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for loc, lastmod in urls:
    xml.append('  <url>')
    xml.append(f'    <loc>{loc}</loc>')
    xml.append(f'    <lastmod>{lastmod}</lastmod>')
    xml.append('  </url>')
xml.append('</urlset>')

os.makedirs(os.path.dirname(output), exist_ok=True)
with open(output, 'w', encoding='utf-8') as f:
    f.write('\n'.join(xml))

print(f'Wrote sitemap with {len(urls)} entries to {output}')
