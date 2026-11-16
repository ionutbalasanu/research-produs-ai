# Faza 4, pasul 6: propuneri

Data: 2026-11-16. Curs BNR 13.11.2026: 1 USD = 4,8428 lei (faza4/date/bnr_nbrfxrates.xml).

## Verdict

**2 propuneri susținute de date și 1 propunere slabă, păstrată cu rezerve. Toate trei sunt pe Shopify App Store.** Pe WordPress.org nu a ieșit nicio propunere. Motivul: nou-veniții mici care trec de 1.000 de instalări sunt în majoritate gratuiți, iar WordPress.org nu arată vânzări. Niciun grup WordPress nu are 3 autori mici cu preț citit care să rezolve aceeași problemă (PAS1_WORDPRESS.md, BUZUNARE.md).

| Ordine | Propunere | Buzunar | Tăria dovezii |
|---|---|---|---|
| 1 | Buton de retragere și etichetă de garanție UE, multilingv, fără modificări în temă | B1 | cea mai tare: 7 nou-veniți mici peste prag, rata 3,7%, liderul e un nou-venit de 10 luni |
| 2 | Bibliotecă de blocuri ușoare pentru temă, la preț fix mic | B4 | medie: rata 3,7%, dar liderii au mii de recenzii, iar diferențierea e slabă |
| 3 | Import de liste de prețuri și cataloage de la furnizori | B8 | slabă: rata 0,4%, curba la 90 de zile aproape plată; păstrată pentru legătura cu faza 1 (09-P4) |

Corecțiile aduse de verificarea independentă sunt în VERIFICARE.md și au fost aplicate în textul de mai jos.

**Ce e comun tuturor trei (verificat în sursă):**
- **Comision Shopify:** 0% pe primul 1.000.000 $ de venit brut din aplicații, socotit pe toată durata contului, apoi 15%. Toate încasările au o taxă de procesare de 2,9% plus taxele de vânzare aplicabile. Înregistrarea costă 19 $ o singură dată.
  - Sursa: https://shopify.dev/docs/apps/launch/distribution/revenue-share, `faza4/date/platforma/revenue-share.html`.
- **Facturare:** obligatoriu prin Shopify Billing API sau Shopify App Pricing. Facturarea în afara platformei e interzisă (cerința 1.2).
  - Sursa: https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements.
- **Tema magazinului** se poate modifica doar prin „theme app extensions" (cerința 5.1.1).
- **Revizuirea:** fiecare aplicație publică e revizuită manual înainte de listare. **Durata revizuirii nu e scrisă pe pagina citită, deci e necunoscută.** Sursa: https://shopify.dev/docs/apps/launch/app-store-review/review-process.
- **Rata de conversie gratuit → plătit: NECUNOSCUT.** Nu am găsit o sursă citabilă în cele două magazine.
- **Venitul net pe client** = preț × (1 − 2,9%), înainte de taxele de vânzare și de impozitele proprietarului (pe care nu le-am calculat).

---

## Propunerea 1: buton de retragere și etichetă de garanție UE (Shopify)

### Ce se construiește
1. O aplicație care adaugă butonul de retragere și pagina-formular printr-un „app embed" și un „app proxy". Nu atinge paginile și secțiunile existente.
2. Formularul verifică numărul comenzii și e-mailul față de comanda reală și trimite confirmarea automată.
3. Butonul se afișează doar pentru piețele UE și dispare la 14 zile după livrare.
4. Include eticheta armonizată a garanției legale.
5. Interfața și formularul sunt traduse în limbile UE, inclusiv româna.

### Unde se listează și cu cine concurează
Shopify App Store, categoria „Legal" (store-management-security-legal: 544 de lansări în fereastră, PAS2_SHOPIFY.md).

| Concurent | Preț | Recenzii | Lansat |
|---|---|---|---|
| eu-widerrufsbutton (401layers UG) | 9,99 $/lună sau 99,99 $/an; 29,99 $/lună | 2.324, 4,9 | 2026-01-09 |
| eu-withdrawal-form (BuschBytes) | 9 $/lună; 25 $/lună | 582, 4,8 | 2026-03-11 |
| eu-widerruf-pro (ECOMBEAT) | 11,99 $ și 17,99 $/lună | 330, 5,0 | 2026-05-07 |

Sursa: paginile aplicațiilor, 2026-11-16 (BUZUNARE.md, B1). **verificat în sursă**

