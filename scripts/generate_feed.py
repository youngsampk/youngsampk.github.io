#!/usr/bin/env python3
"""
Generate a simple RSS 2.0 feed from generated HTML files under `docs/posts`.
Usage:
  python scripts/generate_feed.py --site-url https://example.com --input-dir docs/posts --output docs/feed.xml --max-items 20

The script looks for `index.html` files in subfolders, extracts <title> or <h1> as title, uses file mtime for pubDate, and pulls a short description from meta[name=description] or first <p>.
"""
import os
import argparse
import re
import email.utils

parser = argparse.ArgumentParser()
parser.add_argument("--site-url", required=True)
parser.add_argument("--input-dir", default="docs/posts")
parser.add_argument("--output", default="docs/feed.xml")
parser.add_argument("--max-items", type=int, default=20)
args = parser.parse_args()

site_url = args.site_url.rstrip('/')
input_dir = args.input_dir
output = args.output
max_items = args.max_items

entries = []

title_re = re.compile(r'<title>(.*?)</title>', re.I|re.S)
meta_desc_re = re.compile(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', re.I)
h1_re = re.compile(r'<h1[^>]*>(.*?)</h1>', re.I|re.S)
first_p_re = re.compile(r'<p[^>]*>(.*?)</p>', re.I|re.S)

for root, dirs, files in os.walk(input_dir):
    if 'index.html' not in files:
        continue
    path = os.path.join(root, 'index.html')
    rel = os.path.relpath(path, 'docs').replace('\\', '/') if path.startswith('docs') else os.path.relpath(path, input_dir).replace('\\', '/')
    url_path = os.path.relpath(path, 'docs').replace('\\', '/') if path.startswith('docs') else os.path.relpath(path, input_dir).replace('\\', '/')
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    title = None
    m = title_re.search(txt)
    if m:
        title = re.sub(r'\s+', ' ', m.group(1)).strip()
    if not title:
        m = h1_re.search(txt)
        if m:
            title = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    desc = None
    m = meta_desc_re.search(txt)
    if m:
        desc = m.group(1).strip()
    if not desc:
        m = first_p_re.search(txt)
        if m:
            desc = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    mtime = os.path.getmtime(path)
    pubDate = email.utils.formatdate(mtime, usegmt=True)
    # build link relative to site root assuming docs/ maps to site root
    rel_url = os.path.relpath(path, 'docs').replace('\\', '/')
    link = site_url + '/' + rel_url
    entries.append({'title': title or 'Untitled', 'link': link, 'description': desc or '', 'pubDate': pubDate, 'mtime': mtime})

# sort by mtime desc
entries.sort(key=lambda x: x['mtime'], reverse=True)
entries = entries[:max_items]

now = email.utils.formatdate(usegmt=True)

def escape_xml(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
         .replace('"', '&quot;').replace("'", '&apos;'))

rss = ['<?xml version="1.0" encoding="UTF-8"?>',
    '<rss version="2.0">',
    '  <channel>',
    f'    <title>{os.path.basename(os.getcwd())} feed</title>',
    f'    <link>{site_url}/</link>',
    '    <description>RSS feed generated from site</description>',
    f'    <lastBuildDate>{now}</lastBuildDate>']

for e in entries:
    rss.append('    <item>')
    rss.append('      <title>' + escape_xml(e['title']) + '</title>')
    rss.append('      <link>' + e['link'] + '</link>')
    rss.append('      <guid isPermaLink="true">' + e['link'] + '</guid>')
    rss.append('      <pubDate>' + e['pubDate'] + '</pubDate>')
    if e['description']:
        rss.append('      <description>' + escape_xml(e['description']) + '</description>')
    rss.append('    </item>')

rss.extend(['  </channel>', '</rss>'])

os.makedirs(os.path.dirname(output), exist_ok=True)
with open(output, 'w', encoding='utf-8') as f:
    f.write('\n'.join(rss))

print(f'Wrote RSS feed with {len(entries)} items to {output}')
