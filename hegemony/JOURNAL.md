# HEGEMONY → Türkçe Kural Kitabı — TEKNİK DEFTER (tek doğruluk kaynağı)

**Kaynak:** `Hegemony-English-Rulebook-v1.2.pdf` (Adobe InDesign 19, 2023-11-03).
**Boyut:** 280×280 mm kare (793.701 pt) — Grimcoven ile AYNI → `render_check.py` 1058px sabiti geçerli.
**Sayfa:** 40. **Master çıktı:** `hegemony_TR.html`.
**Üretim yöntemi:** Grimcoven ile aynı reveal-mask tekniği; tek self-contained HTML, font+görsel base64 gömülü.

> Bu defter KİLİT. Sözlük kesinleşince KİLİTLENİR; sapma yok, yeni terim KARARLAR.md'ye işlenir.

---

## ORTAM

- `export PATH="/opt/homebrew/bin:$PATH"`; python = `/usr/bin/python3`.
- `cd hegemony && export PDF="$PWD/pdf/Hegemony-English-Rulebook-v1.2.pdf"`.
- Poppler (pdftoppm/pdfimages/pdftotext/pdffonts) + fonttools/brotli/PIL KURULU.
- **PDF KORUMA:** Kanonik PDF `hegemony/pdf/...pdf` (15.815.127 bayt, `chmod 444`). Pristine yedek
  ayrıca `~/Downloads/Hegemony-English-Rulebook-v1.2.pdf`. Bir oturumda kök kopyası metin-modu yeniden
  yazma ile bozulmuştu (CR→LF + ikili baytlar U+FFFD'ye → 26MB, "Bad FCHECK"). **PDF'i ASLA metin aracıyla
  açma/yeniden yazma; bozulursa Downloads veya pdf/ kopyasından `cp` ile geri al.**
- Render-check = Chrome headless (`render_check.py`): `build.py` → `_check.html` (literal renk) →
  `render_check.py <toplam> N` → `/tmp/r_pNN.png`. Sayfa N: `y0=(N−1)×1080`, yük. 1058.
- `var()` check'te literal hex'e çevrilir (build.py `COLORS` dict).

## FONTLAR (indirildi, tam TR glif kapsamı ✓)

- **Başlık/kalın:** Montserrat (variable woff2, `'Mont'`) — normal + italik. PDF başlıkları Montserrat Bold/SemiBold büyük-harf.
- **Gövde:** Roboto (variable woff2, `'Robo'`) — normal + italik. PDF gövdesi Roboto.
- `fonts/Montserrat.woff2`, `Montserrat-Italic.woff2`, `Roboto.woff2`, `Roboto-Italic.woff2`.
  Tam variable (100–900) + ğĞşŞıİöÖçÇüÜ doğrulandı. (google/fonts variable TTF → fonttools woff2.)
- **Webdings** PDF'te ufak simgeler için kullanılmış (CID) — bunlar İKON; font değil, `IC_*` olarak çıkarılır.

## TASARIM TOKENLARI (build.py `:root` / `COLORS`) — ⚠ GEÇİCİ, ÖRNEKLENECEK

Hegemony düz **beyaz zemin** + sınıf renkleri. Aşağıdakiler placeholder; her sayfanın
`base_pN.jpg`'inden **örneklenip** kesinleştirilecek (PIL ile metin-dışı pikselden):
- `--paper #fff` · `--ink #1a1a1a` · `--ink-soft #4a4a4a` · `--accent #e8b21f` (sarı/altın vurgu) · `--rule #d8d8d8`
- Sınıf renkleri (DOĞRULANACAK): `--wc` İşçi (kırmızı) · `--mc` Orta (yeşil) · `--cap` Kapitalist (mavi) · `--state` Devlet (mor).
- **İŞ:** ilk partide gerçek hex'leri örnekle, bu listeyi + COLORS'ı güncelle.

## REVEAL-MASK / METİN-SİLME YÖNTEMLERİ (Grimcoven'dan farkı)

Hegemony'de zemine göre 2 yöntem:
- **A) DÜZ-DOLGU kapak (YALNIZCA tamamen boş-beyaz zemin, yakınında GÖRSEL YOK):** EN metnin üstüne beyaz kutu +
  TR. **UYARI:** kart/görsel içeren sayfalarda KULLANMA → kapak kayınca kart görselini örter (s.4 felaketi). Yalnız
  s.2 gibi boş-beyaz gutter etiketleri için güvenli. Solid renkli bar etiketi için bar rengini örnekle (`#f2ae26`).
