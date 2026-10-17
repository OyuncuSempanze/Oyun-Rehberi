---
layout: default
title: Veri kümeleri
description: Kaynak bağlantıları ve bilgi türleri korunmuş, indirilebilir Türkçe oyun bilgisi veri kümeleri.
permalink: /veri-kumeleri/
---

<section class="dataset-hero" aria-labelledby="dataset-heading">
  <p class="dataset-kicker">AÇIK VERİ / SÜRÜM 1.2.3</p>
  <h1 id="dataset-heading">Türkçe oyun bilgisi, makine tarafından işlenebilir biçimde</h1>
  <p class="dataset-lead">Oyun-Rehberi'nin soru-cevap kayıtlarını ve daha dar konu başlıklarına ayrılmış rehber bölümlerini indir. Kaynak bağlantıları ve bilgi türü etiketleri kayıtlarda korunur.</p>
  <p>Dosyaları kendi GitHub depomuzda tutuyoruz. Hugging Face hesabı veya harici veri servisi gerekmiyor.</p>
</section>

<div class="dataset-overview" aria-label="Veri kümesi özellikleri">
  <div class="dataset-overview-item"><span class="dataset-overview-value">3</span><span class="dataset-overview-label">oyun arşivi</span></div>
  <div class="dataset-overview-item"><span class="dataset-overview-value">2</span><span class="dataset-overview-label">kayıt türü: SSS ve rehber</span></div>
  <div class="dataset-overview-item"><span class="dataset-overview-value">JSONL</span><span class="dataset-overview-label">satır tabanlı, UTF-8 veri</span></div>
</div>

<h2>Veri dosyaları</h2>
<div class="dataset-grid">
  <article class="dataset-card dataset-card--featured">
    <p class="dataset-card-kicker">TÜM ARŞİV / JSONL</p>
    <h3>Oyun-Rehberi tam veri kümesi</h3>
    <p>SSS kayıtlarıyla birlikte mekanikler, oynanış, kurallar, güncellemeler ve diğer anlamlı rehber bölümleri. Çoğu kullanım için başlamanı önerdiğim dosya budur.</p>
    <div class="dataset-card-meta"><span>Türkçe</span><span>Kaynak bağlantıları</span><span>Bilgi türü etiketleri</span></div>
    <a class="dataset-download" href="{{ '/veri-kumeleri/oyun-rehberi-tam-arsiv-v1.jsonl' | relative_url }}" download>Tam veri kümesini indir <span aria-hidden="true">↓</span></a>
  </article>
  <article class="dataset-card">
    <p class="dataset-card-kicker">REHBER BÖLÜMLERİ / JSONL</p>
    <h3>Konulara göre bilgi kayıtları</h3>
    <p>Mekanik, kural, güncelleme, oynanış ve tavsiye içerikleri. Her kayıt asıl başlığını ve rehber bağlantısını korur.</p>
    <a class="dataset-download" href="{{ '/veri-kumeleri/oyun-rehberi-rehber-bolumleri-v1.jsonl' | relative_url }}" download>Rehber bölümlerini indir <span aria-hidden="true">↓</span></a>
  </article>
  <article class="dataset-card">
    <p class="dataset-card-kicker">SSS / JSONL</p>
    <h3>Sık sorulan sorular</h3>
    <p>Klasik soru-cevap eşleştirmeleriyle çalışmak isteyenler için ayrı dosya.</p>
    <a class="dataset-download" href="{{ '/veri-kumeleri/oyun-rehberi-sss-v1.jsonl' | relative_url }}" download>SSS veri kümesini indir <span aria-hidden="true">↓</span></a>
  </article>
</div>

