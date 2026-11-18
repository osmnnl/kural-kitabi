from PIL import Image
import numpy as np
import sys
img=sys.argv[1]
im = np.array(Image.open(img).convert('L')); H,W=im.shape
def band(x0p,x1p,label):
    x0,x1=int(W*x0p/100),int(W*x1p/100); col=im[:,x0:x1]
    prof=(col<110).sum(1); th=max(3,(x1-x0)//40); rows=prof>th
    out=[]; i=0
    while i<H:
        if rows[i]:
            j=i
            while j<H and (rows[j] or (j+3<H and rows[j:j+4].any())): j+=1
            out.append((round(i/H*100,1),round(j/H*100,1),int(prof[i:j].mean())))
            i=j
        else: i+=1
    print('--- %s ---'%label)
    for b in out:
        tag='ART' if b[2]>(x1-x0)*0.22 else 'text'
        print('  y %5s-%5s%%  d=%4d  %s'%(b[0],b[1],b[2],tag))
for a in sys.argv[2:]:
    x0,x1,lab=a.split(',')
    band(float(x0),float(x1),lab)