- **A2) GRİ-PİLL kapak (lejant hapları, s.3):** açık-gri yuvarlak hap (#ededed) + TR. Hap = etiket zemini, kart değil.
- **B) INPAINT temiz-plaka (kapak/fotoğraf/dokulu zemin):** Zemin fotoğraf/gradyan/dokuluysa düz-dolgu dikiş
  bırakır. cv2 (`opencv-python-headless`, `--user` kurulu) ile EN metin piksellerini maskeleyip
  `cv2.inpaint(...,TELEA,7)` ile sil → temiz plaka `art/cover_clean.jpg`; TR'yi üstüne **şeffaf** divlerle diz.
  **Maske kuralı:** yalnız metin dikdörtgenlerinde parlak/altın pikselleri işaretle; **logo, ikon, renkli bar
  HARİÇ** (ikon x-aralıklarını ölçüp dışla). Dilate 5px, sonra inpaint. (Kapak s.1 bu yöntemle yapıldı.)
  **★ KART/GÖRSEL içeren TÜM sayfalarda VARSAYILAN = B (inpaint+ŞEFFAF overlay).** Kartları cardmask ile KORU
  (renkli büyük-bileşen + beyaz-gövdeli kartlar için açık-dikdörtgen, dilate 11px). TR'yi background'SUZ (şeffaf)
  div'le bindirip kart asla örtülmesin. (s.4 bu yöntemle düzeltildi — reçete: GERIBILDIRIM.md.)
- Her iki yöntemde de 4-NOKTA DENETİMİ (İKON/BİNDİRME/SIZINTI/ROZET-KUTU) geçerli.

### s.1 KAPAK — yapıldı (referans)
- `art/cover_clean.jpg` = inpaint ile EN metni silinmiş plaka (fotoğraf+logo+4 kutu ikonu+renkli barlar korundu).
- build.py ASSETS `COVER_CLEAN`. p01.html: plaka full-bleed + mm-konumlu şeffaf TR divleri.
- Renkler: başlık altın `#eaae4a`, turuncu satır `#e4a534`, MIDDLE etiketi koyu (sarı bar), diğer etiketler beyaz.
- Kutu sınıf adları = KİLİTLİ terim (Kapitalist Sınıf/Orta Sınıf/İşçi Sınıfı/Devlet). İkonlar SANAT.

---

## SAYFA HARİTASI (tip: A metin · B diyagram/kurulum · C kolaj-kart)

| s. | Bölüm | Tip |
|----|-------|-----|
| 1 | Kapak ("The nation is in disarray." — açılış metni) | C |
| 2 | COMPONENTS (bileşen listesi/kolaj) | C |
| 3 | SYMBOLS (ikon/sembol lejantı — **İKON SETİ KAYNAĞI**) | C |
| 4 | COMPONENT ANATOMY (kart/bileşen anatomisi, etiketli) | B |
| 5–7 | GAME BOARD (oyun tahtası, bölgeler) | B |
| 8–9 | GAME SETUP (genel kurulum) | B |
| 10–11 | PLAYER SETUPS (sınıf-bazlı kurulum) | B |
| 12–13 | HOW TO PLAY — MAIN RULES | A |
| 14–17 | HOW TO PLAY — WORKING CLASS (İşçi Sınıfı) | A/B |
| 18–21 | HOW TO PLAY — CAPITALIST CLASS (Kapitalist Sınıf) | A/B |
| 22–25 | HOW TO PLAY — MIDDLE CLASS (Orta Sınıf) | A/B |
| 26–29 | HOW TO PLAY — THE STATE (Devlet) | A/B |
| 30–31 | POLITICS TABLE (siyaset tablosu) | B |
| 32 | ELECTION EXAMPLE (seçim örneği) | B |
| 33 | (devam / örnek) | A |
| 34–35 | CREDITS (künye) | A/C |
| 36–39 | CARD RELATED QUESTIONS (kart SSS) | A |
| 40 | Arka kapak (logo/amblem) | C |

