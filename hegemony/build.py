#!/usr/bin/env python3
"""Hegemony TR rulebook builder.
Reads page fragments from pages/ , embeds fonts+art as base64, emits a single
self-contained HTML (and a 'check' variant with literal colors for render_check.py).

Sayfa boyutu: 280x280mm (PDF 793.7pt kare) — Grimcoven ile aynı, render_check.py 1058px sabiti geçerli.
Fontlar: Montserrat (başlık/kalın) + Roboto (gövde), variable woff2, tam TR glif kapsamı.
ASSETS: parti parti BASEN/CLEANPARCHN ve IC_* eklenir (şimdilik yalnız fontlar).
"""
import base64, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent
PAGES = ROOT/'pages'
ART = ROOT/'art'
FONTS = ROOT/'fonts'

def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()

# asset token -> file path (her parti genişletilir)
ASSETS = {
  'MONT2': FONTS/'Montserrat.woff2',
  'MONTI2': FONTS/'Montserrat-Italic.woff2',
  'ROBO2': FONTS/'Roboto.woff2',
  'ROBOI2': FONTS/'Roboto-Italic.woff2',
  # --- art (parti parti eklenecek) ---
  'COVER_CLEAN': ART/'cover_clean.jpg',   # s.1 İngilizce metni inpaint ile silinmiş kapak plakası
  'BASE2': ART/'base_p2.jpg',             # s.2 COMPONENTS (dokunulmamış; beyaz zemin, düz-dolgu kapak)
  'BASE3': ART/'base_p3.jpg',             # s.3 SYMBOLS
  'BASE4': ART/'clean_p4.jpg',            # s.4 — İngilizce metni inpaint ile silinmiş (kartlar korundu); TR şeffaf bindirilir
  # 'COVER': ART/'cover.jpg',
  # 'BASE4': ART/'base_p4.jpg', 'CLEANPARCH4': ART/'parchment4.jpg', ...
}

FONTFACE = """
@font-face{font-family:'Mont';src:url(data:font/woff2;base64,@@MONT2@@) format('woff2');font-weight:100 900;font-style:normal;font-display:swap;}
@font-face{font-family:'Mont';src:url(data:font/woff2;base64,@@MONTI2@@) format('woff2');font-weight:100 900;font-style:italic;font-display:swap;}
@font-face{font-family:'Robo';src:url(data:font/woff2;base64,@@ROBO2@@) format('woff2');font-weight:100 900;font-style:normal;font-display:swap;}
@font-face{font-family:'Robo';src:url(data:font/woff2;base64,@@ROBOI2@@) format('woff2');font-weight:100 900;font-style:italic;font-display:swap;}
"""

