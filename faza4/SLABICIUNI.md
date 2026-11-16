# Faza 4, pasul 4: slăbiciuni în primele 6 buzunare

Data: 2026-11-16. Fereastra: recenzii de 1-3 stele și fire de suport nerezolvate din 2025-11-16 până azi.

## Metodă

- **Shopify:** la nou-veniți am citit toate recenziile (`faza4/date/shopify/recenzii/<handle>.json`). La lideri am citit primele 6 pagini filtrate pe 1, 2 și 3 stele (`faza4/date/shopify/recenzii_lideri_1-3.json`). Filtrul a întors doar recenzii de 1-3 stele (343 de 1, 54 de 2, 84 de 3). Linkul fiecărei recenzii e de forma `https://apps.shopify.com/reviews/<id>`. Am verificat că răspunde 200. **Shopify nu are forum public de suport pe aplicație**, deci „fire de suport nerezolvate" nu există ca sursă.
- **WordPress:** paginile `reviews/?filter=1|2|3` și `/unresolved/` ale pluginurilor din buzunare, salvate în `faza4/date/wp/suport/`.
- Citatele au cel mult 15 cuvinte și sunt copiate din text. Unde originalul nu e în engleză, traducerea mea e între paranteze drepte. Toate citatele sunt **verificat în sursă**. Gruparea lor pe teme e **dedusă**.
- Multe recenzii de 1-3 stele nu au text (doar steaua). Nu le-am folosit ca citat.

## Teme care apar în toate cele 6 buzunare (dedus)

1. **Aplicația scrie în temă și lasă urme după dezinstalare.** Apare în B1, B2, B4 și B7.
2. **„Gratuit" care se dovedește plătit după instalare.** Apare în B1, B2, B5 și B8.
3. **Facturare după dezinstalare și rambursări refuzate.** Apare la liderii din B4, B5 și B8.
4. **Nu merge pe piețe și limbi multiple (Shopify Markets).** Apare în B1, B2 și B8.

Pentru un produs nou, acestea sunt slăbiciuni de execuție, nu de funcție. Asta înseamnă că un nou-venit poate concura prin calitate și onestitate, nu doar prin funcții. Dar înseamnă și că diferențierea e greu de arătat pe pagina din magazin înainte de recenzii. **dedus**

---

## B1. Conformitate cu dreptul consumatorului UE

Legătură cu faza 1: vecină cu **09-P5** (retururi), dar nu identică.

| Temă | Citat | Aplicație | Data | Link |
|---|---|---|---|---|
| Strică tema și paginile | „Plättet also bei uns als u. a. das Impressum, was ein no go ist" [a șters la noi, printre altele, pagina de impressum] | eu-widerrufsbutton (lider) | 2026-09-23 | https://apps.shopify.com/reviews/2370644 |
| Strică tema și paginile | „it disabled my existing main-page section … and replaced it with its own" | eu-widerrufsbutton | 2026-06-23 | https://apps.shopify.com/reviews/2256904 |
| Gratuit care nu e gratuit | „Nie informują, że darmowy plan działa tylko w trybie testowym." [nu spun că planul gratuit merge doar în mod de test] | eu-widerrufsbutton | 2026-06-19 | https://apps.shopify.com/reviews/2252470 |
| Gratuit care nu e gratuit | „why there are paid tiers on something that is required by the law" | eu-widerrufsbutton | 2026-06-25 | https://apps.shopify.com/reviews/2261117 |
| Se poate face și gratuit | „Umsetzung mit Shopify Forms kostenlos" [implementarea cu Shopify Forms e gratuită] | eu-widerrufsbutton (recenzie de 3 stele) | 2026-05-27 | https://apps.shopify.com/reviews/2220411 |
| O singură limbă | „Can't change language. Only German." | eu-widerruf-pro | 2026-08-19 (magazin din **România**) | https://apps.shopify.com/reviews/2327985 |
| O singură limbă | „I can't get the Dutch version installed" | eu-withdrawal-form | 2026-07-10 | https://apps.shopify.com/reviews/2279804 |
| Logica legală incompletă | „Ce bouton devrait aussi disparaître automatiquement 14 jours après la réception" [butonul ar trebui să dispară singur la 14 zile după primire] | wideruf-button | 2026-06-15 | https://apps.shopify.com/reviews/2245033 |
| Prețul crește după ce se aplică legea | „added a paid plan after the shopify email went out" | wideruf-button | 2026-06-12 | https://apps.shopify.com/reviews/2242175 |
| Funcție de bază pusă la plata superioară | „Automatic Check period if available or not for is only at $25" | eu-withdrawal-form | 2026-06-12 | https://apps.shopify.com/reviews/2241566 |
| Suport | „Offers no support, does not respond to emails." | eu-widerrufsbutton | 2026-07-07 | https://apps.shopify.com/reviews/2274392 |
| Nu verifică datele comenzii (WooCommerce) | „It does not check against anything in a real order" | eu-order-withdrawal-button-for-woocommerce (vendidero), WP.org | 2026-08-24 | https://wordpress.org/support/topic/almost-unusable-none-of-the-entered-values-is-checked-against-any-order-inform/ |
| Vechiul lider (bifă de termeni) | „a simple checkbox should no't cost an subscription" | terms-and-conditions-checkbox | 2026-07-21 | https://apps.shopify.com/reviews/2291682 |