**Parti sırası önerisi:** önce kapak/künye blokları (1–4), sonra board/setup (5–11), sonra
sınıf bölümleri (12–29), en son tablo/örnek/SSS (30–39, 40). 3–4 sayfa/parti.

---

## KİLİTLİ SÖZLÜK ✅ (2026-06-17 kilitlendi — sapma YOK; yeni terim KARARLAR.md'ye)

> 40 sayfa tarandı (board-game-translator). Her terim birebir+tutarlı uygulanır. Karışan çiftler için **D bölümü**ne uy.

### KORUNAN (çevrilmez — özel ad / marka / sanat)
- **Hegemony** (+ alt başlık "Lead Your Class to Victory"), **Vardi/Vardis** (kurgusal para birimi, sembol ₥),
  **IMF** (açılımı parantezle "Uluslararası Para Fonu", kısaltma kalır), tasarımcı/sanatçı/playtester adları,
  **Hegemonic Project Limited** + telif metni.
- **Kart adları = SANAT** (kart üzerinde İngilizce basılı): State Scholarship, Health Crisis, Extra Shift (kart olarak),
  Privatization, Migration, Higher VAT, Public Opinion Polling… → SSS'de İngilizce, yanına parantez TR açıklama olabilir.
- **Şirket örnek-adları** (Supermarket, Shopping Mall, College, Clinic, Public Hospital, University…) → **İngilizce bırak**
  (oyuncu karttaki basılı adı arıyor); ilk geçişte parantez TR açıklama opsiyonel. [KARARLAR K6]
- **Kod-etiketleri** (Policy 1–7 kodları, Section A/B/C, L1/L2/L3, 1A/4.B): kod aynen (1A, 4.B); ama "1. Politika",
  "A bölümü", "3. Kademe" çevrilir.

### ÇEVRİLEN

**Sınıflar / roller / işçiler**
| EN | TR | Not |
|----|----|----|
| Working Class | İşçi Sınıfı | kırmızı |
| Middle Class | Orta Sınıf | yeşil |
| Capitalist Class | Kapitalist Sınıf | mavi |
| The State | Devlet | mor |
| Class | Sınıf | "3 Classes" → "3 Sınıf" |
| Player Role | Oyuncu Rolü | s.3 |
| Worker | İşçi | meeple/figür |
| Unskilled / Skilled / Any Skilled | Vasıfsız / Vasıflı / Herhangi Vasıflı | |
| Employee | Çalışan | Orta Sınıf şirketindeki İşçi Sınıfı figürü |
| Unemployed Workers (area) | İşsiz İşçiler (alanı) | |
| Immigrant / Immigration | Göçmen / Göç | |

**Kaynaklar / mallar / jetonlar**
| EN | TR | Not |
|----|----|----|
| Resource | Kaynak | |
| Goods | Mallar | yalnız Yiyecek+Lüks |
| Services | Hizmetler | Sağlık/Eğitim/Nüfuz |
| Goods & Services | Mallar ve Hizmetler | |
| Food | Yiyecek | [K5] |
| Luxury | Lüks | |
| Health | Sağlık | |
| Education | Eğitim | |
| **Influence** | **Nüfuz** | [K1] — ASLA "Etki" (effect ile karışır). Media/Personal Influence → Medya/Kişisel Nüfuz |
| Machinery | Makine | [K6] — "Makine jetonu"; Automated≠Machinery |
| Wealth | **Servet** | Kapitalist tablo/işaretleyici; Prosperity≠Wealth! |
| Prosperity | **Refah** | İşçi/Orta Sınıf ZP kaynağı; Welfare≠Prosperity! |
| Victory Point (VP) | Zafer Puanı (ZP) | "3VP" → "3 ZP" |
| Money | Para | |
| Token / Marker / Cube | Jeton / İşaretleyici / Küp | |

