---
layout: default
title: Wplace.live Mekanikleri
description: "Wplace.live piksel yenilenmesi, Droplets, mağaza, klan merkezi ve şablon sistemi hakkında Türkçe açıklamalar."
---

# Mekanikler

*Doğrulama notu (15 Ekim 2026): Bazı sayısal değerler, mağaza ücretleri ve ilerleme bilgileri topluluk kaynaklarına veya oyun içi gözleme dayanır. Bunların tamamı resmî yama notlarında doğrulanamıyor. Güncel ücretlerde oyun içindeki mağaza ve resmî yama notları esas alınmalıdır.*

## Temel Mekanikler

- Oyuncular başlangıçta 30 piksel hakkıyla başlar ve harcanan her piksel her 30 saniyede bir yenilenir. Bu yenileme süresi normal kanvas için sabittir. Oyuncular bu hızı **ana haritada** kısaltamaz [Kaynak](https://github.com/TeamRealB/Wplace-Protocol/blob/main/README_EN.md) [Resmî Kaynak](https://wplace.live/patch-notes). (Not: Klan merkezlerinde şarj yenileme süresi, “Alliance Headquarters” yükseltmeleriyle klana özel haritada 10 ya da 5 saniyeye indirilebilir.)

- Oyuncular Damla (Droplets) adı verilen puanları biriktirir ve bunları mağazada çeşitli kozmetik eşyalar ile oyun içi geliştirmeler için harcayabilir [Kaynak](https://placepixels.com/wplace-droplets). Örneğin profil resimleri, avatarlar, bayraklar veya renk paketleri Droplets’le satın alınır.

## Droplets ve Prism

Resmî 1.7.3 yama notları, bazı geri bildirim ve hata bildirimlerinin etkisine bağlı olarak Droplets veya Prism ödülü verilebildiğini belirtiyor. Prism'in tüm kazanım yolları ve kullanım alanları burada kesin olarak belgelenmediği için bu ayrıntılar oyun içinden ayrıca kontrol edilmelidir. [Resmî 1.7.3 yama notları](https://wplace.live/patch-notes/1.7.3)

## Dükkan

- **Anında +30 Piksel:** Mevcut piksel hakkına 30 adet ekler. Maliyet: 500 Droplets [Kaynak](https://placepixels.com/wplace-droplets).

- **Kalıcı +5 Kapasite:** Piksel havuzu maksimumunu 5 artırır. Maliyet: 500 Droplets [Kaynak](https://github.com/TeamRealB/Wplace-Protocol/blob/main/README_EN.md).

- **Bayrak (Ulusal Bölge):** 20.000 Droplets karşılığında satın alınır. Aktifleştirilen ülke bayrağı altında boyanan her pikselin %10’u anında geri gelir [Kaynak](https://github.com/TeamRealB/Wplace-Protocol/blob/main/README_EN.md). Bayrak bir defa satın alındığında **kalıcı olarak** hesaba eklenir. **(Yani örneğin Türkiye bayrağı alınıp seçildiğinde, Türkiye sınırları içinde boyanan piksellerin %10’u anında geri kazanılır.)**

- **Kozmetik Ürünler:** Özel avatar veya kilitli renk gibi öğelerdir. Örneğin özel avatar 20.000, premium renkler ise 2.000 Droplets’tır [Kaynak](https://placepixels.com/wplace-droplets). Bu ürünler yalnızca görsel amaçlıdır ve oynanışı etkilemez.

## Damlacık Kazanma

- **Piksel Boyayarak:** Ana haritaya her yerleştirilen piksel için 1 Droplet verilir [Kaynak](https://github.com/TeamRealB/Wplace-Protocol/blob/main/README_EN.md).

- **Seviye Atlayarak:** Hesap seviyesi yükseldiğinde 500 Droplets kazanılır [Kaynak](https://github.com/TeamRealB/Wplace-Protocol/blob/main/README_EN.md).

- **Gerçek Parayla Satın Alarak:** Droplets, mağaza üzerinden **gerçek para** karşılığında da satın alınabilir [Kaynak](https://apps.apple.com/tr/app/wplace-paint-the-world/id6792942987).

## Klan (Alliance)

- **Klan Oluşturma:** Yeni bir klan kurmak için 25.000 Droplet gereklidir [Oyun İçi Gözlem]. Klan kurulduğunda bir Alliance Profile (topluluk profili) oluşturulur ve lider/kurucusu belirlenir.

- **Ortak Kanvas (Klan Merkezi):** Her klanın oyun haritası dışında özel bir boyama alanı (Headquarters) vardır. Klan üyeleri bu alanda kendi piksel havuzlarından harcama yaparak boyama yapabilirler. [Resmî Kaynak](https://wplace.live/patch-notes). Bu “HQ” kanvası ana haritadan tamamen ayrıdır. Üyeler burada boyama yaptığında ana kanvastaki hakları etkilenmez.
  
- **Şablon Paylaşımı:** Klan liderleri veya yöneticileri, klana özel ortak şablonlar (overlays) ekleyebilir. Bu şablonlar klan üyelerine sunulur ve herkes tarafından kullanılabilir [Resmî Kaynak](https://wplace.live/patch-notes). (Örneğin bir turnuva veya proje şablonu klan ile paylaşılarak bütün üyelerin aynı referans üzerinde çalışması sağlanabilir.)
  
- **Klan İlerleme:** Klanlar, üyelerinin ana haritaya attığı her geçerli piksel için Alliance Coin kazanır (bu sistem yama notlarında belirtilmiştir). Klan liderleri bu puanlarla başlık, bayrak, yeni renkler ve HQ yükseltmeleri gibi klan geliştirmeleri satın alabilir. Klan içi puan kazanımı büyük ölçüde üyelerin ana kanvas çalışmasıyla sağlanır [Resmî Kaynak](https://wplace.live/patch-notes). Klan yükseltmeleri ise klan merkezindeki araçlar ve kişiselleştirme (profil resmi, açıklama vb.) ile ilgilidir [Resmî Kaynak](https://wplace.live/patch-notes).

## Şablon (Overlay)

- Oyuncular kendi şablon (overlay) görsellerini yükleyebilir. Desteklenen formatlar arasında PNG, JPEG, WebP, PSD ve ORA bulunur [Resmî Kaynak](https://wplace.live/patch-notes). Wplace’te PSD ve ORA projeleri katmanlarını koruyacak şekilde içe aktarılabilir. (PNG/JPEG/WebP dosyaları da doğrudan yüklenebilir.) Yüklenen şablon üzerinde oyuncu döndürme, ölçekleme veya katman ekleme gibi düzenlemeler yapabilir.
  
- **Otomatik Boyama Yok:** Şablonlar kendi kendine piksel boyamazlar, sadece referans amaçlıdır. Yani şablon, hangi koordinattaki pikselin hangi renge boyanacağını göstererek oyuncuya kolaylık sağlar [Oyun İçi Gözlem]. Böylece katılımcılar referans görsel üzerinde rehber alarak daha hızlı ve hatasız çizebilirler.

Kaynaklar: Wplace resmî yama notları ve topluluk rehberleri. Oyun içi gözlemler, yukarıdaki mekaniklerin uygulamadaki durumunu desteklemektedir.
