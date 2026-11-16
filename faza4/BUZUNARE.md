# Faza 4, pasul 3: buzunare

Data: 2026-11-16. Curs BNR 13.11.2026: 1 USD = 4,8428 lei, 1 EUR = 5,3498 lei.

**Buzunar** = un grup de aplicații sau pluginuri care rezolvă aceeași problemă și în care cel puțin 3 nou-veniți mici au trecut pragul.
- Shopify: lansată după 2024-11-16, cel puțin 20 de recenzii, plan plătit, dezvoltator cu cel mult 3 aplicații. Firmele mari au fost scoase de mână.
- WordPress: lansat după 2024-11-16, cel puțin 1.000 de instalări active, autor cu cel mult 5 pluginuri și fără firmă mare în spate.

**Numitorul** e numărul de aplicații lansate în fereastră care se potrivesc cu expresia buzunarului (nume + subtitlu la Shopify; slug + nume + etichete + descriere scurtă la WordPress). Expresiile sunt în `faza4/date/shopify/buzunare_numitori.json` și `faza4/date/wp/grupuri_expresii.txt`. Rata = nou-veniți mici peste prag / numitor.

Curbele primelor 90 de zile:
- **Shopify:** numărul de recenzii primite în primele 30, 60 și 90 de zile de la „Launched". Sunt numărate din toate recenziile descărcate, în `faza4/date/shopify/recenzii/<handle>.json`, iar rezultatul e în `faza4/date/shopify/curbe_recenzii.json`. Recenziile nu sunt vânzări. Sunt cel mai apropiat semn public, pentru că doar un magazin cu aplicația instalată poate lăsa recenzie.
- **WordPress:** descărcări în primele 30, 60 și 90 de zile de la `added`, din `stats/plugin/1.0/downloads.php` (`faza4/date/wp/descarcari/`).

## Ce s-a schimbat la praguri și de ce

1. **WordPress: pragul de 1.000 de instalări măsoară atenția, nu plata.** La pasul 1, majoritatea nou-veniților mici care l-au trecut nu au versiune plătită (PAS1_WORDPRESS.md). L-am păstrat ca prag de intrare, dar am adăugat o condiție: un buzunar WordPress trebuie să aibă **cel puțin 2 nou-veniți mici cu preț citit**. Altfel nu poate susține o propunere.
2. **Shopify: „cel mult 3 aplicații" lasă să treacă firme mari** (Judge.me, Trustpilot, Chatbase, Shogun, GoKwik, Clickpost). Le-am scos de mână.
3. **Shopify: recenziile vin în valuri.** Exemple: product-variant-options are 46 de recenzii în primele 90 de zile și 0 în august-octombrie 2026. mida-fraud-ip-blocker are 3 în primele 90 de zile și 345 în august-octombrie 2026. Asta sugerează campanii de cerut recenzii, nu un flux natural. Compar curbele prin mediană, nu prin medie. **dedus**

## Clasament (dedus)

Am ordonat buzunarele după numărul de nou-veniți mici plătiți, mediana recenziilor în primele 90 de zile și ritmul din august-octombrie 2026. Primele 6 merg la pasul 4.

