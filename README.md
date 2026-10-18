# 🎮 Oyun-Rehberi

Oyunlar hakkında kaynaklı ve düzenli bir Türkçe bilgi arşivi. Özellikle ana akım medyada daha az yer bulan niş ve bağımsız yapımlara odaklanır.

🌐 [Web sitesini görüntüle](https://oyuncusempanze.github.io/Oyun-Rehberi/)

## Bilgi standartları

Etiketler bilginin dayanağını gösterir. Bunlar bir güvenilirlik puanı değildir ve bilginin kaynağını belirtmek için kullanılır.

- **[Resmî Kaynak]** Bilginin geliştirici, yayıncı veya oyunun resmî kanalları tarafından yayımlandığını belirtir. Bağlantı, mümkün olduğunda doğrudan ilgili açıklamaya götürür.
- **[Oyun İçi Gözlem]** Bilginin oyun deneyimi sırasında doğrudan görüldüğünü veya test edildiğini belirtir. Bu bir şüphe ya da uyarı etiketi değildir.
- **[Kaynak]** Bir iddianın dayanağını incelemek için kullanılan bağlantıyı veya bağımsız başvuru kaynağını belirtir.
- **[Öneri]** Arşiv yazarının deneyimine, gözlemine veya genel sorun çözme ilkelerine dayanarak sunduğu tavsiyeyi belirtir. Resmî bir kural veya zorunluluk anlamına gelmez. Gerektiğinde önerinin dayanağını açıklayan diğer etiketlerle birlikte kullanılabilir.

Resmî açıklamalar ve oyun içi gözlemler birbirinden ayrı tutulur. **[Resmî Kaynak]** etiketi yalnızca resmî kanallar için kullanılır. Bir bilgi doğrudan oyunda kontrol edildiyse **[Oyun İçi Gözlem]** ile belirtilir. Başka kaynaklardan yararlanıldığında ilgili bağlantı, mümkün olduğunca dayandığı bilginin yanında yer alır.

Sürüm numarası ve kontrol tarihi, özellikle güncelleme geçmişi veya zamanla değişen fiyat ve kurallar gibi bilgiler için bağlam sağladığında belirtilir. Güncel oynanışı anlatan bir bilginin artık geçerli olmadığı kontrol edilirse ilgili bölüm güncellenir veya bilgi kaldırılır. Önceki sürümlerdeki davranış tarihsel açıdan önemliyse güncelleme geçmişinde korunabilir.

## Rehber yapısı

Her oyunun `index.md` sayfası ilgili rehberlere bağlantı verir. `oyun-hakkinda.md` temel bilgileri toplar. Mekanikler, güncellemeler, kurallar veya görseller için ayrı dosya, konu yeterince kapsamlıysa açılır. Boş ya da tekrarlayan sayfalar eklenmez.

## Veri kümeleri

Sitedeki [Veri kümeleri sayfasından](https://oyuncusempanze.github.io/Oyun-Rehberi/veri-kumeleri/) indirilebilir JSONL dosyaları sunulur. Veri kümesi SSS kayıtlarının yanında mekanikler, oynanış, kurallar, güncellemeler ve diğer rehber bölümlerini de içerir. Kayıtlar kaynak bağlantılarını, bilgi türü etiketlerini ve asıl rehber sayfasını korur.

Oyun rehberi veya SSS Markdown içeriğini düzenledikten sonra veri kümesi dosyalarını yeniden üret:

```bash
python scripts/build_dataset.py
```

Üretilmiş dosyaların güncel içerikle eşleştiğini kontrol etmek için:

```bash
python scripts/build_dataset.py --check
```

GitHub Actions bu kontrolü oyun rehberleri, SSS sayfaları veya veri kümesi dosyaları değiştiğinde otomatik çalıştırır.

## Lisans

OyuncuSempanze tarafından oluşturulan özgün rehber metinleri, oyun içi gözlem yazıları ve arşivin özgün seçim ve düzenlemesi [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) kapsamında lisanslanır. Lisans bütün depoya otomatik olarak uygulanmaz. Site kaynak kodu ve arayüzü, oyun ekran görüntüleri, üçüncü taraf görseller ve başka hak sahiplerine ait içerikler kapsam dışındadır.

Ayrıntılar için [lisans kapsamı sayfasına](lisans.md) ve depodaki [LICENSE dosyasına](LICENSE) bak.
