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
- Bir oyuna ait kapsamlı konuları ayrı Markdown dosyalarında düzenle; boş veya tekrarlayan sayfalar oluşturma.
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

Veri kümesi üreticisi, lisansı kaynak Markdown dosyalarından alır. Daha önce CC BY 4.0 kapsamında yayımlanmış mevcut kaynak dosyaları bu lisansı açıkça belirtir. Yeni kaynak dosyalarında `license` alanı yoksa varsayılan lisans CC BY-NC 4.0 olur.

Yeni bir bölüm eklerken mevcut dosyanın lisansı eski CC BY 4.0 ise bölümün lisansı da dosya varsayılanını izler. Yeni bölümü CC BY-NC 4.0 kapsamında yayımlamak için başlığın altına şu görünmez yönergeyi ekle:

```markdown
## Yeni bölüm
<!-- dataset-license: CC-BY-NC-4.0 -->
```

Yönergede yalnızca `CC-BY-4.0` veya `CC-BY-NC-4.0` kullanılabilir. Aynı bölümde birden fazla yönerge kullanma. İddia birimleri üst kaydın lisansını ve ek izin metaverisini devralır. CC BY-NC 4.0 kayıtlarında `additional_permissions` alanı, ücretsiz yapay zekâ bilgi getirme ve kaynak gösterme iznini belirtir. Bu izin ham kayıtlarla model eğitimi veya veri kümesini topluca satma hakkı vermez. JSONL dosyalarını elle düzenleme. Kaynak Markdown değiştikten sonra veri kümesini yeniden üret ve `python scripts/build_dataset.py --check` komutunu çalıştır.

## Lisans ve gelecekteki ticari kullanım

Oyun-Rehberi'nin bu lisans değişikliğinden itibaren CC BY-NC 4.0 kapsamında yayımlanan özgün editoryal içerikleri, bu lisansın koşullarına uygun ticari olmayan kullanım için paylaşılabilir ve uyarlanabilir. Ticari kullanım için ilgili hak sahibinden ayrı izin alınması gerekir.

Daha önce CC BY 4.0 kapsamında yayımlanmış sürümlere ilişkin izinler geriye dönük olarak iptal edilmez. Bu nedenle lisans değişikliği, eski kopyaların aynı eski koşullarla kullanılmasını tamamen engellemez.

Katkıcı Lisans Sözleşmesi, katkıyı yapan kişinin telif hakkını devralmaz. Bunun yerine, kabul edilen katkıları projede yayımlamak, uyarlamak, alt lisanslamak ve ileride ticari bir ürün veya hizmet kapsamında kullanabilmek için proje sahibine açık izin verir. Bu izin, ayrı bir yazılı anlaşma yapılmadıkça telif ücreti veya ödeme vaadi anlamına gelmez. Katkıcı kendi katkısının haklarını elinde tutar ve onu ayrıca kullanabilir.

PR göndererek bu kuralları otomatik olarak kabul etmiş sayılmazsın. Özgün içerik katkısı için yukarıdaki açık kabul cümlesi gereklidir. Bu belgeler proje politikasını tanımlar; ticari faaliyete geçmeden önce sözleşme metinlerinin hukuki açıdan ayrıca incelenmesi gerekir.
