#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grimcoven yardımcı belgelerini (SSS + Av İpuçları) kendi-kendine yeten,
indirilebilir, baskıya-hazır TR HTML olarak dizer (fontlar base64 gömülü).
Çıktı: ../site/rulebooks/grimcoven_SSS.html, grimcoven_av_ipuclari.html"""
import base64, os, html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
SITE = ROOT.parent / 'site'
FONTS = SITE / 'assets' / 'fonts'
OUT = SITE / 'rulebooks'

def b64(p):
    return base64.b64encode(pathlib.Path(p).read_bytes()).decode()

FACE = """
@font-face{{font-family:'GrenzeG';src:url(data:font/woff2;base64,{g}) format('woff2');font-weight:300 700;font-display:swap;}}
@font-face{{font-family:'Lora';src:url(data:font/woff2;base64,{l}) format('woff2');font-weight:400 700;font-style:normal;font-display:swap;}}
@font-face{{font-family:'Lora';src:url(data:font/woff2;base64,{li}) format('woff2');font-weight:400 700;font-style:italic;font-display:swap;}}
""".format(g=b64(FONTS/'GrenzeGotisch.woff2'), l=b64(FONTS/'Lora.woff2'), li=b64(FONTS/'Lora-Italic.woff2'))

CSS = """
:root{
  --ink:#231a13;--ink-soft:#4a3a2c;--oxblood:#8a1c18;--oxblood-deep:#5c110e;
  --gold:#9a7a31;--gold-soft:#b58f3e;--parch:#ece0c4;--parch-2:#e0d0ac;
  --rule:rgba(138,28,24,.22);--edge:#bfa06c;
}
*{box-sizing:border-box;margin:0;padding:0;}
html{-webkit-text-size-adjust:100%;}
body{
  font-family:'Lora',Georgia,serif;color:var(--ink);line-height:1.66;
  background:#0d0908;background-image:radial-gradient(120% 70% at 50% -10%,rgba(120,24,18,.28),transparent 60%);
  padding:42px 18px 80px;-webkit-font-smoothing:antialiased;
}
.sheet{
  max-width:840px;margin:0 auto;position:relative;
  background:linear-gradient(170deg,#efe3c8,#e4d4b0 55%,#ddcaa2);
  color:var(--ink);padding:64px 70px 56px;border:1px solid var(--edge);
  border-radius:3px;box-shadow:0 40px 90px -28px rgba(0,0,0,.85),0 0 0 1px rgba(0,0,0,.25);
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E"),linear-gradient(170deg,#efe3c8,#e4d4b0 55%,#ddcaa2);
}
.sheet::before{content:"";position:absolute;inset:9px;border:1px solid var(--rule);border-radius:2px;pointer-events:none;}
/* başlık */
.head{text-align:center;margin-bottom:8px;}
.eyebrow{font-family:'GrenzeG',serif;font-size:.9rem;letter-spacing:.42em;text-transform:uppercase;color:var(--gold);margin-bottom:10px;}
.doc-title{font-family:'GrenzeG',serif;font-weight:500;font-size:clamp(2.4rem,7vw,3.7rem);line-height:.96;color:var(--oxblood);letter-spacing:.02em;}
.doc-sub{font-style:italic;color:var(--ink-soft);font-size:.98rem;margin-top:10px;}
.flourish{display:flex;align-items:center;justify-content:center;gap:14px;margin:22px auto 30px;}
.flourish .ln{height:1px;width:90px;background:linear-gradient(90deg,transparent,var(--gold));}
.flourish .ln.r{background:linear-gradient(90deg,var(--gold),transparent);}
.flourish svg{width:18px;height:18px;color:var(--oxblood);}
/* FAQ */
.section{font-family:'GrenzeG',serif;font-weight:500;font-size:1.6rem;color:var(--oxblood);
  letter-spacing:.03em;margin:36px 0 4px;padding-bottom:6px;border-bottom:2px solid var(--rule);}
.topic{font-weight:700;font-size:.96rem;letter-spacing:.04em;color:var(--oxblood-deep);
  margin:22px 0 7px;text-transform:none;display:flex;align-items:baseline;gap:9px;}
.topic::before{content:"";flex:none;width:9px;height:9px;transform:rotate(45deg);background:var(--gold-soft);
  position:relative;top:-1px;}
.qa{margin:0 0 13px;padding-left:2px;}
.qa .q{font-weight:700;color:var(--ink);margin-bottom:3px;}
.qa .q b{color:var(--oxblood);font-weight:700;margin-right:.4em;}
.qa .a{color:var(--ink-soft);padding-left:16px;border-left:2px solid var(--rule);}
.qa .a b{color:var(--gold);font-weight:700;margin-right:.4em;}
/* Tips */
.lede{font-style:italic;font-size:1.08rem;color:var(--ink-soft);text-align:center;max-width:640px;margin:0 auto 8px;}
.lede-2{text-align:center;color:var(--ink);margin:18px auto 30px;max-width:660px;font-weight:600;}
.tip{display:grid;grid-template-columns:54px 1fr;gap:6px 16px;margin:0 0 20px;align-items:start;}
.tip .num{font-family:'GrenzeG',serif;font-weight:600;font-size:2.5rem;line-height:.8;color:var(--gold);
  text-align:center;grid-row:span 2;padding-top:4px;
  text-shadow:0 1px 0 rgba(0,0,0,.08);}
.tip .lead{font-weight:700;color:var(--oxblood-deep);font-size:1.05rem;line-height:1.3;}
.tip .desc{color:var(--ink-soft);}
/* footer */
.foot{margin-top:40px;padding-top:20px;border-top:1px solid var(--rule);text-align:center;}
.foot .mk{font-family:'GrenzeG',serif;font-size:1.05rem;color:var(--oxblood);letter-spacing:.05em;}
.foot small{display:block;font-style:italic;color:var(--ink-soft);font-size:.82rem;margin-top:5px;}
.docbar{max-width:840px;margin:0 auto 20px;display:flex;align-items:center;justify-content:space-between;gap:12px;}
.back{display:inline-flex;align-items:center;gap:8px;font-family:'GrenzeG',serif;font-size:.8rem;letter-spacing:.2em;
  text-transform:uppercase;color:#c9b487;background:rgba(20,12,10,.7);border:1px solid rgba(184,146,63,.35);
  padding:9px 16px;border-radius:2px;}
.back:hover{color:#e6c275;border-color:rgba(197,48,42,.5);}
.prnt{font-family:'GrenzeG',serif;font-size:.82rem;letter-spacing:.14em;text-transform:uppercase;cursor:pointer;
  color:#f0dcae;background:rgba(20,12,10,.7);border:1px solid rgba(184,146,63,.45);
  padding:9px 17px;border-radius:2px;display:inline-flex;align-items:center;gap:8px;transition:all .25s;}
.prnt:hover{color:#fff;border-color:rgba(197,48,42,.6);background:rgba(46,16,14,.85);}
.prnt svg{width:15px;height:15px;}
@media print{
  @page{size:A4;margin:12mm;}
  html,body{background:#e7dcc0 !important;margin:0;padding:0;}
  .docbar{display:none !important;}
  .sheet{box-shadow:none;border:none;border-radius:0;max-width:none;margin:0;
    padding:6mm 7mm;background:linear-gradient(170deg,#efe3c8,#e6d6b2) !important;}
  .sheet::before{display:none;}
  .section,.topic,.head,.flourish,h1,h2{break-after:avoid;}
  .tip,.qa{break-inside:avoid;}
  *{-webkit-print-color-adjust:exact;print-color-adjust:exact;}
}
@media(max-width:600px){.sheet{padding:40px 26px;}.tip{grid-template-columns:40px 1fr;gap:4px 12px;}.tip .num{font-size:2rem;}}
"""

FLOUR = '<div class="flourish"><span class="ln"></span><svg viewBox="0 0 32 32" fill="currentColor"><path d="M16 1l2.2 10.2L28 14l-9.8 2.8L16 27l-2.2-10.2L4 14l9.8-2.8z"/></svg><span class="ln r"></span></div>'
BACK = ('<div class="docbar">'
        '<a class="back" href="../grimcoven.html">&#8592; Grimcoven</a>'
        '<button class="prnt" type="button" onclick="window.print()">'
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6">'
        '<path d="M6 9V3h12v6M6 18H4v-7h16v7h-2M8 14h8v8H8z"/><path d="M9 13h6"/></svg>'
        'Yazdır / PDF</button></div>')

def page(title_tab, eyebrow, title, sub, body):
    return f"""<!DOCTYPE html>
<html lang="tr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_tab}</title>
<style>{FACE}{CSS}</style></head>
<body>
{BACK}
<article class="sheet">
  <div class="head">
    <div class="eyebrow">{eyebrow}</div>
    <h1 class="doc-title">{title}</h1>
    <div class="doc-sub">{sub}</div>
  </div>
  {FLOUR}
  {body}
  <div class="foot"><div class="mk">KURAL KİTABI</div>
    <small>Grimcoven · Awaken Realms · gayriresmî Türkçe çeviri (kişisel kullanım)</small></div>
</article>
</body></html>"""

def sec(t): return f'<h2 class="section">{t}</h2>'
def topic(t): return f'<p class="topic">{t}</p>'
def qa(q,a): return f'<div class="qa"><p class="q"><b>S</b>{q}</p><p class="a"><b>C</b>{a}</p></div>'
def tip(n,lead,desc): return f'<div class="tip"><div class="num">{n}</div><div class="lead">{lead}</div><div class="desc">{desc}</div></div>'

# ============================== SSS ==============================
faq = []
faq.append(sec('Genel Sorular'))
faq.append(topic('Verilen Yara ile Açlık'))
faq.append(qa('Çoğu Corruption kartı, yara vermeyi ve verilen her bir yara için Açlık jetonu ıskartaya atmayı söyler. Eğer bu yara Savunma jetonuyla engellendiyse, yine de Açlık ıskartaya atar mıyım?',
 'Hayır. Savunma jetonlarıyla engellenen yara, verilmiş sayılmaz. Bu, Duality’nin Assault Armor’ının Eylemlerinden biri gibi diğer etkiler için de geçerlidir. Ayrıca, örneğin 6 Açlık’ınız varsa ve saldırdığınız Avcı’nın yalnızca 3 Can’ı kaldığı için yalnızca 3 yara verdiyseniz, yalnızca 3 Açlık ıskartaya atarsınız. Bunun nedeni 6 değil yalnızca 3 yara vermiş olmanızdır.'))
faq.append(topic('Tek bir Eylemde birden fazla Sersemleme/Lanet jetonu'))
faq.append(qa('Tek bir Eyleme birden fazla Durum jetonu yerleştirebilir miyim?','Hayır.'))
faq.append(topic('Alanın Griefbound/Çevre tarafından tamamen işgal edilmesi'))
faq.append(qa('Bir alandaki 4 model yuvasının tümünün Griefbound ve Çevre modelleri tarafından işgal edildiği bir durum olabilir (ör. Convergence’ın Tornadoları). Bir Avcı böyle bir alana girebilir mi?',
 'Hayır. Bu alana hiçbir model giremez (başka bir Çevre bile). Böyle bir alana Işınlanma etkileri gerçekleştirilemez. Modeller yine de böyle bir alanın içinden geçebilir, ancak hareketlerini orada bitiremezler.'))
faq.append(topic('“Hareket X” ile “X’e kadar Hareket”'))
faq.append(qa('“Hareket X” ile “X’e kadar Hareket” arasında bir fark var mı?',
 'Avcı’nın etkileri için — hayır. Bir Avcı, dilerse her zaman daha kısa bir hareket gerçekleştirebilir. Bu, zorunlu bir hareket olmadığı sürece geçerlidir (aşağıya bakınız).'))
faq.append(topic('Gönüllü ile zorunlu hareket'))
faq.append(qa('“Gönüllü” ile “zorunlu” hareketi nasıl ayırt ederim?',
 'Bir Avcı, bir hareketi kendi Eylemi olarak ya da “dost” bir kaynaktan (başka bir Avcı, Yoldaş vb.) gelen bir etkiyle gerçekleştirdiğinde, buna gönüllü hareket denir ve etkinin önerdiğinden daha kısa olabilir (ör. Hareket 3 yerine Avcı 1 Hareket eder). Bir Avcı, Düşman, Çevre veya Açlık gibi dışarıdan gelen “düşmanca” bir etkiyle hareket ettirildiğinde, buna “zorunlu” hareket denir. Mümkün olan en geniş ölçüde çözülmelidir.'))
faq.append(topic('Düşman hareketi'))
faq.append(qa('Bir Düşman “Hareket 3” etmek zorundaysa ve benden 2 alan uzaktaysa, Düşman 3’lük tam hareketi çözüp yanımdan geçer mi?',
 'Hayır. Düşmanlar genellikle bir Avcı’ya olabildiğince yaklaşmak ister; dolayısıyla Hareket 3 etmek zorundaysalar ve en yakın Avcı 2 alan uzaktaysa, Düşman son hareket puanını göz ardı ederek yalnızca 2 Hareket eder. Bazı etkiler bu kuralı değiştirebilir.'))
faq.append(topic('Giriş etkisi'))
faq.append(qa('“Giriş” etkisi, böyle bir etkiye sahip bir alanın içinden geçersem mi olur, yoksa yalnızca hareketimi orada bitirirsem mi?',
 'Etki yalnızca bir model hareketini “giriş” etkisine sahip bir alanda BİTİRİRSE olur.'))
faq.append(qa('“Giriş” Işınlanma etkilerinde olur mu? Ya zorunlu hareketle ne olur?','Evet, bu etkilerin ikisi de “giriş”i tetikler.'))
faq.append(qa('Halihazırda bir “giriş” etkisine sahip bir alanda/arazide bulunuyorsam, bu Eylemlerimden herhangi birinde tetiklenir mi (Hazine ve Lament toplamaya benzer şekilde)?','Hayır.'))
faq.append(qa('“Giriş”, kendi kendine tetiklenebilir mi? Ör. River arazi kartı beni nehir boyunca 1 alan aşağı hareket ettirdiğinde, hemen başka bir “giriş” etkisi olur mu?','Hayır.'))
faq.append(qa('Bir Tormentor’ın İşkence Aleti levhasındayım. En yakın İşkence Aleti’ne doğru 1 Hareket etmeye zorlanıyorum. Zaten bir İşkence Aleti üzerinde olduğum için hareket etmiyorum. “Giriş” etkisini çözer miyim?','Hayır.'))
faq.append(topic('Yardım Eylemini Tazeleme'))
faq.append(qa('Yardım yuvasına yerleştirilen zarı Tazelersem ne olur? Yardım işaretleyicisini Oyuncudan geri alır mıyım?',
 'Hayır. Yardım işaretleyicisi, Tazeleme aşamasına kadar o Oyuncunun elinde kalır. O zamana dek Yardım işaretleyicisi, Eylem yuvanıza yerleştirilen zarı taklit eder. Bu durumda taklit edeceği bir şey olmadığından, Yardım işaretleyicisi “yüzsüz” ve “renksiz” bir zar olarak kabul edilir.'))
faq.append(topic('Eylemi kendisiyle Tazeleme'))
faq.append(qa('Bir Eylem kendini Tazeleyebilir mi? Ör. Hunger Overflow’un “1 Eylem Tazele” etkisi vardır. Bu durumda Hunger Overflow kendini Tazeleyebilir mi?','Hayır.'))
faq.append(topic('Hedef ile Düşman'))
faq.append(qa('Bazı kart etkileri, oyuncunun ek “hedefler” eklemesine izin verir. Bir Düşman ile bir “hedef” arasındaki fark nedir?',
 'Hedef daha geniş bir sınıflandırmadır. Oyunda Düşman olmayan ama yine de yara alabilen varlıklar bulunur — ör. Undead General’ın Banner’ları ya da Sır kartlarından birindeki Ironclad Safe. Bunlar Düşman olmasa da, o Eylemler onları “ek hedefler” olarak içerebilir.'))
faq.append(topic('Öldürme etkileri ile Opportunity kartları — çözüm sırası'))
faq.append(qa('Bir Griefbound’un Attack kartını öldürürsem önce ne olur — Opportunity mi yoksa Evolution kartımdaki “Öldürmede” etkisi mi?','Çözüm sırasına oyuncular karar verebilir.'))
faq.append(topic('Iskartaya atılan bir karttaki jetonlar'))
faq.append(qa('Bir kartı ıskartaya atmam/desteye geri koymam söyleniyor ve bu kartın üzerinde jetonlar/zarlar var. Bunlara ne olur?',
 'Onlar da ıskartaya atılır. Jetonlar ortak havuza döner (eğer jeton Avcı’ya özelse sahibine döner) ve zarlar sahibinin ıskarta havuzuna yerleştirilir.'))

faq.append(sec('Ana Kutu Avcı/Griefbound Soruları'))
faq.append(topic('Death Jester’ın birden fazla Bahsi'))
faq.append(qa('“İstediğin sayıda Bahis yap” diyen bir kartı nasıl çözerim? Bu, “Başarılı bir Bahiste” pasif etkileriyle nasıl etkileşir?',
 'Eyleme zarları yerleştirdikten sonra ama onu çözmeden önce, istediğiniz sayıda Bahis yapabilirsiniz. Her birinden sonra durmaya karar verebilirsiniz. Başarısız bir Bahiste tüm başarılar kaybedilir, Eylemin hiçbir etkisi olmaz ve daha fazla Bahis yapamazsınız. Yine de varsa “başarısız bir Bahiste” etkilerini çözersiniz. Başarılı her Bahisten sonra durmaya, Bahis etkisini çözmeye (genellikle bir Eylemi X kez tekrarlamak) ve tüm “başarılı bir Bahiste” etkilerini elde etmeye karar verebilirsiniz (bu tür her etki X kez çözülür; X, başarılı Bahislerin sayısıdır).'))
faq.append(topic('Death Jester’ın Yozlaşmış formu — “Fate destesini çevir”'))
faq.append(qa('Fate destesi açık çevrildikten sonra içine bakabilir miyim, yoksa yalnızca en üstteki kart mı görünür?','Yalnızca en üstteki kart görünür.'))
faq.append(topic('Mannequin String kartları'))
faq.append(qa('Bloodless Husk etkisinden sonra bir Arm kartını String tarafına çevirdiğimde, bu String seçilen Avcı’ya mı verilir yoksa onu ben mi tutarım?','Mannequin oyuncusu kartı String formunda tutar.'))
faq.append(qa('Bir etki nedeniyle bir Arm kartını kaybedersem/çevirirsem, onu nasıl geri kazanır/geri çeviririm?',
 'Buna izin veren herhangi bir etkiyle. Arm’ları geri kazanmak çok nadirdir — bir biçimiyle, Yozlaşmış Form’a (Yozlaşma 15) ulaşıldıktan sonra yapılır. String kartlarını geri çevirmek, Evolution destesindeki tek bir kartla yapılabilir.'))
faq.append(topic('Technomancer’ın ek parça güçlendirmeleri'))
faq.append(qa('Technomancer’ın Weapon/Armor kartındaki “Tüm Weapon/Armor ek parça güçlendirmeleri artık aktif” Eylemi bir Weapon/Armor sayıldığından, kendi türünden tüm ek parça bonuslarını otomatik olarak tetikler mi?',
 'Hayır. Bu bonusların daha sonra başka Weapon/Armor Eylemleriyle aktif edilmesine olanak tanır.'))

faq.append(sec('Genişleme Avcı/Griefbound Soruları'))
faq.append(topic('Clockwork Giant’ın Durum jetonları'))
faq.append(qa('Bir Gear kartının üzerinde Sersemleme jetonları / Lanet jetonları / zarlar var ve Gear değiştirmem gerekiyor. Bunlara ne olur?','Jetonlar/zarlar ıskartaya atılır.'))

faq_html = page('Grimcoven — Resmî Oyun SSS', 'Grimcoven', 'Resmî Oyun SSS', 'Sürüm 1.2 · Ocak 2026', '\n'.join(faq))

# ============================== AV İPUÇLARI ==============================
tips_intro = (
 '<p class="lede">Sizi selamlıyorum, Avcılar. Kararlılığınız önünde eğiliyor, cesaretinizi en büyük '
 'saygıyla anıyorum; zira bu hiç bitmeyen savaşımızda her bir savaşçı ağırlığınca altın değerindedir. '
 'Bu yüzden, Lament biçimli iğrençliklere karşı seferinize başlayacak kadar güçlü hissetmeden önce, bir an '
 'durup sizin için derlediğim öğütlere kulak verin. Ve bunları asla unutmayın, çünkü hiçbirinizi kaybetmek '
 'istemiyoruz. En azından, henüz pek erken değil.</p>'
 '<p class="lede-2">Grimcoven zorlu bir oyundur. İşte oyunu daha az zorlayıcı kılmanıza yardımcı olabilecek bazı genel ipuçları:</p>'
)
TIPS = [
 ('Her turda tüm zarları kullanmanın bir yolunu bulun.','Geriye kullanılmamış zar bırakarak pas geçmemeye çalışın. Zarlar sizin eylemlerinizdir, bu yüzden onları boşa harcamayın.'),
 ('Eyleme geçmeden önce plan yapın.','İdeal olarak birkaç sıra, hatta mümkünse tüm bir tur ileriyi düşünün. Hiçbir plan yapmadan kavganın ortasına baş üstü dalmak çoğu zaman size ölümden başka bir şey getirmez.'),
 ('Avcı arkadaşlarınızla konuşun ve eylemlerinizi koordine edin.','Onlara bu turda ne kadar yara verebileceğinizi ve hangi hedeflere ulaşıp ulaşamayacağınızı bildirin.'),
 ('Birbirinize yardım edin.','Başkasına daha uygun olan simgelere sahip olabilirsiniz; zar istemekten de çekinmeyin.'),
 ('Düşmanlarınızı gözlemleyin.','Düşmanların neler yapabileceğine ya da gelecekteki eylemlerinin ne olabileceğine dikkat edin. Çoğu, mesafenizi korursanız zararsızdır. Örneğin, 2 hareket eden ve 2 menzilden saldıran bir Düşmanın etkin menzili 4’tür. Konum alırken bu sayıyı aklınızda tutun.'),
 ('Harita üzerinde ne kadar çok Düşman varsa, çembere alınmak o kadar kolaylaşır!','Denklemi basitleştirmek için biraz kaba kuvvet kullanın! Bazı Düşmanlardan kurtulmak size nefes alacak alan açar ve kalanların etrafında plan yapmayı kolaylaştırır.'),
 ('Odaklanmış bir Griefbound tehlikelidir!','Griefbound’un ODAKLANMIŞ etkilerine dikkat edin. Bazen onlardan kurtulmak, sizi bir saldırıdan ya da başka kötü etkilerden kurtarabilir.'),
 ('Hareketiniz sınırlıdır.','Evrimler ve Eşyalar olmadan iki hareket Eylemi vardır: Koşu ve Sürat. İkisini de tüketirseniz, bu turda bir daha hareket edemezsiniz. Çatışmaya girmeden önce daima bir kaçış planınız olsun!'),
 ('Portalları kullanın.','Portallar size yardım etmek için oradadır — Düşmanlar onları kullanamaz. Üstünlüğünüzü kullanmak ve Düşmanlarınızdan kaçmak için Portalları olabildiğince sık kullanın.'),
 ('Düşmanlar bir alana saldırma eğilimindedir.','Durum gerektiriyorsa, tüm Avcıların aynı Saldırıdan etkilenmemesi için ayrılın. Can sınırlıdır; bu yüzden Düşmanlardan kaçamıyorsanız, Avcılardan birini öne koyarak feda edin. İdeal olarak en çok Can’a ya da Savunma jetonuna sahip olanı seçin.'),
 ('Düşmanlarınızı yanıltın.','Düşmanları dar geçitlerde ve onlarla daha kolay başa çıkabileceğiniz yerlerde toplamak işe yarar. Düşmanlar gruplanmışsa ve sizin de bazı alan etkili saldırılarınız varsa, aynı anda birçoğunu vurabilirsiniz.'),
 ('Engelleri ve Sisi kendi yararınıza kullanın.','Birçok Düşman saldırısı belirli bir Menzil ve Görüş Hattı gerektirir. Saldırılardan kaçınmak için onların Menzilinin dışına çıkın ve Görüş Hatlarını kesin.'),
 ('Çevrenizi kullanın ve onu keşfedin.','Seçeneksiz hissediyorsanız Çevre kartlarına bakın — tam da şu an ihtiyacınız olan şey olabilir. Ya da biraz vakit ayırabilirseniz, keşfedin ve Sır çekin! Kullanabileceğiniz birçok güçlendirme barındırabilirler.'),
 ('Tüm Avcılar eşit yaratılmamıştır.','Farklı Avcıların farklı karmaşıklık puanları vardır. Bunaldığınızı hissediyorsanız, oynaması daha kolay olan birini seçin. Tarzınıza en uygun olanı bulun ve onda ustalaşın.'),
 ('Takımınızı ve teçhizatınızı kişiselleştirin.','Her Avcı her Griefbound’a karşı iyi oynamaz ve bazen bunu zor yoldan öğrenirsiniz. Ayrıca farklı başlangıç teçhizatlarının etkinliği, karşılaştığınız Haritaya ya da Düşmanlara göre değişebilir.'),
 ('Stratejik anlarda Kritik Yaralanma almaktan korkmayın.','Bu, tüm Durumları ve Açlığı atmanızı sağlar. Üstelik görevi tamamlamayı başarırsanız, sizi İyileştirir de. Bazen umutsuzca su yüzünde kalmaya çalışmaktansa dalıp geri sıçramak daha iyidir.'),
 ('Aşırı özgüven hızlı ve kesin bir katildir.','Unutmayın ki Son Perde’ye Girmek Avcı Aşamasını sona erdirir! Bunu, sıralarınızı boşa harcamayacak bir şekilde tetiklemeye çalışın. Griefbound, Avcı Aşaması sırasında Son Perde’ye Girerse, büyük olasılıkla konumunuz bozulmuş halde yakalanır ve korkunç bir şekilde öldürülürsünüz.'),
 ('Yozlaş. Kendini. Akıllıca.','Lament’e teslim olup Yozlaşmış biçimi aceleyle almak her zaman tavsiye edilmez. Ayrıca bazı Yozlaşma kartları Yozlaşma kaybetmenizi sağlar. Yozlaşma şeridinde, Yozlaşma kartı etkilerinde şansınız yaver giderse defalarca Evrim geçirmenizi sağlayabilecek noktaları arayın!'),
 ('Taktikleri taktiksel kullanın.','Taktik jetonu güçlü bir araçtır. Yalnızca zarları yeniden atmanızı değil, aynı zamanda zaman kazanmanızı da sağlar! Unutmayın ki bu jeton, oyunun herhangi bir anında ya da bir Eylem olarak kullanılabilir. Bir Eylem olarak kullanırsanız, bir saldırıyı koordine etmenizi sağlayabilir ve pas geçmek zorunda kalmadan önce size o değerli tek sırayı kazandırabilir. Bazen hiç zar yeniden atmadan kullanmak bile yararlıdır.'),
 ('Bazen sadece yeniden denemeniz gerekir.','Bir Senaryoyu defalarca yeniden oynamaktan çekinmeyin; çünkü Düşmanların düzenlerini öğrenmek zafere giden ilk adımdır. Ayrıca zorlanıyorsanız Kolay mod seçeneklerini de kullanabilirsiniz (Kural Kitabı s. 30). Daha rahat bir oynanışı tercih edebilir ya da yeni bir Avcının veya Griefbound’un potansiyelini öğrenmek için daha kolay bir süreç isteyebilirsiniz.'),
]
tips_body = tips_intro + '\n'.join(tip(i+1,l,d) for i,(l,d) in enumerate(TIPS))
tips_html = page('Grimcoven — Evrensel Av İpuçları', 'Grimcoven', 'Evrensel Av İpuçları', 'Avcılar için öğütler', tips_body)

OUT.mkdir(parents=True, exist_ok=True)
(OUT/'grimcoven_SSS.html').write_text(faq_html, encoding='utf-8')
(OUT/'grimcoven_av_ipuclari.html').write_text(tips_html, encoding='utf-8')
print('SSS:', len(faq_html)//1024, 'KB ·', faq_html.count('class="qa"'), 'S/C')
print('İPUÇLARI:', len(tips_html)//1024, 'KB ·', tips_html.count('class="tip"'), 'ipucu')
