#!/usr/bin/env python3
"""Generate a catalog page fragment (e.g. component overview).
Each overlay covers the English text with a slice of the page's own clean
parchment (seamless) and prints Turkish text on top.
Overlay tuple: (kind, top%, left%, width%, height%, html_text)
kind in {title, head, cap, note}"""
import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent  # portable: /home/claude (sandbox) or local project dir

def emit(cls, base_tok, parch_tok, overlays):
    P = []
    P.append('<style>.%s .cov{background-image:url(data:image/jpeg;base64,@@%s@@);'
             'background-size:280mm 280mm;background-repeat:no-repeat;}</style>' % (cls, parch_tok))
    P.append('<section class="page catalog %s">' % cls)
    P.append('  <img class="base" src="data:image/jpeg;base64,@@%s@@" alt="">' % base_tok)
    # pass 1: parchment-reveal masks (behind text)
    for kind, top, left, w, h, text in overlays:
        L = left * 2.8; T = top * 2.8; W = w * 2.8; H = h * 2.8
        P.append('  <div class="cov" style="left:%.2fmm;top:%.2fmm;width:%.2fmm;height:%.2fmm;'
                 'background-position:-%.2fmm -%.2fmm;"></div>' % (L, T, W, H, L, T))
    # pass 2: Turkish text (in front of every mask)
    for kind, top, left, w, h, text in overlays:
        L = left * 2.8; T = top * 2.8; W = w * 2.8; H = h * 2.8
        P.append('  <div class="txt c-%s" style="left:%.2fmm;top:%.2fmm;width:%.2fmm;height:%.2fmm;">%s</div>'
                 % (kind, L, T, W, H, text))
    P.append('</section>')
    return '\n'.join(P) + '\n'

