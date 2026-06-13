GRIMCOVEN -> TURKCE KURAL KITABI / PROJE DURUMU
================================================
Kaynak PDF: GC_Rulebook_280x280mm_bleed3mm__36_pages.pdf (36 sayfa, 280x280mm, gercek vektor metin)
Hedef: TEK self-contained Turkce HTML (tum font+gorsel base64, cevrimdisi, 1:1 baski)

TAMAMLANAN: sayfa 1-36 — TÜM KİTAP BİTTİ (hepsi render+QC edildi).
KALAN: yok. Master = grimcoven_TR.html (s.1-36, ~18 MB).

DERLEME:
  python3 build.py 1 2 3 ... 11        -> /home/claude/preview.html (tam) + _check.html (wkhtml icin literal renk)
  wkhtmltoimage --enable-local-file-access --width 1058 _check.html /tmp/r.png
  Her sayfa render'da 1058px yuksek; sayfa N krop: y0=(1058+22)*(N-1), yukseklik 1058.
ASSET kaydi build.py icindeki ASSETS dict'inde (token->dosya). Yeni sayfa icin BASEnn/CLEANPARCHnn ekle.

URETIM YONTEMLERI (sayfa tipine gore):
  A) Metin agirlikli -> base render + parsomen-reveal kaplar (.txtcol) icinde akan Turkce. (s.6,7,9,10,11)
  B) Diyagram/kurulum -> base render KAL, sadece metin bloklarini reveal-kap ile cevir. (s.7,8,9,10)
  C) Kolaj/kart-jeton (genel bakis) -> gen_catalog.py overlay listesi (reveal maske + Turkce yazi). (s.4,5)
  Ornek kartlar / diyagram ic etiketleri (THIS TURN, ATTACK DECK vb.) = SANAT olarak Ingilizce birakildi.
  Ornek/figur CAPTION'lari (italik) = CEVRILIR (.capit/.capc; italik, ortali, ~7.5-8pt). Diyagram CALLOUT etiketleri
  (s.18 pano: "Stat card slot" vb. parsomen kenardaki aciklama etiketleri) = CEVRILDI (kucuk .lbl kaplari, kilavuz cizgi sanat kalir).
  ROMA RAKAMLI ADIM ROZETI (s.17 IV, s.20 V): kirmizi amblem SANAT kalir; baslik kabini rozetin SAGINA koy
  (left~157mm), govdeyi rozet ALTINDAN tam genislik baslat (rozet alt sinirini bands ile olc, s.17'de 38mm).
  s.17-20 = tip A/B (yogun metin + ornek kart/diyagram/cember-diyagram sanat). Yogun sayfada govde 7.7-8.2pt.

REVEAL-MASK teknigi (cekirdek):
  base = sayfanin tam render'i (Ingilizce bake). Ingilizceyi gizlemek icin metin bolgesinin uzerine,
  arka plani sayfanin KENDI temiz parsomeni olan bir div koy:
    background-image:parchmentNN; background-size:280mm 280mm;
    background-position:-Lmm -Tmm   (L,T = div'in sayfadaki sol/ust ofseti, mm)
  box-sizing:border-box; background-origin:border-box  (padding bg'yi kaydirmaz).
  Boylece o bolgeye AIT parsomen dilimi gorunur -> dikissiz. Ustune Turkce yazi.
  mm = yuzde * 2.8  (280mm sayfa).
  KRITIK: cikinti yapan adim numaralarini ortmek icin kaplari biraz SOLA genislet (left ~%7).
  Turkce daha uzun -> kap yuksekligini bol tut (tasma diyagrama girmesin); gerekirse fontu 8.0pt'ye dusur.

PARSOMEN CIKARMA: pdfimages -all ; tam-sayfa, lum 178-216 & sat 30-56 olan x-000 = SICAK parsomen
  (x-001 BEYAZ alttabaka -> YANLIS). tools_extract.py bunu otomatik secer.

OLCUM: tools_bands.py (kolon icindeki metin/sanat bantlarini y% olarak verir) + tools_grid.py (izgara).
  Pozisyonlari HER ZAMAN bands/grid ile olc; goz karari izgara okumasi hatali olabildi.

TASARIM TOKENLARI:
  --parchment #ead7bd  --clay #d4b297(callout)  --ink #1d1d1b  --ink-soft #4a3f36
  --oxblood #8a1c18(KIRMIZI gotik baslik + kutu kenar)  --gold #b8923f
  Font: Display=Grenze Gotisch ('GrenzeG', oxblood, ~28pt); Govde=Lora (Reg/It/Bold), gomulu WOFF2+WOFF.
BASLIK RENK KURALI:
  Bolum/chapter buyuk baslik = KIRMIZI gotik (gt): GAME SETUP, ROUND OVERVIEW, HUNTERS PHASE.
  Sayfa-ust bolum basligi (h1, ~15.5pt KOYU): Enemies Setup, Hunter Setup, Final steps, Griefbound/Environment setup.
  Alt baslik (h2, ~13pt KOYU): Map Setup, Event/Minions/Elite Setup, Dice slots, Hunter Turns, Hunter dice vb.
  Govde p 8.4pt/lh1.34; .step (asili girinti pl4.6 ti-4.6); .bullet (pl8.5 ti-3.2); .callout (clay+kenar).
SATIRICI IKONLAR (art/icons/, base64 IC_*): players, die_off/spd/def/arc, sym_off(kilic)/spd(ok)/def(kalkan)/arc(yildiz),
  lament(kirmizi damla), health(kirik kalp=Can), umark(❖ Evrensel Isaretleyici, ASSIST kartindan), wound(kirmizi X=Yara/hasar),
  range(siyah firca-oku=Menzil, inline height:.6em kullan; ic'de fazla kalin durur),
  die_enemy(krem cok-yuzlu zar=Dusman/atilan zar; siluet-dolgu ile cikarildi: her satir koyu-kenar min/max arasi opak),
  claw(pence glifi 𝑤=zar penç-sonucu; sym_arc yildizla KARISTIRMA — glif kimligini EN render'dan dogrula),
  lock(asma kilit=Yozlasma seridindeki Evrim simgesi), die6(krem d6 kupu=Avci zari kazanimi, siluet-dolgu),
  noenter(carpili bot=alana girilmez), nolos(carpili goz ∅=Gorus Hatti olculmez).
  move(bot=Hareket degeri), light(beyaz kanat, siluet-dolgu+rakam maskesi)/dark(koyu kanat)=Duality Isik/Karanlik,
  die_atk(koyu kup=Saldiri zari)/die_shd(mavi kup=Kalkan zari; mavi-piksel taramayla bbox bulundu).
  KURAL: kapak boyu EN metin bandina gore (TR kisa kalirsa EN kuyruk sizar); ikonun TUM gecislerini say;
  kapak sol kenari = sanat sag kenari OLCUMU (hex x170'e uzaniyordu, kapak x165 kirpti — s.23 dersi).
  s.24-27 PARTI DERSLERI (2026-06-12):
  (1) KOLON-ARASI GAP SIZINTISI: EN satir sonlari kapagin sag kenarini asabilir (s.27: EN 138.2, kapak 136.6) —
      her kolonda EN max-sag X'i OLC, kapagi gap'e dogru genislet (sag kolona 0.5mm kala).
  (2) KAPAK ALTINDA SANAT: kapagi konumlarken ALTINDAKI bolgeyi de dogrula (s.24: kapak 110-156 yanlisti;
      EN paragraf 98.2-116.8 USTTE sizdi + kukla eskizi 138.5+ ALTTA gizlendi). Bant-analizi (run/gap) kullan.
  (3) TAM-GENISLIK AYRAC CIZGILERI: kirmizi ince cizgiler (s.26 y=163, x23-252) kapak altinda kalirsa KIRIK gorunur —
      kapak ustunu cizginin ALTINA al (kirmizi-piksel taramasiyla y'sini bul).
  (4) MADDE LISTESI + SAGDA SANAT ETIKETI: tam-genislik kapak EN maddeleri gecmek icin uzatilamazsa
      kapagi BOL: tam-genislik (baslik+giris) + dar madde kapagi (s.26: 244x28.6 + 95x24.5).
  (5) Descender sizintisi: EN satirin alt kuyrugu kapak sinirinin hemen altinda soluk KESIK CIZGI olarak gorunur —
      kapagi 1.5-2mm asagi uzat.
  s.28-36 PARTI DERSLERI (2026-06-13):
  (6) BASE KOORDINAT SISTEMINI DOGRULA (s.36 dersi): base_pN.jpg bleed DAHIL cikarilmis olabilir —
      o zaman sanat y_base = 0.979*y_phi + 2.94 (286mm->280mm sikisma). ANKRAJ TESTI: folyonun phi-konumu
      (mm-3) ile render konumunu karsilastir; esitse bleed'siz, ~2.6mm asagi-kaymissa bleed'li.
      Bleed'li sayfada kapaklari PHI olcusuyle DEGIL base olcusuyle konumla (base_pN.jpg uzerinde bant olc).
  (7) GLIF DOGRULAMA KAZANDIRIR: s.28 'Sprint icin' zar = YESIL kup (Surat zari; TR'de 'Saldiri zari' yaziliydi -> duzeltildi);
      s.29 'missing X' = WOUND (health degil); s.30 'Instead they gain X' = ❖ UMARK (TR 'Lament' yaziliydi -> duzeltildi);
      s.30 'gains [2]' = SIYAH KALKAN-2 (def2; TR 'bir zar' yaziliydi -> duzeltildi); s.32 Enhance isareti = ❖ UMARK
      (TR 'Teknoloji zari simgesi' yaziliydi -> duzeltildi). Ikon ekleme oncesi HER glifin kimligini EN hi-res'ten dogrula.
  (8) TABLO HUCRE ETIKETLERI (s.28 rundown): hucre = IKON ustte (sanat, korunur) + ETIKET altta. Etiket bandini
      satir-profiliyle olc (ikon bandi ile karistirma!), duz-dolgu kapakla cevir (hucre zemin rengini ornekle;
      ilk hucre farkli renkte olabilir). Caption kutu icindeyse ayni yontem.
  (9) IKON CIKARIMI: yogun-blob yontemi (sutun basina koyu piksel >= esik) metin harflerinden ikonu ayirir;
      bbox'i once X-kumesiyle bul, sonra o pencerede Y-profilini olc (komsu satir descender'lari karismasin — s.30 def2 dersi).
  Yeni ikonlar: crave(kirmizi fiyonk=Ihtiras), tdie(turuncu kup=Teknoloji zari), def2(siyah kalkan-2=Savunma jetonu degeri 2),
  forge(mermi silueti=Dokum), dieg(gri cok yuzlu zar=herhangi zar), cog/dmag/dagi(carklı/cift-buyu/cift-ceviklik Zar Etkisi simgeleri).
  CSS: .ic{height:1em;valign:-.16em}  .ic-d{height:1.25em;valign:-.32em}. Oyuncu-sayisi ikonu metinde "oyuncu" kelimesi de olabilir.
  REVIEW-PASS (2026-06-12, s.13+): reveal-mask uretimde EN govdedeki satir-ici ikonlari sistematik olarak dusurmus —
  her sayfada base_pN.jpg'i tarayip wound[X]/health[♥]/lament/range[➤]/players ikonlarini EN'deki yere geri ekle.
  Cok-yuzlu zar ARTIK var (die_enemy/IC_DIE, siluet-dolgu). Hala metin: Savunma jetonu kalkanlari [2]/[4]
  (krem rakam≈parsomen; rakam metin yaziliyor, gercek jetonlar bitisik diyagramda). Gerekirse siluet-dolgu ile cikar.
  ADIM ROZETLERI (EVENT/MINIONS/ELITE "X STEP"): base-render SANATI, reveal-kapakla ORTME. Rozetli baslik =
  2-blok (baslik+ilk para rozetin SAGINDA ayri kap; govde ALTINDA tam-genislik). KUTU-ICI caption = duz-dolgu (reveal degil).
  KULLANICI 2. GORSEL TURU DERSLERI (2026-06-13):
  (10) 180° TERS METIN (s.34 Sonsoz epic tasarimi): EN'de govde bilerek bas-asagi basili (baslik+not DUZ kalir).
      TEKNIK: kapak div'ini DONDURME (parsomen doner -> doku dikisi). Bunun yerine METNI ic-sarmalayicida dondur:
      .flip{transform:rotate(180deg);transform-origin:center} ; <div class=txtcol ...><div class=flip>...<p>...</div></div>.
      Parsomen arka plan duz kalir = Ingilizce ters metni dikissiz orter; yalniz <p> metni ters gorunur (ic-sarmalayici tepeye yaslanir, metin kutu USTUNDEN baslar = EN ile hizalanir).
      SUTUN ESLEME: EN'i 180° cevirip OKU (flipped-SOL=hikaye basi A, flipped-SAG=devami B). Normal yonde A SAG kutuda, B SOL kutuda (180° harita: dusuk-x<->yuksek-x). Icerigi buna gore TAKAS et (uzun yari uzun kutuya). Baslik+not kapagini govde kutusuyla BITISIK yap (EN not 2. satir "marked as won" sizar — s.34: h18->19.5).
  (11) KOMSU SUTUN SANATINI KIRPMA (s.35 standee hasari): ikon/standee-legend sayfasinda etiket kapaklari, KOMSU
      sutundaki standee gorseline binebilir. KURAL: her etiket kapagi (a) kendi sutun sanatini gecmemeli, (b) bir sonraki
      sutun standee'sinin SOL kenarindan once bitmeli. EN etiket metin-sagini + komsu standee sol-kenarini OLC, kapagi
      arasina sigdir (s.35: sol etiket w72->54 cunku orta standee x110.7'de; orta etiket w60->49 cunku sag standee x185'te).
  (12) GORSEL-ICI DIYAGRAM ETIKETLERINI CEVIRME (s.26, kullanici istegi — SANAT politikasini gecersiz kilar):
      .dlbl{font-family Lora; font-weight 700; font-size 7pt (cap-height ~1.68mm OLCULDU = 7pt); color ink}.
      Zemin = parsomen reveal (gorsel-ici zeminle ayni). Kapak: (a) kilavuz cizgilerine (sari) DOKUNMA — EN'de sol/sag/alt
      konumunu olc, kapagi cizginin obur yaninda baslat/bitir; (b) maroon CERCEVE cizgisine dokunma (s.26 sag etiketler x250.7);
      (c) CERCEVE METNIN ARKASINDAN GECIYORSA (s.26 "Evrim alanlari" ustunde kirmizi cizgi y75.8-76) kapagi cizginin ALTINDAN
      baslat (metin y78-80.5, kapak y76.7) ki cizgi KIRILMASIN. Pano/board sanatina tasma (etiketler panonun solunda/saginda).
  KULLANICI 2. GORSEL TURU — 2. PARTI DERSLERI (2026-06-13, p19+p36):
  (13) ORNEK KART REVEAL-KAPAKLA KIRPILMASIN (s.19 LAMENT RAIN): metin kapagi alttaki ornek-kart SANATINI ortmemeli.
      Kartin y-sinirini ol (s.19 kart y83-140); kapagi kartin USTUNDE bitir (h86->61). TR metin EN'den kisaysa zaten sigar
      (s.19 TR y76.7'de bitti) — kap boyunu metne gore kis, bol tutup karta tasirma.
  (14) JETON-LEGEND ETIKETLERI JETONU ORTMESIN (s.36 SAG sutun JETONLAR): her "– Etiket" kapagi KENDI jetonunun sag
      kenarina cekilir (jeton kaybi yok). Jeton-etiket bosulugu <1.5mm (cok yakin) → kapak kacinilmaz olarak jeton kenarina
      ~0-1mm deger; bunu kabul et ama jeton GOVDESINI kesme. Konumu RENDER'dan (r_pNN) ampirik ayarla.
  (15) base_pNN.jpg OLCUMU ILE RENDER ARASINDA SAPMA (s.36): base_p36.jpg'de olculen x render'dan ~6mm sapabildi
      (bleed + dosya/render hiza farki). KAPAK KONUMUNU base'den DEGIL, RENDER krop'undan dogrula. Kapaklar HTML left'te
      1:1 render olur (debug: left:171 -> render x172, JETONLAR left:139 -> x139 ile dogrulandi).
  (16) DEBUG ARKA PLANI OPAK OLSUN: kapagin gercek yerini gormek icin gecici arka plan verirken rgba(...,0.55) gibi
      YARI-SAYDAM KULLANMA — altindaki Ingilizce gorunup "kapak ortmuyor" yanilgisi yaratir. Opak renk kullan, sonra geri al.
  (17) ASIRI KAYDIRMA JETONU KESER (s.36): etiketi jetonu acmak icin sola kaydirirken fazla kacma — 8mm kaydirma
      Savunma [4] jetonunu kesti, 6mm optimaldi. Her satir kendi jetonuna gore (genis jeton=az kaydir).

SOZLUK (KILITLI - tutarli uygula):
  KORU: Grimcoven, Lament, Griefbound, Pretender, Crowholme, Abyss, Portal, tum Hunter/kart/lore adlari.
  CEVIR: Hunter=Avci, Enemy=Dusman, Minion=Usak (Convicted=Mahkum, Undead=Olusuz), Elite Enemy=Seckin Dusman,
  Corrupted=Yozlasmis, Companion=Yoldas, Deputy=Yardimci, Board/pano, Corruption=Yozlasma, Hunger=Aclik,
  Tactic=Taktik, Defense=Savunma, Bullet=Mermi, Craving=Ihtiras, Status=Durum, Burn=Yanik, Stun=Sersemleme,
  Curse=Lanet, Treasure=Hazine, Lament Rift=Lament Yarigi, Health=Can, Map=Harita, Map tile=Harita Parcasi,
  Terrain=Arazi, Environment=Cevre, Landmark=Simge Yapi, Area=Bolge, Hunt Book=Av Kitabi, Hunt Sheet=Av Cizelgesi,
  Scenario=Senaryo, Setup=Kurulum, standee=ayaklik, model=model, Torture Device=Iskence Aleti, Swarm=Suru,
  Stomach=Mide, Divider=Ayrac, Help card=Yardim karti, Evolution=Evrim, Item=Esya, Event=Olay, Final Attack=Son Saldiri,
  Opportunity=Firsat, Stage=Evre, Secret=Sir, Quest=Gorev, Busy=Mesgul, First player=Ilk Oyuncu, Level=Seviye,
  Round=Tur, Turn=Sira, Phase=Asama, Step=Adim, Action=Eylem, Refresh=Tazeleme, Active pool=Aktif havuz,
  Discarded pool=Iskarta havuzu, Weapon=Silah, Armor=Zirh, Tier=Kademe, track=serit, Attack deck=Saldiri destesi,
  This Turn=Bu Sira, Next Turn=Sonraki Sira, dice=zar, damage=yara, Spawn=Cagirma, Named Elite=Adli Seckin, Critical Injury=Kritik Yaralanma, Line of Sight(LoS)=Gorus Hatti, Dice Effect=Zar Etkisi,
  Boss=Bas Dusman, Final Act=Son Perde, Trophy=Ganimet, FOCUSED=ODAKLANMIS, Lose condition=Kaybetme kosulu, tile=levha, coven=tarikat,
  Final Perdition=Nihai Mahvolus, Heal=Iyilestirme, "Once per Hunters Phase"=Avci Asamasi basina bir kez, Spaces=Alanlar, Teleport=Isinlanma,
  Light=Isik, Dark=Karanlik, Craving=Ihtiras, Rapid Hunt=Hizli Av, Enhanced=Gelistirilmis, Keywords=Anahtar Sozcukler, Epilogue=Sonsoz, Personality=Kisilik, Boss=Bas Dusman, "Open and Play"=Ac ve Oyna.
  KORU (cevrilmez): tum Avci adlari (Duality, Gunslinger, Keeper, Technomancer, Mannequin, Death Jester), Pretender'lar, dusman/patron adlari (Vampire, Alchemist, Bellfrog, Striga, Chimera, Convergence, Devourer, Tormentor, Swarm Mistress, Undead General, Graveyard Dragon), Arms/String/Balance/E'zlaaz/Fate/Hanged Man gibi bilesen-yetenek adlari.
   "Ac ve Oyna" / Adim I,II,III / oyuncu-sayisi -> kelime.

ORTAM (sandbox): headless chromium YOK. wkhtmltoimage (WebKit) render-check; var() okuyamaz -> build.py _check.html'e
  literal hex yazar (sadece renk; url() degil). pip: --break-system-packages. fonttools+brotli+Pillow kurulu.
ORTAM (YEREL MAC, bu repo): wkhtmltoimage brew'den KALDIRILMIS. Render-check = Google Chrome headless.
  Kullanim: python3 build.py 1..N  ->  python3 render_check.py <toplam> <kropPN...>  (Chrome _check.html'i 1058px
  genislikte cekip sayfa N'i (N-1)*1080 ofsetinden kirpar -> /tmp/r_pNN.png). Chrome var() okur. PATH'e /opt/homebrew/bin.
  build.py/gen_catalog.py ROOT artik __file__ tabanli (tasinabilir). pip --user ile /usr/bin/python3 (3.9) icine kuruldu.
  Master teslim: sandbox'ta /mnt/user-data/outputs/grimcoven_TR.html; yerelde repo koku grimcoven_TR.html.

VERIMLILIK (yeni kural): ONIZLEME "parti" gorselleri URETME. Master HTML'i /mnt/user-data/outputs/grimcoven_TR.html
  uzerine build.py ile guncelle (bastan uretmek token degil; dosyaya yazilir). QC icin MINIMUM, hedefli krop bak.
