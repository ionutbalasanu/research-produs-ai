# Faza 5: verificare independentă (PRECEDENTE.md și CALENDAR.md)

Data verificării: 2026-11-16. Toate sursele au fost redeschise azi de verificator. Fișierele descărcate sunt în `/tmp/claude-0/verif/` (în afara repo-ului). Nimic din memorie la date legale.

Verdicte: **confirmat**; **corectat** (valoarea corectă + sursa); **neverificabil** (motivul).

---

## A. Datele legale (text oficial, prin Cellar și legislation.gov.uk)

EUR-Lex nu a fost folosit (provocare WAF). Textele au fost redescărcate cu `faza5/scripts/cellar.sh` și citite cu `text.py`.

| Afirmație | Sursă redeschisă | Verdict |
|---|---|---|
| GPSR, art. 52: „It shall apply from 13 December 2024." | Cellar 32023R0988 | confirmat |
| EAA, art. 31 alin. (2): „They shall apply those measures from 28 June 2025"; art. 2 alin. (2): servicii „provided to consumers after 28 June 2025" | Cellar 32019L0882 | confirmat |
| Buton de retragere, art. 2 alin. (1): transpunere „by 19 December 2025", aplicare „from 19 June 2026" | Cellar 32023L2673 | confirmat |
| 2024/825, art. 4 alin. (1): „By 27 March 2026 … from 27 September 2026"; art. 22a (acte de punere în aplicare „By 27 September 2025", alin. 2 și 4); considerentul 28: „directly next to the picture of the good in the case of online sale" și „placed as a general reminder on the website" | Cellar 32024L0825 | confirmat |
| CRA, art. 71 alin. (2): aplicare de la 11.12.2027; art. 14 de la 11.09.2026; capitolul IV de la 11.06.2026 | Cellar 32024R2847 | confirmat |
| CRA, art. 13 alin. (19): textul citat (luna și anul sfârșitului perioadei de suport, „at the time of purchase") | Cellar 32024R2847 | confirmat |
| CRA, art. 20 alin. (2) lit. (b): distribuitorul verifică respectarea art. 13 alin. (15), (16), (18), (19), (20) | Cellar 32024R2847 | confirmat |
| CRA, art. 64 alin. (2): până la 15.000.000 EUR sau 2,5% din cifra de afaceri mondială („whichever is higher") pentru art. 13 | Cellar 32024R2847 | confirmat |
| CRA: „Fără excepție pentru microîntreprinderi la această obligație" | Cellar 32024R2847, art. 64 alin. (10) lit. (a): scutirea de amenzi a micro- și micilor întreprinderi privește doar termenele de notificare din art. 14 | confirmat |
| CRA, art. 69: se aplică doar produselor introduse pe piață după 11.12.2027 | Cellar 32024R2847, art. 69 alin. (2): produsele introduse înainte intră sub regulament doar dacă suferă o „substantial modification" după acea dată | confirmat (cu nuanța modificării substanțiale, care merită o jumătate de frază în CALENDAR) |
| 2025/2439, art. 1 lit. (c) inserează alin. 3a: „Article 1, points (14), (15)(c), (26) and (27), points (2) and (3) of Annex I and point (2) of Annex II shall apply from 1 January 2028"; JO 3.12.2025 | Cellar 32025R2439 | confirmat. În plus, lit. (f) adaugă alin. 6: până la 31.12.2027 se poate aplica deja, opțional, regimul nou |
| 2024/2865: punctul (27) inserează art. 48a; textul „When substances or mixtures are placed on the market through distance sales, the offer shall clearly and visibly indicate the label elements referred to in Article 17." | Cellar 32024R2865 | confirmat. Data inițială a punctului (27) era 1.07.2026 (art. 2 alin. 2 original), confirmat |
| UK, Tobacco and Vapes Act 2026, s.175(3): s.1, 2, 5, 6 etc. intră în vigoare la 1.1.2027 | legislation.gov.uk/ukpga/2026/18/section/175 | confirmat |
| UK, s.1: infracțiune vânzarea către „born on or after 1 January 2009"; amendă de nivel 4; SI 2026/996 „Coming into force 1st January 2027" | legislation.gov.uk, s.1 și uksi/2026/996/made | confirmat. Nuanță: s.1 se întinde doar pe Anglia și Țara Galilor (E+W); Scoția și Irlanda de Nord au secțiunile proprii (s.52, s.72-73), tot din 1.1.2027 prin s.175(3)(b)-(c). „UK" e corect ca ansamblu |
| UK, abonamente DMCCA (Partea 4, Capitolul 2): fără regulament de commencement | legislation.gov.uk: s.254, 257, 259 marcate „prospective"; lista SI-urilor DMCCA are doar Commencement No. 1 (2024/1226), No. 2 (2025/272), No. 3 (2026/284, Capitolul 4, ADR) și amendamentul 2026/1040 (doar prelungește tranziția ADR la 7.01.2027) | confirmat |
| Omnibus VI (2025/0531(COD)): text agreat 26.06.2026 (scrisoarea Coreper GEDA/A/(2026)004193), votat de PE 22.10.2026 (T10-0362/2026), „Awaiting Council's 1st reading position" | oeil.europarl.europa.eu, fișa procedurii | confirmat |
| Rezumatul poziției PE restrânge art. 48a la vânzările „for the general public" | oeil, document-summary?id=1920911 (datat 22/10/2026) | confirmat (rezumat, nu text, deci rămâne „doar fragment"). Rezumatul nu conține date de aplicare, deci mutarea la 2030 rămâne **neverificabilă** din surse oficiale |

---

## B. Shopify: pagini live, recenzii, numărători

Ritm: cel mult o cerere la 1,2 secunde către apps.shopify.com.

### B1. Paginile aplicațiilor (live, 2026-11-16)

| Aplicație | Lansată (live) | Recenzii (live) | Prețuri (live) | Față de PRECEDENTE.md | Verdict |
|---|---|---|---|---|---|
| eu-widerrufsbutton | 9.01.2026 | 2.324, rating 4,9 | gratuit; 9,99 $/lună sau 99,99 $/an; 29,99 $/lună sau 299,99 $/an | la fel | confirmat |
| eu-withdrawal-form | 11.03.2026 | 582, 4,8 | gratuit; 9 $/lună sau 90 $/an; 25 $/lună sau 250 $/an | la fel | confirmat |
| sea-accessibility-ada-wcag | 8.01.2025 | 331, 5,0 | gratuit; 9, 14, 19 $/lună | la fel | confirmat |
| gpsr | 17.09.2024 | 29, **rating 4,9** | gratuit; 15 $/lună sau 149 $/an; 29 $/lună sau 299 $/an | PRECEDENTE scrie „rating 4,8" | **corectat**: 4,9 (https://apps.shopify.com/gpsr; și `candidati_grupe.json` are 4,9) |
| eu-warranty-garan-label | 5.08.2026 | 50, 5,0 | gratuit; 4,99 $/lună sau 49,90 $/an | la fel | confirmat |
| eu-widerruf-pro (la alegere) | 7.05.2026 | 330, 5,0 | gratuit; 11,99 și 17,99 $/lună | la fel | confirmat |
| widerruf-app (la alegere) | 15.05.2026 | 10, 5,0 | gratuit; 12 $/lună sau 120 $/an | **lipsește din grupul de retragere** (vezi B3) | corectat |

Dezvoltatorul 401layers (pagina de partener `apps.shopify.com/partners/quaternico`) are 2 aplicații: `gpsr` și `eu-widerrufsbutton`. **confirmat**. Sitemapul `sitemap_apps_en.xml` are 30.532 de handle-uri, din care 11 încep cu `avada-`. **confirmat**

### B2. Eșantion de pagini de recenzii comparate cu `faza5/date/shopify/recenzii/<handle>.json`

| Pagină | Rezultat | Verdict |
|---|---|---|
| eu-widerrufsbutton/reviews?page=1 | 10/10 recenzii găsite în JSON, aceleași date | confirmat |
| eu-widerrufsbutton/reviews?page=150 | 10/10 | confirmat |
| eu-withdrawal-form/reviews?page=20 | 10/10 | confirmat |
| sea-accessibility-ada-wcag/reviews?page=10 | 10/10 | confirmat |
| gpsr/reviews?page=2 | 10/10 | confirmat |

### B3. Numărători și metoda de încadrare (`faza5/scripts/valuri.py`)

| Afirmație | Recalculare | Verdict |
|---|---|---|
| Buton: total lunar 2025-12..2026-11 = 0, 6, 13, 30, 37, 324, 2.788, 176, 137, 104, 67, 34 (25 de aplicații) | recalculat direct din cele 25 de fișiere JSON: identic | confirmat (cu metoda autorilor) |
| eu-widerrufsbutton: 1.947 în iunie 2026, 81 în aug.-oct. | identic | confirmat |
| EAA (vârf 42), Avada 32 în iunie 2025, 128 în aug.-oct. 2026 (Avada 33); GPSR (vârf 9); garanție (147 în sept., 199 în aug.-oct.) | identic | confirmat |
| „44 listate înainte au 3.696 de recenzii; 75 listate după au 68" | identic cu regulile din `valuri.py` | confirmat ca aritmetică, **corectat** ca valoare (vezi rândul următor) |
| Încadrarea pe grupuri | **Eroare în `valuri.py`:** în regex-ul de excludere `EXCL`, termenul `RMA` cu `re.I` prinde orice cuvânt care conține „rma": *confirmation*, *Germany*, *Conforma*, *Clearmark*, *information*. 13 aplicații corecte au fost scoase: la retragere `widerruf-app` (Maiko, 10 recenzii, lansată 15.05.2026), `widerruf-button` (3, 20.02.2026), `eu-withdrawal-by-heartcoding` (3, 8.07.2026), `consentico-withdrawal`, `cancellation-button-info`, `retractation-ue`, `recesso-digitale-eu`, `withdrawal-form` (0); la GPSR `blockio-gpsr-guard`, `gpsr-shield` (0); la EAA `testamur`, `conforma` (0); la garanție `eu-guarantee-notice-garan` (1). În plus, termenul `claims` scoate `eu-green-claims-guarantees` („EU Green Claims & GARAN Label", 5 recenzii, lansată 14.08.2026), care e o aplicație GARAN, iar `alt text` scoate `accessora` (widget de accesibilitate, 5 recenzii). | **corectat**. Valori corectate (doar eroarea `RMA`): retragere 126 de aplicații, **46 înainte cu 3.709 recenzii, 80 după cu 71**; iunie 2026 **2.792**, octombrie 2026 **72** (se adaugă `widerruf-app`: 4 în iunie, 5 în octombrie, 1 în noiembrie); GPSR 58 de aplicații (57 după, 4 recenzii); EAA 105 (78 după, 14); garanție 78 (27 după, 19). Cu `eu-green-claims-guarantees`, garanția are 52 de recenzii în octombrie. **Nicio concluzie nu se schimbă.** Sursa: `candidati_grupe.json`, fișierele JSON de recenzii, paginile live |
| 65,2% Germania, 5,2% Austria, 4,5% Franța din 3.451 de recenzii (7 aplicații, faza 4) | recalculat din `faza4/date/shopify/recenzii/*.json`, câmpul `meta[0]`: 2.250 / 181 / 156 din 3.451 | confirmat |
| „~19 ori" (2.788/147) și „~66 de ori" (2.788/42); „70% din recenziile lunii" (1.947/2.788 = 69,8%) | aritmetică | confirmat |
| Zile față de termen: −161, −100, −43, −44, −16, −87, −171, −53, −32, −95, −67 | recalculate din datele „Launched" | confirmat |

