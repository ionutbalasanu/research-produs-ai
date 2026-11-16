# Faza 4, pasul 2: Shopify App Store, măsurare

Data: 2026-11-16. Fereastra: aplicații cu data „Launched" ≥ 2024-11-16.

## Ce există, verificat înainte de folosire (verificat în sursă)

- `https://apps.shopify.com/robots.txt` (salvat în `faza4/date/shopify/robots.txt`): permite paginile de categorie, de aplicație și de dezvoltator. Interzice `*q=*`, deci nu am folosit căutarea magazinului.
- `https://apps.shopify.com/sitemap.xml`: indexuri pe limbi pentru aplicații, dezvoltatori și categorii. `sitemap_apps_en.xml` are **30.532 de aplicații**, dar fără dată de lansare, deci nu ajunge singur pentru măsurare.
- `sitemap_categories_en.xml` are 161 de adrese. **122 sunt categorii-frunză** care au listă completă la `/categories/<slug>/all?sort_by=newest`, cu 24 de aplicații pe pagină. Celelalte 39 sunt doar părinți (`/all` → 404). Lista și răspunsurile sunt în `faza4/date/shopify/cat_index.txt`.
- Cardul din listă arată numele, eticheta de preț și, dacă există, ratingul și numărul de recenzii. Pagina aplicației arată „Launched <dată>", dezvoltatorul (cu link la `/partners/<id>`) și planurile de preț.
- Sortarea „newest" urmează data „Launched". Am verificat pe 6 aplicații dintr-o categorie și la granița a două categorii: ultima aplicație păstrată e din 2024-11-18, respectiv 2024-11-26, iar prima aruncată e din 2024-11-15 în ambele.

## Acoperire

**Toate cele 122 de categorii-frunză au fost parcurse până la 2024-11-16. Nu a rămas nicio categorie neacoperită.** Paginile brute sunt în `faza4/date/shopify/cat/` (1.163 de pagini), cele ale aplicațiilor în `app/` (2.052), cele ale dezvoltatorilor în `partner/` (361).

Ce nu e acoperit:
1. **Aplicațiile retrase din magazin** nu mai apar. Numitorul conține doar supraviețuitorii. **dedus**
2. **O aplicație poate fi în 2 categorii.** De aceea suma pe categorii (25.436) e mai mare decât numărul de aplicații unice (**20.755**). Din 39.802 listări pe categorii, 64% sunt din ultimele 24 de luni. **verificat în sursă**
3. **Recenziile de pe card** sunt citite din textul „X out of 5 stars (N)". Aplicațiile fără recenzii nu au textul ăsta și apar cu 0.

## Praguri aplicate

1. Lansată ≥ 2024-11-16 (data de pe pagina aplicației).
2. Cel puțin 20 de recenzii.
3. **Plan plătit:** cel puțin un plan cu preț > 0 în secțiunea de prețuri a paginii (`$X/month`, `$X/year` sau `$X one-time`) sau „$" în eticheta de preț.
4. **Dezvoltator cu cel mult 3 aplicații:** numărul de carduri distincte de pe pagina `/partners/<id>`.

| Pas | Aplicații |
|---|---|
| Lansate în fereastră (unice) | 20.755 |
| … cu ≥ 20 recenzii | 451 (2,2%) |
| … și plan plătit | 302 |
| … și dezvoltator cu ≤ 3 aplicații (trec toate) | **182** (0,88% din 20.755) |

Lista celor 451, cu toate câmpurile, e în `faza4/date/shopify/candidati_20recenzii.tsv`.

**Atenție la pragul 4 (dedus):** „cel mult 3 aplicații" lasă să treacă și firme mari care au puține aplicații pe Shopify: Judge.me (judgeme-email), Trustpilot, Chatbase, Shogun, Reddit, PayPal, GoKwik, Clickpost. Le-am scos de mână când am format buzunarele, la pasul 3.

## Numitorul pe fiecare categorie

Numărătorile sunt pe categorie. O aplicație din două categorii se numără în amândouă.