# ---------------- PAGE 4 ----------------
p4 = [
 ('title', 6.6, 6.0, 80, 5.2, 'BİLEŞENLERE GENEL BAKIŞ'),
 # section headers
 ('head', 13.5, 7.0, 22, 2.7, '7 Pano'),
 ('head', 13.5, 50.5, 18, 2.7, 'Kitaplar'),
 ('head', 31.7, 7.0, 18, 2.7, 'İşaretçiler'),
 ('head', 31.7, 50.5, 14, 2.7, '66 Zar'),
 ('head', 47.7, 7.0, 34, 2.7, '30 çift taraflı Harita Parçası'),
 ('head', 47.7, 76.0, 20, 2.7, 'Avcı parçaları'),
 ('head', 62.9, 7.0, 16, 2.7, 'Modeller'),
 # notes
 ('note', 15.7, 7.0, 36, 3.2, '* Not: Oyununuzun sürümüne göre kutunuzda tek<br>katmanlı ya da çift katmanlı panolar bulabilirsiniz.'),
 ('note', 33.9, 7.0, 46, 1.8, '* Not: Oyununuzun sürümüne göre karton ya da plastik işaretçiler bulabilirsiniz.'),
 ('note', 65.3, 7.0, 74, 1.8, '* Not: Oyununuzun sürümüne göre kutunuzda minyatür ya da ayaklık (standee) bulabilirsiniz. Sürümden bağımsız olarak hepsine “model” denir.'),
 # boards captions
 ('cap', 28.0, 5.5, 17, 3.2, '1 Griefbound panosu/<br>Çift Katman pano*'),
 ('cap', 28.0, 20.5, 17, 3.2, '5 Avcı panosu/<br>Çift Katman pano*'),
 ('cap', 27.9, 35.0, 15, 2.5, 'Yardımcı panosu (solo)'),
 # books captions
 ('cap', 27.9, 48.0, 16, 2.5, '6 Av kitabı'),
 ('cap', 27.6, 56.5, 18, 3.8, 'Öğretici Senaryo<br>kitapçığı'),
 ('cap', 27.9, 68.0, 16, 2.5, 'Bu Kural Kitabı'),
 ('cap', 27.9, 78.5, 14, 2.5, 'Av Çizelgesi'),
 # markers captions
 ('cap', 43.5, 5.5, 17, 1.9, '5 Yozlaşma işaretçisi'),
 ('cap', 43.5, 20.0, 16, 1.9, '5 Destek işaretçisi*'),
 ('cap', 43.5, 34.0, 16, 1.9, '10 Evrensel işaretçi*'),
 # dice captions
 ('cap', 43.5, 49.0, 16, 1.9, '60 Avcı zarı (4 renkte)'),
 ('cap', 43.5, 64.0, 12, 1.9, '4 Düşman zarı'),
 ('cap', 43.5, 78.0, 13, 1.9, '2 Teknoloji zarı'),
 # map tiles captions
 ('cap', 59.6, 4.0, 31, 4.2, '23 Arazi Harita Parçası (Orman,<br>Bataklık, Mezarlık, Nehir, Sis,<br>Engel, Derin su, Köprü)'),
 ('cap', 60.5, 35.0, 14, 1.9, '2 Bölge Çevre parçası'),
 ('cap', 60.2, 49.0, 14, 3.0, '4 İşkence Aleti/<br>Sürü parçası'),
 ('cap', 60.5, 64.0, 12, 1.9, '1 Mide parçası'),
 ('cap', 60.5, 78.0, 13, 1.9, '6 Avcı parçası'),
 # models row1
 ('cap', 75.2, 4.0, 21, 4.3, '6 Griefbound<br>modeli/ayaklığı*'),
 ('cap', 75.2, 27.5, 19, 4.3, '6 Avcı<br>modeli/ayaklığı*'),
 ('cap', 75.2, 50.0, 21, 4.3, '6 Yozlaşmış Avcı<br>modeli/ayaklığı*'),
 ('cap', 75.2, 73.0, 21, 4.3, '4 Seçkin Düşman<br>modeli/ayaklığı*'),
 # models row2
 ('cap', 87.9, 4.0, 21, 4.3, '16 Uşak<br>modeli/ayaklığı*'),
 ('cap', 87.9, 27.5, 19, 4.3, '4 Portal<br>modeli/ayaklığı*'),
 ('cap', 87.9, 50.0, 21, 4.3, '7 Yoldaş ayaklığı/<br>ve 1 Yoldaş modeli*'),
 ('cap', 88.8, 73.0, 21, 2.4, '12 Çevre ayaklığı'),
]

