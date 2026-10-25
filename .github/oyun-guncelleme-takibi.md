# Oyun güncelleme takibi

Bu takip sistemi, arşivdeki her oyunu sürekli elle kontrol etmek zorunda kalmamak için kontrol zamanı gelen oyunları listeler.

## Sistem ne yapar?

GitHub Actions her pazartesi Türkiye saatiyle 11.00 civarında takip dosyasını inceler. Kontrol zamanı gelen oyun varsa depoda **Oyun güncelleme kontrolü** başlıklı bir GitHub Issue oluşturur veya açık olan hatırlatmayı günceller. Yeni bir oyun kontrol sırasına girdiğinde açık hatırlatmaya Türkçe bir yorum da eklenir.

Bir oyun için kontrol tarihi boş bırakılmışsa ilk kontrol gerekir. Takip aralığı oyunun değişme sıklığına göre belirlenmiştir. Bu aralıklar başlangıç değerleridir ve deneyime göre değiştirilebilir.

## Sistem ne yapmaz?

Bu sürüm oyunların mağaza sayfalarını veya yama notlarını otomatik olarak taramaz. Oyunun yeni sürüm aldığını kendi başına doğrulamaz ve rehberleri değiştirmez. Yalnızca kaynak bağlantılarına bakma zamanını hatırlatır.

## Kontrolü nasıl kaydederiz?

1. Hatırlatmadaki resmî kaynakları aç ve önceki kontrol tarihinden sonra yeni sürüm veya önemli bir değişiklik olup olmadığına bak.
2. Değişiklik varsa ilgili rehberi güncelle. Değişiklik yoksa rehbere dokunmak gerekmez.
3. `.github/oyun-guncelleme-takibi.json` dosyasındaki ilgili oyunun `last_checked` alanını kontrolü yaptığın Türkiye tarihine göre `YYYY-MM-DD` biçiminde değiştir.
4. Değişiklikleri ana dala aldıktan sonra takip sistemi bir sonraki çalışmasında zamanı gelmeyen oyunları hatırlatma listesinden çıkarır. Kontrol edilecek oyun kalmadığında açık hatırlatmayı otomatik kapatır.

Örnek olarak `"last_checked": "2026-10-25"` kullanılır. İlk kontrol tarihi henüz bilinmiyorsa alan `null` kalır.

## Takip aralıkları

- **Bloody Bastards** için 30 gün.
- **DATA WING** için 90 gün.
- **Wplace.live** için 7 gün.

Bunlar kesin kurallar değildir. Çevrim içi hizmetlerde değişiklikler daha sık olabileceği için Wplace.live başlangıçta daha sık kontrol edilir. DATA WING için kayıtlı bir kontrol tarihi olmadığı için ilk kontrol listelenir.