| Categorie | Listate azi | Lansate după 2024-11-16 (numitor) | ≥20 recenzii | Trec toate pragurile | Rată |
|---|---|---|---|---|---|
| finding-products-sourcing-options-dropshipping | 606 | 277 | 12 | 4 | 1.4% |
| finding-products-sourcing-options-print-on-demand-pod | 378 | 154 | 6 | 2 | 1.3% |
| finding-products-sourcing-options-sourcing-options-other | 98 | 45 | 0 | 0 | 0.0% |
| finding-products-sourcing-options-wholesale | 367 | 269 | 13 | 4 | 1.5% |
| marketing-and-conversion-advertising-ads | 413 | 209 | 8 | 2 | 1.0% |
| marketing-and-conversion-advertising-advertising-other | 176 | 125 | 4 | 2 | 1.6% |
| marketing-and-conversion-advertising-affiliate-programs | 293 | 165 | 1 | 1 | 0.6% |
| marketing-and-conversion-checkout-cart-customization | 577 | 335 | 18 | 2 | 0.6% |
| marketing-and-conversion-checkout-checkout-other | 441 | 316 | 10 | 3 | 0.9% |
| marketing-and-conversion-checkout-order-limits | 175 | 136 | 8 | 3 | 2.2% |
| marketing-and-conversion-customer-loyalty-customer-loyalty-other | 82 | 47 | 1 | 1 | 2.1% |
| marketing-and-conversion-customer-loyalty-donations | 83 | 32 | 1 | 0 | 0.0% |
| marketing-and-conversion-customer-loyalty-loyalty-and-rewards | 474 | 288 | 11 | 4 | 1.4% |
| marketing-and-conversion-customer-loyalty-wishlists | 249 | 176 | 6 | 1 | 0.6% |
| marketing-and-conversion-gifts-gift-cards | 61 | 28 | 0 | 0 | 0.0% |
| marketing-and-conversion-gifts-gift-wrap-and-messages | 80 | 52 | 2 | 2 | 3.8% |
| marketing-and-conversion-gifts-gifts-other | 85 | 46 | 3 | 1 | 2.2% |
| marketing-and-conversion-marketing-abandoned-cart | 375 | 225 | 10 | 6 | 2.7% |
| marketing-and-conversion-marketing-email-marketing | 437 | 224 | 6 | 3 | 1.3% |
| marketing-and-conversion-marketing-marketing-other | 388 | 281 | 2 | 2 | 0.7% |
| marketing-and-conversion-marketing-sms-marketing | 170 | 75 | 1 | 0 | 0.0% |
| marketing-and-conversion-marketing-web-push | 66 | 28 | 0 | 0 | 0.0% |
| marketing-and-conversion-promotions-discounts | 1245 | 818 | 33 | 11 | 1.3% |
| marketing-and-conversion-promotions-giveaways-and-contests | 73 | 41 | 1 | 1 | 2.4% |
| marketing-and-conversion-promotions-promotions-other | 212 | 114 | 3 | 1 | 0.9% |
| marketing-and-conversion-social-trust-product-reviews | 495 | 305 | 11 | 3 | 1.0% |
| marketing-and-conversion-social-trust-social-proof | 370 | 167 | 11 | 2 | 1.2% |
| marketing-and-conversion-social-trust-social-trust-other | 112 | 76 | 0 | 0 | 0.0% |
| marketing-and-conversion-upsell-and-bundles-countdown-timer | 198 | 121 | 2 | 0 | 0.0% |
| marketing-and-conversion-upsell-and-bundles-pre-orders | 128 | 74 | 8 | 2 | 2.7% |
| marketing-and-conversion-upsell-and-bundles-product-bundles | 544 | 379 | 23 | 7 | 1.8% |
| marketing-and-conversion-upsell-and-bundles-stock-alerts | 340 | 233 | 10 | 4 | 1.7% |
| marketing-and-conversion-upsell-and-bundles-upsell-and-bundles-other | 151 | 99 | 0 | 0 | 0.0% |
| marketing-and-conversion-upsell-and-bundles-upsell-and-cross-sell | 1253 | 794 | 44 | 14 | 1.8% |
| orders-and-shipping-inventory-erp | 215 | 121 | 1 | 0 | 0.0% |
| orders-and-shipping-inventory-inventory-optimization | 742 | 556 | 3 | 1 | 0.2% |
| orders-and-shipping-inventory-inventory-other | 274 | 198 | 0 | 0 | 0.0% |
| orders-and-shipping-inventory-inventory-sync | 645 | 236 | 4 | 2 | 0.8% |
| orders-and-shipping-orders-invoices-and-receipts | 547 | 382 | 5 | 3 | 0.8% |
| orders-and-shipping-orders-order-editing | 195 | 154 | 5 | 3 | 1.9% |
| orders-and-shipping-orders-order-tracking | 363 | 226 | 7 | 3 | 1.3% |
| orders-and-shipping-orders-orders-other | 549 | 380 | 5 | 4 | 1.1% |
| orders-and-shipping-returns-and-warranty-returns-and-exchanges | 285 | 193 | 7 | 4 | 2.1% |
| orders-and-shipping-returns-and-warranty-returns-and-warranty-other | 57 | 44 | 3 | 2 | 4.5% |
| orders-and-shipping-returns-and-warranty-warranties-and-insurance | 104 | 58 | 4 | 3 | 5.2% |
| orders-and-shipping-shipping-solutions-delivery-and-pickup | 663 | 348 | 11 | 4 | 1.1% |
| orders-and-shipping-shipping-solutions-shipping | 1173 | 585 | 9 | 4 | 0.7% |
| orders-and-shipping-shipping-solutions-shipping-rates | 569 | 261 | 8 | 3 | 1.1% |
| orders-and-shipping-shipping-solutions-shipping-solutions-other | 487 | 222 | 0 | 0 | 0.0% |
| orders-and-shipping-shipping-solutions-third-party-logistics-3pl | 248 | 124 | 0 | 0 | 0.0% |
| sales-channels-selling-in-person-retail | 158 | 91 | 5 | 2 | 2.2% |
| sales-channels-selling-in-person-selling-in-person-other | 59 | 44 | 1 | 0 | 0.0% |
| sales-channels-selling-in-person-sku-and-barcodes | 142 | 109 | 2 | 1 | 0.9% |
| sales-channels-selling-in-person-store-locator | 162 | 107 | 1 | 0 | 0.0% |
| sales-channels-selling-online-marketplaces | 253 | 96 | 7 | 3 | 3.1% |
| sales-channels-selling-online-product-feeds | 326 | 196 | 1 | 1 | 0.5% |
| sales-channels-selling-online-selling-online-other | 144 | 107 | 5 | 2 | 1.9% |
| sales-channels-selling-online-store-data-importer | 464 | 307 | 6 | 3 | 1.0% |
| selling-products-custom-products-custom-file-upload | 216 | 161 | 4 | 0 | 0.0% |
| selling-products-custom-products-custom-products-other | 262 | 180 | 6 | 2 | 1.1% |
| selling-products-custom-products-product-variants | 589 | 367 | 19 | 9 | 2.5% |
| selling-products-digital-goods-and-services-digital-goods-and-services-other | 46 | 20 | 0 | 0 | 0.0% |
| selling-products-digital-goods-and-services-digital-products | 130 | 79 | 2 | 1 | 1.3% |
| selling-products-digital-goods-and-services-event-booking | 160 | 102 | 6 | 1 | 1.0% |
| selling-products-digital-goods-and-services-nfts-and-tokengating | 13 | 2 | 0 | 0 | 0.0% |
| selling-products-payments-pay-later | 104 | 64 | 3 | 3 | 4.7% |
| selling-products-payments-payment-experience | 146 | 103 | 3 | 2 | 1.9% |
| selling-products-payments-payment-options-other | 96 | 54 | 1 | 1 | 1.9% |
| selling-products-payments-subscriptions | 168 | 108 | 5 | 0 | 0.0% |
| selling-products-pricing-pricing-optimization | 384 | 283 | 6 | 4 | 1.4% |
| selling-products-pricing-pricing-other | 177 | 121 | 1 | 0 | 0.0% |
| selling-products-pricing-pricing-quotes | 230 | 154 | 4 | 0 | 0.0% |
| store-design-content-blogs | 266 | 184 | 4 | 4 | 2.2% |
| store-design-content-content-other | 212 | 129 | 1 | 1 | 0.8% |
| store-design-content-metafields | 171 | 108 | 0 | 0 | 0.0% |
| store-design-content-product-content | 544 | 463 | 5 | 3 | 0.6% |
| store-design-design-elements-animation-and-effects | 141 | 79 | 0 | 0 | 0.0% |
| store-design-design-elements-badges-and-icons | 421 | 266 | 6 | 1 | 0.4% |
| store-design-design-elements-design-elements-other | 300 | 121 | 1 | 0 | 0.0% |
| store-design-images-and-media-3d-ar-vr | 419 | 357 | 3 | 3 | 0.8% |
| store-design-images-and-media-image-editor | 426 | 323 | 8 | 3 | 0.9% |
| store-design-images-and-media-image-gallery | 265 | 114 | 6 | 3 | 2.6% |
| store-design-images-and-media-images-and-media-other | 314 | 207 | 2 | 1 | 0.5% |
| store-design-images-and-media-video-and-livestream | 326 | 206 | 2 | 1 | 0.5% |
| store-design-internationalization-cookie-consent | 95 | 58 | 1 | 0 | 0.0% |
| store-design-internationalization-currency-and-translation | 209 | 117 | 6 | 3 | 2.6% |
| store-design-internationalization-geolocation | 160 | 75 | 7 | 4 | 5.3% |
| store-design-internationalization-internationalization-other | 45 | 21 | 0 | 0 | 0.0% |
| store-design-notifications-banners | 469 | 285 | 11 | 0 | 0.0% |
| store-design-notifications-forms | 219 | 136 | 1 | 1 | 0.7% |
| store-design-notifications-notifications-other | 80 | 46 | 0 | 0 | 0.0% |
| store-design-notifications-pop-ups | 508 | 270 | 11 | 3 | 1.1% |
| store-design-product-display-collections | 181 | 127 | 6 | 4 | 3.1% |
| store-design-product-display-product-comparison | 269 | 205 | 7 | 4 | 2.0% |
| store-design-product-display-product-display-other | 525 | 364 | 5 | 1 | 0.3% |
| store-design-search-and-navigation-navigation-and-menus | 167 | 91 | 2 | 2 | 2.2% |
| store-design-search-and-navigation-search-and-filters | 345 | 263 | 3 | 3 | 1.1% |
| store-design-search-and-navigation-search-and-navigation-other | 114 | 63 | 2 | 0 | 0.0% |
| store-design-site-optimization-accessibility | 159 | 124 | 8 | 3 | 2.4% |
| store-design-site-optimization-seo | 1255 | 995 | 33 | 18 | 1.8% |
| store-design-site-optimization-site-optimization-other | 276 | 202 | 8 | 3 | 1.5% |
| store-design-storefronts-mobile-app-builder | 112 | 53 | 3 | 1 | 1.9% |
| store-design-storefronts-page-builder | 392 | 234 | 14 | 10 | 4.3% |
| store-design-storefronts-storefronts-other | 287 | 151 | 8 | 4 | 2.6% |
| store-management-finances-accounting | 379 | 214 | 4 | 2 | 0.9% |
| store-management-finances-finances-other | 92 | 71 | 2 | 0 | 0.0% |
| store-management-finances-taxes | 217 | 151 | 5 | 1 | 0.7% |
| store-management-operations-analytics | 1779 | 1286 | 16 | 10 | 0.8% |
| store-management-operations-bulk-editor | 611 | 451 | 10 | 5 | 1.1% |
| store-management-operations-operations-other | 286 | 234 | 0 | 0 | 0.0% |
| store-management-operations-staff-notifications | 132 | 86 | 1 | 1 | 1.2% |
| store-management-operations-workflow-automation | 597 | 387 | 8 | 3 | 0.8% |
| store-management-security-accounts-and-login | 218 | 116 | 4 | 0 | 0.0% |
| store-management-security-anti-theft | 101 | 50 | 1 | 0 | 0.0% |
| store-management-security-fraud | 318 | 248 | 9 | 4 | 1.6% |
| store-management-security-legal | 650 | 544 | 20 | 8 | 1.5% |
| store-management-security-security-other | 132 | 99 | 1 | 0 | 0.0% |
| store-management-support-chat | 1110 | 836 | 24 | 15 | 1.8% |
| store-management-support-faq | 145 | 96 | 2 | 1 | 1.0% |
| store-management-support-helpdesk | 296 | 218 | 3 | 2 | 0.9% |
| store-management-support-support-other | 150 | 102 | 2 | 1 | 1.0% |
| store-management-support-surveys | 177 | 113 | 5 | 4 | 3.5% |

