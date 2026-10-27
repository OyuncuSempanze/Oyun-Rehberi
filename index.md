---
title: Kaynaklı Türkçe Oyun Arşivi
description: Kaynaklı Türkçe oyun rehberleri ve veri kümeleri.
---



<section class="archive" id="arsiv" aria-labelledby="archive-heading">
  <div class="section-heading">
    <h1 id="archive-heading">Oyunlar</h1>
  </div>

  <div class="archive-tools">
    <label class="archive-search">
      <span class="visually-hidden">Oyunlarda ara</span>
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="10.8" cy="10.8" r="6.8"></circle><path d="m16 16 4.2 4.2"></path></svg>
      <input id="archive-search" type="search" placeholder="Oyun ara..." autocomplete="off" aria-describedby="archive-count">
    </label>
    <p id="archive-count" class="archive-count" aria-live="polite">4 oyun</p>
  </div>

  <div class="archive-filters" role="group" aria-label="Oyun türüne göre filtrele">
    <button class="archive-filter is-active" type="button" data-filter="all" aria-pressed="true">Tümü</button>
    <button class="archive-filter" type="button" data-filter="combat" aria-pressed="false">Dövüş</button>
    <button class="archive-filter" type="button" data-filter="pixel-map" aria-pressed="false">Piksel haritası</button>
    <button class="archive-filter" type="button" data-filter="arcade" aria-pressed="false">Arcade</button>
    <button class="archive-filter" type="button" data-filter="incremental" aria-pressed="false">Boşta ilerleme</button>
  </div>

  <div class="game-grid" id="game-grid">
    <a class="game-card" href="{{ '/oyunlar/bloody-bastards/' | relative_url }}" data-category="combat" data-search="Bloody Bastards fizik tabanlı dövüş silah zırh özelleştirme mekanik" aria-label="Bloody Bastards rehberini aç">
      <span class="game-card-title">Bloody Bastards</span>
      <span class="game-card-description">Dövüş, silahlar ve zırhlar.</span>
    </a>

    <a class="game-card" href="{{ '/oyunlar/wplace.live/' | relative_url }}" data-category="pixel-map" data-search="Wplace.live wplace live ortak piksel haritası çizim kurallar harita mekanikleri güncelleme" aria-label="Wplace.live rehberini aç">
      <span class="game-card-title">Wplace.live</span>
      <span class="game-card-description">Piksel haritası ve kurallar.</span>
    </a>

    <a class="game-card" href="{{ '/oyunlar/DATA-WING/' | relative_url }}" data-category="arcade" data-search="DATA WING hikâye odaklı arcade yarış momentum hareket seviyeler bölüm mekanikleri" aria-label="DATA WING rehberini aç">
      <span class="game-card-title">DATA WING</span>
      <span class="game-card-description">Hareket ve bölüm mekanikleri.</span>
    </a>
    <a class="game-card" href="{{ '/oyunlar/antimatter-dimensions/' | relative_url }}" data-category="incremental" data-search="Antimatter Dimensions idle boşta ilerleme sayı üretimi geliştirmeler Infinity" aria-label="Antimatter Dimensions rehberini aç">
      <span class="game-card-title">Antimatter Dimensions</span>
      <span class="game-card-description">Sayı üretimi ve aşamalı ilerleme.</span>
    </a>
  </div>

  <p class="archive-empty" id="archive-empty" hidden>Sonuç yok.</p>
</section>

<section class="dataset-promo" aria-labelledby="dataset-promo-heading">
  <div class="dataset-promo-copy">
    <h2 id="dataset-promo-heading">Veri kümeleri</h2>
  </div>
  <div class="dataset-promo-actions">
    <a class="dataset-promo-download" href="{{ '/veri-kumeleri/oyun-rehberi-tam-arsiv-v1.jsonl' | relative_url }}" download>Tam arşivi indir</a>
    <a class="dataset-promo-link" href="{{ '/veri-kumeleri/' | relative_url }}">Tüm dosyalar</a>
  </div>
</section>

<script src="{{ '/assets/js/archive-search.js' | relative_url }}" defer></script>
