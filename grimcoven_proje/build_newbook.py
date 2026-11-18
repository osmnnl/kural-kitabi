#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""YENİ TASARIM — Grimcoven TR kural kitabı (örnek: s.1-3).
Akan/temiz dizgi: çevrilmiş metin gerçek metin, dokümandan çıkarılmış görseller yerleştirilir.
Kendi-kendine yeten (font+görsel base64). A3 kuşe baskıda kusursuz + webde mobil-uyumlu.
Çıktı: newbook/grimcoven_yeni_ornek.html"""
import base64, pathlib
ROOT = pathlib.Path(__file__).resolve().parent
NB = ROOT / 'newbook'
A = NB / 'assets'
F = ROOT.parent / 'site' / 'assets' / 'fonts'

def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
def font(p, fmt): return f"url(data:font/{fmt};base64,{b64(p)}) format('{ 'woff2' if fmt=='woff2' else 'truetype'}')"
def img(p, mime): return f"data:image/{mime};base64,{b64(p)}"

GREN = font(F/'GrenzeGotisch.woff2','woff2')
LORA = font(F/'Lora.woff2','woff2')
LORAI = font(F/'Lora-Italic.woff2','woff2')
METAM = font(F/'Metamorphous.ttf','ttf')
COVER = img(A/'cover.jpg','jpeg')
TILE = img(A/'parch_tile.jpg','jpeg')
ORN = img(A/'ornament.png','png')
QR = img(A/'qr.png','png')
import os
def plates(sub):
    d=A/sub; out={}
    for f in sorted(os.listdir(d)):
        nm,ext=f.rsplit('.',1)
        out[nm]=img(d/f,'jpeg' if ext.lower() in ('jpg','jpeg') else 'png')
    return out
P4=plates('p4'); P5=plates('p5'); P6=plates('p6')

FACE = f"""
@font-face{{font-family:'Gren';src:{GREN};font-weight:300 700;font-display:swap;}}
@font-face{{font-family:'Lora';src:{LORA};font-weight:400 700;font-style:normal;font-display:swap;}}
@font-face{{font-family:'Lora';src:{LORAI};font-weight:400 700;font-style:italic;font-display:swap;}}
@font-face{{font-family:'Metam';src:{METAM};font-weight:400;font-display:swap;}}
"""

CSS = """
:root{
  --void:#0d0807;--void2:#150d0a;
  --parch:#ece0c4;--parch-d:#ddcaa2;--parch-dd:#cdb682;
  --ink:#241a10;--ink2:#4c3a28;--ink3:#6b5640;
  --oxblood:#8a1c16;--oxblood-d:#5d120e;--crimson:#b3261d;
  --gold:#9a7a32;--gold-b:#c4a04c;--edge:#bc9c66;
  --rule:rgba(138,28,22,.26);
  --shadow:0 40px 90px -30px rgba(0,0,0,.9);
}
*{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%;}
body{font-family:'Lora',Georgia,serif;color:var(--ink);line-height:1.72;background:var(--void);
  -webkit-font-smoothing:antialiased;}