## Legătura cu faza 1 (domeniile 09 și 10)

| Problema din faza 1 | Categoria Shopify | Lansate | Trec toate pragurile |
|---|---|---|---|
| 09-P1 chargeback | store-management-security-fraud | 248 | 4 (niciunul nu face dosare de chargeback; vezi B7) |
| 09-P2 mesajele clienților | store-management-support-chat, helpdesk | 836, 218 | 15, 2 |
| 09-P3 reconcilierea plăților | store-management-finances-accounting | 214 | 2 |
| 09-P4 importul cataloagelor furnizorilor | store-management-operations-bulk-editor, sales-channels-selling-online-store-data-importer | 451, 307 | 5, 3 |
| 09-P5 retururi (închisă în faza 3) | orders-and-shipping-returns-and-warranty-* | 193 + 58 + 44 | 4 + 3 + 2, dar majoritatea sunt butoane de retragere UE (B1), nu fluxuri de retur |
| 10-P3 sincronizarea stocului între canale | orders-and-shipping-inventory-inventory-sync | 236 | 2 |
| 10-P1 și 10-P2 (Amazon) | nu au categorie Shopify directă | — | — |

Valorile din tabel sunt **verificat în sursă** (din numărătoare). Corespondența dintre probleme și categorii e **dedusă**.
