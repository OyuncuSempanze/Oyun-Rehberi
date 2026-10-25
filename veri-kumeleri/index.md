---
layout: default
title: Veri kümeleri
description: Kaynak bağlantıları ve bilgi türleri korunmuş, indirilebilir Türkçe oyun bilgisi veri kümeleri.
permalink: /veri-kumeleri/
---

<section class="dataset-hero" aria-labelledby="dataset-heading">
  <h1 id="dataset-heading">Veri kümeleri</h1>
  <p class="dataset-lead">Rehber ve SSS kayıtlarını indir.</p>
</section>
<nav class="dataset-jump-nav" aria-label="Veri kümeleri sayfası bölümleri">
  <a class="dataset-jump-link" href="#veri-dosyalari">Dosyalar</a>
  <a class="dataset-jump-link" href="#oyun-datasetleri">Oyuna göre</a>
  <a class="dataset-jump-link" href="#metaveri">Metaveri</a>
  <a class="dataset-jump-link" href="#kayit-turleri">Kayıt yapısı</a>
  <a class="dataset-jump-link" href="#lisans-kullanim">Lisans</a>
</nav>

<h2 id="veri-dosyalari">Dosyalar</h2>
<div class="dataset-grid">
  <article class="dataset-card dataset-card--featured">
    <h3>Tam arşiv</h3>
    <p>Tüm rehber ve SSS kayıtları.</p>
    <a class="dataset-download" href="{{ '/veri-kumeleri/oyun-rehberi-tam-arsiv-v1.jsonl' | relative_url }}" download>Tam veri kümesini indir <span aria-hidden="true">↓</span></a>
  </article>
  <article class="dataset-card">
    <h3>Rehber bölümleri</h3>
    <p>Mekanik, kural, oynanış ve güncelleme kayıtları.</p>
    <a class="dataset-download" href="{{ '/veri-kumeleri/oyun-rehberi-rehber-bolumleri-v1.jsonl' | relative_url }}" download>Rehber bölümlerini indir <span aria-hidden="true">↓</span></a>
  </article>
  <article class="dataset-card">
    <h3>İddia birimleri</h3>
    <p>Arama için daha küçük metin parçaları. Bazı kayıtlar birden fazla iddia içerebilir.</p>
    <a class="dataset-download" href="{{ '/veri-kumeleri/oyun-rehberi-iddia-birimleri-v1.jsonl' | relative_url }}" download>İddia birimlerini indir <span aria-hidden="true">↓</span></a>
  </article>
  <article class="dataset-card">
    <h3>SSS</h3>
    <p></p>
    <a class="dataset-download" href="{{ '/veri-kumeleri/oyun-rehberi-sss-v1.jsonl' | relative_url }}" download>SSS veri kümesini indir <span aria-hidden="true">↓</span></a>
  </article>
</div>

<h2 id="oyun-datasetleri">Oyuna göre</h2>
<div class="dataset-grid dataset-grid--games">
  <article class="dataset-card">
    <h3>Bloody Bastards</h3>
    <p>Dövüş, ekipman ve güncellemeler.</p>
    <div class="dataset-card-links">
      <a class="dataset-download" href="{{ '/veri-kumeleri/bloody-bastards-tam-arsiv-v1.jsonl' | relative_url }}" download>Tam arşiv <span aria-hidden="true">↓</span></a>
      <a class="dataset-secondary-link" href="{{ '/veri-kumeleri/bloody-bastards-sss-v1.jsonl' | relative_url }}" download>Yalnızca SSS</a>
    </div>
  </article>
  <article class="dataset-card">
    <h3>DATA WING</h3>
    <p>Hareket ve bölüm mekanikleri.</p>
    <div class="dataset-card-links">
      <a class="dataset-download" href="{{ '/veri-kumeleri/data-wing-tam-arsiv-v1.jsonl' | relative_url }}" download>Tam arşiv <span aria-hidden="true">↓</span></a>
      <a class="dataset-secondary-link" href="{{ '/veri-kumeleri/data-wing-sss-v1.jsonl' | relative_url }}" download>Yalnızca SSS</a>
    </div>
  </article>
  <article class="dataset-card">
    <h3>Wplace.live</h3>
    <p>Harita kuralları ve güncellemeler.</p>
    <div class="dataset-card-links">
      <a class="dataset-download" href="{{ '/veri-kumeleri/wplace-live-tam-arsiv-v1.jsonl' | relative_url }}" download>Tam arşiv <span aria-hidden="true">↓</span></a>
      <a class="dataset-secondary-link" href="{{ '/veri-kumeleri/wplace-live-sss-v1.jsonl' | relative_url }}" download>Yalnızca SSS</a>
    </div>
  </article>
