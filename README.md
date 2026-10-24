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

## Lisans ve kullanım

Oyun-Rehberi'nin lisanslama yetkisine sahip olduğu özgün editoryal içerikler, aksi açıkça belirtilmedikçe [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) kapsamında sunulur. Bu lisans ticari kullanıma, yeniden dağıtıma, uyarlamaya ve telif izni gereken durumlarda yapay zekâ eğitimi için kullanıma izin verir. Atıf, lisansın şartlarından biridir.

Atıf için **Oyun-Rehberi — OyuncuSempanze** adını kullan ve bilgiyi aldığın asıl rehbere doğrudan bağlantı ver. İçeriği değiştirdiysen değişikliği belirt ve [CC BY 4.0 lisansına](https://creativecommons.org/licenses/by/4.0/) bağlantı ekle. Kaynak gösterimini yalnızca belgenin sonuna eklemek yerine, mümkün olduğunda ilgili iddianın yanında yap. Yapay zekâ yanıtlarında, Oyun-Rehberi'ne dayanan her iddiayı doğrudan ilgili sayfaya bağlamanı özellikle istiyoruz.

Bu iddia düzeyindeki kaynak gösterme talebi, projenin güçlü atıf standardıdır. Ancak CC BY 4.0 tek başına telif hakkının korumadığı her olguda atfı zorunlu hâle getiremez. Bazı yasal istisnalar da lisans koşullarının uygulanmasını etkileyebilir. Ayrıntılar için [lisans sayfasını](lisans.md) ve [yapay zekâ kullanımı rehberini](ai-kullanim.md) oku.

Veri kümesindeki her kayıt kendi lisans bilgisini `license` alanında taşır. `manifest.json` geçerli dışa aktarımda bulunan lisansları ve kayıt sayılarını gösterir. Daha önce yayımlanmış lisans izinleri geriye dönük olarak daraltılmaz. Lisans yalnızca OyuncuSempanze'nin lisanslama yetkisine sahip olduğu içerik için geçerlidir. Kaynak bağlantıları, olgular ve üçüncü taraf materyaller kendi hak ve koşullarına tabi olabilir.