### Slăbiciunea atacată (citate din SLABICIUNI.md, B1)
- **Strică tema și paginile:** „it disabled my existing main-page section … and replaced it with its own" (eu-widerrufsbutton, 2026-06-23, https://apps.shopify.com/reviews/2256904). „Plättet also bei uns als u. a. das Impressum" (2026-09-23, https://apps.shopify.com/reviews/2370644).
- **O singură limbă:** „Can't change language. Only German." (eu-widerruf-pro, 2026-08-19, magazin din România, https://apps.shopify.com/reviews/2327985). „I can't get the Dutch version installed" (eu-withdrawal-form, 2026-07-10, https://apps.shopify.com/reviews/2279804).
- **Nu verifică comanda:** „It does not check against anything in a real order" (vendidero, WooCommerce, 2026-08-24, https://wordpress.org/support/topic/almost-unusable-none-of-the-entered-values-is-checked-against-any-order-inform/).
- **Butonul nu expiră:** „Ce bouton devrait aussi disparaître automatiquement 14 jours après la réception" (wideruf-button, 2026-06-15, https://apps.shopify.com/reviews/2245033).
- **„Gratuit" care e doar mod de test:** „Nie informują, że darmowy plan działa tylko w trybie testowym." (2026-06-19, https://apps.shopify.com/reviews/2252470).

### Modelul de preț și numărul de clienți
- **Preț:** un singur plan, 7,99 $/lună, cu buton, formular, etichetă și toate limbile incluse. Plus 14 zile de probă cu toate funcțiile, fără plan „gratuit" care e de fapt mod de test. Prețul e la nivelul celui mai ieftin concurent (wideruf-button, 7,99 $). **dedus**
- **Net pe client:** 7,99 × 0,971 = 7,76 $ = **37,57 lei/lună**.
- **2.000 lei/lună = 54 de magazine plătitoare. 3.000 lei/lună = 80.**
- **Rata gratuit → plătit: NECUNOSCUT.** Cu probă de 14 zile, numărul de instalări necesare nu se poate estima.

### Efortul de construire (dedus): 6-8 săptămâni
Ce e greu:
1. **Teme diferite fără modificări în cod.** Plângerile liderului arată exact asta.
2. **Accesul la datele protejate ale clienților** (nume, e-mail din comandă), pentru verificarea comenzii. Shopify cere o cerere separată pentru aceste câmpuri. Durata aprobării: **necunoscută**.
3. **Textele legale corecte în 20+ limbi și regula de 14 zile** pe date de livrare care lipsesc uneori din comandă.
4. **Livrarea sigură a e-mailurilor**, fără ca formularul să poată fi folosit pentru spam (vezi plângerea despre vendidero).

### Efortul lunar de operare și suport (dedus)
- 3-6 ore pe săptămână de suport scris, mai ales la instalare și pentru teme ciudate.
- Actualizări la schimbările legale sau ale temelor Shopify.
- Cost de găzduire și de e-mail tranzacțional: necunoscut.

### Riscuri specifice
- **(d) juridic, dedus:** aplicația dă un text cu efect legal. O greșeală poate deveni reclamația comerciantului. Se reduce folosind formularul-tip oficial și un text explicit că nu e consultanță juridică. Riscul rămâne.
- **(b) parțial nativ:** Shopify a adăugat pe 18 iunie 2026 reguli de anulare pe piață. Un recenzent spune că se poate face gratuit cu Shopify Forms. **doar fragment.** Concurenții au primit totuși 313 recenzii noi în august-octombrie 2026, însumate.
- **Moment:** valul a trecut. Recenziile liderilor au fost concentrate în iunie-iulie 2026, iar o aplicație listată în 2027 prinde doar magazinele noi și pe cele care schimbă aplicația. **dedus**

### Semnele de la 30, 60 și 90 de zile
Comparate cu curbele reale din B1 (recenzii în primele 30/60/90 de zile):
- Cel lansat înaintea valului: eu-widerrufsbutton, 5/15/27.
- Mediana celor 7 nou-veniți din B1: 19/48/49.

| Ziua | Continuăm dacă | Ne oprim dacă |
|---|---|---|
| 30 | ≥ 3 recenzii și ≥ 5 magazine plătitoare | — (prea devreme) |
| 60 | ≥ 8 recenzii și ≥ 15 plătitoare | — |
| 90 | ≥ 15 recenzii și ≥ 25 plătitoare (pe drumul spre 54) | **< 8 recenzii și < 12 plătitoare.** E sub curba celui mai lent nou-venit din B1 (eu-widerrufsbutton, 27 la 90 de zile), redusă la jumătate pentru lipsa valului. |

Pragurile sunt propunerea mea. **dedus**

---

## Propunerea 2: bibliotecă de blocuri ușoare pentru temă (Shopify)

### Ce se construiește
1. O aplicație cu 25-40 de blocuri de pagină: beneficii, FAQ, comparație, logo-uri, testimoniale, tabele.
2. Blocurile sunt livrate ca „app blocks" printr-o „theme app extension", deci nu e scris cod în temă.
3. Fiecare bloc are CSS minim, se încarcă doar unde e folosit și dispare complet la dezinstalare.
4. Plată lunară mică și fixă, fără limită de pagini.

### Unde se listează și cu cine concurează
Shopify App Store, categoria „Page builder" (store-design-storefronts-page-builder: 234 de lansări, 10 trec pragurile).

| Concurent | Preț | Recenzii | Lansat |
|---|---|---|---|
| Section Store (section-factory) | 15 $/lună | 3.043, 4,9 | 2022-03-29 |
| sectionheroes | 22,9 $ și 36,9 $/lună | 59, 5,0 | 2025-12-12 |
| ecombe-page-builder | 14,99 $; 39,99 $; 79,99 $/lună | 35, 5,0 | 2026-01-28 |

Liderul pe numărul de recenzii e PageFly (5.929, de la 24 $/lună). Sursa: paginile aplicațiilor, 2026-11-16 (BUZUNARE.md, B4). **verificat în sursă**

### Slăbiciunea atacată (SLABICIUNI.md, B4)
- **Cod lăsat în temă:** „pagefly added random code even when I wasn't using their app" (2026-02-06, https://apps.shopify.com/reviews/2071170).
- **Editorul nu arată pagina reală:** „Constant discrepancies between editor and live page." (PageFly, 2026-08-27, https://apps.shopify.com/reviews/2338753).
- **Pagini încărcate:** „Creates a lot of bloat." (EComposer, 2025-12-02, https://apps.shopify.com/reviews/1985259).
- **Prea scump pentru magazine mici:** „$59USD a month … This isn't feasible for me." (GemPages, 2026-07-30, https://apps.shopify.com/reviews/2304100). „the pricing model is completely unreasonable for smaller Shopify stores" (fudge-agent, 2026-08-15, https://apps.shopify.com/reviews/2323853).

### Modelul de preț și numărul de clienți
- **Preț:** 9,99 $/lună, toate blocurile, fără limită de pagini. **dedus**
- **Net:** 9,99 × 0,971 = 9,70 $ = **46,98 lei/lună**.
- **2.000 lei = 43 de magazine plătitoare. 3.000 lei = 64.**
- **Rata gratuit → plătit: NECUNOSCUT.**

### Efortul de construire (dedus): 4-6 săptămâni pentru primele 25 de blocuri
Ce e greu:
1. **Blocurile de aplicație pot fi puse doar în secțiunile temei care le acceptă.** Asta limitează ce se poate oferi față de concurenții mai vechi.
2. **Testarea pe multe teme.**
3. **Diferențierea.** O recenzie acuză deja un nou-venit că e „Cheap copy of the SectionStore app" (2026-02-25, https://apps.shopify.com/reviews/2096300).

### Efortul lunar (dedus)
- 4-8 ore pe săptămână: blocuri noi (aici e valoarea care se reînnoiește) și suport scris.
- Meseria de bază a agenției (HTML, CSS, design de pagini) se potrivește. Platforma e alta (Liquid), nu WordPress.

### Riscuri specifice
- **(b) parțial nativ, dedus:** temele gratuite Shopify au deja multe secțiuni.
- **Concurență, verificat în sursă:** 219 lansări în 24 de luni. Liderii au mii de recenzii.

### Semnele de la 30, 60 și 90 de zile
Curbele B4 (recenzii în primele 30/60/90 de zile): mediana 0/3,5/5; cel mai bun ecombe-page-builder 17/26/29; cel mai slab versio-smart-blocks 0/0/0, care a ajuns totuși la 65 de recenzii mai târziu.

| Ziua | Continuăm dacă | Ne oprim dacă |
|---|---|---|
| 30 | ≥ 3 magazine plătitoare | — |
| 60 | ≥ 2 recenzii și ≥ 8 plătitoare | — |
| 90 | ≥ 5 recenzii (mediana B4) și ≥ 15 plătitoare | **< 2 recenzii și < 6 plătitoare** |

Pragurile sunt propunerea mea. **dedus**

---

## Propunerea 3 (slabă): import de liste de prețuri și cataloage de la furnizori (Shopify)

### Ce se construiește
1. Aplicația primește fișierul furnizorului (Excel, CSV, mai târziu PDF).
2. Potrivește coloanele o singură dată pe furnizor și găsește produsele după SKU sau cod de bare.
3. Arată diferențele (preț, stoc, produse noi) înainte de aplicare și le aplică în masă, cu posibilitate de anulare.
4. Gândită pentru cine nu e „XL guru".

### Unde se listează și cu cine concurează
Categoriile „Bulk editor" (451 de lansări) și „Store data importer" (307).

| Concurent | Preț | Recenzii | Lansat |
|---|---|---|---|
| Matrixify (excel-export-import) | 20, 50, 200 $/lună | 1.896, 4,9 | 2017-07-07 |
| altera-import-export-excel | 15 $/lună | 268, 5,0 | 2025-02-21 |
| bulkflow-files-import-export | 15 $/lună, 159 $/an | 38, 5,0 | 2025-05-14 |

Sursa: BUZUNARE.md, B8. **verificat în sursă**

### Slăbiciunea atacată (SLABICIUNI.md, B8; faza 1, 09-P4)
- **Greu de folosit:** „Unless you are an XL guru this app is rubbish." (Matrixify, 2026-08-27, https://apps.shopify.com/reviews/2337848).
- **Erori fără explicație:** „It constantly throws errors at you without providing any explanation" (2026-04-06, https://apps.shopify.com/reviews/2150840).
- **Salt mare de preț:** „If you need more, you are pushed toward a $200/month plan." (2026-05-31, https://apps.shopify.com/reviews/2225395).
- **Nu merge pe piețe:** „it does not allow modifications per market" (bulk-ai, 2026-03-16, https://apps.shopify.com/reviews/2122975).

### Modelul de preț și numărul de clienți
- **Preț:** 19 $/lună, fără limită de rânduri pentru un magazin. **dedus**
- **Net:** 18,45 $ = **89,34 lei/lună**.
- **2.000 lei = 23 de magazine plătitoare. 3.000 lei = 34.**
- **Rata gratuit → plătit: NECUNOSCUT.**

### Efortul de construire (dedus): 8-12 săptămâni
Ce e greu:
1. **Fișierele furnizorilor diferă fiecare.** PDF-ul e cel mai greu, deci intră abia în versiunea a doua.
2. **Potrivirea variantelor și a prețurilor pe piețe.**
3. **Limitele API-ului la cataloage mari și anularea sigură a unei aplicări greșite.**

### Efortul lunar (dedus)
6-10 ore pe săptămână. Aproape fiecare client nou vine cu alt format de fișier.

### Riscuri specifice
- **Semnal slab, verificat în sursă:** rata 5/1.147 = 0,4%. Mediana recenziilor la 90 de zile e 1.
- **Lider vechi și puternic:** Matrixify, 1.896 de recenzii.

### Semnele de la 30, 60 și 90 de zile
Curbele B8: recenziile la 90 de zile au fost 0-4 (mediana 1). altera-import-export-excel a crescut abia după 6 luni (57 de recenzii în august-octombrie 2026). La 90 de zile, recenziile nu sunt deci un semn util. Se măsoară magazinele plătitoare.

| Ziua | Continuăm dacă | Ne oprim dacă |
|---|---|---|
| 30 | ≥ 2 magazine plătitoare | — |
| 60 | ≥ 4 plătitoare | — |
| 90 | ≥ 6 plătitoare și ≥ 1 recenzie | **< 3 plătitoare** |
| 180 | ≥ 15 plătitoare | **< 10 plătitoare** |

Pragurile sunt propunerea mea. **dedus**

---

## Ce nu a ieșit, pe scurt

- **B2 (vizibilitate AI):** 10 nou-veniți mici pe Shopify. Funcția de bază (llms.txt) se face și de mână, iar recenzentul de la lovedbyai o spune explicit. În plus, 700 de lansări arată clonare masivă. Nu propun.
- **B7 (ramburs și fraudă):** confirmarea comenzilor prin OTP cere integrări SMS pe țări (criteriul e). Cererea din România nu e măsurată.
- **B5 (opțiuni de produs):** liderii au peste 3.000 de recenzii, iar mediana nou-veniților la 90 de zile e 2. Construcția atinge coșul și prețul, unde orice greșeală costă comerciantul bani.
- **WordPress:** WP-A (MCP) are un adaptor oficial gratuit, deci criteriul (b). WP-E și WP-G nu au destule prețuri citite.