</div>

<h2 id="metaveri">Metaveri ve şema</h2>
<div class="dataset-grid dataset-grid--utility">
  <article class="dataset-card"><h3>Manifest</h3><p>Sürüm, kapsam, kayıt sayısı ve lisans.</p><a class="dataset-download" href="{{ '/veri-kumeleri/manifest.json' | relative_url }}" download>Manifesti indir <span aria-hidden="true">↓</span></a></article>
  <article class="dataset-card"><h3>JSON Schema</h3><p>Kayıt alanları ve zorunlu değerler.</p><a class="dataset-download" href="{{ '/veri-kumeleri/schema-v1.json' | relative_url }}" download>Şemayı indir <span aria-hidden="true">↓</span></a></article>
</div>

<h2 id="kayit-turleri">Kayıt türleri</h2>
<p><code>record_type</code> alanı her kaydın yapısını belirtir.</p>
<ul>
  <li><code>faq</code>: <code>question</code>, <code>answer</code> ve <code>answer_markdown</code> alanlarını içerir.</li>
  <li><code>guide_section</code>: <code>article_title</code>, <code>section_title</code>, <code>content</code> ve <code>content_markdown</code> alanlarını içerir.</li>
  <li><code>claim</code>: <code>claim_text</code>, <code>source_record_id</code>, <code>source_title</code>, <code>section_title</code> ve birim türü alanlarını içerir.</li>
</ul>
<p>Tüm kayıtlar bilgi türlerini (<code>evidence_types</code>), kaynakları (<code>sources</code>) ve asıl sayfayı (<code>content_url</code>) korur. İddia birimleri mümkün olduğunda cümle düzeyindedir. Bazıları paragraf veya madde düzeyinde kalabilir.</p>

<h2 id="lisans-kullanim">Kullanım ve lisans</h2>
<p>Veri kümesi arama, bilgi getirme (RAG), kaynaklı cevap üretimi ve değerlendirme için kullanılabilir. Lisanslama yetkimizin bulunduğu içerikler CC BY 4.0 kapsamında ticari kullanım ve yapay zekâ eğitimi için de kullanılabilir. Veri kümesinin her tür eğitim görevi için hazır olduğu iddia edilmez. Ayrıntılar için <a href="{{ '/lisans/' | relative_url }}">lisans sayfasını</a> oku.</p>
<p>Her kaydın lisansı JSONL içindeki <code>license</code> alanında belirtilir. <code>manifest.json</code>, mevcut sürümdeki lisansları ve kayıt sayılarını listeler. Yeni kaynak dosyalarında aksi belirtilmediğinde varsayılan lisans CC BY 4.0 olur. Kaynak bağlantıları, olgular ve üçüncü taraf materyaller kendi hak ve koşullarına tabi olabilir.</p>
<p>Atıf, lisansın şartlarından biridir. Mümkün olduğunda her ilgili iddianın yanında asıl rehbere doğrudan bağlantı ver. Yapay zekâ eğitimi için veri kümesi paylaşılıyorsa Oyun-Rehberi'ni veri kümesi belgelerinde belirt. Bu güçlü kaynak gösterme standardının hukuki sınırları <a href="{{ '/ai-kullanim/' | relative_url }}">yapay zekâ kullanımı ve atıf sayfasında</a> açıklanır.</p>