# Hegemony paleti — TOKENLAR GEÇİCİ; her sayfanın base_pN.jpg'inden ÖRNEKLENİP güncellenecek (JOURNAL).
CSS = """
:root{--paper:#ffffff;--ink:#1a1a1a;--ink-soft:#4a4a4a;--accent:#e8b21f;--rule:#d8d8d8;
  --wc:#c8102e;--mc:#2e7d32;--cap:#1565c0;--state:#5e35b1;}
*{box-sizing:border-box;}
html,body{margin:0;padding:0;}
body{background:#2a2a2a;font-family:'Robo',Arial,sans-serif;}

/* toolbar */
.toolbar{position:fixed;top:0;left:0;right:0;height:54px;z-index:1000;display:flex;align-items:center;gap:14px;padding:0 18px;background:#1c1c1c;color:#f0f0f0;border-bottom:1px solid #444;box-shadow:0 2px 10px rgba(0,0,0,.4);}
.toolbar b{font-family:'Mont',sans-serif;font-weight:800;letter-spacing:1px;color:#e8b21f;font-size:17px;}
.toolbar .sp{flex:1;}
.toolbar button{font-family:'Mont',sans-serif;font-weight:700;font-size:14px;cursor:pointer;color:#1c1c1c;background:#e8b21f;border:none;border-radius:7px;padding:9px 16px;}
.toolbar button:hover{background:#f3c647;}
.toolbar .hint{font-size:12px;color:#bbb;max-width:46ch;line-height:1.25;}

/* stage */
.viewport{padding:78px 12px 28px;}
.page-wrap{margin:0 auto 22px;}
.page{position:relative;width:280mm;height:280mm;overflow:hidden;background:var(--paper);color:var(--ink);transform-origin:top left;box-shadow:0 18px 60px rgba(0,0,0,.55);-webkit-print-color-adjust:exact;print-color-adjust:exact;}

/* folio */
.folio{position:absolute;bottom:7mm;z-index:3;font-family:'Mont',sans-serif;font-weight:600;font-size:11pt;color:var(--ink-soft);}
.folio.r{right:10mm;} .folio.l{left:12mm;}

/* ---- cover ---- */
.page.cover{padding:0;}
.cover-art{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0;}

/* ---- catalog/anatomi pages: base render + reveal text covers ---- */
.page.catalog{padding:0;}
.page.catalog .base{position:absolute;inset:0;width:100%;height:100%;z-index:0;}
.cov{position:absolute;z-index:1;}                /* düz-dolgu/reveal kapağı */
.txt{position:absolute;z-index:2;display:flex;align-items:center;justify-content:center;}
.c-title{justify-content:flex-start;font-family:'Mont',sans-serif;font-weight:800;color:var(--ink);font-size:30pt;line-height:1.0;letter-spacing:.5px;text-transform:uppercase;}
.c-head{justify-content:flex-start;font-family:'Mont',sans-serif;font-weight:700;color:var(--ink);font-size:13.5pt;line-height:1.05;}
.c-cap{font-family:'Robo',sans-serif;font-weight:400;color:var(--ink);font-size:8pt;line-height:1.16;text-align:center;}
/* katalog etiket kapakları (s.2,3,4): amber bar + beyaz kapak + caption */
.page.catalog .hb{position:absolute;z-index:2;background:#f2ae26;display:flex;align-items:center;justify-content:center;font-family:'Mont';font-weight:700;font-size:8.5pt;color:#fff;letter-spacing:.3px;text-align:center;line-height:1.05;}
.page.catalog .hc{position:absolute;z-index:2;background:#fff;display:flex;align-items:center;justify-content:center;text-align:center;font-family:'Mont';}
.page.catalog .cap{height:9mm;font-weight:600;font-size:7pt;line-height:1.18;color:#3a3a3a;letter-spacing:.2px;}
.page.catalog .cap.sm{font-size:6pt;line-height:1.12;}
.page.catalog .pill{position:absolute;z-index:2;background:#ededed;border-radius:1.6mm;display:flex;align-items:center;justify-content:center;text-align:center;font-family:'Mont';font-weight:600;font-size:6pt;line-height:1.12;color:#444;letter-spacing:.1px;padding:0 .6mm;}
.page.catalog .pill.s{font-size:5.3pt;line-height:1.08;}

/* ---- setup/main-rules pages: base render + akan TR metni reveal-kolonlarda ---- */
.page.setup{padding:0;}
.page.setup .base{position:absolute;inset:0;width:100%;height:100%;z-index:0;}
.txtcol{position:absolute;z-index:1;box-sizing:border-box;color:var(--ink);font-family:'Robo',sans-serif;background:var(--paper);background-repeat:no-repeat;background-origin:border-box;background-size:280mm 280mm;}
.txtcol .gt{font-family:'Mont',sans-serif;font-weight:800;color:var(--ink);font-size:24pt;line-height:1;margin:0 0 2.6mm;letter-spacing:.4px;text-transform:uppercase;}
.txtcol h1{font-family:'Mont',sans-serif;font-weight:700;color:var(--ink);font-size:14pt;margin:0 0 1.4mm;line-height:1.05;}
.txtcol h2{font-family:'Mont',sans-serif;font-weight:700;color:var(--ink);font-size:11.5pt;margin:2.4mm 0 1.1mm;line-height:1.1;}
.txtcol p{font-size:8.4pt;line-height:1.34;margin:0 0 1.6mm;text-align:left;}
.txtcol .step{font-size:8.4pt;line-height:1.32;margin:0 0 1.5mm;padding-left:4.6mm;text-indent:-4.6mm;}
.txtcol .bullet{font-size:8.4pt;line-height:1.3;margin:.5mm 0;padding-left:8.5mm;text-indent:-3.2mm;}
.txtcol b{font-weight:700;}
.txtcol i{font-style:italic;}
.ic{height:1.0em;width:auto;vertical-align:-0.16em;}
.ic-d{height:1.25em;width:auto;vertical-align:-0.32em;}

@media print{
  @page{size:280mm 280mm;margin:0;}
  html,body{background:#fff;}
  .toolbar{display:none !important;}
  .viewport{padding:0;}
  .page-wrap{margin:0 !important;width:auto !important;height:auto !important;}
  .page{transform:none !important;box-shadow:none;margin:0;break-after:page;page-break-after:always;}
  .page:last-child{break-after:auto;page-break-after:auto;}
}
"""