**Tahta bölgeleri**
| EN | TR | Not |
|----|----|----|
| Game Board / Main Board | Oyun Tahtası / Ana Tahta | |
| Player Board / Player Aid | Oyuncu Tahtası / Oyuncu Yardımı | "General Player Aid" → "Genel Oyuncu Yardımı" |
| Rule Aid | Kural Yardımı | |
| Politics Table | Siyaset Tablosu | |
| Business Deals / Export / Import (area) | Ticari Anlaşmalar / İhracat / İthalat (alanı) | |
| Foreign Market / Local Market | Dış Pazar / Yerel Pazar | |
| State Treasury | Devlet Hazinesi | Supply≠Treasury! |
| Supply | **Stok** | "return to the Supply" → "Stok'a geri"; Hazine ile KARIŞTIRMA [D] |
| Private / Public Sector | Özel / Kamu Sektörü | |
| Public Services (area) | Kamu Hizmetleri (alanı) | |
| VP Track / Round Track | ZP Şeridi / Tur Şeridi | |
| Tax Multiplier (track) | Vergi Çarpanı (şeridi) | |
| Vote Results / Events / State Benefits (area) | Oy Sonuçları / Olaylar / Devlet Yardımları (alanı) | |
| Population Track | Nüfus Şeridi | |
| Prosperity (track) | Refah (şeridi) | |
| Trade Union | Sendika | |
| **Income** / **Revenue** / **Capital** (area) | **Gelir** / **Hasılat** / **Sermaye** | üçü AYRI! [D] |
| Storage / Storage tile / Storage Limit | Depo / Depo karosu / Depo Sınırı | |
| Free Trade Zone (tile) | Serbest Ticaret Bölgesi (karosu) | |
| Legitimacy | Meşruiyet | "Meşruiyet'i" |

**Bileşenler / kartlar**
| EN | TR | Not |
|----|----|----|
| Components / Symbols / Component Anatomy | Bileşenler / Semboller / Bileşen Anatomisi | bölüm başlıkları |
| Regular / Small Cards | Standart / Küçük Kartlar | |
| Action / Event / Export / Immigration Card | Eylem / Olay / İhracat / Göç Kartı | |
| Business Deal Card | Ticari Anlaşma Kartı | |
| Political Agenda (Card) | Siyasi Gündem (Kartı) | |
| Company / Public / Private / Automated Company | Şirket / Kamu / Özel / Otomatik Şirket | |
| Capitalist/Middle Class Company | Kapitalist/Orta Sınıf Şirketi | |
| Cooperative Farm | Kooperatif Çiftliği | |
| Cloth Bag / Transparent Markers / Wooden Components | Kumaş Torba / Şeffaf İşaretleyiciler / Ahşap Bileşenler | |
| Voting Cube / Influence Cube | Oy Küpü / Nüfuz Küpü | |
| Bill Marker | Tasarı İşaretleyicisi | |
| Policy/Legitimacy/Prosperity/Scoring/Wealth/Tax Multiplier/Round Marker | Politika/Meşruiyet/Refah/Puanlama/Servet/Vergi Çarpanı/Tur İşaretleyicisi | |
| Strike Token | Grev Jetonu | |
| Demonstration Token | Gösteri Jetonu | [K4] — ASLA "Eylem" (Action ile karışır) |
| Welfare Tile | Refah Devleti Karosu / Refah Karosu | [K2] "Health/Education Welfare Tile" → "Sağlık/Eğitim Refah Karosu" |
| Vote / Voting Token | Oy / Oy Jetonu | |
| Loan | **Kredi** | [K3] — "Pay Off Loan" → "Krediyi Kapat" |
| Legitimacy Token / Point | Meşruiyet Jetonu / Puanı | |

