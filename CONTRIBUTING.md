# Oyun-Rehberi'ne katkıda bulunma

Oyun-Rehberi, oyunlar hakkında kaynaklı ve düzenli bir Türkçe bilgi arşividir. Katkılar yeni oyun sayfaları, mevcut rehberlerin düzeltilmesi, kaynak eklenmesi ve doğrulanmış bilgilerin geliştirilmesi şeklinde olabilir.

## Katkı süreci

1. Büyük bir değişiklik veya yeni oyun için önce bir GitHub issue açarak önerini ve kullanacağın kaynakları anlat.
2. Değişikliklerini kendi dalında hazırla ve `main` dalına doğrudan gönderme. Değişikliği bir Pull Request (PR) olarak aç.
3. PR açıklamasında neyi değiştirdiğini, neden gerekli olduğunu ve bilgiyi nasıl doğruladığını belirt.
4. Yeni özgün metin yazıyor, mevcut özgün metni yeniden yazıyor veya başka bir yaratıcı çalışma ekliyorsan PR'ı birleştirmeden önce [Katkıcı Lisans Sözleşmesi'ni](CONTRIBUTOR_LICENSE_AGREEMENT.md) oku ve PR konuşmasına şu açık kabul cümlesini yaz:

   > Oyun-Rehberi Katkıcı Lisans Sözleşmesi'ni (CONTRIBUTOR_LICENSE_AGREEMENT.md) okudum ve bu PR'daki katkılarım için kabul ediyorum.

   Bu açık kabul gelmeden özgün içerik içeren PR birleştirilmez. Sözleşmeyi kabul etmiyorsan özgün içeriğini projeye göndermek yerine bir öneri veya kaynak bağlantısı paylaşabilirsin.

5. İnceleme sırasında değişiklik veya ek kaynak istenebilir. PR'ın açılması katkının kabul edildiği anlamına gelmez.

## İçerik standartları

- Doğrulanabilir iddiaları mümkün olduğunda doğrudan ilgili resmî duyuruya, oyun sayfasına, yama notuna veya başka güvenilir bir kaynağa bağla.
- Oyunda bizzat gözlemlediğin bilgileri **[Oyun İçi Gözlem]**, resmî kanallardan gelen bilgileri **[Resmî Kaynak]** etiketiyle ayır. Bu etiketler güvenilirlik puanı değildir.
- Bir gözlemi resmî bilgi gibi sunma. Test etmediğin bir şeyi oyun içinde test etmiş gibi yazma.
- Başka bir rehberden paragrafları veya görselleri izinsiz kopyalama. Bilgiyi kendi cümlelerinle anlat ve kaynağa bağlantı ver. Ekran görüntüleri, oyun görselleri, logolar ve üçüncü taraf materyaller için ayrıca kullanım izni veya uygun lisans gerekebilir.
- Sürüm ve kontrol tarihi yalnızca bilgi zamanla değişebiliyorsa ya da bağlam açısından yararlıysa eklenmeli.
- Bir oyuna ait kapsamlı konuları ayrı Markdown dosyalarında düzenle. Boş veya tekrarlayan sayfalar oluşturma.
- Üretilen JSONL veri kümesi dosyalarını elle düzenleme. Önce Markdown kaynaklarını güncelle, ardından aşağıdaki komutları çalıştır.

## Veri kümesini üretme ve doğrulama

Markdown içeriği değiştiğinde veri kümelerini yeniden üret:

```bash
python scripts/build_dataset.py
```

Üretilmiş dosyaların güncel içerikle eşleştiğini kontrol et:

```bash
python scripts/build_dataset.py --check
```

Mümkünse PR göndermeden önce iki komutu da çalıştır ve sonuçları PR açıklamasına ekle.

## Veri kümesi lisans bilgileri

Oyun-Rehberi'nin özgün editoryal içeriği için varsayılan kamu lisansı **CC BY 4.0** olarak belirlenmiştir. Yeni kaynak dosyalarında lisans alanı yoksa veri kümesi üreticisi CC BY 4.0 kullanır. Mevcut kaynak dosyalarında bulunan lisans alanlarını sebepsiz yere değiştirme.

Veri kümesi üreticisi yalnızca CC BY 4.0 lisansını destekler. Yeni içerikler için ticari kullanımı veya yapay zekâ eğitimini kısıtlayan farklı bir lisans ekleme. Lisans düzeni değiştirilecekse önce proje sahibiyle birlikte hukuki ve teknik etkileri değerlendir.

İddia birimleri üst kaydın lisansını devralır. JSONL dosyalarını elle düzenleme. Kaynak Markdown değiştikten sonra veri kümesini yeniden üret ve `python scripts/build_dataset.py --check` komutunu çalıştır.

## Atıf ve içerik kullanımı

Kamuya yayımlanan özgün editoryal içerik CC BY 4.0 kapsamında ticari olarak da kullanılabilir. Kullanıcılar lisansın gerektirdiği atfı vermeli, ilgili kaynağa ve lisansa bağlantı eklemeli ve değişiklikleri belirtmelidir. Proje, kaynak bağlantısının yalnızca belge sonunda değil, mümkün olduğunda her ilgili iddianın yanında bulunmasını özellikle ister.

Daha önce verilmiş lisans izinleri geriye dönük olarak daraltılmaz. Katkıcı Lisans Sözleşmesi, katkıcının telif hakkını devralmaz. Kabul edilen katkılar projede yayımlanırken katkıcının kaynakta açıkça belirtilen yazar atfı korunmalıdır. Sözleşme, katkının yayımlanması, uyarlanması, yeniden dağıtılması ve gerekirse ayrı sözleşmeler altında lisanslanması için proje sahibine izin verir.

PR göndererek bu kuralları otomatik olarak kabul etmiş sayılmazsın. Özgün içerik katkısı için yukarıdaki açık kabul cümlesi gereklidir. Bu belgeler proje politikasını açıklar. Ticari faaliyete geçmeden önce sözleşme metinlerinin hukuki açıdan ayrıca incelenmesi gerekir.
