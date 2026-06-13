# Usage: python3 tools_grid.py /tmp/su-12.png 5      (5% grid, full page)
#        python3 tools_grid.py /tmp/su-12.png 2 0.6 0.4  (2% grid, crop to 60%x40%)
from PIL import Image, ImageDraw, ImageFont
import sys
img=sys.argv[1]; step=int(sys.argv[2]) if len(sys.argv)>2 else 5
cw=float(sys.argv[3]) if len(sys.argv)>3 else 1.0
ch=float(sys.argv[4]) if len(sys.argv)>4 else 1.0
im=Image.open(img).convert('RGB'); W,H=im.size; d=ImageDraw.Draw(im)
try: f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',18)
except: f=ImageFont.load_default()
for p in range(0,101,step):
    x=int(W*p/100); y=int(H*p/100)
    col=(255,0,0) if p%25==0 else (0,150,255)
    d.line([(x,0),(x,H)],fill=col,width=1); d.line([(0,y),(W,y)],fill=col,width=1)
    d.text((x+1,1),str(p),fill=(190,0,0),font=f); d.text((1,y+1),str(p),fill=(190,0,0),font=f)
out='/tmp/grid_out.png'
im.crop((0,0,int(W*cw),int(H*ch))).resize((int(1120*cw),int(1120*ch))).save(out)
print('saved',out)