**Aşamalar / adımlar**
| EN | TR | Not |
|----|----|----|
| Round / Turn | **Tur** / **El** | "on your turn" → "sıranda"; bir Tur'da 5 el [D] |
| Phase / Step | Aşama / Adım | |
| Preparation / Action / Production / Elections / Scoring Phase | Hazırlık / Eylem / Üretim / Seçim / Puanlama Aşaması | |
| Endgame / Game End | Oyun Sonu | |
| Produce Goods & Services | Mal ve Hizmet Üret | |
| Cover Needs | İhtiyaçları Karşıla | |
| Check IMF / Pay Taxes / Refill Bag / Carry Out Elections | IMF'yi Kontrol Et / Vergileri Öde / Torbayı Doldur / Seçimleri Yürüt | |
| Apply Event Penalties | Olay Cezalarını Uygula | |
| Score Legitimacy / Score Political Agenda | Meşruiyeti Puanla / Siyasi Gündemi Puanla | |
| Game Setup / Main Board Setup / Player Setup | Oyun / Ana Tahta / Oyuncu Kurulumu | |

**Eylemler**
| EN | TR | Not |
|----|----|----|
| Basic / Free / Main Action | Temel / **Bedava** / Ana Eylem | [K7] üçlü tutarlı |
| Event Action | Olay Eylemi | Devlet |
| Propose Bill | Tasarı Öner | |
| Immediate Vote | Anlık Oylama | |
| Assign Workers | İşçi Ata | |
| Buy Goods & Services | Mal ve Hizmet Satın Al | |
| Strike / Demonstration (action) | Grev (Yap) / Gösteri (Yap) | |
| Apply Political Pressure | Siyasi Baskı Uygula | |
| Build / Sell Company | Şirket Kur / Sat | |
| Sell to the Foreign Market | Dış Pazara Sat | |
| Make Business Deal / Lobby | Ticari Anlaşma Yap / Lobi Yap | |
| Meet with a Party's MPs | Bir Partinin Vekilleriyle Görüş | MPs=milletvekilleri |
| Extra Tax / Campaign | Ek Vergi / Kampanya (Yap) | Devlet |
| Extra Shift (eylem) | Ek Vardiya | kart adı olarak "Extra Shift" (İngilizce) [D] |
| Adjust Prices / Wages | Fiyatları / Ücretleri Ayarla | |
| Give Bonus | Prim Ver | |
| Buy Storage / Receive Benefits | Depo Satın Al / Yardımları Al | |
| Pay Off Loan / Pay Interest | Krediyi Kapat / Faiz Öde | interest=faiz |
| Drop Prosperity | Refahı Düşür | |
| Use Healthcare / Education / Luxury | Sağlık Hizmeti / Eğitim / Lüks Kullan | |
| Swap Workers | İşçi Değiştir | |
| **Provide** / **Spend** | **Tedarik Et** / **Harca** | AYRI! Provide=önce alabilir, Spend=eldekini [D] |
| Discard | At / İskartaya çıkar | |

**Politikalar / ideoloji**
| EN | TR | Not |
|----|----|----|
| Policy / Section (A/B/C) | Politika / Bölüm (A/B/C) | "Policies 4 & 5" → "4. ve 5. Politika" |
| 1. Fiscal Policy | Maliye Politikası | |
| 2. Labor Market | **İş Gücü Piyasası** | [K8] |
| 3. Taxation | Vergilendirme | |
| 4. Welfare State: Health & Benefits | Refah Devleti: Sağlık ve Yardımlar | |
| 5. Welfare State: Education | Refah Devleti: Eğitim | |
| 6. Foreign Trade / 7. Immigration | Dış Ticaret / Göç | |
| Ideology / Socialism / Neoliberalism | İdeoloji / Sosyalizm / Neoliberalizm | |
| Nationalism / Globalism | Milliyetçilik / Küreselcilik | Politika 6-7 |
| IMF Intervention | IMF Müdahalesi | |

