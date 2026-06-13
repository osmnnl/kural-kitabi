#!/usr/bin/env python3
"""Grimcoven TR rulebook builder.
Reads page fragments from pages/ , embeds fonts+art as base64, emits a single
self-contained HTML (and a wkhtml 'check' variant with literal colors)."""
import base64, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent  # portable: /home/claude (sandbox) or local project dir
PAGES = ROOT/'pages'
ART = ROOT/'art'
FONTS = ROOT/'fonts'

def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()

# asset token -> file path (extended each batch)
ASSETS = {
  'GRENZE2': FONTS/'GrenzeGotisch.woff2', 'GRENZE1': FONTS/'GrenzeGotisch.woff',
  'LORA2': FONTS/'Lora.woff2', 'LORA1': FONTS/'Lora.woff',
  'LORAI2': FONTS/'Lora-Italic.woff2', 'LORAI1': FONTS/'Lora-Italic.woff',
  'COVER': ART/'cover.jpg', 'GRIMLOGO': ART/'grimcoven_logo.png',
  'PARCH2': ART/'parchment2.jpg', 'ORN_L': ART/'ornament_p2_flip.png',
  'PARCH3': ART/'parchment.jpg', 'ORN_R': ART/'ornament.png', 'QR': ART/'p3img-004.png',
  'BASE4': ART/'base_p4.jpg', 'CLEANPARCH4': ART/'parchment4.jpg',
  'BASE5': ART/'base_p5.jpg', 'CLEANPARCH5': ART/'parchment5.jpg',
  'BASE6': ART/'base_p6.jpg', 'CLEANPARCH6': ART/'parchment6.jpg',
  'BASE7': ART/'base_p7.jpg', 'CLEANPARCH7': ART/'parchment7.jpg',
  'BASE8': ART/'base_p8.jpg', 'CLEANPARCH8': ART/'parchment8.jpg',
  'BASE9': ART/'base_p9.jpg', 'CLEANPARCH9': ART/'parchment9.jpg',
  'BASE10': ART/'base_p10.jpg', 'CLEANPARCH10': ART/'parchment10.jpg',
  'BASE11': ART/'base_p11.jpg', 'CLEANPARCH11': ART/'parchment11.jpg',
  'BASE12': ART/'base_p12.jpg', 'CLEANPARCH12': ART/'parchment12.jpg',
  'BASE13': ART/'base_p13.jpg', 'CLEANPARCH13': ART/'parchment13.jpg',
  'BASE14': ART/'base_p14.jpg', 'CLEANPARCH14': ART/'parchment14.jpg',
  'BASE15': ART/'base_p15.jpg', 'CLEANPARCH15': ART/'parchment15.jpg',
  'BASE16': ART/'base_p16.jpg', 'CLEANPARCH16': ART/'parchment16.jpg',
  'BASE17': ART/'base_p17.jpg', 'CLEANPARCH17': ART/'parchment17.jpg',
  'BASE18': ART/'base_p18.jpg', 'CLEANPARCH18': ART/'parchment18.jpg',
  'BASE19': ART/'base_p19.jpg', 'CLEANPARCH19': ART/'parchment19.jpg',
  'BASE20': ART/'base_p20.jpg', 'CLEANPARCH20': ART/'parchment20.jpg',
  'BASE21': ART/'base_p21.jpg', 'CLEANPARCH21': ART/'parchment21.jpg',
  'BASE22': ART/'base_p22.jpg', 'CLEANPARCH22': ART/'parchment22.jpg',
  'BASE23': ART/'base_p23.jpg', 'CLEANPARCH23': ART/'parchment23.jpg',
  'BASE24': ART/'base_p24.jpg', 'CLEANPARCH24': ART/'parchment24.jpg',
  'BASE25': ART/'base_p25.jpg', 'CLEANPARCH25': ART/'parchment25.jpg',
  'BASE26': ART/'base_p26.jpg', 'CLEANPARCH26': ART/'parchment26.jpg',
  'BASE27': ART/'base_p27.jpg', 'CLEANPARCH27': ART/'parchment27.jpg',
  'BASE28': ART/'base_p28.jpg', 'CLEANPARCH28': ART/'parchment28.jpg',
  'BASE29': ART/'base_p29.jpg', 'CLEANPARCH29': ART/'parchment29.jpg',
  'BASE30': ART/'base_p30.jpg', 'CLEANPARCH30': ART/'parchment30.jpg',
  'BASE31': ART/'base_p31.jpg', 'CLEANPARCH31': ART/'parchment31.jpg',
  'BASE32': ART/'base_p32.jpg', 'CLEANPARCH32': ART/'parchment32.jpg',
  'BASE33': ART/'base_p33.jpg', 'CLEANPARCH33': ART/'parchment33.jpg',
  'BASE34': ART/'base_p34.jpg', 'CLEANPARCH34': ART/'parchment34.jpg',
  'BASE35': ART/'base_p35.jpg', 'CLEANPARCH35': ART/'parchment35.jpg',
  'BASE36': ART/'base_p36.jpg', 'CLEANPARCH36': ART/'parchment36.jpg',
  'IC_PLAYERS': ART/'icons/players.png', 'IC_LAMENT': ART/'icons/lament.png', 'IC_HEALTH': ART/'icons/health.png',
  'IC_UMARK': ART/'icons/umark.png',
  'IC_WOUND': ART/'icons/wound.png', 'IC_RANGE': ART/'icons/range.png', 'IC_DIE': ART/'icons/die_enemy.png', 'IC_CLAW': ART/'icons/claw.png', 'IC_LOCK': ART/'icons/lock.png', 'IC_DIE6': ART/'icons/die6.png',
  'IC_NOENTER': ART/'icons/noenter.png', 'IC_NOLOS': ART/'icons/nolos.png', 'IC_ENTER': ART/'icons/enter.png',
  'IC_MOVE': ART/'icons/move.png', 'IC_LIGHT': ART/'icons/light.png', 'IC_DARK': ART/'icons/dark.png',
  'IC_DIE_ATK': ART/'icons/die_atk.png', 'IC_DIE_SHD': ART/'icons/die_shd.png',
  'IC_CRAVE': ART/'icons/crave.png', 'IC_TDIE': ART/'icons/tdie.png', 'IC_DEF2': ART/'icons/def2.png',
  'IC_FORGE': ART/'icons/forge.png', 'IC_DIEG': ART/'icons/dieg.png', 'IC_COG28': ART/'icons/cog28.png',
  'IC_FJESTER': ART/'icons/fig_jester.png', 'IC_FKING': ART/'icons/fig_king.png', 'IC_FQUEEN': ART/'icons/fig_queen.png',
  'IC_FPRINCESS': ART/'icons/fig_princess.png', 'IC_FPRINCE': ART/'icons/fig_prince.png', 'IC_FKNIGHT': ART/'icons/fig_knight.png',
  'IC_COG': ART/'icons/cog.png', 'IC_DMAG': ART/'icons/dmag.png', 'IC_DAGI': ART/'icons/dagi.png',
  'IC_DIE_OFF': ART/'icons/die_off.png', 'IC_DIE_SPD': ART/'icons/die_spd.png',
  'IC_DIE_DEF': ART/'icons/die_def.png', 'IC_DIE_ARC': ART/'icons/die_arc.png',
  'IC_SYM_OFF': ART/'icons/sym_off.png', 'IC_SYM_SPD': ART/'icons/sym_spd.png',
  'IC_SYM_DEF': ART/'icons/sym_def.png', 'IC_SYM_ARC': ART/'icons/sym_arc.png',
}