| Loc | ID | Buzunar | Magazin | Lansate (numitor) | Nou-veniți mici peste prag | Rată | Mediana recenziilor la 90 de zile (nou-veniți) |
|---|---|---|---|---|---|---|---|
| 1 | B1 | Conformitate cu dreptul consumatorului UE (buton de retragere, eticheta de garanție) | Shopify | 189 | 7 | 3,7% | 49 |
| 2 | B2 | Vizibilitate în căutarea AI (llms.txt, indexare AI) | Shopify + WordPress | 700 + 780 | 10 + 3 | 1,4% / 0,4% | 7,5 |
| 3 | B7 | Verificarea comenzilor ramburs, fraudă, blocarea roboților și a țărilor | Shopify + WordPress | 437 + 125 | 7 + 4 | 1,6% / 3,2% | 3 |
| 4 | B8 | Import/export și editare în masă (Excel, CSV) | Shopify | 1.147 | 5 | 0,4% | 1 |
| 5 | B5 | Opțiuni de produs, imagini pe variantă, tabele de mărimi | Shopify | 536 | 8 | 1,5% | 2 |
| 6 | B4 | Secțiuni și pagini pentru temă (constructor) | Shopify | 219 | 8 | 3,7% | 5 |
| 7 | B6 | Comenzi și mesaje prin WhatsApp/chat | Shopify + WordPress | 454 + 791 | 5 + 4 (gratuite) | 1,1% / 0,5% | 7 |
| 8 | B9 | Data estimată a livrării, programarea ridicării | Shopify | 241 | 5 | 2,1% | 0 |
| 9 | B3 | Articole de blog SEO generate cu AI | Shopify (+ conectori SaaS pe WP) | 268 | 4 | 1,5% | 7 |
| 10 | WP-A | Conectarea agenților AI (MCP) la site | WordPress | 248 | 5 | 2,0% | 6.715 descărcări |
| 11 | WP-E | Gestionarea bibliotecii media | WordPress | 630 | 5 | 0,8% | 1.512 descărcări |
| 12 | WP-G | Widgeturi Elementor | WordPress | 1.094 | 7 | 0,6% | 1.063 descărcări |

La B3 și B6 câte o aplicație a fost adăugată de mână (ai-blog-post-generator-1, instachat). Expresia nu le-a prins, așa că numitorul de mai sus le include (+1). **dedus**

Eliminate înainte de clasament:
- **Accesibilitate (accessify, isonomy, testparty: 3 nou-veniți, 124 de lansări):** criteriul (d). Aplicațiile de tip „overlay" promit conformitate legală pe care vânzătorul nu o poate garanta. **dedus**
- **Protecția expedierii și garanții (easy-shipping-protection, inhouse, dyrect):** criteriul (d). E un produs apropiat de asigurare, cu risc fiscal și juridic. **dedus**
- **Editarea comenzii de către client:** doar 2 nou-veniți mici după ce am scos Clickpost (firmă de logistică).
- **Bundles și reduceri:** 14 nou-veniți trec pragurile, dar liderii au mii de recenzii, iar curbele nou-veniților sunt cele mai slabe. Nu l-am pus în primele 12. Locul l-au luat buzunarele mai legate de faza 1 sau de proprietar. **dedus**

---

## B1. Conformitate cu dreptul consumatorului UE (Shopify)

**Ce vând.** Un buton „retragere din contract" și un formular pe site, cu confirmare automată prin e-mail. Contextul: directiva (UE) 2023/2673, aplicabilă din 19 iunie 2026 (data apare în recenzii, dar nu am citit directiva). Nou-veniții din august 2026 adaugă eticheta armonizată a garanției legale. **verificat în sursă** (descrierile și prețurile din paginile aplicațiilor)

| Aplicație | Lansată | Recenzii | Rating | Preț | Recenzii la 30/60/90 de zile | Recenzii aug.-oct. 2026 |
|---|---|---|---|---|---|---|
| eu-widerrufsbutton (401layers UG, 2 aplicații) | 2026-01-09 | 2.324 | 4,9 | 9,99 $/lună sau 99,99 $/an; 29,99 $/lună | 5 / 15 / 27 | 76 |
| eu-withdrawal-form (BuschBytes, 2) | 2026-03-11 | 582 | 4,8 | 9 $/lună, 25 $/lună | 22 / 49 / 79 | 92 |
| eu-widerruf-pro (ECOMBEAT, 3) | 2026-05-07 | 330 | 5,0 | 11,99 $ și 17,99 $/lună | 85 / 261 / 289 | 35 |
| wideruf-button (Anviara LLC, 1) | 2026-05-06 | 108 | 4,8 | 7,99 $/lună | 14 / 91 / 93 | 13 |
| eu-widerrufsbutton-1 (Visionz GmbH, 3) | 2026-05-12 | 51 | 5,0 | 5,99 $/lună, 24,99 $/lună | 21 / 45 / 48 | 2 |
| eu-guarantee-warranty-label (Consentico, 3) | 2026-08-26 | 49 | 5,0 | 4,99 $ și 9,99 $/lună | 19 / 48 / 49 | 49 |
| eu-warranty-garan-label (Nico Münster et al., 2) | 2026-08-05 | 50 | 5,0 | 4,99 $/lună | 0 / 40 / 46 | 46 |