body::before{content:"";position:fixed;inset:0;z-index:0;pointer-events:none;
  background:radial-gradient(125% 75% at 50% -10%,rgba(150,28,22,.30),transparent 55%),
    radial-gradient(100% 80% at 50% 115%,rgba(90,17,14,.20),transparent 60%),
    linear-gradient(180deg,#0d0807,#0a0605);}
img{display:block;max-width:100%;}
::selection{background:var(--oxblood);color:var(--parch);}

/* ---- araç çubuğu (yalnız web) ---- */
.bar{position:fixed;top:0;left:0;right:0;z-index:40;display:flex;justify-content:space-between;align-items:center;
  padding:13px 22px;background:linear-gradient(180deg,rgba(10,6,5,.92),rgba(10,6,5,.0));backdrop-filter:blur(3px);}
.bar .bk{font-family:'Metam',serif;font-size:.66rem;letter-spacing:.28em;text-transform:uppercase;color:#caa86e;
  display:inline-flex;gap:9px;align-items:center;}
.bar .bk:hover{color:var(--gold-b);}
.bar .pr{font-family:'Metam',serif;font-size:.64rem;letter-spacing:.2em;text-transform:uppercase;cursor:pointer;
  color:#f0dcae;background:rgba(20,12,10,.7);border:1px solid rgba(184,146,63,.5);padding:9px 16px;border-radius:2px;
  display:inline-flex;gap:8px;align-items:center;transition:.25s;}
.pr:hover{color:#fff;border-color:rgba(197,48,42,.7);background:rgba(46,16,14,.85);}
.pr svg,.bk svg{width:14px;height:14px;}

/* ---- akış kabı: tomus yaprakları ---- */
.book{position:relative;z-index:1;max-width:1040px;margin:0 auto;padding:30px 18px 80px;}
.page{position:relative;}

/* parşömen yaprak */
.leaf{position:relative;background-color:var(--parch);
  background-image:linear-gradient(180deg,rgba(255,250,236,.5),rgba(205,182,130,.18)),url(--TILE--);
  background-size:auto,760px;background-blend-mode:normal,multiply;
  border:1px solid var(--edge);border-radius:3px;box-shadow:var(--shadow);
  padding:62px 64px 70px;margin-bottom:34px;overflow:hidden;}
.leaf::before{content:"";position:absolute;inset:0;pointer-events:none;border-radius:3px;
  box-shadow:inset 0 0 120px rgba(90,60,28,.28),inset 0 0 0 1px rgba(120,90,50,.18);
  background:radial-gradient(120% 90% at 50% 40%,transparent 60%,rgba(74,46,18,.16));}
.leaf>*{position:relative;z-index:1;}

/* ---- KAPAK ---- */
.cover{min-height:calc(100vh - 60px);border-radius:4px;overflow:hidden;display:flex;flex-direction:column;
  justify-content:flex-end;align-items:center;text-align:center;position:relative;border:1px solid var(--edge);
  box-shadow:var(--shadow);margin-bottom:34px;background:#1a0606;}
.cover .art{position:absolute;inset:0;background:url(--COVER--) center/cover no-repeat;}
.cover .art::after{content:"";position:absolute;inset:0;
  background:radial-gradient(80% 60% at 50% 34%,transparent,rgba(8,3,3,.30) 78%),
    linear-gradient(180deg,rgba(8,3,3,.55) 0%,transparent 24%,transparent 50%,rgba(8,3,3,.72) 86%,rgba(8,3,3,.95));}
.cover .ci{position:relative;z-index:2;padding:0 24px 8vh;width:100%;}
.cover .badge{font-family:'Metam',serif;font-size:.62rem;letter-spacing:.34em;text-transform:uppercase;
  color:#e7c98e;border:1px solid rgba(214,178,110,.5);background:rgba(12,6,5,.5);backdrop-filter:blur(2px);
  padding:6px 15px;border-radius:2px;display:inline-block;margin-bottom:34px;}
.cover h1{font-family:'Gren',serif;font-weight:500;color:#f3e7cf;line-height:.84;letter-spacing:.02em;
  font-size:clamp(3.6rem,15vw,10rem);
  text-shadow:0 0 50px rgba(197,48,42,.6),0 3px 1px rgba(0,0,0,.8),0 0 14px rgba(0,0,0,.7);}
.cover .gr{display:flex;align-items:center;justify-content:center;gap:16px;margin:18px auto 14px;max-width:560px;}
.cover .gr i{height:1px;flex:1;background:linear-gradient(90deg,transparent,var(--gold-b));}
.cover .gr i:last-child{background:linear-gradient(90deg,var(--gold-b),transparent);}
.cover .gr svg{width:20px;height:20px;color:var(--gold-b);filter:drop-shadow(0 0 6px rgba(196,160,76,.6));}
.cover .sub{font-family:'Gren',serif;font-weight:500;font-size:clamp(1.5rem,5vw,2.7rem);letter-spacing:.22em;
  color:#e6c884;text-shadow:0 0 22px rgba(196,160,76,.5),0 2px 0 rgba(0,0,0,.7);}
.cover .tag{font-style:italic;font-size:clamp(1rem,2.4vw,1.3rem);color:#e9d6b4;margin-top:20px;
  text-shadow:0 1px 8px rgba(0,0,0,.8);}

/* ---- bölüm başlıkları ---- */
.kicker{font-family:'Metam',serif;font-size:.66rem;letter-spacing:.34em;text-transform:uppercase;
  color:var(--gold);display:block;margin-bottom:8px;}
h2.sec{font-family:'Gren',serif;font-weight:500;font-size:clamp(2rem,5vw,3rem);color:var(--oxblood);
  line-height:.98;letter-spacing:.015em;margin:0 0 6px;}
.sec-rule{display:flex;align-items:center;gap:13px;margin:0 0 22px;}
.sec-rule i{height:2px;flex:1;background:linear-gradient(90deg,var(--oxblood),transparent);max-width:200px;}
.sec-rule svg{width:15px;height:15px;color:var(--gold-b);transform:rotate(45deg);}
.sec-block{margin:0 0 34px;}
.sec-block+.sec-block{margin-top:8px;}

p{margin:0 0 14px;}
.lead{font-size:1.08rem;}
strong,b{color:var(--oxblood-d);font-weight:700;}
.slogan{font-family:'Gren',serif;font-weight:500;font-size:1.5rem;color:var(--oxblood);letter-spacing:.01em;margin:0 0 14px;}

/* iki sütun gövde */
.cols{columns:2;column-gap:40px;}
.cols>p{margin:0 0 14px;break-inside:avoid-column;}
.cols.one{columns:1;}

/* tezhip ilk-harf */
.dropcap::first-letter{font-family:'Gren',serif;font-weight:500;color:var(--oxblood);
  font-size:3.5em;line-height:.72;float:left;margin:.04em .09em -.06em 0;text-shadow:0 2px 0 rgba(120,40,20,.18);}

/* yemin (şiir) */
.oath{position:relative;margin:0 auto 30px;max-width:560px;text-align:center;font-style:italic;
  color:var(--ink2);font-size:1.12rem;line-height:1.95;padding:18px 30px;}
.oath::before,.oath::after{content:"";position:absolute;left:50%;transform:translateX(-50%);width:120px;height:1px;
  background:linear-gradient(90deg,transparent,var(--gold),transparent);}
.oath::before{top:0;}.oath::after{bottom:0;}
.oath b{display:block;font-style:normal;font-family:'Gren',serif;font-weight:500;color:var(--oxblood);
  font-size:1.15rem;letter-spacing:.04em;margin-top:10px;}

/* madde */
ul.bul{list-style:none;margin:0 0 14px;padding:0;}
ul.bul li{position:relative;padding-left:22px;margin-bottom:7px;}
ul.bul li::before{content:"";position:absolute;left:3px;top:.62em;width:7px;height:7px;transform:rotate(45deg);
  background:var(--oxblood);}

/* callout kutusu — Oyun Modları */
.callout{position:relative;background:linear-gradient(180deg,rgba(120,86,40,.14),rgba(94,64,28,.20));
  border:1.5px solid var(--gold);border-radius:5px;padding:24px 28px 20px;margin:8px 0 30px;
  box-shadow:inset 0 0 40px rgba(120,80,30,.14);}
.callout::before,.callout::after{content:"";position:absolute;width:14px;height:14px;border:2px solid var(--oxblood);}
.callout::before{top:6px;left:6px;border-right:none;border-bottom:none;}
.callout::after{bottom:6px;right:6px;border-left:none;border-top:none;}
.callout h3{font-family:'Gren',serif;font-weight:500;font-size:1.55rem;color:var(--oxblood);margin:0 0 10px;letter-spacing:.02em;}
.callout p{margin:0 0 10px;}
.callout .mode{color:var(--oxblood-d);font-family:'Gren',serif;font-weight:500;font-size:1.12rem;letter-spacing:.01em;}

/* ilk adımlar + QR */
.first{display:grid;grid-template-columns:1fr 168px;gap:30px;align-items:start;}
.first .qr{background:#fff;border:1px solid var(--edge);border-radius:6px;padding:11px;box-shadow:0 10px 26px -12px rgba(0,0,0,.5);}
.first .qr img{width:100%;image-rendering:pixelated;}
.first .qrcap{font-family:'Metam',serif;font-size:.56rem;letter-spacing:.18em;text-transform:uppercase;
  color:var(--ink3);text-align:center;margin-top:9px;}

/* İÇİNDEKİLER */
.toc{columns:2;column-gap:46px;margin-bottom:8px;}
.toc .row{display:flex;align-items:baseline;gap:6px;break-inside:avoid;margin-bottom:3px;}
.toc .row.grp{margin-top:13px;}
.toc .row.grp .t{font-family:'Gren',serif;font-weight:500;font-size:1.12rem;color:var(--oxblood);letter-spacing:.01em;}
.toc .row.sub .t{padding-left:16px;color:var(--ink2);font-size:.93rem;}
.toc .t{white-space:nowrap;}
.toc .row a.t{color:inherit;border-bottom:1px solid transparent;}
.toc .row a.t:hover{border-color:var(--oxblood);}
.toc .dots{flex:1;border-bottom:1.5px dotted rgba(120,90,50,.5);transform:translateY(-3px);min-width:14px;}
.toc .pg{font-family:'Metam',serif;font-size:.78rem;color:var(--ink3);letter-spacing:.04em;}
.toc .row.grp .pg{color:var(--oxblood);}

/* KÜNYE */
.credits{columns:3;column-gap:30px;font-size:.82rem;line-height:1.5;color:var(--ink2);}
.credits .c{break-inside:avoid;margin-bottom:11px;}
.credits .cl{font-family:'Metam',serif;font-size:.6rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--oxblood-d);display:block;margin-bottom:1px;}

/* folyo */
.folio{position:absolute;bottom:24px;font-family:'Gren',serif;font-size:1.05rem;color:var(--oxblood);opacity:.8;}
.folio.l{left:64px;}.folio.r{right:64px;}

/* süs ayraç (bölümler arası) */
.divider{display:flex;align-items:center;justify-content:center;gap:14px;margin:6px 0 30px;}
.divider i{height:1px;width:80px;background:linear-gradient(90deg,transparent,var(--gold));}
.divider i:last-child{background:linear-gradient(90deg,var(--gold),transparent);}
.divider svg{width:22px;height:22px;color:var(--oxblood);}

/* ===== BİLEŞENLER (s.4-5) ===== */
.comp-grid{display:grid;grid-template-columns:1fr 1fr;gap:30px 38px;margin-bottom:6px;}
.comp.full{grid-column:1/-1;}
.comp{display:flex;flex-direction:column;}
.comp-h{display:flex;align-items:center;gap:11px;margin-bottom:10px;}
.comp-h .cnt{font-family:'Gren',serif;font-weight:500;font-size:1.3rem;color:#f3e7cf;background:var(--oxblood);
  min-width:1.85em;height:1.85em;padding:0 .3em;display:inline-flex;align-items:center;justify-content:center;
  border-radius:3px;box-shadow:0 3px 9px -3px rgba(90,17,14,.75);}
.comp-h h3{font-family:'Gren',serif;font-weight:500;font-size:1.45rem;color:var(--oxblood);letter-spacing:.01em;line-height:1;}
.plate{width:100%;height:auto;display:block;}
.plate+.plate{margin-top:7px;}
.comp .items{font-size:.85rem;color:var(--ink2);margin:11px 0 0;line-height:1.55;}
.comp .items b{color:var(--oxblood-d);font-weight:700;}
.comp .note{display:block;font-style:italic;font-size:.74rem;color:var(--ink3);margin-top:4px;}
.grp-h{font-family:'Gren',serif;font-weight:500;font-size:1.7rem;color:var(--oxblood);margin:32px 0 18px;
  display:flex;align-items:center;gap:13px;letter-spacing:.01em;}
.grp-h::after{content:"";flex:1;height:2px;background:linear-gradient(90deg,var(--rule),transparent);}

/* ===== KURULUM (s.6) ===== */
.setup-grid{display:grid;grid-template-columns:1fr 1fr;gap:30px 42px;align-items:start;}
.blk h3.sub{font-family:'Gren',serif;font-weight:500;font-size:1.5rem;color:var(--oxblood);margin:0 0 9px;}
.blk+.blk{margin-top:20px;}
.steps{list-style:none;counter-reset:stp;padding:0;margin:0;}
.steps>li{position:relative;padding-left:48px;margin-bottom:16px;overflow:hidden;}
.steps>li::before{counter-increment:stp;content:counter(stp);position:absolute;left:0;top:-2px;
  font-family:'Gren',serif;font-size:1.1rem;color:#f3e7cf;background:var(--oxblood);width:32px;height:32px;
  display:flex;align-items:center;justify-content:center;border-radius:50%;box-shadow:0 3px 8px -3px rgba(90,17,14,.7);}
.steps .nm{font-weight:700;color:var(--oxblood-d);}
.pc{list-style:none;margin:9px 0 0;padding:0;font-size:.92rem;}
.pc li{position:relative;padding-left:34px;margin-bottom:5px;}
.pc .n{position:absolute;left:0;top:.05em;font-family:'Metam',serif;font-size:.62rem;letter-spacing:.05em;
  background:var(--ink);color:var(--parch);border-radius:3px;padding:2px 7px;}
.diag{float:right;width:92px;margin:2px 0 6px 14px;}
.diag img{width:100%;filter:drop-shadow(0 6px 14px rgba(0,0,0,.4));}
.diag .cap{font-family:'Metam',serif;font-size:.5rem;letter-spacing:.1em;text-transform:uppercase;
  color:var(--ink3);text-align:center;margin-top:4px;}

/* ============ RESPONSIVE ============ */
@media(max-width:820px){
  .comp-grid,.setup-grid{grid-template-columns:1fr;}
  .cols{columns:1;}.toc{columns:1;}.credits{columns:2;}
  .leaf{padding:42px 26px 56px;}
  .folio.l{left:26px;}.folio.r{right:26px;}
  .first{grid-template-columns:1fr;justify-items:center;}
  .first .qr{max-width:200px;}
}
@media(max-width:480px){
  .book{padding:14px 10px 50px;}
  .credits{columns:1;}
  .leaf{padding:34px 20px 50px;border-radius:2px;}
  .oath{padding:14px 6px;font-size:1rem;}
  .cover{min-height:86vh;}
}

/* ============ A3 BASKI ============ */
@media print{
  @page{size:A3 portrait;margin:18mm 17mm;}
  @page cover{margin:0;}
  html,body{background:#fff;}
  body::before{display:none;}
  .bar{display:none !important;}
  .book{max-width:none;margin:0;padding:0;}
  .cover{page:cover;break-after:page;min-height:0;height:417mm;width:297mm;border:none;border-radius:0;
    box-shadow:none;margin:0;overflow:hidden;}
  .cover .ci{padding-bottom:46mm;}
  .leaf{break-before:page;border:none;border-radius:0;box-shadow:none;margin:0;min-height:0;
    padding:6mm 7mm 14mm;background-color:#ece0c4;}
  .leaf::before{box-shadow:inset 0 0 0 1px rgba(120,90,50,.25);background:none;}
  .cols{columns:2;column-gap:14mm;}
  .toc{columns:2;}.credits{columns:3;}
  .callout,.toc .row,.cols>p,.credits .c,.oath,.first{break-inside:avoid;}
  .comp,.steps>li,.grp-h{break-inside:avoid;}
  .comp-grid{gap:8mm 12mm;}
  .folio.l{left:6mm;}.folio.r{right:6mm;}
  *{-webkit-print-color-adjust:exact;print-color-adjust:exact;}
}
""".replace('--TILE--', TILE).replace('--COVER--', COVER)

# flourish svg
DIA = '<svg viewBox="0 0 32 32" fill="currentColor"><path d="M16 1l2.4 11.6L28 16l-9.6 3.4L16 31l-2.4-11.6L4 16l9.6-3.4z"/></svg>'

def sechead(kicker, title):
    return (f'<span class="kicker">{kicker}</span><h2 class="sec">{title}</h2>'
            f'<div class="sec-rule"><i></i>{DIA}</div>')

# ---------------- İÇİNDEKİLER ----------------
TOC = [
 ('grp','Grimcoven Nedir?','3','#nedir'),('grp','Kazanmak ya da Kaybetmek','3','#kazan'),
 ('grp','Bileşenlere Genel Bakış','4','#bilesenler'),('grp','Oyun Kurulumu','6','#kurulum'),
 ('grp','Tura Genel Bakış','11',''),
 ('grp','Avcı Aşaması','11',''),('sub','Avcı zarları','11',''),('sub','Zar yuvaları','11',''),
 ('sub','Eylemleri Çözme ve Eylem Türleri','12',''),('sub','Yara Verme','13',''),
 ('sub','Savunma ve Taktik jetonları','13',''),
 ('grp','Düşman Aşaması','14',''),('sub','Olaylar','14',''),('sub','Uşaklar','15',''),
 ('sub','Seçkin Düşmanlar','16',''),('sub','Griefbound','18',''),
 ('grp','Lament Aşaması','21',''),('sub','Yozlaşma adımı','21',''),('sub','Nihai Mahvoluş','21',''),
 ('sub','Evrim adımı','21',''),
 ('grp','Tazeleme Aşaması','22',''),('sub','Tazeleme adımı','22',''),('sub','Durum adımı','22',''),
 ('sub','Durumlar ve Açlık','22',''),
 ('grp','Diğer Kurallar','23',''),
 ('grp','Harita','23',''),('sub','Arazi ve özel alanlar','23',''),('sub','Çevre','24',''),
 ('sub','Kritik Yaralanma ve Avcı Ölümü','25',''),('sub','Sırlar','25',''),('sub','Yoldaşlar','25',''),
 ('sub','Senaryo Sonu','25',''),
 ('grp','Avcılar','26',''),('sub','Avcıya özel kurallar','27',''),
 ('grp','Oyun Modları','30','#modlar'),('grp','Pretender’lar','31',''),('grp','Sözlük','33',''),
 ('grp','Sonsöz','34',''),('grp','Av Kitabı','35',''),('grp','Anahtar Sözcükler','36',''),
 ('grp','İkonlar','36',''),('grp','Jetonlar','36',''),
]
def toc_html():
    out=[]
    for kind,t,pg,href in TOC:
        cls='row grp' if kind=='grp' else 'row sub'
        title=f'<a class="t" href="{href}">{t}</a>' if href else f'<span class="t">{t}</span>'
        out.append(f'<div class="{cls}">{title}<span class="dots"></span><span class="pg">{pg}</span></div>')
    return '<div class="toc">'+''.join(out)+'</div>'

# ---------------- KÜNYE ----------------
CREDITS = [
 ('Oyun','Krzysztof Belczyk'),
 ('Ürün Sorumlusu','Marcin Świerkot, Michał Matłosz'),
 ('Oyun Tasarımı','Krzysztof Belczyk'),
 ('Baş Geliştirici','Wojciech Zieliński'),
 ('Test ve Geliştirme','Michał Oracz, Piotr Chmielewski, Paulina Włodarczyk, Tomasz Zawadzki'),
 ('Dahili Test','Konrad Sulżycki, Wojciech Frelich, Michał Lach, Andrzej Betkiewicz, Filip Tomaszewski, Ernest Kiedrowicz, Andrzej Chojnowski, Dawid Kozłowski, Mikołaj Kaczmarczyk, Aleksandra Fajlert-Kaluża, Kinga Janik'),
 ('Ek Test','Konrad Kozłowski, Szymon Tęcza, Michał Dzik, Wojciech Tomczuk, Łukasz Szczepanowski, Weronika Sobota, Paweł Brzozowski, Karol Lipski, Szymon Dominicki, Przemysław Golus, Grzegorz Dubec, Diego García, Marcin Ciućmański, Rigo Garcia, Szymon Sobota, Karolina Ścisłowicz, Alain Concepcion, Magdalena Romantowska, Olha Symon, Silvia Rodríguez, Ashley Hightower, Hanna Andrushchyshyna, Mateusz Wójcik, Filip Szawica, Rafał Kaczmarczyk, Martin Kielesiński, Michał Plata, Szymon Kulka, Krzysztof Piechnik, Jakub Błachut, Tymoteusz Hatala, Franciszek Stępniewski-Janowski, Łukasz Jach, Zuzanna Banasiak, Weronika Tiesler, Adrian Przednówek, Błażej Bernaś, Anna Lis-Wilkosz, Tymoteusz Muller, Marta Siennicka, Łukasz Styrna'),
 ('Anlatı Tasarımı','Marcin Mortka, Krzysztof Belczyk, Wojciech Zieliński'),
 ('Metin Yazımı','Marcin Mortka, Krzysztof Piskorski, Andrzej Betkiewicz'),
 ('Redaksiyon','Tyler Brown, Daniel Morley, Anna Merriman, Wiktoria Ślusarczyk'),
 ('Sanat Yönetmenliği','Patryk Jędraszek, Adrian Radziun'),
 ('Grafik Tasarım','Adrian Radziun, Aleksandra Fajlert-Kaluża, Michał Lechowski, Michał Oracz, Bartosz Fąfrowicz, Karolina Łaski-Getka, Łukasz Styrna, Michał Stachowiak'),
 ('İllüstrasyonlar','Jakub Dzikowski, Ewa Labak, Piotr Foksowicz, Piotr Orleański, Pamela Łuniewska, Patryk Jędraszek, Magdalena Cieplak, Krzysztof Piasek, Jakub Witowski, Aleksander Brodziński, Maciej Łaszkiewicz, Agnieszka Szade'),
 ('Karakter Tasarımı','Ewa Labak, Patryk Jędraszek, Agnieszka Szade, Piotr Orleański'),
 ('3B Modelleme','Piotr Gacek, Marek Kondratowicz, Michał Lisek, Mateusz Modzelewski, Mateusz Wajda, Jędrzej Chomicki'),
 ('Dizgi (DTP)','Kinga Janik, Patrycja Marzec, Rafał Janiszewski, Jędrzej Cieślak, Aneta Koperkiewicz, Katarzyna Janik, Angelika Kajmowicz, Alicja Filip'),
 ('Üretim','Jacek Szczypiński, Witold Chudy, Olga Baraniak, Zofia Jerzyńska, Mateusz Wolski, Michał Matłosz'),
 ('Lojistik','Katarzyna Grdeń, Sebastian Nowakowski, Michał Kot, Magdalena Kazuń, Szymon Sobczak, Łukasz Puła'),
 ('Halkla İlişkiler ve İletişim','Maciej Guzik-Pałys, Dominika Maksymiak, Marta Siennicka, Jacek Wala'),
 ('Müşteri Desteği','Katarzyna Dabiach, Alicja Wojciechowska, Grzegorz Janusz, Bartłomiej Giercarz'),
 ('Proje Yönetimi','Piotr Chmielewski, Anna Czajka, Adrianna Kocięcka'),
 ('Manevi Destek','Anna Lis-Wilkosz, Jordan Luminais, Kamil Cieśla, Paweł Samborski'),
 ('Özel Teşekkürler','Andrzej Klimek, Martin Fučík, Matthias Schrammek, Michał “Niedzwiedz” Michalski, Georgi “Grebeny” Teofilov, Michał Szewczyk, Filip Cyrus Madej ve oyunun yaratılışı ile geliştirilmesi sırasında bize destek olan herkese, özellikle de harika Discord Topluluğumuza!'),
]
def credits_html():
    out=[f'<div class="c"><span class="cl">{l}</span>{n}</div>' for l,n in CREDITS]
    return '<div class="credits">'+''.join(out)+'</div>'

# ---------------- İÇERİK ----------------
HTML = f"""<!DOCTYPE html>
<html lang="tr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Grimcoven — Kural Kitabı (Türkçe)</title>
<style>{FACE}{CSS}</style></head>
<body>
<div class="bar">
  <a class="bk" href="../../site/grimcoven.html"><svg viewBox="0 0 24 16" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M22 8H3M9 2L3 8l6 6"/></svg>Grimcoven</a>
  <button class="pr" type="button" onclick="window.print()"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M6 9V3h12v6M6 18H4v-7h16v7h-2M8 14h8v8H8z"/></svg>A3 Yazdır / PDF</button>
</div>

<div class="book">

  <!-- ===== KAPAK (s.1) ===== -->
  <section class="cover page">
    <div class="art"></div>
    <div class="ci">
      <span class="badge">Gayriresmî Türkçe Sürüm</span>
      <h1>GRIMCOVEN</h1>
      <div class="gr"><i></i>{DIA}<i></i></div>
      <div class="sub">KURAL KİTABI</div>
      <p class="tag">“Avı başlat. Ya da uğruna öl.”</p>
    </div>
  </section>

  <!-- ===== s.2 — İÇİNDEKİLER + KÜNYE ===== -->
  <section class="leaf page" id="icindekiler">
    <div class="sec-block">
      {sechead('Tomus', 'İçindekiler')}
      {toc_html()}
    </div>
    <div class="divider"><i></i>{DIA}<i></i></div>
    <div class="sec-block">
      {sechead('Emeği Geçenler', 'Künye')}
      {credits_html()}
    </div>
    <span class="folio r">2</span>
  </section>

  <!-- ===== s.3 — GRIMCOVEN NEDİR? / KAZANMAK / İLK ADIMLAR ===== -->
  <section class="leaf page" id="nedir">
    <div class="sec-block">
      {sechead('Giriş', 'Grimcoven Nedir?')}
      <blockquote class="oath">
        Hür irademle ve aklı başında, bu ağır yemini ediyorum.<br>
        Kendimi büyük Av’a adıyorum.<br>
        Korku karşısında sarsılmayacağım.<br>
        Ölüm karşısında son nefesime dek savaşacağım.<br>
        Lament beni çağırdığında, baştan çıkmaya direneceğim.<br>
        Ve bu kutsal yemine sadık kalamazsam,<br>
        kardeşlerimden başıma bir ödül koymalarını dilerim.<br>
        <b>Böyle diyorum ben, Grimcoven’in avcısı.</b>
      </blockquote>
      <div class="cols">
        <p class="dropcap"><strong>Grimcoven</strong>, RPG ögeleri taşıyan acımasız bir boss-savaşı oyunudur. Her oyun, mevcut havuzdan seçilen çok sayıda Senaryo’dan birine dayanır. Her Senaryo farklı bir dünya, farklı kurallar, farklı tehditler sunar — ama amaç hep aynı kalır: Griefbound’u alt et, hayatta kal ve Lament’in baştan çıkarıcı gücüne boyun eğme.</p>
        <p>Her oyunda korkunç bir varlıkla — bir <strong>Griefbound</strong> ile — karşılaşırsınız; ona bir <strong>Seçkin Düşman</strong> ile gölgelerden ve gerçekliğin çatlaklarından türeyen bitmek bilmez aşağılık <strong>Uşak</strong> sürüleri eşlik eder.</p>
        <p>Her tur bir zar atışıyla başlar — atışların sonuçları sizin kaynaklarınız olur. Bunları Eylemleri etkinleştirmek, yetenekleri tetiklemek ve hayatta kalmak — elbette zafer kazanmak — için en iyi stratejiyi kurmak üzere harcarsınız.</p>
        <p>Düşmanlarla savaşarak ve ağzını açmış <strong>Rift</strong>’leri keşfederek <strong>Lament</strong> toplarsınız — acıyla beslenen, gizemli, nabız gibi atan bir madde. Lament size hayal gücünüzün ötesinde bir güç bahşeder; ama her damlası sizi biraz daha yozlaştırarak geri dönüşü olmayan o noktaya, savaştıklarınızın dünyasına katılacağınız ana yaklaştırır.</p>
        <p>Lament, yetenekler geliştirmenizi ve yeni Eylem kartları ile zarlar satın almanızı sağlar; ama aynı zamanda insanlığınızı da koparıp alır. Yine de bu savaşta geri duramazsınız, çünkü düşmanlarınız da her geçen turla güçlenir.</p>
        <p>Bu sizin mesleğiniz. Bu sizin dünyanız: tehlikeler ve fedakârlıklarla dolu. Bir <strong>Avcı</strong> grubu toplayın. <strong>Silah</strong>larınızı ve <strong>Zırh</strong>larınızı seçin. Ava başlayın, ama daha ilk adımlardan amansız bir mücadeleye hazır olun. Bazen biri daha ilk turda dizlerinin üstüne çöker — bu acımasız dünyada beklenmedik bir şey değildir. En baştan beri ölümün eşiğinde dengede durursunuz. Bazıları, hatta birçoğu, avdan hiç dönmeyebilir.</p>
        <p>Savaş alanı yalnızca harabe ve kandan ibaret değildir. <strong>Arazi</strong> çeşitlidir; dengeleri tersine çevirebilecek tuhaflıklarla doludur. Ormanların, bataklıkların ya da çatlamış toprağın arasında, Haritanın farklı yerlerini birbirine bağlayan kadim <strong>Portal</strong>lar; değerli bulgu ve aletlerle ağzına kadar dolu <strong>Hazine</strong>ler; hatta bazen kayıp karakterler, gizemli makineler, unutulmuş harabeler ya da ürkütücü güç noktaları bulursunuz. Doğru anda kullanıldıklarında, savaşın gidişatını değiştirebilirler… ya da sizi değiştirebilirler.</p>
      </div>
    </div>

    <div class="sec-block" id="kazan">
      {sechead('Amaç', 'Kazanmak ya da Kaybetmek')}
      <p class="slogan">Griefbound’u avla. Ya da uğruna öl.</p>
      <p>Oyun, ya Avcılar Griefbound’u öldürdüğünde ya da kaybetme koşullarından biri sağlandığında sona erer:</p>
      <ul class="bul">
        <li>Avcıların vakti dolar (Olay destesi boşken bir Olay kartı çekilmesi gerekir).</li>
        <li>Avcılardan biri ölür (bkz. s.&nbsp;25).</li>
      </ul>
      <p>Ayrıca her Griefbound, Senaryoya yeni kazanma ya da kaybetme koşulları ekleyebilir. Her Senaryonun ardından, Avcıların kazanıp kazanmadığına göre uygun bir <strong>Sonsöz</strong> okunmalıdır.</p>

      <aside class="callout" id="modlar">
        <h3>Oyun Modları</h3>
        <p>Grimcoven, oyuncuların deneyimlerini diledikleri gibi şekillendirmesine olanak tanır. Uzunluk bakımından iki ana oyun modu vardır:</p>
        <p><span class="mode">Uzun Av</span> — tahminen 2-4 saatte oynanır; Avın erken, orta ve geç evrelerini baştan sona oynamanızı sağlar. Sonraki sayfalardaki kurulum talimatları bu modun nasıl hazırlanacağını anlatır.</p>
        <p><span class="mode">Hızlı Av</span> — tahminen 1-2 saatte oynanır. Avcılar ve Griefbound, panodaki durum çoktan kızışmışken oyunun ortasından başlar. Bu mod, Uzun Av kurulumunun ardından birkaç değişiklik gerektirir ve başlangıçta biraz daha karmaşıktır.</p>
        <p>Bunların yanı sıra, Oyuncu tercihlerine göre oyunu zorlaştıracak ya da kolaylaştıracak birçok ek seçenek vardır. <strong>Kolay mod</strong>, <strong>Zor mod</strong> ya da <strong>Hızlı Av</strong> seçeneklerinin kurulumuna dair tüm bilgiler s.&nbsp;30’da anlatılmıştır.</p>
      </aside>
    </div>

    <div class="sec-block">
      {sechead('Başlangıç', 'İlk Adımlar')}
      <div class="first">
        <div>
          <p>Oyunun temellerini daha iyi kavramak için, bileşenleri Ana Kutu’da nasıl düzenleyeceğinizi ve Grimcoven’i nasıl oynayacağınızı öğreten videolarımızı izlemenizi öneririz.</p>
          <p>Videoları izlemek için yandaki QR kodu okutun. Sizi web sayfamızdaki Grimcoven video arşivine yönlendirecektir.</p>
        </div>
        <div>
          <div class="qr"><img src="{QR}" alt="QR kod — Grimcoven video arşivi"></div>
          <div class="qrcap">Video Arşivi</div>
        </div>
      </div>
    </div>
    <span class="folio r">3</span>
  </section>

  <!-- ===== s.4 — BİLEŞENLERE GENEL BAKIŞ ===== -->
  <section class="leaf page" id="bilesenler">
    <div class="sec-block">
      {sechead('Kutu İçeriği', 'Bileşenlere Genel Bakış')}
      <div class="comp-grid">
        <div class="comp"><div class="comp-h"><span class="cnt">7</span><h3>Pano</h3></div>
          <img class="plate" src="{P4['boards']}" alt="Panolar">
          <p class="items"><b>1</b> Griefbound panosu · <b>5</b> Avcı panosu · Yardımcı panosu (solo)
            <span class="note">* Sürüme göre tek ya da çift katmanlı panolar.</span></p></div>
        <div class="comp"><div class="comp-h"><h3>Kitaplar</h3></div>
          <img class="plate" src="{P4['books']}" alt="Kitaplar">
          <p class="items"><b>6</b> Av Kitabı · Öğretici Senaryo kitapçığı · Bu Kural Kitabı · Av Çizelgesi</p></div>
        <div class="comp"><div class="comp-h"><h3>İşaretleyiciler</h3></div>
          <img class="plate" src="{P4['markers']}" alt="İşaretleyiciler">
          <p class="items"><b>5</b> Yozlaşma · <b>5</b> Assist · <b>10</b> Evrensel işaretleyici
            <span class="note">* Karton ya da plastik.</span></p></div>
        <div class="comp"><div class="comp-h"><span class="cnt">66</span><h3>Zar</h3></div>
          <img class="plate" src="{P4['dice']}" alt="Zarlar">
          <p class="items"><b>60</b> Avcı zarı (4 renk) · <b>4</b> Düşman zarı · <b>2</b> Teknoloji zarı</p></div>
        <div class="comp"><div class="comp-h"><span class="cnt">30</span><h3>Harita Parçası</h3></div>
          <img class="plate" src="{P4['maptiles']}" alt="Harita parçaları">
          <p class="items"><b>23</b> Arazi parçası (Orman, Bataklık, Mezarlık, Nehir, Sis, Engel, Derin su, Köprü) · <b>2</b> Bölge Çevre · <b>4</b> İşkence Aleti / Sürü · <b>1</b> Mide parçası
            <span class="note">* çift taraflı</span></p></div>
        <div class="comp"><div class="comp-h"><h3>Avcı Parçaları</h3></div>
          <img class="plate" src="{P4['huntertiles']}" alt="Avcı parçaları">
          <p class="items"><b>6</b> Avcı parçası</p></div>
        <div class="comp full"><div class="comp-h"><h3>Modeller</h3></div>
          <img class="plate" src="{P4['models1']}" alt="Modeller — 1. sıra">
          <img class="plate" src="{P4['models2']}" alt="Modeller — 2. sıra">
          <p class="items"><b>6</b> Griefbound · <b>6</b> Avcı · <b>6</b> Yozlaşmış Avcı · <b>4</b> Seçkin Düşman · <b>16</b> Uşak · <b>4</b> Portal · <b>7</b> Yoldaş ayaklığı + <b>1</b> Yoldaş modeli · <b>12</b> Çevre ayaklığı
            <span class="note">* Sürüme göre minyatür ya da ayaklık; her durumda “model” olarak anılır.</span></p></div>
      </div>
      <span class="folio l">4</span>
    </div>
  </section>

  <!-- ===== s.5 — KARTLAR + JETONLAR ===== -->
  <section class="leaf page" id="kartlar">
    <div class="sec-block">
      {sechead('Kutu İçeriği', 'Kartlar ve Jetonlar')}
      <h3 class="grp-h">Kartlar</h3>
      <div class="comp-grid">
        <div class="comp"><div class="comp-h"><h3>Özel Kartlar</h3></div>
          <img class="plate" src="{P5['c_custom']}" alt="Özel kartlar">
          <p class="items"><b>36</b> Griefbound Stat kartı · <b>6</b> Yardımcı Stat kartı · <b>20</b> Ayraç</p></div>
        <div class="comp"><div class="comp-h"><h3>Büyük Boy Kartlar</h3></div>
          <img class="plate" src="{P5['c_oversized']}" alt="Büyük boy kartlar">
          <p class="items"><b>10</b> Yardım kartı · <b>12</b> Seçkin Düşman kartı</p></div>
      </div>
      <h3 class="grp-h">Standart Kartlar</h3>
      <div class="comp-grid">
        <div class="comp"><img class="plate" src="{P5['std1']}" alt="">
          <p class="items"><b>167</b> Avcı Evrim · <b>58</b> Avcı Eşya · <b>21</b> Olay kartı</p></div>
        <div class="comp"><img class="plate" src="{P5['std2']}" alt="">
          <p class="items"><b>25</b> Çevre · <b>222</b> Saldırı · <b>36</b> Son Saldırı kartı</p></div>
        <div class="comp"><img class="plate" src="{P5['std3']}" alt="">
          <p class="items"><b>36</b> Fırsat · <b>48</b> Evre · <b>32</b> Uşak kartı</p></div>
        <div class="comp"><img class="plate" src="{P5['std4']}" alt="">
          <p class="items"><b>20</b> Yozlaşma · <b>56</b> Sır · <b>30</b> Diğer kart</p></div>
      </div>
      <h3 class="grp-h">Jetonlar</h3>
      <div class="comp-grid">
        <div class="comp"><img class="plate" src="{P5['tok1']}" alt="">
          <p class="items"><b>20</b> Yara (1, 3, 10) · <b>37</b> Savunma (2, 4) · <b>10</b> Taktik jetonu</p></div>
        <div class="comp"><img class="plate" src="{P5['tok2']}" alt="">
          <p class="items"><b>40</b> Lament · <b>5</b> Tur sırası ayaklığı · <b>15</b> Açlık jetonu</p></div>
        <div class="comp"><img class="plate" src="{P5['tok3']}" alt="">
          <p class="items"><b>45</b> Durum (Yanık, Sersemleme, Lanet) · <b>8</b> Hazine · <b>8</b> Lament Yarığı jetonu</p></div>
        <div class="comp"><img class="plate" src="{P5['tok4']}" alt="">
          <p class="items"><b>4</b> Griefbound Seviye · <b>8</b> Seçkin Düşman Seviye · <b>4</b> Kişilik jetonu</p></div>
        <div class="comp"><img class="plate" src="{P5['tok5']}" alt="">
          <p class="items"><b>6</b> Kanat (3 Beyaz, 3 Siyah) · <b>10</b> Mermi · <b>5</b> İhtiras jetonu</p></div>
        <div class="comp"><img class="plate" src="{P5['tok6']}" alt="">
          <p class="items"><b>2</b> Görev jetonu · İlk Oyuncu jetonu · Meşgul jetonu</p></div>
      </div>
      <span class="folio r">5</span>
    </div>
  </section>

  <!-- ===== s.6 — OYUN KURULUMU ===== -->
  <section class="leaf page" id="kurulum">
    <div class="sec-block">
      {sechead('Hazırlık', 'Oyun Kurulumu')}
      <aside class="callout"><h3>Aç ve Oyna</h3>
        <p>İlk oyun için, bileşenlerin, oyun ögelerinin ve kuralların çoğunda size rehberlik etmesi amacıyla <strong>Öğretici Senaryo kitapçığını</strong> kullanmanızı öneririz.</p></aside>
      <div class="setup-grid">
        <div>
          <div class="blk"><h3 class="sub">Bir Senaryo Seç</h3>
            <p>Av Çizelgesi’ni alın ve bir Griefbound seçin. Her Griefbound’un oynanabilecek <strong>5 Senaryosu</strong> vardır; ilki en kolay, beşincisi en zorudur. Oynamak için bir Senaryo seçin ya da rastgele belirleyin. Seçtiğiniz Griefbound’a ait Av Kitabı’nı alın ve seçilen Senaryo kurulumuna gidin.</p>
            <p>Av Kitabı, ilgili Griefbound’un her Senaryosu için özel kurallarını, Harita düzenlerini ve bileşen listelerini içerir. Ayrıca aşağıdaki kurulum yordamında yer almayan ek kuralları da barındırır.</p></div>
          <div class="blk"><h3 class="sub">Senaryo Kurulumu</h3>
            <p>İlerleyen sayfalarda bir Senaryonun nasıl kurulacağına dair genel açıklamayı bulabilirsiniz. Bu süreç, kullanılan bileşenlerin listesini içermez; bu listeyi her Griefbound için Av Kitabı’nda bulabilirsiniz. İlk kurulumu yaparken Kural Kitabı’nı rehber, Av Kitabı’nı bileşen listesi olarak eşzamanlı kullanın. Bir Senaryoyu kurmaya alıştıktan sonra ihtiyaç duyacağınız tek kaynak Av Kitabı olacaktır.</p></div>
        </div>
        <div>
          <div class="blk"><h3 class="sub">Harita Kurulumu</h3>
            <ol class="steps">
              <li><span class="nm">Haritayı kurun.</span> Haritayı Harita Parçalarından oluşturun. Parçaların üzerindeki kodları ve Av Kitabı’ndaki şemayı kullanın. Çoğu Harita’da, kurulumda sonradan eklenecek, özel ve 3 alanlı bir Çevre parçası bulunur; bu genellikle rastgeledir ve bir soru işaretiyle gösterilir.</li>
              <li><div class="diag"><img src="{P6['diag1']}" alt="Lament Yarığı"><div class="cap">Lament Yarığı</div></div><span class="nm">Lament Yarıkları.</span> Av Kitabı’nda gösterildiği gibi, işaretli alanlara Rift jetonlarını rastgele ve yüzü açık şekilde yerleştirin.</li>
              <li><div class="diag"><img src="{P6['diag2']}" alt="Portal modeli"><div class="cap">Portal modeli</div></div><span class="nm">Portallar.</span> Av Kitabı’nda gösterildiği gibi, Portal simgesi bulunan her alana bir Portal Modeli yerleştirin.</li>
              <li><span class="nm">Lament.</span> Oyuncu sayısına bağlı olarak Haritaya Lament yerleştirin:
                <ul class="pc">
                  <li><span class="n">2 / solo</span> Çift numaralı her Lament Yarığına 1 Lament.</li>
                  <li><span class="n">3</span> Çift numaralı her Yarığa 1 Lament + 7 numaralı Yarığa 1 Lament.</li>
                  <li><span class="n">4</span> Çift numaralı her Yarığa 1 Lament + 1 ve 7 numaralı Yarıklara 1’er Lament.</li>
                  <li><span class="n">5</span> Her Lament Yarığına 1 Lament.</li>
                </ul></li>
              <li><div class="diag"><img src="{P6['diag3']}" alt="Hazine"><div class="cap">Hazine</div></div><span class="nm">Hazineler.</span> Av Kitabı’nda gösterildiği gibi, Hazine simgesi bulunan her alana 1 rastgele Hazine jetonunu yüzü kapalı şekilde yerleştirin.</li>
            </ol></div>
        </div>
      </div>
      <span class="folio l">6</span>
    </div>
  </section>

</div>
</body></html>"""

NB.mkdir(parents=True, exist_ok=True)
out = NB / 'grimcoven_yeni_ornek.html'
out.write_text(HTML, encoding='utf-8')
print('yazıldı:', out, '·', len(HTML)//1024, 'KB')