Fire de suport nerezolvate pe WordPress (wt-eu-withdrawal-button, eu-withdrawal-compliance, eu-order-withdrawal-button-for-woocommerce): **0** pe pagina `/unresolved/`, la 2026-11-16. **verificat în sursă**

## B2. Vizibilitate în căutarea AI

Legătură cu faza 1: nu are ID direct în domeniile 09 și 10.

| Temă | Citat | Aplicație | Data | Link |
|---|---|---|---|---|
| Nu se vede efectul | „We had only 4 traffics from AI agents since we installed this app" | index-gpt | 2026-03-23 | https://apps.shopify.com/reviews/2132221 |
| Se poate face fără aplicație | „just another company trying to get you to pay for something that you can do" | lovedbyai (WP.org, 2 stele) | 2026-08-02 | https://wordpress.org/support/topic/pointless-24/ |
| Conținut greșit generat | „hundreds of items like alcohol and cigarettes which we don't sell at all" | llms-txt-generator-ai-search | 2026-03-22 | https://apps.shopify.com/reviews/2130722 |
| Lasă fișiere după dezinstalare | „the file it created (a faulty file) still remains on my store" | llms-txt-generator-ai-search | 2026-05-15 | https://apps.shopify.com/reviews/2205524 |
| Strică ce exista | „It broke my llm.txt it give 404 now" | llms-txt-generator-ai-search | 2026-04-18 | https://apps.shopify.com/reviews/2168499 |
| Lider: nu merge pe piețe multiple | „not properly designed for a multi-market setup" | Booster SEO (lider) | 2026-09-19 | https://apps.shopify.com/reviews/2366373 |
| Lider: arată „100% optimized", dar nu aplică | „none of the changes were actually being applied to our store" | Booster SEO | 2026-03-05 | https://apps.shopify.com/reviews/2107068 |
| Lider: încetinește urmărirea | „Avada blocked it just to show a fake high speed score" | Avada SEO Suite | 2025-12-29 | https://apps.shopify.com/reviews/2017833 |
| Lider: cote mici în planul gratuit | „they only give you 50 quota to fix your alt text" | seolab | 2026-05-13 | https://apps.shopify.com/reviews/2202554 |

Fire nerezolvate pe WordPress: website-llms-txt are 16 fire pe pagina `/unresolved/`. Exemple: „“Custom llms.txt text” not shown", „File Not Updating After Changes Made" (`faza4/date/wp/suport/website-llms-txt_unresolved.html`). Datele firelor nu sunt citite unul câte unul. **doar fragment**