Surse: `https://apps.shopify.com/<handle>` și `/reviews`, citite pe 2026-11-16. **verificat în sursă**

- **Liderul e un nou-venit.** eu-widerrufsbutton are 2.324 de recenzii în 10 luni. Vechiul lider al categoriei „legal" e terms-and-conditions-checkbox (2019, 569 de recenzii). **verificat în sursă**
- **Rata:** 7 / 189 = 3,7%, cea mai mare dintre buzunare. **verificat în sursă** (numărătoarea), **dedus** (granițele grupului)
- **Curba:** valul a venit în jurul termenului de 19 iunie. Recenziile nou-veniților sunt concentrate în iunie-iulie 2026. În august-octombrie, eu-widerrufsbutton a primit doar 76, adică ~3% din total. **verificat în sursă**
- **Platforma a reacționat.** În changelog-ul Shopify (18 iunie): „Set cancellation rules for buyers … to enable EU-specific policies in response to changing right of withdrawal regulations" (`faza4/date/platforma/shopify_changelog_withdrawal.html`). Nu știu dacă asta acoperă cerința fără aplicație. Faptul că aplicațiile au primit recenzii noi și după 18 iunie sugerează că nu o acoperă complet. **doar fragment**
- **Pe WordPress**, aceeași problemă are 113 lansări, iar 3 au trecut de 1.000 de instalări (vendidero 6.000, Fernando Tellado 2.000, WebToffee 1.000). Toți trei au peste 5 pluginuri, deci acolo nu e buzunar de autori mici. **verificat în sursă**
- **Legătură cu faza 1:** 09-P5 (retururi). Candidata de retururi din faza 3 a fost închisă. Aici problema e alta, obligația legală de retragere, nu fluxul de retur. **dedus**

## B2. Vizibilitate în căutarea AI (Shopify + WordPress)

**Ce vând:** fișier llms.txt, indexare pentru ChatGPT/Perplexity, date structurate pentru agenții de cumpărături, urmărirea roboților AI.

| Aplicație | Lansată | Recenzii / instalări | Preț | Curba la 30/60/90 de zile |
|---|---|---|---|---|
| llms-txt-generator-ai-search (ArcSpeed) | 2025-06-30 | 79 rec., 4,4 | 9 $/lună, 99 $/an | 4 / 14 / 23 rec. |
| kedra-ai-index (Kedra Apps) | 2026-04-27 | 50 rec., 4,9 | 10 $/lună, 25 $/lună | 9 / 34 / 38 |
| llms-txt-agent (Go Plus NZ) | 2025-08-25 | 47 rec., 5,0 | 7,95 $ și 14,95 $/lună | 4 / 7 / 12 |
| shoprank-ai (Zipify Lab) | 2025-12-04 | 42 rec., 4,7 | 9,99 $/lună | 0 / 0 / 0 |
| kwik-geo-1 (GoExcelsior) | 2026-06-11 | 37 rec., 5,0 | 149 $/lună | 0 / 3 / 15 |
| ai-index-pro (ECOMBEAT) | 2026-05-19 | 32 rec. | 14,99 $/lună | 3 / 22 / 24 |
| storerank-ai | 2025-08-21 | 31 rec. | 29 $/lună | 0 / 2 / 2 |
| fourty-ai (40rty) | 2025-10-15 | 22 rec. | 49 $/lună | 1 / 1 / 2 |
| link-gpt (Gemcy) | 2026-01-01 | 26 rec. | 47 $/lună | 0 / 0 / 3 |
| index-gpt | 2024-11-25 | 156 rec. | 12 $/lună | 0 / 0 / 0 |
| WP: llms-txt-generator (aeomatic) | 2025-01-11 | 1.000 inst. | 49 $/an | 168 / 423 / 698 descărcări |
| WP: lovedbyai-seo-for-llms-and-ai-search | 2026-01-13 | 1.000 inst. | 29 $/lună (anual) | 568 / 1.793 / 3.392 |
| WP: llm-bot-tracker-by-hueston | 2025-09-09 | 1.000 inst. | gratuit | 1.090 / 1.306 / 1.456 |