---

## C. WordPress.org

| Afirmație | Sursă redeschisă | Verdict |
|---|---|---|
| OneTap, descărcări 2024-12..2025-12: 142, 230, 543, 1.030, 2.346, 3.595, 6.586, 11.193, 4.850, 10.216, 12.346, 30.131, 18.299 | `stats/plugin/1.0/downloads.php?slug=accessibility-onetap&limit=730` (serie 17.11.2024-15.11.2026) | confirmat |
| OneTap, ultimele trei luni 56.145 | aug. 20.603 + sept. 26.591 + oct. 8.951 | confirmat. Observație: 2026 oscilează puternic (iulie 46.915, octombrie 8.951), deci „creșterea continuă" e adevărată pentru 2025, nu pentru ultimele luni |
| OneTap: 60.000 de instalări, adăugat 12.11.2024 | `plugins/info/1.2` | confirmat |
| Autorul OneTap are 1 plugin | `plugins/info/1.2/?action=query_plugins&request[author]=wponetap`: 1 rezultat | confirmat |
| eu-order-withdrawal-button-for-woocommerce, martie-noiembrie 2026: 161, 550, 1.577, 10.028, 5.622, 9.434, 6.325, 9.513, 4.906; aug.-oct. 25.272 | `downloads.php?slug=eu-order-withdrawal-button-for-woocommerce&limit=730` | confirmat |
| același plugin: 6.000 de instalări, adăugat 26.03.2026, vendidero cu 7 pluginuri | `plugins/info/1.2` și `query_plugins&request[author]=vendidero` (7) | confirmat |
| Germanized: 70.000 de instalări | `plugins/info/1.2`, slug woocommerce-germanized | confirmat |

