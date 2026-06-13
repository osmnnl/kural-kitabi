# Usage: python3 tools_extract.py 12   (needs /tmp/su-12.png to exist + the source PDF path below)
import sys, glob, os
from PIL import Image
import numpy as np
pg=sys.argv[1]
PDF=os.environ.get('PDF','/mnt/user-data/uploads/GC_Rulebook_280x280mm_bleed3mm__36_pages___lowres__compressed.pdf')
os.makedirs('/tmp/ext%s'%pg,exist_ok=True)
os.system('cd /tmp/ext%s && pdfimages -all -f %s -l %s "%s" x >/dev/null 2>&1'%(pg,pg,pg,PDF))
best=None;score=-1
for fpath in sorted(glob.glob('/tmp/ext%s/x*'%pg)):
    try: im=Image.open(fpath).convert('RGB')
    except: continue
    w,h=im.size
    if w*h<1200*1200: continue
    a=np.array(im.resize((40,40))).astype(int); lum=a.sum(2).mean()/3; sat=(a.max(2)-a.min(2)).mean()
    if 178<lum<216 and 30<sat<56:   # WARM parchment, not white underlay
        if w*h>score: score=w*h; best=fpath
if best:
    Image.open(best).convert('RGB').save('art/parchment%s.jpg'%pg,'JPEG',quality=78,optimize=True)
    print('parchment%s.jpg saved from'%pg, best)
else: print('!! parchment not auto-found for page',pg,'- inspect /tmp/ext%s manually'%pg)
# base render (su-NN.png must already exist via pdftoppm -r 150)
suf=glob.glob('/tmp/su-%s.png'%pg) or glob.glob('/tmp/su-0%s.png'%pg)
if suf:
    Image.open(suf[0]).convert('RGB').resize((1500,1500),Image.LANCZOS).save('art/base_p%s.jpg'%pg,'JPEG',quality=82,optimize=True,progressive=True)
    print('base_p%s.jpg saved'%pg)
