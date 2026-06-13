# KURAL KİTABI — Grimcoven (Türkçe)

Awaken Realms **Grimcoven** kutu oyununun kural kitabı ve yardımcı belgelerinin
**gayriresmî Türkçe yerelleştirmesi** ve dizgisi. Her belge çevrimdışı açılan,
baskıya uygun, kendi-kendine yeten HTML olarak yeniden dizildi.

## İçerik

**`site/`** — yayına hazır statik site (*KURAL KİTABI*):
- **Kural Kitabı** — 36 sayfa, 1:1 baskıya uygun, tek self-contained HTML
- **Resmî Oyun SSS** — A4 baskıya hazır PDF + HTML
- **Evrensel Av İpuçları** — A4 baskıya hazır PDF + HTML

**`grimcoven_proje/`** — çalışma kaynakları:
- Dizgi script'leri (`build.py`, `build_docs.py`, `tools_*.py`, `render_check.py`)
- Fontlar (`fonts/` — SIL Open Font License)
- Sayfa parçaları (`pages/`)
- Teknik günlük (`JOURNAL.md`)

## Yayınlama

Statik site; derleme adımı yok. **Yayın dizini: `site/`**
- **Netlify:** "Add new site → Deploy manually" → `site/` klasörünü sürükle. Ya da bu repoyu bağla; *Publish directory* = `site`, *Build command* boş.
- **GitHub Pages:** Pages yalnızca kök ya da `/docs`'tan yayınladığı için `site/` içeriğini bir `docs/` klasörüne taşı, ya da `site/`'ı yayınlayan bir Pages Action ekle. (En kolayı Netlify.)

## Yeniden dizgi hakkında

Telif nedeniyle **yayıncının orijinal PDF'leri ve bunlardan türetilmiş görsel render'lar bu
depoda bulunmaz.** Script'ler bu kaynaklarla birlikte çalışacak şekilde tasarlanmıştır;
yayınlanan çıktı (`site/`) ise tüm font ve görselleri gömülü olarak içerir ve tek başına çalışır.

## Telif & Sorumluluk Reddi

Bu, hayranlar tarafından hazırlanmış **gayriresmî** bir çeviridir; yalnızca kişisel ve topluluk
kullanımı içindir, **ticari amaç taşımaz.** *Grimcoven* ile tüm ilgili isim, görsel ve içerik
**© Awaken Realms**'e aittir. Bu proje Awaken Realms ile bağlantılı ya da onun tarafından
onaylanmış değildir. Hak sahibinin talebi hâlinde içerik kaldırılır.

Kullanılan yazı tipleri (Grenze Gotisch, Lora, Metamorphous) SIL Open Font License (OFL) altındadır.