## B7. Ramburs, fraudă, blocarea roboților și a țărilor

Legătură cu faza 1: **09-P1** (chargeback). Plângerile despre roboți și comenzi false sunt înrudite, dar produsul e altul (prevenție).

| Temă | Citat | Aplicație | Data | Link |
|---|---|---|---|---|
| Blochează clienți reali | „it ended up denying access to even my current clients" | mida-fraud-ip-blocker | 2026-03-03 | https://apps.shopify.com/reviews/2104538 |
| Blochează roboți buni (Google) | „MIDA is blocking web-crawlers" | mida-fraud-ip-blocker | 2026-04-28 | https://apps.shopify.com/reviews/2181936 |
| Strică SEO | „This app destroyed my SEO and cost me a month of sales." | mida-fraud-ip-blocker | 2026-06-03 | https://apps.shopify.com/reviews/2229142 |
| Nu oprește roboții | „we still get bot abandoned checkouts and page views" | Blockify (lider) | 2025-12-26 | https://apps.shopify.com/reviews/2015619 |
| Nu blochează țara | „It's impossible to block a country's IP address.!!!" | Blockify | 2026-01-07 | https://apps.shopify.com/reviews/2027430 |
| Conflicte cu alte aplicații | „The app is blocking so many other apps from my website" | Blockify | 2026-03-01 | https://apps.shopify.com/reviews/2102088 |
| Chargeback-uri tot trec | „we're still getting chargebacks due to orders being flagged high risk" | blocklist | 2026-05-28 | https://apps.shopify.com/reviews/2222047 |
| Preț | „significantly more expensive compared to other competing apps" | cartsaver-otp-cod | 2026-10-22 | https://apps.shopify.com/reviews/2404252 |
| WordPress: se blochează singur adminul | „It locked me out of my admin panel." | advanced-ip-blocker (WP.org) | 2026-03-10 | https://wordpress.org/support/topic/t-locked-me-out-of-my-admin-panel/ |

## B8. Import/export și editare în masă

Legătură cu faza 1: **09-P4** (cataloagele și listele de prețuri ale furnizorilor).

| Temă | Citat | Aplicație | Data | Link |
|---|---|---|---|---|
| Greu de folosit fără Excel | „Unless you are an XL guru this app is rubbish." | Matrixify (lider) | 2026-08-27 | https://apps.shopify.com/reviews/2337848 |
| Preț pe trepte mari | „If you need more, you are pushed toward a $200/month plan." | Matrixify | 2026-05-31 | https://apps.shopify.com/reviews/2225395 |
| Plan gratuit inutil | „The free version is completely useless. This app charges you 30usd" | Matrixify | 2026-06-23 | https://apps.shopify.com/reviews/2257527 |
| Erori fără explicație | „It constantly throws errors at you without providing any explanation" | Matrixify | 2026-04-06 | https://apps.shopify.com/reviews/2150840 |
| Facturare după dezinstalare | „Nous sommes facturés depuis plusieurs mois alors que l'application est desintallée" [suntem facturați de câteva luni, deși aplicația e dezinstalată] | Matrixify | 2026-05-15 | https://apps.shopify.com/reviews/2205879 |
| Facturare după dezinstalare | „Canceled and uninstalled app May 6th and still charged renewal May 9th" | Hextom Bulk Product Edit | 2026-05-14 | https://apps.shopify.com/reviews/2203626 |
| Editare incompletă | „only deleted 11 sections in the descriptions, 18 descriptions unedited" | Hextom Bulk Product Edit | 2026-02-07 | https://apps.shopify.com/reviews/2071703 |
| Nu merge pe piețe | „it does not allow modifications per market" | bulk-ai | 2026-03-16 | https://apps.shopify.com/reviews/2122975 |
| Fișierele furnizorilor | „they do not sign ADA's being supplied by major Suppliers" | Matrixify | 2026-03-05 | https://apps.shopify.com/reviews/2108094 |