---

## D. Platforma

| Afirmație | Sursă redeschisă | Verdict |
|---|---|---|
| Feed-ul are 1.660 de intrări | https://changelog.shopify.com/feed.xml | confirmat |
| 18.06.2026 „Self-serve returns now support cancellations", cu fraza „This enables merchants selling in the EU to offer a withdrawal policy" | feed, Thu 18 Jun 2026 09:30 -0400 | confirmat |
| 16.07.2026 Managed Markets acceptă cereri de anulare și retur în UE | feed, „Shopify Managed Markets now supports EU buyer cancellation and return requests" | confirmat |
| 10.11.2026: reguli de retur și anulare pe piață; variabile Liquid noi pentru ora cererii | feed, două intrări din 10 Nov 2026 (`return.requested_at`, `requested_edit.requested_at`) | confirmat |
| 17.06.2026 câmpul „disclosures" (Prop 65, choking hazard, tipuri personalizate) | feed, „Product listings now support a disclosures field" | confirmat |
| Nicio intrare GPSR, EAA, etichetă de garanție | căutare în titluri și descrieri după GPSR, product safety, accessib, EAA, WCAG, guarantee, warranty, GARAN: niciun rezultat despre aceste obligații. Singura intrare apropiată: 17.07.2025 „Image ALT text can now be translated" (accesibilitate generală, fără EAA) | confirmat |
| Germanized 3.18.0 (GPSR) 26.09.2024, −78; 4.0.0 (buton) 26.03.2026, −85; 4.1.0 (GARAN) 27.08.2026, −31 | antet `last-modified` pe `plugins.svn.wordpress.org/woocommerce-germanized/tags/<ver>/readme.txt`: 26.09.2024, 26.03.2026, 27.08.2026; changelog-urile din readme conțin exact liniile citate | confirmat |
| Metoda (data ultimei modificări a readme-ului din etichetă) | Etichetele de corecție următoare au date imediat după: 3.18.1 pe 26.09.2024, 4.0.1 pe 27.03.2026, 4.1.1 pe 28.08.2026. Secvența e coerentă cu o lansare în ziua etichetei | confirmat ca rezonabilă; rămâne marcată „dedus" |

