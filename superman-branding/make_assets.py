#!/usr/bin/env python3
"""Generate SUPERMAN brand icons using the included original user-facing logo artwork."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
HERE=Path(__file__).resolve().parent
O=HERE/'assets'; O.mkdir(exist_ok=True)
logo=Image.open(O/'superman-source.png').convert('RGBA')
a=logo.getchannel('A').getbbox()
logo=logo.crop(a)
# Inset slightly to prevent favicon edges clipping
SIZE=512
s=int(SIZE*.89)
logo=logo.resize((s,s),Image.Resampling.LANCZOS)
base=Image.new('RGBA',(SIZE,SIZE),(0,0,0,0)); base.alpha_composite(logo,((SIZE-s)//2,(SIZE-s)//2))
base.save(O/'superman-mark-512.png')
for size in [16,32,48,64,96,180,192,256]:
    base.resize((size,size),Image.Resampling.LANCZOS).save(O/f'superman-mark-{size}.png')
base.save(O/'superman-mark.webp','WEBP',quality=95,method=6)
base.resize((256,256),Image.Resampling.LANCZOS).save(O/'favicon.ico',sizes=[(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)])
# Responsive wordmark using drawn type, does not require distributing any font files.
fpath='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
font=ImageFont.truetype(fpath,94)
sub=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',26)
word=Image.new('RGBA',(1280,300),(0,0,0,0));d=ImageDraw.Draw(word)
icon=base.resize((230,230),Image.Resampling.LANCZOS)
word.alpha_composite(icon,(10,33))
d.text((260,72),'SUPERMAN',font=font,fill=(240,236,255,255))
d.text((265,183),'B R O W S E R',font=sub,fill=(89,213,255,255))
word.save(O/'superman-wordmark.png')
word.save(O/'superman-wordmark.webp',quality=96)
# Original SVG substitute (raster embedded in SVG, faithful to artwork)
import base64
p64=base64.b64encode((O/'superman-mark-512.png').read_bytes()).decode()
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512"><image width="512" height="512" href="data:image/png;base64,{p64}"/></svg>'''
(O/'superman-mark.svg').write_text(svg,encoding='utf-8')
print('Generated SUPERMAN favicon, logos, wordmark')