- **Lideri:** la Shopify, în categoria SEO, sunt suitele vechi (Booster SEO 5.483 de recenzii, Avada SEO 4.689, de la 34,95 $/lună) și seolab (2.935, lansată 2024-12-16, de la 14 $/lună). Pe WordPress e website-llms-txt (50.000 de instalări, autor cu 6 pluginuri). **verificat în sursă**
- **Rata:** Shopify 10/700 = 1,4%, WordPress 3/780 = 0,4%. **verificat în sursă**
- **Curba:** mediana la 90 de zile e de 7,5 recenzii. Creștere lentă, cu valuri mici. **verificat în sursă**
- **Risc (b), dedus:** un fișier llms.txt se face și de mână. Un recenzent spune explicit asta (vezi pasul 4).

## B7. Ramburs, fraudă, blocarea roboților și a țărilor (Shopify + WordPress)

| Aplicație | Lansată | Recenzii / instalări | Preț | Curba la 30/60/90 de zile |
|---|---|---|---|---|
| mida-fraud-ip-blocker (MIDA, 3) | 2025-09-19 | 580 rec., 4,9 | 9, 19, 39 $/lună | 0 / 0 / 3 (345 în aug.-oct. 2026) |
| partialy-partial-payment-cod | 2025-06-16 | 76 | 10 $/lună | 0 / 3 / 7 |
| cartsaver-otp-cod (Xtnd) | 2025-05-20 | 63 | 9,99-159,99 $/lună | 0 / 0 / 3 |
| neo-cod-form-upsell-pixel-otp | 2026-05-15 | 55 | 6,99 $/lună | 9 / 11 / 12 |
| blocklist (Blox) | 2025-02-24 | 22 | 19 $/lună | 0 / 0 / 0 |
| cartwatch (Vynt Labs) | 2026-05-26 | 21 | 9,99 $/lună | 0 / 0 / 3 |
| codsaver-1 | 2026-03-23 | 20 | 2,99-10 $/lună | 1 / 5 / 12 |
| WP: botblocker-security | 2025-11-02 | 3.000 inst. | preț necunoscut (pagina dă 400) | 616 / 1.109 / 2.095 descărcări |
| WP: advanced-ip-blocker | 2025-06-26 | 3.000 | gratuit | 691 / 1.743 / 2.281 |
| WP: country-access-blocker | 2025-09-19 | 1.000 | gratuit | 124 / 304 / 473 |
| WP: geo-blocker | 2025-05-18 | 1.000 | gratuit | 82 / 141 / 234 |

- **Lider Shopify:** Blockify (2018, 1.873 de recenzii, de la 9,99 $/lună). **verificat în sursă**
- **Rata:** Shopify 7/437 = 1,6%; WordPress 4/125 = 3,2%, dar pe WordPress niciunul nu are preț citit. **verificat în sursă**
- **Legătură cu faza 1:** 09-P1 (chargeback). Niciun nou-venit nu face dosare de chargeback. Fac prevenție: blochează IP-uri și confirmă comenzile ramburs prin OTP. **dedus**
- **Pentru proprietar (dedus):** confirmarea comenzilor ramburs prin OTP ține de piețele cu ramburs (aplicațiile vin din Egipt, India, Pakistan, America Latină). Nu am verificat cererea din România în aceste magazine.

## B8. Import/export și editare în masă (Shopify)

| Aplicație | Lansată | Recenzii | Preț | Curba la 30/60/90 de zile |
|---|---|---|---|---|
| altera-import-export-excel (Abnoba LLC, 1) | 2025-02-21 | 268, 5,0 | 15 $/lună | 0 / 0 / 1 (57 în aug.-oct.) |
| etsy-import-and-sync-by-sp | 2025-04-14 | 48 | 9,99 $ și 19,99 $/lună | 0 / 0 / 0 |
| bulkflow-files-import-export | 2025-05-14 | 38 | 15 $/lună, 159 $/an | 0 / 1 / 1 |
| bulk-ai (AC App-Commerce UG) | 2025-11-18 | 33 | 29-249 $/lună | 0 / 1 / 4 |
| send2many-order-upload | 2024-12-06 | 31 | 50 $/lună | 0 / 0 / 1 |