---

## E. Pasul 3 (CRA și CLP pe Shopify)

Căutare fără căutarea din magazin: handle-urile din `sitemap_apps_en.xml` (30.532) filtrate după cra, cyber, clp, hazard, ghs, sds, warning, prop65, disclosure, dpp, product-safety etc., plus paginile GPSR deja salvate în `faza5/date/shopify/app/` (scanate după CLP, GHS, pictogram, signal word, Cyber Resilience, support period), plus două căutări web. 30 de pagini redeschise live.

| Afirmație | Sursă redeschisă | Verdict |
|---|---|---|
| gpsr-clp-hazard-labels: voidroot GmbH, 10.07.2026, 1 recenzie, gratuit până la 5 produse, 9,99 $/lună sau 99 $/an | pagina live | confirmat |
| clp-hazard-info-display (CLPLens): momiji-shop, 10.07.2026, 0 recenzii, „plan gratuit" | pagina live: gratuit (5 produse, doar previzualizare), **Starter 19 $/lună sau 190 $/an, Growth 39 $/lună sau 390 $/an, 79 $/lună sau 790 $/an** | **corectat**: preț „gratuit; 19, 39, 79 $/lună" |
| gpsr-compliance-2: Shark Tech systems, 25.08.2026, 0 recenzii, 9,99 $/lună | pagina live | confirmat |
| CLP: „3 aplicații Shopify cu 0-1 recenzii", „valul nu a început" | **GCM / gpsr (401layers, 29 de recenzii, liderul GPSR și firma care a câștigat valul butonului) oferă deja în planul Basic „FULL GHS Hazard/Safety Statements Set" și „Safety & Hazard Information"** (https://apps.shopify.com/gpsr). Alte aplicații cu pictograme de pericol, toate cu 0 recenzii: conformica-gpsr (11.06.2026), meetanshi-eu-gpsr-compliance (5.05.2026), eu-compliance-kit-1 (19.10.2026), sds-manager-app (GHS, 15.09.2025) | **corectat**: valul (recenzii) nu a început, dar terenul nu e gol: cel puțin 7 aplicații afișează elemente CLP/GHS, iar una are recenzii și un autor dovedit |
| CRA: „Singura aplicație CRA, craledger-duty-records (0 recenzii)" | pagina live confirmă craledger (9.07.2026, 0). În plus: **complyo** (lansată 22.05.2026, 0 recenzii, scaner „EU AI Act and CRA", 29 $/lună Pro) și **eu-compliance-kit-1** (19.10.2026, 0 recenzii), care listează „software updates" printre informațiile afișate pe pagina produsului | **corectat**: 3 aplicații care menționează CRA sau actualizările software; niciuna nu afișează explicit perioada de suport CRA și niciuna nu are recenzii. Concluzia „neînceput" rămâne |
| Alte aplicații de avertizări (product-warnings 238 de recenzii, alertify-product-warnings 19, advanced-product-warning 6, k-warnings 2 etc.) | pagini live | fără mențiuni CLP, GHS sau CRA. Nu schimbă nimic |
| Căutările web | O căutare web a raportat 2.172 de recenzii pentru CLPLens și 91 pentru SDS App; paginile live arată 0 și 0 | rezumatele căutării web sunt greșite; s-au folosit doar paginile live |