**Vergi / ekonomi**
| EN | TR | Not |
|----|----|----|
| Tax / Taxes | Vergi / Vergiler | |
| Income / Employment / Corporate Tax | Gelir / İstihdam / Kurumlar Vergisi | |
| Tax Multiplier | Vergi Çarpanı | |
| Welfare Tax (modifier) | Refah Vergisi (çarpan değiştiricisi) | |
| Tariff(s) | Tarife / Gümrük tarifesi | |
| Wage / Minimum Allowable Wage | Ücret / İzin Verilen Asgari Ücret | "Level 1/2/3 Wage" → "1./2./3. Kademe Ücret" |
| Interest / Profit / Cost / Price | Faiz / Kâr / Maliyet / Fiyat | |
| Production Bonus | Üretim Bonusu | |
| Industry | Endüstri | s.4: 5 endüstri |

**Endüstri adları (s.4) / durum**
| EN | TR | Not |
|----|----|----|
| Agriculture / Healthcare / Media | Tarım / Sağlık / Medya | endüstri renkleri |
| Luxury / Education (endüstri) | Lüks / Eğitim | |
| Operational / Non-operational / Fully operational | Faal / Faal değil / Tam faal | |
| Committed (Workers) | Bağlı (İşçiler) | yan yatır |
| Standing / lying down | Ayakta / yatık | |
| Slot / Hand / Deck / pile | Yuva / El / Deste / yığın | |
| Face-up / Face-down | Açık / Kapalı | |
| Election / Vote | Seçim / Oy | |
| In Favor / Against / Abstain | Lehte / Aleyhte / Çekimser kal | |
| Bill | Yasa Tasarısı / Tasarı | ilk geçiş "Yasa Tasarısı", sonra "Tasarı" |
| Population / Reward / Penalty / Task | Nüfus / Ödül / Ceza / Görev | |
| Administration | Yönetim / İktidar | |

### D) KARIŞAN ÇİFTLER — DEMİR KURALLAR (kuralı bozar, çok dikkat)
1. **Refah(Prosperity) ↔ Servet(Wealth) ↔ Refah Devleti(Welfare):** "Refah" tek başına = Prosperity. Welfare DAİMA
   nitelemeli ("Refah Devleti/Karosu"). Wealth DAİMA "Servet". (s.7, s.21 aynı sayfada geçer.)
2. **Nüfuz(Influence) ↔ Meşruiyet(Legitimacy) ↔ etki(effect):** "Etki" yalnız "card effect"; Influence ASLA "Etki".
3. **Eylem(Action) ↔ Gösteri(Demonstration):** Demonstration ASLA "Eylem".
4. **Gelir(Income) ↔ Hasılat(Revenue) ↔ Sermaye(Capital):** Kapitalist para alanları, üçü ayrı.
5. **Tur(Round) ↔ El(Turn):** bir Tur'da 5 el. "5 turns" → "5 el".
6. **Stok(Supply) ↔ Hazine(Treasury):** kural metni bizzat uyarıyor (s.12), karıştırma.
7. **Tedarik Et(Provide) ↔ Harca(Spend):** Devlet'te (s.27/38) kural farkı taşır.
8. **Ek Vardiya(eylem) ↔ Extra Shift(kart adı, İngilizce):** her geçişte rolü kontrol et.

## İKON SETİ (s.3 SYMBOLS + Webdings'ten çıkarılacak — `art/icons/IC_*`)
Lejanttaki adaylar: Legitimacy, Prosperity, Influence, Population, Education, Health, Food, Luxury,
Machinery, Wealth, Victory Point, Tax Multiplier, Minimum Allowable Wage, Worker (Unskilled/Skilled/Any),
Vardis (para), Vote, Welfare, Storage, Company, sınıf amblemleri (WC/MC/Cap/State). 
**İŞ:** s.3'ü r300+ render et, her sembolü en kontrastlı kaynaktan şeffaf PNG çıkar, build.py ASSETS'e ekle.

---

## DURUM
- Kurulum (hazırlık) tamam: dizin iskelesi, araçlar, fontlar, build.py, boru-hattı duman testi ✓.
- SIRADAKİ: (1) sözlüğü board-game-translator ile kesinleştir → KİLİTLE; (2) ilk parti (kapak + s.2–4).