- **Lider:** Matrixify (excel-export-import, 2017, 1.896 de recenzii, 20/50/200 $/lună). Urmează Hextom Bulk Product Edit (1.203) și Ablestar (942). **verificat în sursă**
- **Rata:** 5/1.147 = 0,4%, cea mai mică dintre primele 6. **verificat în sursă**
- **Curba:** aproape plată în primele 90 de zile (mediana 1). Nou-veniții cresc abia după 6-12 luni. **verificat în sursă**
- **Legătură cu faza 1:** 09-P4 (importul cataloagelor furnizorilor din PDF/Excel). **dedus**

## B5. Opțiuni de produs, imagini pe variantă, tabele de mărimi (Shopify)

| Aplicație | Lansată | Recenzii | Preț | Curba la 30/60/90 de zile |
|---|---|---|---|---|
| variantify (SMC) | 2025-07-14 | 67 | 9,99 $/lună | 1 / 1 / 6 |
| nova-multiple-variant-images (Hey Jak) | 2026-02-16 | 59 | 9,99 $/lună | 2 / 5 / 7 |
| scalechart (Scalechart LLC) | 2026-01-01 | 54 | 29,99 $/lună | 0 / 0 / 0 (39 în aug.-oct.) |
| product-variant-options (Kefi Commerce) | 2026-03-09 | 46 | 5 $/lună | 12 / 40 / 46 |
| gg-variant-images (gg Apps, 1) | 2025-06-26 | 43 | 15 $/lună | 0 / 2 / 2 |
| podifai | 2025-09-10 | 37 | 7,9 $/lună | 0 / 0 / 0 |
| groopie (GIE systems) | 2025-03-21 | 26 | 4,99 $/lună | 1 / 1 / 1 |
| product-options-app (WowApps.io) | 2026-04-13 | 23 | 4,99 $/lună | 0 / 1 / 2 |

- **Lideri:** Globo Product Options (5.297 de recenzii, de la 4,95 $/lună), Easify (3.254), Variant Swatch King (3.236). **verificat în sursă**
- **Rata:** 8/536 = 1,5%. Mediana la 90 de zile: 2 recenzii. **verificat în sursă**

## B4. Secțiuni și pagini pentru temă (Shopify)

| Aplicație | Lansată | Recenzii | Preț | Curba la 30/60/90 de zile |
|---|---|---|---|---|
| versio-smart-blocks | 2025-02-26 | 65 | 19,95 $/lună | 0 / 0 / 0 |
| forge-ai-store-builder | 2025-10-29 | 62 | 29,99 $/lună | 3 / 4 / 6 |
| sectionheroes | 2025-12-12 | 59 | 22,9 $/lună | 0 / 16 / 34 |
| fudge-agent | 2025-07-02 | 58 | 25-349 $/lună | 0 / 1 / 4 |
| titan | 2025-07-18 | 54 | 29 $/lună | 0 / 3 / 4 |
| ecombe-page-builder | 2026-01-28 | 35 | 14,99 $/lună | 17 / 26 / 29 |
| kluckyv5 (Kluck.ai) | 2025-12-23 | 32 | 20-69 $ o singură dată | 0 / 2 / 4 |
| modulo-sections-bundles | 2026-05-29 | 25 | 15 $/lună, 149 $/an | 4 / 6 / 16 |

- **Lideri:** PageFly (5.929 de recenzii), GemPages (4.267), EComposer (3.460), Section Store (3.043, 15 $/lună). **verificat în sursă**
- **Rata:** 8/219 = 3,7%, egală cu B1. Mediana la 90 de zile: 5 recenzii. **verificat în sursă**
- **Pentru proprietar (dedus):** e cel mai apropiat de meseria agenției (construcție de pagini), dar pe Shopify, nu pe WordPress/Elementor.

## B6. Comenzi și mesaje prin WhatsApp/chat (Shopify + WordPress)

