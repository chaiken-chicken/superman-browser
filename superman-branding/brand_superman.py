#!/usr/bin/env python3
"""Rebrand the user-visible InvisiProxy LTS front end without modifying proxy transports.

Run: python3 brand_superman.py /path/to/InvisiProxyLTS

This is intentionally a site branding overlay. It does not alter URLs, service worker
prefixes, app IDs, dependencies, Git metadata, AGPL notices, or engine internals.
"""
from __future__ import annotations
import json
import re
import shutil
import sys
from pathlib import Path
from collections import Counter

HERE = Path(__file__).resolve().parent
BRAND_ASSETS = HERE / 'assets'
if len(sys.argv) < 2:
    raise SystemExit('Usage: python3 brand_superman.py /path/to/InvisiProxyLTS')
repo = Path(sys.argv[1]).expanduser().resolve()
views = repo / 'views'
if not views.is_dir() or not (repo / 'package.json').exists():
    raise SystemExit('Error: This must point to an InvisiProxy LTS checkout containing views/ and package.json.')

changed = Counter()
# Only user-facing assets/text are rebranded. Copyright/credits remain intact.
replacements = [
    ('InvisiProxy LTS', 'SUPERMAN BROWSER'),
    ('InvisiProxyLTS', 'SUPERMAN BROWSER'),
    ('InvisiProxy', 'SUPERMAN'),
    ('invisiProxy', 'supermanBrowser'),
    ('Holy Unblocker LTS', 'SUPERMAN BROWSER'),
]

def rewrite_labels(data: str) -> str:
    # Do not rewrite URLs or internal paths; site references must still work.
    parts = re.split(r'(https?://[^\s\x22\x27<>]+)', data)
    for i in range(0, len(parts), 2):
        chunk = parts[i]
        for a, b in replacements:
            chunk = chunk.replace(a, b)
        parts[i] = chunk
    return ''.join(parts)

def protect_source(path: Path) -> bool:
    return any(s.lower().split('.')[0] in {'credits','license','privacy','copyright','third-party'} for s in path.parts)

# The actual displayed copy and translations, not code or engine internal IDs.
for folder in [views, repo/'locales']:
    if not folder.exists():
        continue
    for f in folder.rglob('*'):
        if not f.is_file() or f.is_symlink() or protect_source(f.relative_to(repo)):
            continue
        if f.suffix.lower() not in {'.html','.yaml','.yml','.json','.md','.txt','.css'}:
            continue
        if 'node_modules' in f.parts or 'dist' in f.parts:
            continue
        try:
            before = f.read_text(encoding='utf-8')
        except (UnicodeError, OSError):
            continue
        after = rewrite_labels(before)
        # On a private, self-hosted site a canonical link to the upstream domain is misleading.
        if f.suffix.lower() == '.html':
            after = re.sub(r'<link\s+rel=["\']canonical["\'][^>]*invisiproxy\.com[^>]*>\s*','',after, flags=re.I)
            # Keep original project authors/credits, but strip upstream company's JSON-LD
            # organization marketing which would impersonate its official website.
            after = re.sub(r'<script\b(?=[^>]*type=["\']application/ld\+json["\'])[^>]*>.*?</script>','',after, flags=re.I|re.S)
        if after != before:
            f.write_text(after,encoding='utf-8')
            changed['text files'] += 1

# Replace only brand icon images; don't replace logos of TikTok, Chess, Google etc.
img_dir = views / 'assets' / 'img'; img_dir.mkdir(parents=True,exist_ok=True)
for p in BRAND_ASSETS.glob('superman-*'):
    if p.suffix.lower() in {'.png','.webp','.svg'} and 'source' not in p.name:
        shutil.copy2(p,img_dir / p.name)
(views / 'favicon.ico').write_bytes((BRAND_ASSETS / 'favicon.ico').read_bytes())
shutil.copy2(BRAND_ASSETS / 'superman-mark.svg', views / 'superman-mark.svg')

brand_stems = {'logo','logo-light','logo-dark','logo_github','favicon',
               'invisiproxy','invisiproxy-logo','invisiproxy-lts',
               'icon-192','icon-512','logo_transparent',
               'new','safari-pinned-tab','apple-touch-icon',
               'android-chrome-192x192','android-chrome-512x512'}