---

## F. Afirmații nesusținute sau concluzii care nu decurg din cifre

| Afirmație | Problema | Verdict |
|---|---|---|
| PRECEDENTE, concluzia 3: „câștigătorii mici s-au listat cu 1,5-5,5 luni înainte (−32 până la −171 de zile)" | −171 e Avada, pe care chiar textul o declară firmă mare. Câștigătorii mici: −32 până la −161 (1-5,3 luni). În plus, nou-venitul mic accessify-web-accessibility s-a listat cu −1 zi și are 45 de recenzii (venite însă în 2026) | **corectat**: „−32 până la −161 de zile (1-5,3 luni)" |
| PRECEDENTE, concluzia 3: „Aplicațiile listate cu 2-6 săptămâni înainte au prins totuși 50-330 de recenzii" | Selectiv. Din cele 16 aplicații de retragere listate între −42 și −14 zile, doar 2 au cel puțin 50 de recenzii (eu-widerrufsbutton-1: 51; eu-withdrawal-button-form: 76); restul au 0-16. 330 și 108 sunt la −43 și −44 de zile (peste 6 săptămâni) | **corectat**: „Din aplicațiile listate cu 2-6 săptămâni înainte, 2 din 16 au trecut de 50 de recenzii; restul au 0-16. Cele cu 330 și 108 s-au listat la ~6 săptămâni." Întărește regula de 3 luni, nu o slăbește |
| PRECEDENTE, „Ce înseamnă", punctul 5: „După val rămâne 3-11% din ritmul lunii termenului" | Amestecă o lună cu o sumă pe trei luni. Ritmul lunar după val: august 137 (4,9%), septembrie 104 (3,7%), octombrie 67 (2,4%). 11% e suma aug.-oct. raportată la o singură lună | **corectat**: „2-5% pe lună (octombrie: 2,4%)" |
| PRECEDENTE, „Ce înseamnă", punctul 4: „plan gratuit + 5-12 $/lună. Doar GPSR (15-29 $) și accesibilitatea (9-39 $) au urcat mai sus" | Liderii butonului au și planuri de 22-30 $/lună (eu-widerrufsbutton 29,99 $; eu-withdrawal-form 25 $; Nayvo 22 $) | **corectat**: „planul de intrare 5-12 $/lună; liderii butonului au și un plan de 22-30 $/lună" |
| PRECEDENTE, concluzia 2: „La toate cele patru valuri, aplicațiile listate după termen au împreună sub 70 de recenzii" | Formularea sună a total pe patru valuri (4 + 14 + 68 + 18 = 104). E adevărat doar pe fiecare val; cu corecția din B3, butonul are 71 | **corectat**: „La fiecare val, aplicațiile listate după termen au împreună cel mult ~70 de recenzii" |
| PRECEDENTE, secțiunea 2, OneTap: „Creșterea continuă după termen" | Adevărat pentru 2025. În 2026 seria oscilează (iulie 46.915, octombrie 8.951) | confirmat pentru 2025; de adăugat „în 2025" |
| PRECEDENTE, concluzia 5 („Germania a fost motorul", „două treimi din valul butonului") | 65,2% e calculat pe 7 aplicații, din care 2 de garanție (99 de recenzii din 3.451). Efectul e neglijabil | confirmat |
| CALENDAR, C2: „Valul nu a început … 3 aplicații" | Vezi E: liderul GPSR afișează deja frazele GHS. Pentru o aplicație nouă, riscul nu e lipsa cererii, ci că 401layers (câștigătorul butonului) are deja baza instalată și funcția | **corectat** (schimbă nuanța lui C2, nu verdictul „trece criteriile") |
| CALENDAR, C1: „nicio aplicație de afișare pe Shopify sau WordPress" | Shopify: complyo și eu-compliance-kit-1 (0 recenzii) ating subiectul (vezi E), niciuna nu afișează explicit perioada de suport | confirmat în esență, de adăugat cele două |
| CALENDAR, C3: „UK" | s.1 e E+W; Scoția și Irlanda de Nord prin s.52 și s.72-73, aceeași dată | confirmat, nuanță opțională |

