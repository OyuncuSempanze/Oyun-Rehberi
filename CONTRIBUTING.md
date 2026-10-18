# Oyun-Rehberi'ne katkıda bulunma

Oyun-Rehberi, oyunlar hakkında kaynaklı, düzenli ve Türkçe bilgi sunan bir arşivdir. Özellikle daha az ele alınan niş ve bağımsız oyunlara odaklanır. Katkılar, bilgi kalitesini ve kaynakların izlenebilirliğini korumalıdır.

## Neye katkı verebilirsin?

- Yeni bir oyun için anlamlı ve kaynaklı rehber içeriği önermek.
- Mevcut bir bilgiyi doğrulamak, güncellemek veya hatasını düzeltmek.
- Eksik mekanik, kural, güncelleme bilgisi ya da açıklama eklemek.
- Veri kümesi üretimini, doğrulamasını veya site işleyişini etkileyen bir sorunu bildirmek.
- Tekrarlanan, boş ya da bilgi değeri düşük bir bölümü sadeleştirmek.

Yeni bir oyun eklemeden önce mevcut arşivde aynı oyunun bulunup bulunmadığını kontrol et. Sırf dosya sayısını artırmak için boş ya da tekrar eden sayfalar oluşturma.

## İçerik kuralları

1. **Kaynakları iddiaların yanına koy.** Mümkün olduğunda doğrudan ilgili resmî açıklamaya bağlantı ver. Bir başkasının yazısını kaynak göstermeden kopyalama.
2. **Bilgi türlerini doğru etiketle.** `[Resmî Kaynak]` yalnızca geliştirici, yayıncı veya oyunun resmî kanalları içindir. Oyunda bizzat gözlenen bilgiler `[Oyun İçi Gözlem]` olarak işaretlenir. Kaynak etiketi bir güvenilirlik puanı değildir.
3. **Gözlemi doğru tarif et.** Gerekli olduğunda nasıl kontrol edildiğini ve hangi sürümde görüldüğünü belirt. Her basit bilgiye gereksiz sürüm notu veya uyarı ekleme.
4. **Gerçek ile öneriyi ayır.** Kişisel tavsiyeyi resmî kural gibi sunma. Doğrulanmamış iddiayı doğrulanmış bilgi olarak yazma.
5. **Hak sahibi olmadığın materyali ekleme.** Başka bir siteden alınmış metin, ekran görüntüsü, görsel, logo veya alıntıyı izin ve lisansını kontrol etmeden depoya koyma. Bir oyunun görselinin internette bulunması, onu yeniden yayımlama hakkı vermez.
6. **Konuya odaklan.** Reklam, spam, hakaret, kişisel bilgiler ve konu dışı içerik gönderme.
7. **Atıf bilgisini bildir.** PR açıklamasında katkın için kullanılmasını istediğin ad veya GitHub kullanıcı adını belirt. Kabul edilen katkı sahipleri `CONTRIBUTORS.md` dosyasına eklenebilir.

## Değişiklikleri nasıl önerirsin?

1. Depoyu kendi hesabına fork et veya uygun bir dalda çalış.
2. Değişiklikleri anlaşılır ve mümkünse tek bir amaca odaklı tut.
3. PR açarken bu dosyadaki kuralları ve PR şablonunu tamamla.
4. Proje sahibi değişiklikleri inceleyebilir, düzeltme isteyebilir, bir kısmını kabul edebilir veya PR'ı reddedebilir. PR açmak, değişikliğin kabul edildiği anlamına gelmez.
5. Birleştirme yapılmadan önce kaynak doğruluğu ve uygun otomatik kontroller incelenir.

Rehber veya SSS Markdown dosyalarını değiştirdiğinde, ilgili veri kümesi çıktıları da değişiyorsa bunları yeniden üret:

~~~bash
python scripts/build_dataset.py
python scripts/build_dataset.py --check
~~~

İlk komut çıktıları oluşturur. İkinci komut üretilmiş dosyaların kaynaklarla eşleştiğini kontrol eder. Üretim çıktılarında değişiklik olduysa ilgili JSONL dosyalarını PR'a dahil et. Sırf değişiklik yapılmış görünsün diye ilgisiz dosyaları düzenleme.

## Lisans, telif ve gelecekte gelir elde edilmesi

Bu bölüm PR gönderirken özellikle okunmalıdır.

- Katkı sahibi, kendisine ait özgün içerik üzerindeki telif hakkını korur. Katkının kabul edilmesi, telif hakkının veya projenin mülkiyetinin devredildiği anlamına gelmez.
- Oyun-Rehberi'nin özgün editoryal metinleri ve açıkça bu koşulu kabul eden katkılar **CC BY 4.0** kapsamında yayımlanır. Bir katkının lisans kapsamına alınması için PR şablonundaki lisans onay kutusunun açıkça işaretlenmesi gerekir. Bu onay verilmeyen katkı birleştirilmez.
- CC BY 4.0, uygun atıf koşullarıyla ticari kullanıma izin verir. Bu izin yalnızca Oyun-Rehberi için değildir: üçüncü kişiler de aynı içeriği lisans koşullarına uyarak ticari amaçlarla kullanabilir. Bu lisans içerik üzerinde münhasırlık sağlamaz.
- Oyun-Rehberi ileride reklam, sponsorluk, üyelik, hizmet, özel çalışma veya başka bir yolla gelir elde ederse, bir PR'ın kabul edilmiş olması katkı sahibine otomatik olarak gelir payı, maaş, ortaklık veya projede karar verme hakkı vermez. Farklı bir ödeme ya da gelir paylaşımı ancak ayrıca ve yazılı olarak kararlaştırılırsa söz konusu olur. Bu açıklama, yürürlükteki hukuk uyarınca vazgeçilemeyen hakları ortadan kaldırmaz.
- Katkının CC BY 4.0 kapsamında başkaları tarafından da ticari amaçla kullanılmasını istemiyorsan bu koşullarla katkı gönderme. Proje sahibinin ticari olarak kullanabileceği ancak diğer herkesin kullanamayacağı bir lisans istenirse ayrı bir lisans sözleşmesi gerekir.
- Katkıyı göndermeden önce içeriği lisanslama yetkin bulunduğundan emin ol. Yaşın veya yerel hukuk nedeniyle bu koşulları kabul etme yetkin konusunda şüphe varsa, katkı göndermeden önce yasal temsilcinden ya da nitelikli bir hukuk uzmanından destek al.

Bu kurallar, katkı sürecini açık hâle getirmek içindir; kişiye özel hukuki danışmanlık veya gelecekte herhangi bir gelir elde edileceği yönünde vaat değildir. Proje ticari bir faaliyete dönüşmeden önce katkı koşullarının hukuk uzmanına inceletilmesi gerekir.

## İnceleme ilkesi

Son karar proje sahibinindir. İnceleme, içeriğin niteliğine, kaynakların uygunluğuna, lisans onayına, teknik kontrollerin sonucuna ve projenin kapsamına göre yapılır. Bir PR'ın reddedilmesi kişisel bir değerlendirme değil, proje kapsamına ilişkin bir karardır.