# ---------------- PAGE 5 ----------------
# measured caption centers (y): custom 20.7 / oversized 35.9 / std-a 50.4 / std-b 64.1 / std-c 76.8 / std-d 89.8
#                               tok r1 21.2 / r2 35.9 / r3 51.0 / r4 64.1 / r5 77.3 / r6 89.8
# card cols x 16/29.5/43.5 ; token cols x 58/72/86.5 ; left = cx - w/2 ; top = cy - h/2
p5 = [
 ('sect', 7.6, 9.0, 16, 2.2, 'Kartlar'),
 ('sect', 7.6, 52.0, 16, 2.2, 'Jetonlar'),
 ('sub', 10.2, 9.5, 22, 2.2, 'Özel kartlar'),
 ('sub', 23.6, 9.5, 28, 2.2, 'Büyük boy kartlar'),
 ('sub', 38.6, 9.5, 26, 2.2, 'Standart kartlar'),
 # cards: custom (cy 20.7)
 ('cap', 19.4, 5.0, 22, 2.6, '36 Griefbound Özellik kartı'),
 ('cap', 19.4, 20.0, 19, 2.6, '6 Yardımcı Özellik kartı'),
 ('cap', 19.6, 37.5, 12, 2.2, '20 Ayraç'),
 # cards: oversized (cy 35.9)
 ('cap', 34.8, 8.0, 16, 2.2, '10 Yardım kartı'),
 ('cap', 34.6, 19.5, 20, 2.6, '12 Seçkin Düşman kartı'),
 # cards: standard a (cy 50.4)
 ('cap', 49.3, 6.0, 20, 2.2, '167 Avcı Evrim kartı'),
 ('cap', 49.3, 20.5, 18, 2.2, '38 Avcı Eşya kartı'),
 ('cap', 49.3, 37.0, 13, 2.2, '21 Olay kartı'),
 # cards: standard b (cy 64.1)
 ('cap', 63.0, 8.0, 16, 2.2, '25 Çevre kartı'),
 ('cap', 63.0, 21.5, 16, 2.2, '222 Saldırı kartı'),
 ('cap', 63.0, 34.5, 18, 2.2, '36 Son Saldırı kartı'),
 # cards: standard c (cy 76.8)
 ('cap', 76.4, 8.0, 16, 2.2, '36 Fırsat kartı'),
 ('cap', 76.4, 22.5, 14, 2.2, '48 Evre kartı'),
 ('cap', 76.4, 36.5, 14, 2.2, '12 Uşak kartı'),
 # cards: standard d (cy 89.8)
 ('cap', 89.7, 8.0, 16, 2.2, '20 Yozlaşma kartı'),
 ('cap', 89.7, 22.5, 14, 2.2, '56 Sır kartı'),
 ('cap', 89.7, 36.5, 14, 2.2, '30 Diğer kart'),
 # tokens: row 1 (cy ~21)
 ('cap', 19.5, 48.5, 19, 3.4, '20 Yara jetonu<br>(değer 1, 3 ve 10)'),
 ('cap', 19.5, 62.5, 19, 3.4, '37 Savunma jetonu<br>(değer 2 ve 4)'),
 ('cap', 19.6, 79.0, 15, 2.2, '10 Taktik jetonu'),
 # tokens: row 2 (cy 35.9)
 ('cap', 34.8, 50.0, 16, 2.2, '40 Lament jetonu'),
 ('cap', 34.8, 63.0, 18, 2.2, '5 Tur sırası ayaklığı'),
 ('cap', 34.8, 79.0, 15, 2.2, '15 Açlık jetonu'),
 # tokens: row 3 (cy 50.4-51)
 ('cap', 49.3, 47.5, 21, 3.4, '45 Durum jetonu<br>(Yanık, Sersemleme ve Lanet)'),
 ('cap', 49.3, 64.0, 16, 2.2, '8 Hazine jetonu'),
 ('cap', 49.3, 78.0, 17, 2.2, '8 Lament Yarığı jetonu'),
 # tokens: row 4 (cy 64.1)
 ('cap', 62.8, 47.5, 21, 2.6, '4 Griefbound Seviye jetonu'),
 ('cap', 62.8, 60.5, 23, 2.6, '8 Seçkin Düşman Seviye jetonu'),
 ('cap', 63.0, 79.0, 15, 2.2, '4 Kişilik jetonu'),
 # tokens: row 5 (cy 76.8-77.3)
 ('cap', 76.3, 48.5, 19, 3.4, '6 Kanat jetonu<br>(3 Beyaz, 3 Siyah)'),
 ('cap', 76.4, 64.0, 16, 2.2, '10 Mermi jetonu'),
 ('cap', 76.4, 79.0, 15, 2.2, '5 İhtiras jetonu'),
 # tokens: row 6 (cy 89.8)
 ('cap', 89.7, 50.0, 16, 2.2, '2 Görev jetonu'),
 ('cap', 89.7, 64.0, 16, 2.2, 'İlk Oyuncu jetonu'),
 ('cap', 89.7, 79.0, 15, 2.2, 'Meşgul jetonu'),
]

if __name__ == '__main__':
    open(ROOT/'pages'/'p04.html','w',encoding='utf-8').write(emit('cat4','BASE4','CLEANPARCH4',p4))
    print('wrote pages/p04.html with', len(p4), 'overlays')
    open(ROOT/'pages'/'p05.html','w',encoding='utf-8').write(emit('cat5','BASE5','CLEANPARCH5',p5))
    print('wrote pages/p05.html with', len(p5), 'overlays')