---

## Corecții de aplicat

1. **`faza5/scripts/valuri.py`**: în `EXCL`, înlocuiește `RMA` (prins cu `re.I` în *confirmation*, *Germany*, *Conforma*, *Clearmark*) cu `\bRMA\b` fără ignorarea majusculelor (sau scoate-l din `EXCL` și testează separat). Reconsideră `claims` (scoate `eu-green-claims-guarantees`, aplicație GARAN) și `alt text` (scoate `accessora`, widget de accesibilitate). Apoi rulează din nou scriptul și regenerează `faza5/date/shopify/valuri_shopify.json`.
2. **`faza5/PRECEDENTE.md`, tabelul „Pe scurt" și secțiunea 3**: retragere 126 de aplicații, 46 înainte (3.709 recenzii), 80 după (71); iunie 2026 2.792, octombrie 72, noiembrie 35; „Din care" și liderul rămân la fel. GPSR: 58 de aplicații, 57 după. EAA: 105, 78 după. Garanție: 78, 27 după cu 19 recenzii (octombrie 52 dacă se include `eu-green-claims-guarantees`). Raportul „~19 ori" și „~66 de ori" rămân practic aceleași.
3. **`faza5/PRECEDENTE.md`, concluzia 2**: „La fiecare val, aplicațiile listate după termen au împreună cel mult ~70 de recenzii"; „46 listate înainte au 3.709; 80 listate după au 71".
4. **`faza5/PRECEDENTE.md`, concluzia 3**: intervalul câștigătorilor mici devine „−32 până la −161 de zile (1-5,3 luni)"; fraza „2-6 săptămâni … 50-330" devine „din 16 aplicații listate cu 2-6 săptămâni înainte, doar 2 au trecut de 50 de recenzii (51 și 76); cele cu 330 și 108 s-au listat la ~6 săptămâni".
5. **`faza5/PRECEDENTE.md`, secțiunea 1**: rating GCM 4,9, nu 4,8.
6. **`faza5/PRECEDENTE.md`, „Ce înseamnă", punctul 4**: adaugă planurile de 22-30 $/lună ale liderilor butonului.
7. **`faza5/PRECEDENTE.md`, „Ce înseamnă", punctul 5**: „2-5% pe lună (octombrie: 2,4%)" în loc de „3-11%".
8. **`faza5/PRECEDENTE.md`, secțiunea 2, OneTap**: „Creșterea continuă după termen, în 2025"; în 2026 seria oscilează.
9. **`faza5/CALENDAR.md`, C2, tabelul de stare**: prețul CLPLens „gratuit; 19, 39, 79 $/lună". Adaugă că GCM / gpsr (401layers, 29 de recenzii) oferă deja „FULL GHS Hazard/Safety Statements Set" și că alte 4 aplicații (conformica-gpsr, meetanshi-eu-gpsr-compliance, eu-compliance-kit-1, sds-manager-app) afișează pictograme de pericol, toate cu 0 recenzii. Rezumatul din tabelul „Rezultat" devine „neînceput ca val; funcția există deja la liderul GPSR".
10. **`faza5/CALENDAR.md`, C1, starea de azi**: „Singura aplicație CRA" devine „trei aplicații ating CRA: craledger-duty-records (evidențe), complyo (scaner, 22.05.2026), eu-compliance-kit-1 (listează „software updates", 19.10.2026), toate cu 0 recenzii; niciuna nu afișează explicit perioada de suport". Opțional: la art. 69, „cu excepția celor modificate substanțial după 11.12.2027".
11. **`faza5/CALENDAR.md`, C3** (opțional): s.1 acoperă Anglia și Țara Galilor; Scoția și Irlanda de Nord prin s.52 și s.72-73, aceeași dată.

**Schimbă vreo corecție o concluzie?** Nu, la pasul 1: valul butonului rămâne singurul mare, listarea după termen rămâne fără recenzii, iar corecția de la punctul 4 întărește regula „cel târziu cu 3 luni înainte". La pasul 3, corecția 9 schimbă nuanța lui C2: CLP nu e un teren gol, pentru că liderul GPSR (aceeași firmă care a luat 70% din valul butonului) afișează deja frazele GHS. C2 trece în continuare criteriile, dar avantajul unui nou-venit e mai mic decât sugerează „neînceput".