- Shopify: ca-chat-order-button-widget (83 de recenzii, 4,99-14,99 $/lună), instachat (421, 14,99-49,99 $/lună), whatsapp-pilot (22, 15 $/lună), whatify (27, rating 3,2), wasp-order-confirmation (23, 5-20 $/lună). Lider: Shopify Inbox (gratuit, 5.818 recenzii), deci criteriul (b) e parțial îndeplinit pentru chatul simplu. **verificat în sursă**
- WordPress: 4 butoane flotante gratuite (WP-D). Niciunul nu are preț citit. **verificat în sursă**
- Rata: Shopify 5/454 = 1,1%. Mediana la 90 de zile: 7. **verificat în sursă**

## B9. Data estimată a livrării și programarea ridicării (Shopify)

- peakship (61 de recenzii, 19,99 $/lună), kite-pickup-delivery-date (48, 4,99 $/lună), kosr (43, 12 $/lună), estimated-delivery-date-eta (26, 5,99 $/lună), shipping-popup-app (20, 55 $/lună). **verificat în sursă**
- Lideri: Zapiet (1.905, 49,99 $/lună), Logbase (1.351, 9,99 $/lună). **verificat în sursă**
- Rata: 5/241 = 2,1%. Mediana la 90 de zile: **0**. Toți au crescut după prima lună de la lansare. **verificat în sursă**

## B3. Articole de blog SEO generate cu AI (Shopify)

- ai-blog-agent (233 de recenzii, 8,99 $/lună), autopilotseo (131, 12,75-54 $/lună), soro (29, 39 $/lună), ai-blog-post-generator-1 (30, 79 $/lună). Lider: SEO Master de la CWILL (1.811). Pe WordPress există 7 conectori ai unor SaaS similare (WP-L, ANEXA.md). **verificat în sursă**
- Rata: 4/268 = 1,5%. Mediana la 90 de zile: 7. **verificat în sursă**

## WP-A. Conectarea agenților AI (MCP) la site (WordPress)

- royal-mcp (10.000 de instalări, „Royally" de la 9 $/lună), diviops-agent (1.000, Pro 29 €/an), enable-abilities-for-mcp (6.000, gratuit), wsp-mcp-ai-agents-connector (3.000, gratuit), cowboy-mcp (2.000, gratuit). **verificat în sursă**
- Lideri: firme mari și WordPress.org însuși (mcp-adapter 70.000, plugin oficial; vibe-ai/SeedProd 100.000; angie/Elementor 100.000). **verificat în sursă**
- Rata: 5/248 = 2,0%. Descărcări la 90 de zile, mediana: 6.715. **verificat în sursă**
- **Criteriul (b), dedus:** WordPress.org publică gratuit un adaptor MCP oficial (mcp-adapter). Funcția de bază devine nativă.

## WP-E. Gestionarea bibliotecii media (WordPress)

- add-from-server-reloaded (4.000; Pro 59 $/an), export-media-as-zip (3.000; Premium, preț necunoscut), calliope-media-import-export (1.000; Pro, preț necunoscut), smart-auto-upload-images (5.000; gratuit), media-sweep (1.000; gratuit). **verificat în sursă**
- Rata: 5/630 = 0,8%. Doar un preț citit. **Nu trece de condiția nouă de la WordPress (2 prețuri citite).** **verificat în sursă**

## WP-G. Widgeturi Elementor (WordPress)

- custom-iframe (4.000; 19 $ o singură dată), aitoel-html-importer (1.000; 47 $/an), dynamic-elementor-acf-repeater (1.000; Pro prin Freemius, preț necunoscut), popup-for-elementor (1.000; Pro, preț necunoscut), pdf-smart-viewer-for-elementor, mox-icons-pack-for-elementor, better-post-filter-widgets-for-elementor (gratuite). **verificat în sursă**
- Rata: 7/1.094 = 0,6%. Fiecare plugin rezolvă altă problemă, deci e un buzunar de canal, nu de problemă. **dedus**

## Candidatele închise în faza 3

- **09-P5 (retururi Shopify)** nu reapare ca buzunar. Categoria retururi conține în cea mai mare parte butoane de retragere UE (B1). Fluxul de retur propriu-zis nu are 3 nou-veniți mici peste prag. **verificat în sursă**
- **09-P1 (chargeback)** nu reapare. B7 face prevenție, nu dosare de dispută. Motivul închiderii din faza 3 (aprobarea API-ului de scriere a dovezilor) rămâne valabil. **dedus**
