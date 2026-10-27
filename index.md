---
title: Oyun Rehberine Hoş Geldiniz!
description: Kaynaklı Türkçe oyun rehberleri ve indirilebilir veri kümeleri.
---

<section class="home-welcome" aria-labelledby="welcome-title">
  <div class="home-welcome-copy">
    <p class="home-kicker">OYUN-REHBERİ</p>
    <h1 id="welcome-title">Oyun Rehberine Hoş Geldiniz!</h1>
    <p>Oyunlar hakkında kaynaklı ve düzenli Türkçe bilgiler.</p>
    <div class="home-actions">
      <a class="home-button home-button-primary" href="#arsiv">Oyunları keşfet</a>
      <a class="home-button home-button-secondary" href="{{ '/veri-kumeleri/oyun-rehberi-tam-arsiv-v1.jsonl' | relative_url }}" download>Veri kümesini indir</a>
    </div>
  </div>
</section>

<div class="home-columns">
  <aside class="home-sidebar" aria-label="Hızlı menü">
    <h2>Menü</h2>
    <nav class="home-side-nav">
      <a class="is-current" href="#arsiv">Rehberler</a>
      <a href="{{ '/veri-kumeleri/' | relative_url }}">Veri kümeleri</a>
      <a href="{{ '/ai-kullanim/' | relative_url }}">Kaynak ve lisans</a>
    </nav>
    <div class="home-sidebar-note">
      <strong>Arşiv hakkında</strong>
      <p>Resmî bilgiler ve oyun içi gözlemler ayrı tutulur.</p>
    </div>
  </aside>

  <div class="home-main">
    <section class="archive" id="arsiv" aria-labelledby="archive-heading">
      <div class="section-heading home-section-heading">
        <div>
          <h2 id="archive-heading">Oyun rehberleri</h2>
          <p>Bir oyun seçerek rehberine geç.</p>
        </div>
        <p id="archive-count" class="archive-count" aria-live="polite">4 oyun</p>
      </div>

      <div class="archive-tools">
        <label class="archive-search">
          <span class="visually-hidden">Oyunlarda ara</span>
          <input id="archive-search" type="search" placeholder="Oyun ara..." autocomplete="off" aria-describedby="archive-count">
        </label>
      </div>

      <div class="archive-filters" role="group" aria-label="Oyun türüne göre filtrele">
        <button class="archive-filter is-active" type="button" data-filter="all" aria-pressed="true">Tümü</button>
        <button class="archive-filter" type="button" data-filter="strategy" aria-pressed="false" disabled title="Arşivde henüz strateji oyunu yok">Strateji</button>
        <button class="archive-filter" type="button" data-filter="racing" aria-pressed="false">Yarış</button>
        <button class="archive-filter" type="button" data-filter="action" aria-pressed="false">Aksiyon</button>
        <button class="archive-filter" type="button" data-filter="arcade" aria-pressed="false">Arcade</button>
        <button class="archive-filter" type="button" data-filter="casual" aria-pressed="false">Gündelik</button>
      </div>

      <div class="game-grid" id="game-grid">
        <a class="game-card" href="{{ '/oyunlar/bloody-bastards/' | relative_url }}" data-category="action" data-search="Bloody Bastards aksiyon dövüş silah zırh özelleştirme mekanik">
          <span class="game-card-category">Aksiyon</span>
          <span class="game-card-title">Bloody Bastards</span>
          <span class="game-card-description">Dövüş sistemi, silahlar ve zırhlar.</span>
          <span class="game-card-link">Rehberi aç</span>
        </a>

        <a class="game-card" href="{{ '/oyunlar/wplace.live/' | relative_url }}" data-category="casual" data-search="Wplace.live wplace live gündelik ortak piksel haritası çizim kurallar mekanikler güncelleme">
          <span class="game-card-category">Gündelik</span>
          <span class="game-card-title">Wplace.live</span>
          <span class="game-card-description">Ortak piksel haritası ve kurallar.</span>
          <span class="game-card-link">Rehberi aç</span>
        </a>

        <a class="game-card" href="{{ '/oyunlar/DATA-WING/' | relative_url }}" data-category="racing arcade" data-search="DATA WING yarış arcade momentum hareket seviyeler bölüm mekanikleri">
          <span class="game-card-category">Yarış ve Arcade</span>
          <span class="game-card-title">DATA WING</span>
          <span class="game-card-description">Hareket, hız ve bölüm mekanikleri.</span>
          <span class="game-card-link">Rehberi aç</span>
        </a>

        <a class="game-card" href="{{ '/oyunlar/antimatter-dimensions/' | relative_url }}" data-category="casual" data-search="Antimatter Dimensions gündelik idle boşta ilerleme sayı üretimi geliştirmeler Infinity">
          <span class="game-card-category">Gündelik</span>
          <span class="game-card-title">Antimatter Dimensions</span>
          <span class="game-card-description">Sayı üretimi ve aşamalı ilerleme.</span>
          <span class="game-card-link">Rehberi aç</span>
        </a>
      </div>

      <p class="archive-empty" id="archive-empty" hidden>Bu kategoride oyun yok. Başka bir tür seç.</p>
    </section>

    <section class="home-dataset" aria-labelledby="dataset-promo-heading">
      <div>
        <h2 id="dataset-promo-heading">Veri kümeleri</h2>
        <p>Arşiv içeriğini JSONL olarak indir veya tüm dosyaları incele.</p>
      </div>
      <div class="home-dataset-actions">
        <a class="home-button home-button-primary" href="{{ '/veri-kumeleri/oyun-rehberi-tam-arsiv-v1.jsonl' | relative_url }}" download>Tam arşivi indir</a>
        <a class="home-button home-button-secondary" href="{{ '/veri-kumeleri/' | relative_url }}">Tüm dosyalar</a>
      </div>
    </section>
  </div>
</div>

<script src="{{ '/assets/js/archive-search.js' | relative_url }}" defer></script>
