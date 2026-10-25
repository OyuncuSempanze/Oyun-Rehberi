---
title: Kaynaklı Türkçe Oyun Arşivi
description: Kaynakları izlenebilir Türkçe oyun rehberleri, oyun içi gözlemler ve indirilebilir yapılandırılmış veri kümeleri.
---

<section class="welcome" aria-labelledby="page-heading">
  <div class="welcome-copy">
    <p class="eyebrow"><span class="status-dot" aria-hidden="true"></span> KAYNAKLI TÜRKÇE OYUN ARŞİVİ</p>
    <h1 id="page-heading">Oyun bilgisi. <em>Kaynağıyla.</em></h1>
    <p class="welcome-description">Kaynakları izlenebilir Türkçe oyun rehberleri ve oyun içi gözlemler. Resmî açıklamalarla gözlemleri ayır, kaynak ilişkilerini koruyan indirilebilir veri kümelerini de incele.</p>
    <div class="welcome-actions">
      <a class="action-primary" href="#arsiv">Oyun arşivini keşfet <span aria-hidden="true">↓</span></a>
      <a class="action-secondary" href="{{ '/veri-kumeleri/' | relative_url }}">Veri kümelerini incele <span aria-hidden="true">↗</span></a>
    </div>
  </div>

</section>

<section class="archive" id="arsiv" aria-labelledby="archive-heading">
  <div class="section-heading">
    <div>
      <p class="section-kicker">OYUN KÜTÜPHANESİ</p>
      <h2 id="archive-heading">Oyun arşivi</h2>
    </div>
    <p class="section-description">İsim, tür veya mekanik üzerinden keşfet.</p>
  </div>

  <div class="archive-tools">
    <label class="archive-search">
      <span class="visually-hidden">Oyunlarda ara</span>
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="10.8" cy="10.8" r="6.8"></circle><path d="m16 16 4.2 4.2"></path></svg>
      <input id="archive-search" type="search" placeholder="Oyun adı, tür veya konu ara..." autocomplete="off" aria-describedby="archive-count archive-help">
    </label>
    <p id="archive-count" class="archive-count" aria-live="polite">3 oyun</p>
  </div>

  <div class="archive-filters" role="group" aria-label="Oyun türüne göre filtrele">
    <button class="archive-filter is-active" type="button" data-filter="all" aria-pressed="true">Tüm oyunlar</button>
    <button class="archive-filter" type="button" data-filter="combat" aria-pressed="false">Dövüş</button>
    <button class="archive-filter" type="button" data-filter="pixel-map" aria-pressed="false">Piksel haritası</button>
    <button class="archive-filter" type="button" data-filter="arcade" aria-pressed="false">Arcade</button>
  </div>
  <p class="archive-help" id="archive-help">Arama ve tür filtresi birlikte çalışır.</p>

  <div class="game-grid" id="game-grid">
    <a class="game-card" href="{{ '/oyunlar/bloody-bastards/' | relative_url }}" data-category="combat" data-search="Bloody Bastards fizik tabanlı dövüş silah zırh özelleştirme mekanik" aria-label="Bloody Bastards rehberini aç">
      <span class="game-card-top">
        <span class="game-emblem game-emblem--combat" aria-hidden="true">
          <svg class="entry-icon" viewBox="0 0 48 48" focusable="false">
            <path d="M13 10L35 37 M35 10L13 37" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round"/>
            <path d="M8 8L17 17 M31 30L40 40 M40 8L31 17 M17 30L8 40" fill="none" stroke="#f2ba72" stroke-width="2.3" stroke-linecap="square"/>
            <circle cx="24" cy="24" r="3" fill="#f2ba72"/>
          </svg>
        </span>
        <span class="game-category">FİZİK TABANLI DÖVÜŞ</span>
        <span class="game-index">01</span>
      </span>
      <span class="game-card-title">Bloody Bastards</span>
      <span class="game-card-description">Dövüş sistemi, silahlar, zırhlar ve karakter özelleştirme hakkında Türkçe rehberler.</span>
      <span class="game-tags"><span>Dövüş</span><span>Ekipman</span><span>SSS</span></span>
      <span class="game-card-footer"><strong>Rehberi aç</strong><span aria-hidden="true">↗</span></span>
    </a>

    <a class="game-card" href="{{ '/oyunlar/wplace.live/' | relative_url }}" data-category="pixel-map" data-search="Wplace.live wplace live ortak piksel haritası çizim kurallar harita mekanikleri güncelleme" aria-label="Wplace.live rehberini aç">
      <span class="game-card-top">
        <span class="game-emblem game-emblem--pixel" aria-hidden="true">
          <svg class="entry-icon" viewBox="0 0 48 48" focusable="false">
            <rect x="8" y="8" width="9" height="9" fill="currentColor"/>
            <rect x="20" y="8" width="9" height="9" fill="#f2ba72"/>
            <rect x="32" y="8" width="9" height="9" fill="currentColor" opacity=".45"/>
            <rect x="8" y="20" width="9" height="9" fill="#f2ba72" opacity=".65"/>
            <rect x="20" y="20" width="9" height="9" fill="currentColor"/>
            <rect x="32" y="20" width="9" height="9" fill="currentColor" opacity=".45"/>
            <rect x="8" y="32" width="9" height="9" fill="currentColor" opacity=".45"/>
            <rect x="20" y="32" width="9" height="9" fill="#f2ba72" opacity=".7"/>
            <rect x="32" y="32" width="9" height="9" fill="currentColor"/>
          </svg>
        </span>
        <span class="game-category">ORTAK PİKSEL HARİTASI</span>
        <span class="game-index">02</span>
      </span>
      <span class="game-card-title">Wplace.live</span>
      <span class="game-card-description">Harita mekanikleri, kurallar, güncellemeler ve oyuncu tavsiyeleri.</span>
      <span class="game-tags"><span>Harita</span><span>Kurallar</span><span>Güncellemeler</span></span>
      <span class="game-card-footer"><strong>Rehberi aç</strong><span aria-hidden="true">↗</span></span>
    </a>

    <a class="game-card" href="{{ '/oyunlar/DATA-WING/' | relative_url }}" data-category="arcade" data-search="DATA WING hikâye odaklı arcade yarış momentum hareket seviyeler bölüm mekanikleri" aria-label="DATA WING rehberini aç">
      <span class="game-card-top">
        <span class="game-emblem game-emblem--arcade" aria-hidden="true">
          <svg class="entry-icon" viewBox="0 0 48 48" focusable="false">
            <path d="M7 24L25 10V19H41V29H25V38Z" fill="currentColor"/>
            <path d="M6 15H15 M4 24H15 M6 33H15" fill="none" stroke="#f2ba72" stroke-width="2" stroke-linecap="round"/>
            <path d="M25 19V29" stroke="#0c1115" stroke-width="1.5"/>
          </svg>
        </span>
        <span class="game-category">HİKÂYE ODAKLI ARCADE</span>
        <span class="game-index">03</span>
      </span>
      <span class="game-card-title">DATA WING</span>
      <span class="game-card-description">Hareket, momentum ve bölüm mekaniklerine odaklanan rehberler.</span>
      <span class="game-tags"><span>Momentum</span><span>Bölümler</span><span>SSS</span></span>
      <span class="game-card-footer"><strong>Rehberi aç</strong><span aria-hidden="true">↗</span></span>
    </a>
  </div>

  <p class="archive-empty" id="archive-empty" hidden>Bu aramayla eşleşen oyun bulunamadı. Farklı bir ad veya konu dene.</p>
</section>

<section class="dataset-promo" aria-labelledby="dataset-promo-heading">
  <div class="dataset-promo-copy">
    <p class="section-kicker">AÇIK VERİ · SÜRÜM 1.3.0</p>
    <h2 id="dataset-promo-heading">Aynı arşiv, makine tarafından da işlenebilir</h2>
    <p>SSS, rehber bölümleri ve daha küçük iddia birimleri indirilebilir JSONL dosyalarında sunulur. Kaynak bağlantıları ve bilgi türü etiketleri kayıtlarda korunur.</p>
    <div class="dataset-promo-meta"><span>JSONL</span><span>Kaynak bilgisi</span><span>İddia birimleri</span></div>
  </div>
  <div class="dataset-promo-actions">
    <a class="dataset-promo-download" href="{{ '/veri-kumeleri/oyun-rehberi-tam-arsiv-v1.jsonl' | relative_url }}" download>Tam veri kümesini indir <span aria-hidden="true">↓</span></a>
    <a class="dataset-promo-link" href="{{ '/veri-kumeleri/' | relative_url }}">Tüm veri dosyaları <span aria-hidden="true">↗</span></a>
  </div>
</section>

<script src="{{ '/assets/js/archive-search.js' | relative_url }}" defer></script>