for p in views.rglob('*'):
    if not p.is_file() or p.is_symlink() or p.name.startswith('superman-') or '.git' in p.parts:
        continue
    if p.suffix.lower() not in {'.png','.webp','.jpg','.jpeg','.ico','.svg'}:
        continue
    name = p.stem.lower()
    # Do not change screenshots or dependency/app icons.
    if not (name in brand_stems or name.startswith('invisiproxy') or name.startswith('favicon')):
        continue
    if protect_source(p.relative_to(repo)):
        continue
    try:
        src = BRAND_ASSETS/'superman-mark-512.png'
        if 'logo' in name and ('light' in name or 'dark' in name):
            src = BRAND_ASSETS/'superman-wordmark.png'
        if p.suffix.lower() == '.svg':
            shutil.copy2(BRAND_ASSETS/'superman-mark.svg',p)
        elif p.suffix.lower() == '.ico':
            shutil.copy2(BRAND_ASSETS/'favicon.ico',p)
        else:
            # Copy pre-encoded PNG/WebP/JPG assets. No Python packages needed in Codespaces.
            ext = p.suffix.lower()
            wide = name in {'logo-light','logo-dark','logo_github','logo_transparent'}
            if ext == '.webp':
                source = BRAND_ASSETS / ('superman-wordmark.webp' if wide else 'superman-mark.webp')
            elif ext in {'.jpg','.jpeg'}:
                source = BRAND_ASSETS / ('superman-wordmark.jpg' if wide else 'superman-mark.jpg')
            else:
                source = BRAND_ASSETS / ('superman-wordmark.png' if wide else 'superman-mark-512.png')
            shutil.copy2(source,p)
        changed['brand images'] += 1
    except Exception as err:
        print(f'Warning: unable to replace brand image {p.relative_to(repo)}: {err}')

# Favicon / installable-app metadata (preserve unrelated manifest fields).
for manifest in [views/'manifest.json',views/'site.webmanifest',views/'manifest.webmanifest']:
    if not manifest.exists(): continue
    try:
        data=json.loads(manifest.read_text(encoding='utf-8'))
        data['name']='SUPERMAN BROWSER'
        data['short_name']='SUPERMAN'
        data['description']='SUPERMAN Browser — community web browser'
        data['icons']=[
            {'src':'/assets/img/superman-mark-192.png','sizes':'192x192','type':'image/png'},
            {'src':'/assets/img/superman-mark-512.png','sizes':'512x512','type':'image/png'},
        ]
        data['theme_color']='#101028'
        data['background_color']='#080b19'
        manifest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        changed['manifests']+=1
    except Exception as e: print(f'Warning: unable to update manifest: {e}')

css=(HERE/'superman-brand.css').read_text(encoding='utf-8')
js=(HERE/'superman-brand.js').read_text(encoding='utf-8')
js_dir=views/'assets'/'js';js_dir.mkdir(parents=True,exist_ok=True)
css_dir=views/'assets'/'css';css_dir.mkdir(parents=True,exist_ok=True)
(js_dir/'superman-brand.js').write_text(js,encoding='utf-8')
(css_dir/'superman-brand.css').write_text(css,encoding='utf-8')
icons_src=HERE/'icons'
icons_dst=views/'assets'/'icons'/'superman'
icons_dst.mkdir(parents=True,exist_ok=True)
for p in icons_src.glob('*.svg'):shutil.copy2(p,icons_dst/p.name)

# Add branding after the stylesheet links. This is independent of the framework.
# Avoid editing the compiled service workers and navigation internals.
for f in views.rglob('*.html'):
    if protect_source(f.relative_to(repo)) or 'dist' in f.parts: continue
    before=f.read_text(encoding='utf-8')
    if '</head>' not in before.lower() or '/assets/js/superman-brand.js' in before: continue
    inject=('\n<!-- SUPERMAN visual branding; original proxy engine unchanged -->\n'
            '<link rel="icon" type="image/png" href="/assets/img/superman-mark-32.png" />\n'
            '<link rel="apple-touch-icon" href="/assets/img/superman-mark-180.png" />\n'
            '<link rel="stylesheet" href="/assets/css/superman-brand.css" />\n'
            '<script defer src="/assets/js/superman-brand.js"></script>\n')
    after=re.sub(r'</head>',lambda m:inject+m.group(0),before,count=1,flags=re.I)
    f.write_text(after,encoding='utf-8')
    changed['branded pages']+=1

# Add a source attribution note and ensure license is preserved.
notice=repo/'SUPERMAN-UPSTREAM-NOTICE.md'
notice.write_text('''# SUPERMAN BROWSER — source attribution\n\nThis is a cosmetic rebrand of the InvisiProxy LTS open-source project.\nUpstream: https://github.com/InvisiProxy/InvisiProxyLTS\n\nThe browser engines, service workers, transports, and original source remain from\nthe upstream project. Please preserve the upstream LICENSE and any copyright notices.\nReview the source license before redistributing or publicly hosting the modified app.\n\nThe SUPERMAN UI branding overlay and custom icons are separately created artwork.\n''',encoding='utf-8')
print('SUPERMAN branding applied:',dict(changed))
print('Proxy engine unchanged. Install/build this repository per upstream instructions.')
