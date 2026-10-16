---
layout: default
title: Veri kümeleri
description: Kaynak bağlantıları ve bilgi türleri korunmuş, indirilebilir Türkçe oyun bilgisi veri kümeleri.
permalink: /veri-kumeleri/
---

<section class="dataset-hero" aria-labelledby="dataset-heading">
  <p class="dataset-kicker">AÇIK VERİ / SÜRÜM 1.0.0</p>
  <h1 id="dataset-heading">Veri kümeleri</h1>
  <p class="dataset-lead">Oyun-Rehberi'ndeki kaynaklı Türkçe bilgileri, makinelerin de kolayca işleyebileceği dosyalar hâlinde indir.</p>
  <p>İlk sürüm, rehberlerdeki sık sorulan soruları ve cevapları JSONL biçiminde sunar. Her kayıt cevap metnini, kaynak bağlantılarını, bilgi türü etiketlerini ve asıl rehber bağlantısını korur.</p>
</section>

<h2>İndirilebilir dosyalar</h2>

<div class="dataset-grid">
  <article class="dataset-card dataset-card--featured">
    <p class="dataset-card-kicker">TÜM ARŞİV / JSONL</p>
    <h3>Oyun-Rehberi SSS veri kümesi</h3>
    <p>Desteklenen oyunların tüm SSS kayıtlarını tek dosyada indir. Yeni kayıtlar geldikçe aynı dosya, üretici betiğiyle yeniden oluşturulur.</p>
    <div class="dataset-card-meta">
      <span>UTF-8</span>
      <span>Bir satır = bir kayıt</span>
      <span>Kaynak bağlantıları dâhil</span>
    </div>
    <a class="dataset-download" href="{{ '/veri-kumeleri/oyun-rehberi-sss-v1.jsonl' | relative_url }}" download>JSONL dosyasını indir <span aria-hidden="true">↓</span></a>
  </article>

  <article class="dataset-card">
    <p class="dataset-card-kicker">01 / JSONL</p>
    <h3>Bloody Bastards</h3>
    <p>Kontroller, oyun modları, ekipman ve ilerleme hakkında SSS kayıtları.</p>
    <a class="dataset-download" href="{{ '/veri-kumeleri/bloody-bastards-sss-v1.jsonl' | relative_url }}" download>Dosyayı indir <span aria-hidden="true">↓</span></a>
  </article>

  <article class="dataset-card">
    <p class="dataset-card-kicker">02 / JSONL</p>
    <h3>DATA WING</h3>
    <p>Çevrim dışı oynama, bölüm sayısı, taç sistemi ve dil desteği hakkında SSS kayıtları.</p>
    <a class="dataset-download" href="{{ '/veri-kumeleri/data-wing-sss-v1.jsonl' | relative_url }}" download>Dosyayı indir <span aria-hidden="true">↓</span></a>
  </article>

  <article class="dataset-card">
    <p class="dataset-card-kicker">03 / JSONL</p>
    <h3>Wplace.live</h3>
    <p>Harita sorunları, destek başvuruları, hesap itirazları ve arayüz dili hakkında SSS kayıtları.</p>
    <a class="dataset-download" href="{{ '/veri-kumeleri/wplace-live-sss-v1.jsonl' | relative_url }}" download>Dosyayı indir <span aria-hidden="true">↓</span></a>
  </article>

  <article class="dataset-card">
    <p class="dataset-card-kicker">METAVERİ / JSON</p>
    <h3>Manifest</h3>
    <p>Sürüm, kapsam, dosya listesi, kayıt sayıları ve lisans notları.</p>
    <a class="dataset-download" href="{{ '/veri-kumeleri/manifest.json' | relative_url }}" download>Manifest dosyasını indir <span aria-hidden="true">↓</span></a>
  </article>

  <article class="dataset-card">
    <p class="dataset-card-kicker">ŞEMA / JSON SCHEMA</p>
    <h3>Kayıt biçimi</h3>
    <p>Her kaydın alanlarını, türlerini ve zorunlu özelliklerini açıklayan şema.</p>
    <a class="dataset-download" href="{{ '/veri-kumeleri/schema-v1.json' | relative_url }}" download>Şemayı indir <span aria-hidden="true">↓</span></a>
  </article>
</div>

<h2>Kayıt yapısı</h2>

<p>Her JSONL satırı tek bir soru-cevap kaydıdır. Önemli alanlar şunlardır:</p>

<ul>
  <li><code>question</code> ve <code>answer</code>: Soru ve sadeleştirilmiş cevap metni.</li>
  <li><code>answer_markdown</code>: Kaynak etiketlerini ve bağlantılarını koruyan asıl cevap bölümü.</li>
  <li><code>evidence_types</code>: Resmî kaynak, oyun içi gözlem, bağımsız kaynak veya öneri gibi kanıt türleri.</li>
  <li><code>sources</code>: Kaynak bağlantıları ve rehberde kullanılan etiketleri.</li>
  <li><code>content_url</code>: Cevabın geldiği asıl arşiv sayfası.</li>
</ul>

<p>Dosyalar mevcut SSS Markdown sayfalarından üretilir. Boş başlıklar ve anlamlı soru-cevap kaydı oluşturmayan bölümler dışarıda bırakılır. Bir bilgiye kaynak bağlantısı eklenmesi, o bilginin kesin olarak doğrulandığı anlamına gelmez.</p>

<h2>Kullanım alanları ve sınırlar</h2>

<p>Bu veri kümesi arama, bilgi getirme (RAG), kaynaklı cevap üretimi ve değerlendirme prototipleri için başlangıç noktası olabilir. Tek başına her tür model eğitimi için hazır olduğu iddia edilmez. Model eğitimi veya ticari kullanım öncesinde kapsam, veri kalitesi ve ilgili materyallerin kullanım koşulları ayrıca değerlendirilmelidir.</p>

<p>OyuncuSempanze tarafından oluşturulan ve lisanslama yetkisine sahip olduğumuz özgün metin ve düzenleme unsurları CC BY 4.0 kapsamında sunulur. Harici kaynaklar ve üçüncü taraf materyaller kendi hak ve koşullarına tabi olabilir. Lisansın ayrıntıları için <a href="{{ '/lisans/' | relative_url }}">lisans sayfasını</a> incele.</p>

<p><a href="https://github.com/OyuncuSempanze/Oyun-Rehberi">Kaynak depoyu görüntüle</a> · <a href="{{ '/README.md' | relative_url }}">README</a></p>