COLORS = {'--parchment':'#ead7bd','--parchment-edge':'#cdb89e','--clay':'#d4b297',
  '--ink':'#1d1d1b','--ink-soft':'#4a3f36','--oxblood':'#8a1c18','--blood':'#b3261f','--gold':'#b8923f'}

FONTFACE = """
@font-face{font-family:'GrenzeG';src:url(data:font/woff2;base64,@@GRENZE2@@) format('woff2'),url(data:font/woff;base64,@@GRENZE1@@) format('woff');font-weight:100 900;font-style:normal;font-display:swap;}
@font-face{font-family:'Lora';src:url(data:font/woff2;base64,@@LORA2@@) format('woff2'),url(data:font/woff;base64,@@LORA1@@) format('woff');font-weight:400 700;font-style:normal;font-display:swap;}
@font-face{font-family:'Lora';src:url(data:font/woff2;base64,@@LORAI2@@) format('woff2'),url(data:font/woff;base64,@@LORAI1@@) format('woff');font-weight:400 700;font-style:italic;font-display:swap;}
"""

CSS = """
:root{--parchment:#ead7bd;--parchment-edge:#cdb89e;--clay:#d4b297;--ink:#1d1d1b;--ink-soft:#4a3f36;--oxblood:#8a1c18;--blood:#b3261f;--gold:#b8923f;}
*{box-sizing:border-box;}
html,body{margin:0;padding:0;}
body{background:#1c1411;font-family:'Lora',Georgia,serif;}

/* toolbar */
.toolbar{position:fixed;top:0;left:0;right:0;height:54px;z-index:1000;display:flex;align-items:center;gap:14px;padding:0 18px;background:linear-gradient(#3a1c18,#2a1310);color:#f0e4d2;border-bottom:1px solid #5a2a22;box-shadow:0 2px 10px rgba(0,0,0,.4);}
.toolbar b{font-family:'GrenzeG',serif;font-weight:700;letter-spacing:.5px;color:#e7c9c4;font-size:17px;}
.toolbar .sp{flex:1;}
.toolbar button{font-family:'Lora',serif;font-weight:700;font-size:14px;cursor:pointer;color:#2a1310;background:linear-gradient(#e9d6bd,#d9c0a2);border:1px solid #b8923f;border-radius:7px;padding:9px 16px;}
.toolbar button:hover{background:#f1e3cd;}
.toolbar .hint{font-size:12px;color:#caa9a2;max-width:46ch;line-height:1.25;}

/* stage */
.viewport{padding:78px 12px 28px;}
.page-wrap{margin:0 auto 22px;}
.page{position:relative;width:280mm;height:280mm;overflow:hidden;background:var(--parchment);color:var(--ink);transform-origin:top left;box-shadow:0 18px 60px rgba(0,0,0,.55);-webkit-print-color-adjust:exact;print-color-adjust:exact;}
.page.parch3{background:url(data:image/jpeg;base64,@@PARCH3@@) center/cover no-repeat,var(--parchment);}
.page.parch2{background:url(data:image/jpeg;base64,@@PARCH2@@) center/cover no-repeat,var(--parchment);}

.content{position:relative;z-index:2;height:100%;padding:13mm 15mm 12mm 15mm;}
.content::after{content:"";display:block;clear:both;}
.col-l{float:left;width:46.5%;}
.col-r{float:right;width:46.5%;}

/* ornaments (real art, bleed off edge) */
.orn{position:absolute;z-index:1;pointer-events:none;}
.orn-r{top:-6mm;right:-7mm;height:96mm;}
.orn-l{top:-6mm;left:-7mm;height:96mm;}

/* headings */
.section{font-family:'GrenzeG',serif;font-weight:700;color:var(--oxblood);font-size:26pt;line-height:1.0;margin:0 0 4.5mm;}
.section.tight{margin-top:1mm;}
.page.front .section{color:var(--ink);}      /* front-matter headers are dark, not red */

.oath{font-style:italic;color:var(--ink-soft);font-size:9pt;line-height:1.55;margin:0 0 4mm;}
.lede{font-style:italic;color:var(--ink-soft);font-size:9.5pt;line-height:1.3;margin:0 0 2.6mm;}
p{font-size:8.6pt;line-height:1.35;margin:0 0 2.4mm;text-align:justify;-webkit-hyphens:auto;hyphens:auto;}
strong{font-weight:700;}
ul.loss{list-style:none;margin:0 0 2.6mm;padding:0;}
ul.loss li{font-size:8.6pt;line-height:1.32;padding-left:5mm;position:relative;margin-bottom:1.2mm;text-align:justify;}
ul.loss li::before{content:"•";color:var(--oxblood);position:absolute;left:1mm;font-weight:700;}

/* clay info box */
.box{background:var(--clay);border:1.6pt solid var(--oxblood);border-radius:4mm;padding:4.5mm 5.5mm 4mm;margin:5mm 0;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact;}
.box .boxtitle{font-family:'Lora',serif;font-weight:700;font-size:13pt;margin:0 0 2.2mm;color:#23120f;}
.box p{font-size:8.4pt;line-height:1.32;margin:0 0 2mm;}
.box p:last-child{margin-bottom:0;}

/* qr */
.qr-wrap{text-align:center;margin-top:4mm;}
.qr{width:40mm;height:40mm;image-rendering:pixelated;border:1.4mm solid #fff;box-shadow:0 1px 5px rgba(0,0,0,.25);}

/* folio */
.folio{position:absolute;bottom:7mm;z-index:3;font-family:'Lora',serif;font-size:11pt;color:var(--ink-soft);}
.folio.r{right:10mm;} .folio.l{left:12mm;}

/* ---- cover ---- */
.page.cover{padding:0;}
.cover-art{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0;}
.cover-logo{position:absolute;left:50%;top:45%;transform:translate(-50%,-50%);width:70%;z-index:2;filter:drop-shadow(0 2px 10px rgba(0,0,0,.45));}
.cover-sub{position:absolute;left:0;right:0;bottom:9%;text-align:center;z-index:2;font-family:'GrenzeG',serif;font-weight:700;color:#f4ece2;font-size:30pt;letter-spacing:8px;text-shadow:0 2px 10px rgba(0,0,0,.7);}

/* ---- page 2: TOC + credits ---- */
.page.p2 .content{padding:19mm 23mm 12mm 24mm;}
.col-toc{float:left;width:39%;}
.col-cred{float:right;width:50%;}
.toc-list{list-style:none;margin:1mm 0 0;padding:0;}
.toc-list li{display:flex;align-items:baseline;font-size:8.6pt;line-height:1.62;color:var(--ink);}
.toc-list li.sub{padding-left:5mm;font-size:8.2pt;}
.toc-list li .d{flex:1 1 auto;margin:0 1.5mm;border-bottom:1px dotted #8a7256;position:relative;top:-3px;}
.toc-list li .pg{flex:0 0 auto;font-variant-numeric:tabular-nums;}
.cred{font-size:7.5pt;line-height:1.32;margin:0 0 1.7mm;text-align:left;}
.cred b{font-weight:700;}

/* ---- catalog pages (component overview): base render + parchment-reveal text covers ---- */
.page.catalog{padding:0;}
.page.catalog .base{position:absolute;inset:0;width:100%;height:100%;z-index:0;}
.cov{position:absolute;z-index:1;}
.txt{position:absolute;z-index:2;display:flex;align-items:center;justify-content:center;}
.c-title{justify-content:flex-start;font-family:'GrenzeG',serif;font-weight:700;color:var(--oxblood);font-size:30pt;line-height:1.0;letter-spacing:.5px;}
.c-head{justify-content:flex-start;font-family:'Lora',serif;font-weight:700;color:var(--ink);font-size:13.5pt;line-height:1.05;}
.c-cap{font-family:'Lora',serif;font-weight:400;color:var(--ink);font-size:8pt;line-height:1.16;text-align:center;}
.c-sect{justify-content:flex-start;font-family:'Lora',serif;font-weight:700;color:var(--ink);font-size:15pt;line-height:1.0;}
.c-sub{justify-content:flex-start;font-family:'Lora',serif;font-weight:700;color:var(--ink-soft);font-size:11pt;line-height:1.0;}
.c-note{justify-content:flex-start;font-style:italic;color:var(--ink-soft);font-size:7.4pt;line-height:1.2;text-align:left;}

/* ---- setup pages: base render + flowing Turkish text in parchment-reveal columns ---- */
.page.setup{padding:0;}
.page.setup .base{position:absolute;inset:0;width:100%;height:100%;z-index:0;}
.txtcol{position:absolute;z-index:1;box-sizing:border-box;color:var(--ink);font-family:'Lora',serif;background-repeat:no-repeat;background-origin:border-box;background-size:280mm 280mm;}
.txtcol .gt{font-family:'GrenzeG',serif;color:var(--oxblood);font-size:28pt;line-height:1;margin:0 0 2.6mm;letter-spacing:.4px;}
.txtcol h1{font-family:'Lora',serif;font-weight:700;color:var(--ink);font-size:15.5pt;margin:0 0 1.4mm;line-height:1.05;}
.txtcol h2{font-family:'Lora',serif;font-weight:700;color:var(--ink);font-size:13pt;margin:2.4mm 0 1.1mm;line-height:1.1;}
.txtcol p{font-size:8.4pt;line-height:1.34;margin:0 0 1.6mm;text-align:left;}
.txtcol .step{font-size:8.4pt;line-height:1.32;margin:0 0 1.5mm;padding-left:4.6mm;text-indent:-4.6mm;}
.txtcol .bullet{font-size:8.4pt;line-height:1.3;margin:.5mm 0;padding-left:8.5mm;text-indent:-3.2mm;}
.txtcol b{font-weight:700;}
.txtcol i{font-style:italic;}
.callout{border:1.1px solid #a06a44;border-radius:3mm;background:rgba(205,170,140,.34);padding:2mm 3mm 2.3mm;margin:.8mm 0 2.6mm;}
.callout .co-h{font-weight:700;font-size:11.5pt;color:var(--ink);margin:0 0 .9mm;}
.callout .co-b{font-size:8.2pt;line-height:1.3;margin:0;}
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

TOOLBAR = ('<div class="toolbar"><b>GRIMCOVEN</b>'
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
      "<title>Grimcoven — Kural Kitabı (TR)</title>\n<style>\n"+FONTFACE+css+"\n</style>\n</head>\n<body>\n"
      +toolbar+"\n<div class=\"viewport\">\n"+wrapped+"\n</div>\n"+script+"\n</body>\n</html>\n")
    # embed assets
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
    build(files, ROOT/'_check.html', check=True)