## B5. Opțiuni de produs, imagini pe variantă

Legătură cu faza 1: nu are ID direct.

| Temă | Citat | Aplicație | Data | Link |
|---|---|---|---|---|
| Strică prețurile | „the prices were automatically changed and displayed higher on the storefront" | Globo Product Options (lider) | 2025-12-16 | https://apps.shopify.com/reviews/2003723 |
| Pierde date din comenzi | „App updates are constantly wiping out custom data on my new orders" | Globo Product Options | 2026-04-19 | https://apps.shopify.com/reviews/2169664 |
| Funcție de bază la plata superioară | „Paywalling 'multiple variant groups' … to the highest tier" | Globo Product Options | 2026-03-06 | https://apps.shopify.com/reviews/2109243 |
| Nu adună prețul opțiunii în coș | „Inputs do not modify the cost of an item in the cart." | Easify (lider) | 2026-06-11 | https://apps.shopify.com/reviews/2241217 |
| Înlocuibil cu cod propriu | „just get chatgpt or Claude to custom code something" | Easify | 2026-06-11 | https://apps.shopify.com/reviews/2241217 |
| Personalizarea nu ajunge în comandă | „Basic personalization text … was not passed on into the order details" | Easify | 2026-05-15 | https://apps.shopify.com/reviews/2204855 |
| Planul gratuit nu permite prețuri | „Free-trial is useless. You can't set pricing of any option." | Easify | 2025-12-11 | https://apps.shopify.com/reviews/1997827 |
| Facturare după ștergere | „keep charging while I deleted the app 3 months ago" | Variant Swatch King (lider) | 2026-10-14 | https://apps.shopify.com/reviews/2394809 |

La nou-veniți (variantify, nova, scalechart, gg-variant-images, product-variant-options, groopie, product-options-app, podifai) există doar 3 recenzii de 1-3 stele în fereastră, două fără conținut util. **verificat în sursă**

## B4. Secțiuni și pagini pentru temă

Legătură cu faza 1: nu are ID direct.

| Temă | Citat | Aplicație | Data | Link |
|---|---|---|---|---|
| Ce se vede în editor nu e ce iese pe site | „Constant discrepancies between editor and live page." | PageFly (lider) | 2026-08-27 | https://apps.shopify.com/reviews/2338753 |
| Scrie cod în temă fără să fie folosit | „pagefly added random code even when I wasn't using their app" | PageFly | 2026-02-06 | https://apps.shopify.com/reviews/2071170 |
| Indisponibilitate | „we lose access to the PageFly console for half a day or more" | PageFly | 2026-05-12 | https://apps.shopify.com/reviews/2200188 |
| Prea scump pentru magazine mici | „$59USD a month … This isn't feasible for me." | GemPages | 2026-07-30 | https://apps.shopify.com/reviews/2304100 |
| Facturare după dezinstalare | „installed the app and deleted it less than 48 hours later and they charged" | GemPages | 2026-04-22 | https://apps.shopify.com/reviews/2173838 |
| Încarcă pagina | „Creates a lot of bloat." | EComposer | 2025-12-02 | https://apps.shopify.com/reviews/1985259 |
| Prețul nou-veniților AI | „the pricing model is completely unreasonable for smaller Shopify stores" | fudge-agent | 2026-08-15 | https://apps.shopify.com/reviews/2323853 |
| Copie | „Cheap copy of the SectionStore app." | versio-smart-blocks | 2026-02-25 | https://apps.shopify.com/reviews/2096300 |

## Ce lipsește (necunoscut)

- Rata reală de plângeri. Recenziile de 1-3 stele sunt puține față de cele de 5 stele, iar valurile de recenzii de 5 stele par cerute (pasul 3). Nu se poate deduce satisfacția reală.
- La Shopify, motivele dezinstalării, dacă nu sunt scrise în recenzie.