COLORS = {'--paper':'#ffffff','--ink':'#1a1a1a','--ink-soft':'#4a4a4a','--accent':'#e8b21f','--rule':'#d8d8d8',
  '--wc':'#c8102e','--mc':'#2e7d32','--cap':'#1565c0','--state':'#5e35b1'}

TOOLBAR = ('<div class="toolbar"><b>HEGEMONY</b>'
  '<span style="opacity:.7;font-size:13px">— Kural Kitabı (TR)</span><span class="sp"></span>'
  '<span class="hint">Yazdırırken: Kenar boşlukları <b>Yok/None</b>, “Arka plan grafikleri” <b>açık</b>, ölçek %100.</span>'
  '<button onclick="window.print()">İndir / Yazdır (PDF)</button></div>')

SCRIPT = """<script>
(function(){function fit(){var vp=document.querySelector('.viewport');if(!vp)return;var vw=vp.clientWidth;
document.querySelectorAll('.page').forEach(function(pg){var pw=pg.offsetWidth,s=Math.min(1,vw/pw);
pg.style.transform='scale('+s+')';var w=pg.parentElement;w.style.width=(pw*s)+'px';w.style.height=(pg.offsetHeight*s)+'px';});}
window.addEventListener('resize',fit);window.addEventListener('load',fit);fit();})();
</script>"""

def build(page_files, out, check=False):
    frags = [pathlib.Path(p).read_text(encoding='utf-8') for p in page_files]
    wrapped = '\n'.join('<div class="page-wrap">%s</div>'%f for f in frags)
    toolbar = '' if check else TOOLBAR
    script = '' if check else SCRIPT
    css = CSS
    vp_pad = 'padding:0;' if check else 'padding:78px 12px 28px;'
    css = css.replace('.viewport{padding:78px 12px 28px;}', '.viewport{%s}'%vp_pad)
    if check:
        css = css.replace('box-shadow:0 18px 60px rgba(0,0,0,.55);','')
    html = ("<!doctype html>\n<html lang=\"tr\">\n<head>\n<meta charset=\"utf-8\">\n"
      "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
      "<title>Hegemony — Kural Kitabı (TR)</title>\n<style>\n"+FONTFACE+css+"\n</style>\n</head>\n<body>\n"
      +toolbar+"\n<div class=\"viewport\">\n"+wrapped+"\n</div>\n"+script+"\n</body>\n</html>\n")
    for tok,path in ASSETS.items():
        if ('@@%s@@'%tok) in html:
            html = html.replace('@@%s@@'%tok, b64(path))
    if check:
        for tok,hexv in COLORS.items():
            html = html.replace('var(%s)'%tok, hexv)
    pathlib.Path(out).write_text(html, encoding='utf-8')
    print(out, round(len(html.encode())/1024/1024,2),'MB')

if __name__=='__main__':
    args = sys.argv[1:]
    if args:
        files = [PAGES/('p%02d.html'%int(a)) for a in args]
    else:
        files = sorted(PAGES.glob('p*.html'))
    files = [str(f) for f in files]
    build(files, ROOT/'preview.html', check=False)
    # render_check.py için _check.html (literal renk):
    build(files, ROOT/'_check.html', check=True)
