from pathlib import Path
from html import escape
HERE=Path(__file__).resolve().parent
D=HERE/'icons'; D.mkdir(exist_ok=True)
# Original, coherent 24x24 outline glyphs for the website's own navigation.
paths={
 'home':'<path d="M3 10.5 12 3l9 7.5V21H7v-7h10v7"/>',
 'globe':'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c-5 5-5 13 0 18M12 3c5 5 5 13 0 18"/>',
 'search':'<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/>',
 'gamepad':'<rect x="3" y="7" width="18" height="11" rx="5"/><path d="M7 12h6M10 9v6M17 11h.01M19 14h.01"/>',
 'settings':'<circle cx="12" cy="12" r="3"/><path d="M10 2h4l.7 2.5 2 .8L19 4l3 3-1.3 2.3.8 2L24 12v3l-2.5.7-.8 2L22 20l-3 2-2.3-1.3-2 .8L14 24h-4l-.7-2.5-2-.8L5 22l-3-2 1.3-2.3-.8-2L0 15v-3l2.5-.7.8-2L2 7l3-3 2.3 1.3 2-.8z" transform="translate(2 2) scale(.82)"/>',
 'apps':'<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
 'info':'<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.2"/>',
 'shield':'<path d="M12 2 21 6v6c0 6-4.5 9-9 10-4.5-1-9-4-9-10V6z"/><path d="m8.5 12 2.5 2.5 5-5"/>',
 'user':'<circle cx="12" cy="8" r="4"/><path d="M4.5 21c0-8 15-8 15 0"/>',
 'users':'<circle cx="10" cy="8" r="3"/><path d="M3 20c0-7 14-7 14 0M18 5c4 2 4 6 0 8M18 15c3 0 4.5 2 4.5 5"/>',
 'star':'<path d="m12 2 3 7 7 1-5.5 4.8 1.7 7.2-6.2-3.8-6.2 3.8 1.7-7.2L2 10l7-1z"/>',
 'heart':'<path d="M12 21s-9-6-9-12a5 5 0 0 1 9-3 5 5 0 0 1 9 3c0 6-9 12-9 12Z"/>',
 'menu':'<path d="M3 6h18M3 12h18M3 18h18"/>',
 'question':'<circle cx="12" cy="12" r="9"/><path d="M9.2 9a3 3 0 1 1 5.3 2c-1.2 1.1-2.5 1.2-2.5 3M12 18v.1"/>',
 'arrow-right':'<path d="M3 12h17m-7-7 7 7-7 7"/>',
 'arrow-left':'<path d="M21 12H4m7-7-7 7 7 7"/>',
 'external-link':'<path d="M14 4h6v6m0-6-9 9"/><path d="M20 14v6H4V4h6"/>',
 'lock':'<rect x="5" y="10" width="14" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
 'cloud':'<path d="M6 18H5a4 4 0 0 1-.5-8 7 7 0 0 1 13.5 0 4 4 0 0 1 .5 8H6"/>',
 'download':'<path d="M12 3v13m-5-5 5 5 5-5M3 20h18"/>',
 'upload':'<path d="M12 17V4M7 9l5-5 5 5M3 20h18"/>',
 'bell':'<path d="M5 17h14l-2-3V9a5 5 0 0 0-10 0v5zm5 3h4"/>',
 'eye':'<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/>',
 'book':'<path d="M4 4h7c2 0 2 1 2 3v14H4zm9 0h7v17h-7"/>',
 'link':'<path d="M10 14a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-2 2M14 10a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l2-2"/>',
 'clock':'<circle cx="12" cy="12" r="9"/><path d="M12 6v6l4 2"/>',
 'refresh':'<path d="M4 10a8 8 0 0 1 14-4l2 2V3m0 5h-5M20 14a8 8 0 0 1-14 4l-2-2v5m0-5h5"/>',
 'play':'<path d="m8 5 12 7-12 7z"/>',
 'pause':'<path d="M7 5v14m10-14v14"/>',
 'sparkles':'<path d="m12 2 2.2 7.8L22 12l-7.8 2.2L12 22l-2.2-7.8L2 12l7.8-2.2z"/>',
 'close':'<path d="M5 5 19 19M19 5 5 19"/>',
}
for name,body in paths.items():
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="black" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">{body}</svg>'
 (D/f'{name}.svg').write_text(svg,encoding='utf-8')
# Aliases used in Font Awesome rendered by InvisiProxy's legacy UI.
aliases={
'home':['house','home','house-chimney'], 'globe':['globe','earth-americas','earth-europe','world'],
'search':['magnifying-glass','search'], 'gamepad':['gamepad','puzzle-piece','dice','chess-knight'],
'settings':['gear','gears','cog','cogs','sliders','wrench'],
'apps':['th','th-large','table-cells','grip','grid'], 'info':['info-circle','circle-info','info'],
'shield':['shield','shield-halved','shield-alt'], 'user':['user','user-circle','circle-user'],
'users':['users','user-group'], 'star':['star','award'], 'heart':['heart'],
'menu':['bars','list'], 'question':['question','question-circle','circle-question'],
'arrow-right':['arrow-right','chevron-right'], 'arrow-left':['arrow-left','chevron-left'],
'external-link':['external-link','external-link-alt','up-right-from-square','arrow-up-right-from-square'],
'lock':['lock','key'], 'cloud':['cloud'], 'download':['download'], 'upload':['upload'],
'bell':['bell'], 'eye':['eye'], 'book':['book','book-open'], 'link':['link'],
'clock':['clock','history'], 'refresh':['sync','sync-alt','refresh','rotate','rotate-right'],
'play':['play'], 'pause':['pause'], 'sparkles':['bolt','rocket','wand-magic-sparkles','fire'],
'close':['times','xmark','close','x'],
}
css='''/* SUPERMAN site rebrand. CSS-only custom navigation pictograms; preserves behavior. */
:root { --superman-purple:#a879ff;--superman-cyan:#3ddcf8;--superman-navy:#0c1026; }
/* Hero and logo receive the custom mark; maintain upstream page layout. */
a:hover {text-decoration-color:var(--superman-cyan)}
.fa,.fas,.far,.fa-solid,.fa-regular{transition:color .2s ease;}
:where(nav,header,.navbar,.menu,.sidebar) .fa,
:where(nav,header,.navbar,.menu,.sidebar) .fas{color:var(--superman-purple)}
'''
for name,alias in aliases.items():
 sel=','.join(f'.fa-{x}::before' for x in alias)
 css+=f'''\n{sel} {{content:"" !important; display:inline-block;vertical-align:-.12em;width:1.06em;height:1.06em;background-color:currentColor;-webkit-mask: url('/assets/icons/superman/{name}.svg') center / contain no-repeat;mask:url('/assets/icons/superman/{name}.svg') center / contain no-repeat;}}\n'''
(HERE/'superman-brand.css').write_text(css,encoding='utf-8')
print('Generated',len(paths),'original line icon SVGs, CSS replacements for',sum(map(len,aliases.values())),'icon class names')
