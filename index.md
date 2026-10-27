---
title: Oyun Rehberi
description: Kaynaklı Türkçe oyun rehberleri ve veri kümeleri.
---

<section class="home-welcome" aria-labelledby="welcome-title">
  <h1 id="welcome-title">Oyun Rehberi</h1>
  <p>Oyunlar hakkında kaynaklı Türkçe bilgiler.</p>
</section>

<section class="archive" id="arsiv" aria-labelledby="archive-heading">
  <div class="section-heading home-section-heading">
    <h2 id="archive-heading">Oyunlar</h2>
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
    <button class="archive-filter" type="button" data-filter="racing" aria-pressed="false">Yarış</button>
    <button class="archive-filter" type="button" data-filter="action" aria-pressed="false">Aksiyon</button>
    <button class="archive-filter" type="button" data-filter="arcade" aria-pressed="false">Arcade</button>
    <button class="archive-filter" type="button" data-filter="casual" aria-pressed="false">Gündelik</button>
  </div>

  <div class="game-grid" id="game-grid">
    <a class="game-card" href="{{ '/oyunlar/bloody-bastards/' | relative_url }}" data-category="action" data-search="Bloody Bastards aksiyon dövüş silah zırh özelleştirme mekanik">
      <span class="game-card-title">Bloody Bastards</span>
      <span class="game-card-description">Dövüş sistemi, silahlar ve zırhlar.</span>
    </a>

    <a class="game-card" href="{{ '/oyunlar/wplace.live/' | relative_url }}" data-category="casual" data-search="Wplace.live wplace live gündelik ortak piksel haritası çizim kuralları mekanikler güncelleme">
      <span class="game-card-title">Wplace.live</span>
      <span class="game-card-description">Ortak piksel haritası ve kurallar.</span>
    </a>

    <a class="game-card" href="{{ '/oyunlar/DATA-WING/' | relative_url }}" data-category="racing arcade" data-search="DATA WING yarış arcade momentum hareket seviyeler bölüm mekanikleri">
      <span class="game-card-title">DATA WING</span>
      <span class="game-card-description">Hareket, hız ve bölüm mekanikleri.</span>
    </a>

    <a class="game-card" href="{{ '/oyunlar/antimatter-dimensions/' | relative_url }}" data-category="casual" data-search="Antimatter Dimensions gündelik idle boşta ilerleme sayı üretimi geliştirmeler Infinity">
      <span class="game-card-title">Antimatter Dimensions</span>
      <span class="game-card-description">Sayı üretimi ve aşamalı ilerleme.</span>
    </a>
  </div>

  <p class="archive-empty" id="archive-empty" hidden>Bu kategoride oyun yok. Başka bir tür seç.</p>
</section>

<script src="{{ '/assets/js/archive-search.js' | relative_url }}" defer></script>