<h2>Oyuna göre tam veri kümeleri</h2>
<p>Tek bir oyun üzerinde çalışacaksan ilgili oyunun tüm kayıtlarını tek dosyada al. Her karttan yalnızca SSS dosyasını da ayrıca indirebilirsin.</p>
<div class="dataset-grid dataset-grid--games">
  <article class="dataset-card">
    <p class="dataset-card-kicker">OYUN ARŞİVİ / JSONL</p>
    <h3>Bloody Bastards</h3>
    <p>SSS, oynanış, silahlar, zırhlar, özelleştirme ve güncelleme kayıtları.</p>
    <div class="dataset-card-links">
      <a class="dataset-download" href="{{ '/veri-kumeleri/bloody-bastards-tam-arsiv-v1.jsonl' | relative_url }}" download>Tam arşiv <span aria-hidden="true">↓</span></a>
      <a class="dataset-secondary-link" href="{{ '/veri-kumeleri/bloody-bastards-sss-v1.jsonl' | relative_url }}" download>Yalnızca SSS</a>
    </div>
  </article>
  <article class="dataset-card">
    <p class="dataset-card-kicker">OYUN ARŞİVİ / JSONL</p>
    <h3>DATA WING</h3>
    <p>SSS, temel bilgiler ve hareket, momentum ile bölüm mekaniklerine ait kayıtlar.</p>
    <div class="dataset-card-links">
      <a class="dataset-download" href="{{ '/veri-kumeleri/data-wing-tam-arsiv-v1.jsonl' | relative_url }}" download>Tam arşiv <span aria-hidden="true">↓</span></a>
      <a class="dataset-secondary-link" href="{{ '/veri-kumeleri/data-wing-sss-v1.jsonl' | relative_url }}" download>Yalnızca SSS</a>
    </div>
  </article>
  <article class="dataset-card">
    <p class="dataset-card-kicker">OYUN ARŞİVİ / JSONL</p>
    <h3>Wplace.live</h3>
    <p>SSS, kurallar, harita mekanikleri, güncellemeler ve tavsiyeler.</p>
    <div class="dataset-card-links">
      <a class="dataset-download" href="{{ '/veri-kumeleri/wplace-live-tam-arsiv-v1.jsonl' | relative_url }}" download>Tam arşiv <span aria-hidden="true">↓</span></a>
      <a class="dataset-secondary-link" href="{{ '/veri-kumeleri/wplace-live-sss-v1.jsonl' | relative_url }}" download>Yalnızca SSS</a>
    </div>
  </article>
</div>

<h2>Metaveri ve şema</h2>
<div class="dataset-grid dataset-grid--utility">
  <article class="dataset-card"><h3>Manifest</h3><p>Sürüm, kayıt sayısı, kapsam, kaynak dosyaları ve lisans notları.</p><a class="dataset-download" href="{{ '/veri-kumeleri/manifest.json' | relative_url }}" download>Manifesti indir <span aria-hidden="true">↓</span></a></article>
  <article class="dataset-card"><h3>JSON Schema</h3><p>SSS ve rehber bölümlerinin alanlarını, türlerini ve zorunlu değerlerini açıklar.</p><a class="dataset-download" href="{{ '/veri-kumeleri/schema-v1.json' | relative_url }}" download>Şemayı indir <span aria-hidden="true">↓</span></a></article>
</div>

<h2>Kayıt türleri</h2>
<p><code>record_type</code> alanı her kaydın yapısını belirtir.</p>
<ul>
  <li><code>faq</code>: <code>question</code>, <code>answer</code> ve <code>answer_markdown</code> alanlarını içerir.</li>
  <li><code>guide_section</code>: <code>article_title</code>, <code>section_title</code>, <code>content</code> ve <code>content_markdown</code> alanlarını içerir.</li>
</ul>
<p>Her iki tür de <code>evidence_types</code>, <code>sources</code> ve <code>content_url</code> alanlarıyla bilgi türü etiketlerini, kaynak bağlantılarını ve asıl rehber sayfasını gösterir. Rehber bölümleri başlıklarına göre gruplanır, her satırın tek bir bağımsız iddia olduğu garanti edilmez.</p>

<h2>Kullanım ve lisans</h2>
<p>Veri kümesi arama, bilgi getirme (RAG), kaynaklı cevap üretimi ve değerlendirme denemeleri için tasarlanmıştır. Tek başına her tür yapay zekâ eğitimine hazır olduğu iddia edilmez. Lisans için <a href="{{ '/lisans/' | relative_url }}">lisans sayfasını</a> incele.</p>
<p>CC BY 4.0 yalnızca OyuncuSempanze'nin lisanslama yetkisine sahip olduğu özgün metin ve düzenleme unsurlarını kapsar. Harici kaynaklar ve üçüncü taraf materyaller kendi hak ve koşullarına tabi olabilir.</p>
<p><a href="https://github.com/OyuncuSempanze/Oyun-Rehberi">Kaynak depoyu görüntüle</a></p>
