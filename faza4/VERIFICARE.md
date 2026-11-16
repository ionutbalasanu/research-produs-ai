# Faza 4: verificare independentă

Data verificării: 2026-11-16. Verificatorul nu a lucrat la pașii 1-4. Nu am modificat alt fișier decât acesta și nu am făcut commit.

## Metodă

- **Fișiere brute.** Am recitit `faza4/date/wp/new_p001.json.gz` … `new_p111.json.gz` cu un script propriu (Python, fără codul autorului). Am deduplicat pe slug și am numărat din nou fereastra și pragul. Expresiile din `faza4/date/wp/grupuri_expresii.txt` le-am aplicat pe textul asamblat din slug (cratime înlocuite cu spații), nume, etichete și descrierea scurtă, cu IGNORECASE.
- **Surse live.** `curl -sSL -A "Mozilla/5.0"` (cu `-g` la API-ul WordPress), cam o cerere pe secundă la apps.shopify.com. Nicio sursă nu a fost blocată în această verificare.
- **Shopify.** Data „Launched", ratingul și numărul de recenzii le-am citit din pagina aplicației (data din text, ratingul și numărul din blocul `aggregateRating`). Planurile le-am citit din secțiunea „Pricing". Numărul de aplicații al dezvoltatorului l-am citit de pe `/partners/<id>` (cardurile distincte și textul „N apps"; cele două au coincis peste tot).
- **Categoria „legal".** Am descărcat paginile 1-25 ale `/categories/store-management-security-legal/all?sort_by=newest` și am deschis ultima aplicație de pe mai multe pagini, apoi am căutat granița prin căutare binară în pagina 23.
- **Curbe.** Am recalculat din `faza4/date/shopify/recenzii/<handle>.json`: o recenzie intră la 30/60/90 de zile dacă (data recenziei − data lansării) < 30/60/90 de zile.
- **Citate.** Am deschis toate cele 55 de linkuri distincte din `SLABICIUNI.md` (52 Shopify, 3 WordPress.org). Am normalizat ghilimelele și spațiile, am scos traducerile dintre paranteze drepte, am împărțit citatul la „…" și am căutat fiecare bucată în textul paginii. Data am citit-o din prima dată de după „All reviews" (Shopify), respectiv din atributul `title` al postării care conține citatul (WordPress.org).

## Rezultat pe scurt

| Zonă | Afirmații verificate | Corespunde | Diferă | Blocat |
|---|---|---|---|---|
| 1. Totaluri WordPress | 6 | 6 | 0 | 0 |
| 2. Numitori grupuri WordPress | 8 | 6 | 2 (doar descrierea metodei) | 0 |
| 3. Prețuri WordPress | 5 | 5 | 0 | 0 |
| 4. Shopify B1 | 9 | 8 | 1 (un plan omis) | 0 |
| 5. Shopify, alte buzunare | 10 | 8 | 2 (planuri omise) | 0 |
| 6. Curbe | 9 | 9 | 0 | 0 |
| 7. Citate | 56 de rânduri | 54 | 2 (date WordPress.org) | 0 |
| 8. Changelog Shopify | 1 | 1 | 0 | 0 |
| 9. Curs BNR | 3 | 3 | 0 | 0 |

**Nicio diferență nu schimbă vreo cifră de rată, vreun clasament sau vreo concluzie.**

## 1. Totaluri WordPress

| Nr | Afirmație | Sursa redeschisă | Ce am găsit | Verdict |
|---|---|---|---|---|
| 1.1 | 27.519 pluginuri cu `added` ≥ 2024-11-16 | new_p001-111.json.gz | 27.750 sluguri unice în total, 27.519 în fereastră | corespunde |
| 1.2 | 268 cu `active_installs` ≥ 1.000 (0,97%) | idem | 268; 268/27.519 = 0,974% | corespunde |
| 1.3 | Pagina 111 coboară la 2024-10-27 | idem | cel mai vechi `added` din arhivă: 2024-10-27 | corespunde |
| 1.4 | add-from-server-reloaded: added 2025-12-10, 4.000 instalări, autor Adeel | API live `plugin_information` | 2025-12-10, 4.000, Adeel | corespunde |
| 1.5 | cowboy-mcp: 2026-07-03, 2.000, autor cu 1 plugin | API live + `request[author]=februality` | 2026-07-03, 2.000; autorul are 1 plugin (cowboy-mcp) | corespunde |
| 1.6 | advanced-ip-blocker: 2025-06-26, 3.000; diviops-agent: 2026-08-20, 1.000 | API live | identic | corespunde |

## 2. Numitorii grupurilor WordPress

| Nr | Afirmație | Sursa redeschisă | Ce am găsit | Verdict |
|---|---|---|---|---|
| 2.1 | WP-A: 248 lansate, 15 cu ≥1.000 | arhivă + grupuri_expresii.txt | 248 / 15, aceleași 15 sluguri ca în anexa PAS1 | corespunde |
| 2.2 | WP-B: 780, 8 | idem | 780 / 8, aceleași sluguri | corespunde |
| 2.3 | WP-C: 125, 5 | idem | **124** dacă iau etichetele doar ca nume afișate (cum spune textul). **125** dacă adaug și cheile etichetelor (slugurile lor). Diferența: `custom-connect-button-block-for-discord`. ≥1.000: 5 în ambele variante, aceleași 5 sluguri | diferă (doar descrierea metodei) |
| 2.4 | WP-E: 630, 8 | idem | **627** după descrierea literală, **630** cu cheile etichetelor și entitățile HTML decodate. Diferența: `prblem-sweep`, `serkify-clean-buddy`, `sjf-cleaner`. ≥1.000: 8 în ambele variante | diferă (doar descrierea metodei) |
| 2.5 | Ratele WP-A..WP-K din PAS1 | aritmetică | 5/248 = 2,0%; 3/780 = 0,4%; 4/125 = 3,2%; 5/630 = 0,8%; restul la fel | corespunde |
| 2.6 | WP-D 791/7, WP-F 610/14, WP-G 1.094/24, WP-H 2.473/36 | idem (verificare suplimentară) | identic | corespunde |
| 2.7 | WP-I 80/5, WP-J 225/6, WP-K 92/3 | idem | identic | corespunde |
| 2.8 | Ordinea câmpurilor nu contează | test propriu | Contează puțin: concatenarea poate face potriviri peste granița dintre câmpuri (WP-B dă 775 dacă câmpurile sunt căutate separat) | observație |

## 3. Prețuri WordPress

| Nr | Afirmație | Sursa redeschisă | Ce am găsit | Verdict |
|---|---|---|---|---|
| 3.1 | add-from-server-reloaded: 59 $/an (1 site), 79 $/an (3 site-uri) | elearningevolve.com/products/add-from-server-pro/ (200) | „Basic $59 /year", „Standard $79 /year, Up to 3 different WordPress sites" | corespunde |
| 3.2 | gr-widget: 4,75 $/lună anual (57 $/an), 5,99 $/lună lunar | grwidget.com/pricing (200) | „$5.99 / month $4.75 / month", „Billed $57.00/year" | corespunde |
| 3.3 | gutensuite-reviewkit: 9,99 / 39,99 / 79,99 $/an | reviewkit.gutensuite.net/pricing (200) | „$9.99 per year 1 site", „$39.99 per year 5 sites", „$79.99 per year Unlimited sites" | corespunde |
| 3.4 | opti-behavior: 89 €/an (1 site), 179 €/an (5) | optiuser.com/opti-behavior/pricing/ (200) | „€89 /year", „€179 /year · 5 sites" (există și Agency 299 €/an, 10 site-uri, nemenționat) | corespunde |
| 3.5 | diviops-agent: Pro de la 29 €/an, regulat 49 €/an | diviops.com (200) | „Pro Starter 1 site 49 €/year regular 29 € / year" | corespunde |

## 4. Shopify, buzunarul B1

Toate cele 7 pagini au răspuns 200. Numărul de recenzii e identic cu cel din tabel la toate 7 (nicio creștere azi).

| Nr | Afirmație (BUZUNARE.md, B1) | Sursa redeschisă | Ce am găsit | Verdict |
|---|---|---|---|---|
| 4.1 | eu-widerrufsbutton: 401layers UG, 2 aplicații; 2026-01-09; 2.324; 4,9; 9,99 $/lună sau 99,99 $/an; 29,99 $/lună | apps.shopify.com/eu-widerrufsbutton, /partners/quaternico | January 9, 2026; 2.324; 4,9; 9,99 $/lună, 99,99 $/an, 29,99 $/lună (299,99 $/an); dezvoltator „401layers UG (haftungsbeschraenkt)", 2 aplicații (eu-widerrufsbutton, gpsr) | corespunde |
| 4.2 | eu-withdrawal-form: BuschBytes, 2; 2026-03-11; 582; 4,8; 9 și 25 $/lună | /eu-withdrawal-form, /partners/jonas-busch-consulting | March 11, 2026; 582; 4,8; 9 $ și 25 $/lună; 2 aplicații (eu-withdrawal-form, bundlr) | corespunde |
| 4.3 | eu-widerruf-pro: ECOMBEAT, 3; 2026-05-07; 330; 5,0; 11,99 și 17,99 $/lună | /eu-widerruf-pro, /partners/andidemartini-shop | May 7, 2026; 330; 5,0; 11,99 și 17,99 $/lună; 3 aplicații (eu-widerruf-pro, ai-index-pro, store-credit-pro). **Observație:** aplicația se numește acum „Address Check & Withdrawal Pro" și se prezintă în primul rând ca verificare de adrese. Butonul de retragere e în planul gratuit, iar planurile plătite adaugă verificarea adreselor. Copia salvată de cercetare are deja același titlu. În cele 319 recenzii salvate, 44 pomenesc retragerea și 0 adresele | corespunde (cu observație) |
| 4.4 | wideruf-button: Anviara LLC, 1; 2026-05-06; 108; 4,8; 7,99 $/lună | /wideruf-button, /partners/anviara | May 6, 2026; 108; 4,8; 7,99 $/lună; 1 aplicație | corespunde |
| 4.5 | eu-widerrufsbutton-1: Visionz GmbH, 3; 2026-05-12; 51; 5,0; 5,99 și 24,99 $/lună | /eu-widerrufsbutton-1, /partners/visionz-harjes-sperlich-gbr1 | May 12, 2026; 51; 5,0; 5,99 $/lună (60 $/an), 24,99 $/lună (250 $/an); 3 aplicații | corespunde |
| 4.6 | eu-guarantee-warranty-label: Consentico, 3; 2026-08-26; 49; 5,0; 4,99 și 9,99 $/lună | /eu-guarantee-warranty-label, /partners/consentico | August 26, 2026; 49; 5,0; 3 aplicații. Planuri: Lite 4,99 $/lună, Pro 9,99 $/lună **și Business 24,99 $/lună (199 $/an)**. Planul Business apare și în copia salvată (`faza4/date/shopify/app/eu-guarantee-warranty-label.html.gz`) | diferă (plan omis) |
| 4.7 | eu-warranty-garan-label: Nico Münster et al., 2; 2026-08-05; 50; 5,0; 4,99 $/lună | /eu-warranty-garan-label, /partners/nico-muenster-roman-rau-jan-felix-school | August 5, 2026; 50; 5,0; 4,99 $/lună (49,90 $/an); 2 aplicații | corespunde |
| 4.8 | Categoria store-management-security-legal: 650 listate, 544 lansate după 2024-11-16 (PAS2) | paginile 1-25 ale `/all?sort_by=newest` + 13 pagini de aplicații | Contorul paginii: 650 de aplicații. Granița e în pagina 23: poziția 544 = isonomy-web-accessibility (lansată 2024-11-26), poziția 545 = verifyid-mitid-aldersbekraeft (2024-11-15). Datele de la capetele paginilor scad monoton (sidrenko 2026-10-28 … ea-accessibility 2025-05-19, age-verification-12 2024-08-15). **544** | corespunde |
| 4.9 | Vechiul lider: terms-and-conditions-checkbox (2019, 569 de recenzii) | /terms-and-conditions-checkbox | December 2, 2019; 569; 4,9 | corespunde |

Ratele și medianele din BUZUNARE.md le-am refăcut aritmetic: 7/189 = 3,7%; mediana la 90 de zile pentru B1 (27, 46, 48, 49, 79, 93, 289) = 49; B2 = 7,5; B7 = 3; B8 = 1; B5 = 2; B4 = 5. Toate corespund. Numitorul B1 (189) nu l-am renumărat.

## 5. Shopify, eșantion din alte buzunare

| Nr | Afirmație | Sursa redeschisă | Ce am găsit | Verdict |
|---|---|---|---|---|
| 5.1 | B2 kedra-ai-index (Kedra Apps): 2026-04-27; 50 rec., 4,9; 10 $/lună, 25 $/lună | /kedra-ai-index, /partners/tarsi-io | April 27, 2026; 50; 4,9; 10 $ și 25 $/lună **și 79 $/lună** (prezent și în copia salvată); 3 aplicații | diferă (plan omis) |
| 5.2 | B2 llms-txt-agent (Go Plus NZ): 2025-08-25; 47; 5,0; 7,95 și 14,95 $/lună | /llms-txt-agent, /partners/go-plus-nz | August 25, 2025; 47; 5,0; 7,95 și 14,95 $/lună; 3 aplicații (ai-blog-agent, llms-txt-agent, stockist-maps) | corespunde |
| 5.3 | B7 mida-fraud-ip-blocker (MIDA, 3): 2025-09-19; 580; 4,9; 9, 19, 39 $/lună | /mida-fraud-ip-blocker, /partners/mida-by-bss-commerce | September 19, 2025; 580; 4,9; 9/19/39 $/lună; 3 aplicații. **Observație:** contul de partener se numește „mida-by-bss-commerce". BSS Commerce e un dezvoltator cu multe aplicații, în alt cont. Nu am găsit contul lor (`/partners/bss-commerce` arată 0 aplicații), deci nu am putut număra | corespunde (cu observație) |
| 5.4 | B7 neo-cod-form-upsell-pixel-otp: 2026-05-15; 55; 6,99 $/lună | /neo-cod-form-upsell-pixel-otp, /partners/theneoapps | May 15, 2026; 55; 5,0; 6,99 $/lună **și 12,99 $/lună** (prezent și în copia salvată); 2 aplicații | diferă (plan omis) |
| 5.5 | B8 altera-import-export-excel (Abnoba LLC, 1): 2025-02-21; 268, 5,0; 15 $/lună | /altera-import-export-excel, /partners/getaltera | February 21, 2025; 268; 5,0; 15 $/lună; 1 aplicație | corespunde |
| 5.6 | B8 bulk-ai (AC App-Commerce UG): 2025-11-18; 33; 29-249 $/lună | /bulk-ai, /partners/alexander-hupfer | November 18, 2025; 33; 4,8; 29, 99, 249 $/lună; 3 aplicații | corespunde |
| 5.7 | B5 product-variant-options (Kefi Commerce): 2026-03-09; 46; 5 $/lună | /product-variant-options, /partners/kefi4 | March 9, 2026; 46; 5,0; 5 $/lună; 3 aplicații | corespunde |
| 5.8 | B5 scalechart (Scalechart LLC): 2026-01-01; 54; 29,99 $/lună | /scalechart, /partners/scalechart-llc | January 1, 2026; 54; 5,0; 29,99 $/lună (180 $/an); 3 aplicații | corespunde |
| 5.9 | B4 sectionheroes: 2025-12-12; 59; 22,9 $/lună | /sectionheroes, /partners/sectionheroes-app | December 12, 2025; 59; 5,0; 22,90 și 36,90 $/lună; 1 aplicație | corespunde |
| 5.10 | B4 ecombe-page-builder: 2026-01-28; 35; 14,99 $/lună | /ecombe-page-builder, /partners/ecombe | January 28, 2026; 35; 5,0; 14,99, 39,99, 79,99 $/lună; 2 aplicații | corespunde |

La 5.9 și 5.10 tabelele din BUZUNARE.md dau doar planul cel mai ieftin. La B4 asta e regula vizibilă a coloanei, deci nu le-am trecut ca diferențe.

## 6. Curbele de recenzii (B1)

| Nr | Aplicație | BUZUNARE.md (30/60/90; aug.-oct.) | Recalculat din recenzii/<handle>.json | Verdict |
|---|---|---|---|---|
| 6.1 | eu-widerrufsbutton | 5 / 15 / 27; 76 | 5 / 15 / 27; 76 (2.300 recenzii parsate) | corespunde |
| 6.2 | eu-withdrawal-form | 22 / 49 / 79; 92 | 22 / 49 / 79; 92 | corespunde |
| 6.3 | eu-widerruf-pro | 85 / 261 / 289; 35 | 85 / 261 / 289; 35 | corespunde |
| 6.4 | wideruf-button | 14 / 91 / 93; 13 | 14 / 91 / 93; 13 | corespunde |
| 6.5 | eu-widerrufsbutton-1 | 21 / 45 / 48; 2 | 21 / 45 / 48; 2 | corespunde |
| 6.6 | eu-guarantee-warranty-label | 19 / 48 / 49; 49 | 19 / 48 / 49; 49 | corespunde |
| 6.7 | eu-warranty-garan-label | 0 / 40 / 46; 46 | 0 / 40 / 46; 46 | corespunde |
| 6.8 | Recenzii parsate față de live: eu-widerrufsbutton | 2.324 live | 2.300 parsate (99,0%), fără duplicate | corespunde |
| 6.9 | Recenzii parsate față de live: eu-widerruf-pro | 330 live | 319 parsate (96,7%), fără duplicate | corespunde |

Notă de metodă: cifrele ies doar cu „< N zile". Cu „≤ N zile" câteva cresc cu 1-4 (de ex. eu-guarantee-warranty-label 23 / 48 / 49). Regula „< N" e cea folosită și ar fi bine să fie scrisă în BUZUNARE.md. Pentru cele 10 aplicații din eșantionul de la punctul 5, valorile din `curbe_recenzii.json` sunt identice cu cele din BUZUNARE.md.

## 7. Citate (SLABICIUNI.md)

Am deschis toate cele 55 de linkuri distincte (56 de rânduri; recenzia 2241217 e folosită de două ori). Toate au răspuns 200. Fiecare citat apare cuvânt cu cuvânt în pagina lui, iar aplicația din titlul paginii e cea din tabel.

| Nr | Buzunar | Rânduri verificate | Citat găsit | Data | Verdict |
|---|---|---|---|---|---|
| 7.1 | B1 (Shopify) | 12: 2370644, 2256904, 2252470, 2261117, 2220411, 2327985, 2279804, 2245033, 2242175, 2241566, 2274392, 2291682 | 12/12 | 12/12 identice. La 2327985 magazinul e din „Romania", cum scrie | corespunde |
| 7.2 | B1 (WordPress.org) | almost-unusable-none-of-the-entered-values… | da, în prima postare (imagophilos) | **diferă:** postarea cu citatul e din „August 22, 2026 at 2:12 pm". Data 2026-08-24 e a răspunsului dezvoltatorului (Dennis) | diferă |
| 7.3 | B2 (Shopify) | 8: 2132221, 2130722, 2205524, 2168499, 2366373, 2107068, 2017833, 2202554 | 8/8 | 8/8 identice | corespunde |
| 7.4 | B2 (WordPress.org) | pointless-24 | da, în prima postare (rosterdotcom) | **diferă:** postarea e din „August 1, 2026 at 6:16 pm". Data 2026-08-02 e a răspunsului (nivso) | diferă |
| 7.5 | B7 (Shopify) | 8: 2104538, 2181936, 2229142, 2015619, 2027430, 2102088, 2222047, 2404252 | 8/8 | 8/8 identice | corespunde |
| 7.6 | B7 (WordPress.org) | t-locked-me-out-of-my-admin-panel | da, în prima postare (truden) | March 10, 2026 = 2026-03-10 | corespunde |
| 7.7 | B8 | 9: 2337848, 2225395, 2257527, 2150840, 2205879, 2203626, 2071703, 2122975, 2108094 | 9/9 | 9/9 identice | corespunde |
| 7.8 | B5 | 8 rânduri, 7 linkuri: 2003723, 2169664, 2109243, 2241217 (×2), 2204855, 1997827, 2394809 | 8/8 | 8/8 identice | corespunde |
| 7.9 | B4 | 8: 2338753, 2071170, 2200188, 2304100, 2173838, 1985259, 2323853, 2096300 | 8/8 | 8/8 identice | corespunde |

## 8. Changelog Shopify (B1)

| Nr | Afirmație | Sursa redeschisă | Ce am găsit | Verdict |
|---|---|---|---|---|
| 8.1 | 18 iunie: „Set cancellation rules for buyers … to enable EU-specific policies in response to changing right of withdrawal regulations" | `faza4/date/platforma/shopify_changelog_withdrawal.html` și live `https://changelog.shopify.com/?search=withdrawal` (200) | În ambele: „June 18 · Self-serve returns now support cancellations · Set cancellation rules for buyers, alongside your return rules - both now configurable per market - to enable EU-specific policies in response to changing right of withdrawal regulations. · Customer accounts". Anul 2026 l-am confirmat pe pagina postării (`/posts/self-serve-returns-now-support-cancellations`: „June 18, 2026") | corespunde |

## 9. Cursul BNR

| Nr | Afirmație | Sursa redeschisă | Ce am găsit | Verdict |
|---|---|---|---|---|
| 9.1 | 1 USD = 4,8428 lei, 13.11.2026 | https://curs.bnr.ro/nbrfxrates.xml | PublishingDate 2026-11-13, USD 4.8428 | corespunde |
| 9.2 | 1 EUR = 5,3498 lei | idem | EUR 5.3498 | corespunde |
| 9.3 | 0,0589 lei/₽ (fz-152-rf: 1.990 ₽ ≈ 117 lei) | idem | RUB 0.0589; 1.990 × 0,0589 = 117,21 | corespunde |

## Corecții necesare

1. **SLABICIUNI.md, secțiunea B1**, rândul „Nu verifică datele comenzii (WooCommerce)", coloana Data: `2026-08-24` → `2026-08-22`.
2. **SLABICIUNI.md, secțiunea B2**, rândul „Se poate face fără aplicație" (lovedbyai), coloana Data: `2026-08-02` → `2026-08-01`.
3. **BUZUNARE.md, tabelul B1**, rândul eu-guarantee-warranty-label, coloana Preț: `4,99 $ și 9,99 $/lună` → `4,99 $, 9,99 $ și 24,99 $/lună`.
4. **BUZUNARE.md, tabelul B2**, rândul kedra-ai-index, coloana Preț: `10 $/lună, 25 $/lună` → `10 $/lună, 25 $/lună, 79 $/lună`.
5. **BUZUNARE.md, tabelul B7**, rândul neo-cod-form-upsell-pixel-otp, coloana Preț: `6,99 $/lună` → `6,99 $ și 12,99 $/lună`.
6. **PAS1_WORDPRESS.md, „Limite de măsură", punctul 4** și **faza4/date/wp/grupuri_expresii.txt**, prima linie: după „etichete" să se precizeze „(atât slugul etichetei, cât și numele ei afișat; entitățile HTML decodate)". Fără precizare, WP-C dă 124 în loc de 125 și WP-E 627 în loc de 630. Numărătorii (≥1.000) nu se schimbă.
7. **BUZUNARE.md, paragraful „Curbele primelor 90 de zile"**, punctul Shopify: de adăugat „o recenzie intră în primele N zile dacă a fost scrisă la mai puțin de N zile de la lansare (< N)".
8. Opțional, **BUZUNARE.md, B1**, după tabel: o notă că eu-widerruf-pro se prezintă acum ca „Address Check & Withdrawal Pro". Butonul de retragere e în planul gratuit, iar planurile plătite vând verificarea adreselor. Recenziile salvate vorbesc doar despre retragere.
9. Opțional, **BUZUNARE.md, B7**: o notă că mida-fraud-ip-blocker vine de la un cont „MIDA by BSS Commerce", deci poate fi o firmă mare care trece pragul de 3 aplicații ca Judge.me sau Trustpilot. Nu am putut număra aplicațiile BSS Commerce.

## Ce nu am putut verifica

- Numitorii buzunarelor Shopify (189 la B1, 700 la B2 etc.). Nu i-am renumărat. Am verificat doar numitorul de categorie „legal" (544).
- Numărul total de aplicații Shopify în fereastră (20.755) și pașii 451 / 302 / 182. Ar fi cerut parcurgerea celor 122 de categorii.
- Numărul de aplicații al BSS Commerce (vezi corecția 9).
- Datele firelor WordPress.org nerezolvate (website-llms-txt, 16 fire). Nu au fost în lista de verificat.
- Descărcările WordPress (curbele la 30/60/90 de zile) și prețurile WordPress din afara celor 5 pagini cerute.
