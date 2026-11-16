# Faza 5, pașii 2 și 3: calendarul 2027-2028 și starea de azi

Data citirii: 2026-11-16. Notele de lucru complete, cu toate citatele: `faza5/date/calendar_ue_note.md` (acte UE) și `faza5/date/calendar_national_note.md` (UK, DE, FR, IT, ES, NL, PL, RO). Textele oficiale sunt în `faza5/date/legal/`.

Criteriile (din sarcină): (1) text adoptat și publicat, cu dată citită în sursa oficială; (2) element tehnic vizibil pe site sau în comandă; (3) aceeași aplicație pentru toate magazinele; (4) sancțiune documentată; (5) fără consultanță juridică.

## Rezultat

**3 obligații trec criteriile.** Una e condiționată de un act UE în curs de adoptare, una e de nișă și prea aproape.

| # | Obligația | Data | Cine e atins | Element pe site | Starea valului azi |
|---|---|---|---|---|---|
| C1 | Cyber Resilience Act, art. 13 alin. (19): data de sfârșit a suportului de securitate, afișată la cumpărare | **11.12.2027** | producătorii de produse cu elemente digitale (și distribuitorii, care verifică) | câmp „suport de securitate până la: luna/anul" pe pagina produsului | **neînceput**: nicio aplicație de afișare pe Shopify sau WordPress |
| C2 | CLP, art. 48a nou: ofertele la distanță arată elementele etichetei de pericol | **1.1.2028**, condiționat (Omnibus VI) | orice magazin care vinde substanțe sau amestecuri periculoase (lumânări, uleiuri esențiale, detergenți, vopsele, lichide pentru țigări electronice) | pictograme GHS, cuvânt de avertizare, fraze H și P, furnizor, cantitate | **neînceput**: 3 aplicații Shopify cu 0-1 recenzii |
| C3 | UK, Tobacco and Vapes Act 2026, s.1: vânzarea de tutun interzisă celor născuți la 1.1.2009 sau după | **1.1.2027** | magazinele online din UK care vând tutun, produse din plante pentru fumat, foițe | poarta de vârstă compară data nașterii cu 1.1.2009, nu cu „18 ani" | **nemăsurat**; termenul e peste 6 săptămâni |

---

## C1. Cyber Resilience Act: perioada de suport afișată la cumpărare

- **Actul:** Regulamentul (UE) 2024/2847, CELEX 32024R2847. Cellar: http://publications.europa.eu/resource/celex/32024R2847. EUR-Lex: https://eur-lex.europa.eu/eli/reg/2024/2847/oj. Regulament, direct aplicabil, fără transpunere. **verificat în sursă**
- **Data:** art. 71 alin. (2): „This Regulation shall apply from 11 December 2027. However, Article 14 shall apply from 11 September 2026 and Chapter IV (Articles 35 to 51) shall apply from 11 June 2026." Citit și de mine pe 2026-11-16, `faza5/date/legal/32024R2847.html`. **verificat în sursă**
- **Ce trebuie să apară:** art. 13 alin. (19): „Manufacturers shall ensure that the end date of the support period referred to in paragraph 8, including at least the month and the year, is clearly and understandably specified at the time of purchase in an easily accessible manner and, where applicable, on the product with digital elements, its packaging or by digital means." **verificat în sursă**. La vânzarea online, „at the time of purchase" înseamnă pagina produsului sau comanda. **dedus**
- **Cine e obligat:** producătorul. Distribuitorul verifică înainte de vânzare că producătorul a respectat art. 13 alin. (19) (art. 20 alin. (2) lit. (b)). Se aplică doar produselor introduse pe piață după 11.12.2027 (art. 69). Fără excepție pentru microîntreprinderi la această obligație. **verificat în sursă**
- **Sancțiunea:** art. 64 alin. (2): până la 15.000.000 EUR sau 2,5% din cifra de afaceri pentru art. 13. **verificat în sursă**. Practică de executare: **necunoscut** (regulamentul nu se aplică încă).
- **Transpunerea în DE, FR, IT, ES, NL, PL, RO:** nu e cazul, e regulament. Autoritățile de supraveghere naționale: **necunoscut**.
- **Criteriul (5):** aplicația afișează o dată pe care o dă producătorul. Nu stabilește durata suportului. **dedus**

**Starea de azi (pasul 3):**
- **Shopify:** nicio aplicație care afișează perioada de suport. Singura aplicație CRA, craledger-duty-records (momiji-shop, lansată 9.07.2026, 0 recenzii), ține evidențele producătorului (raportarea vulnerabilităților, art. 14), nu afișarea pe site (https://apps.shopify.com/craledger-duty-records). **verificat în sursă**
- **WordPress.org:** 5 pluginuri CRA (cra-vulnerability-monitor-eu-cyber-resilience-act, 50 de instalări; cra-vuln-notify, 20; trei cu 0), toate pentru dezvoltatori care își raportează propriul software, nu pentru magazine (`faza5/date/wp/cautare_pas3.json`). **verificat în sursă**
- **Platforma:** Shopify a lansat pe 17.06.2026 câmpul nativ „disclosures" pentru produse: „support built-in disclosure types for California Proposition 65 warnings and choking-hazard notices, plus custom disclosure types for other product-specific warnings or notices", afișat pe temele compatibile într-o secțiune „Disclosures" (https://changelog.shopify.com/posts/product-listings-now-support-a-disclosures-field). Un tip personalizat „perioadă de suport" se poate face nativ, gratuit. **verificat în sursă** (funcția), **dedus** (folosirea pentru CRA). WooCommerce și Germanized: nimic despre CRA. **verificat în sursă** (readme Germanized)
- **Timp până la termen:** 12,8 luni. Construcție din decembrie 2026, listare în martie 2027, adică ~9 luni înainte: **fereastra de 3-6 luni din pasul 1 se poate prinde**. **dedus**

---

## C2. CLP: elementele etichetei în oferta la distanță

- **Actul:** Regulamentul (UE) 2024/2865 (modifică CLP 1272/2008), CELEX 32024R2865, cu data mutată de Regulamentul (UE) 2025/2439, CELEX 32025R2439 (JO 3.12.2025). Cellar: http://publications.europa.eu/resource/celex/32024R2865 și http://publications.europa.eu/resource/celex/32025R2439. **verificat în sursă**
- **Data:** 2025/2439, art. 1 lit. (c), inserează alin. 3a: „Article 1, points (14), (15)(c), (26) and (27), points (2) and (3) of Annex I and point (2) of Annex II shall apply from 1 January 2028". Punctul (27) inserează art. 48a. Citit și de mine pe 2026-11-16. **verificat în sursă**
- **Ce trebuie să apară:** art. 48a: „When substances or mixtures are placed on the market through distance sales, the offer shall clearly and visibly indicate the label elements referred to in Article 17." Elementele art. 17: furnizorul (nume, adresă, telefon), cantitatea nominală, identificatorii produsului, pictogramele de pericol, cuvântul de avertizare, frazele de pericol (H), frazele de precauție (P), informații suplimentare. Art. 48 nou: reclamele pentru produse periculoase arată pictogramele și frazele. **verificat în sursă**
- **Cine e obligat:** cine face oferta la distanță. Fără excepție pentru microîntreprinderi. Că obligația cade pe orice magazin, nu doar pe primul furnizor: **dedus**.
- **Sancțiunea:** CLP art. 47, sancțiuni naționale „effective, proportionate and dissuasive". **verificat în sursă**. Cuantumuri și practică: **necunoscut**.
- **Condiția:** Omnibus VI (procedura 2025/0531(COD)): text agreat la 26.06.2026, votat de Parlament la 22.10.2026 (T10-0362/2026), „Awaiting Council's 1st reading position" (https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025/0531(COD), citit prin WebFetch pe 2026-11-16). **verificat în sursă**. Rezumatul oficial al poziției Parlamentului păstrează obligația, dar o restrânge la vânzările „for the general public" (https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1920911). **doar fragment** (rezumat, nu text). Mutarea datei la 1.1.2030 apare doar în surse secundare; pagina Consiliului dă 403, iar descărcarea textului adoptat de pe europarl.europa.eu a fost refuzată de sistemul de permisiuni al acestei sesiuni. **necunoscut**. Dacă actul apare în JO înainte de 1.1.2028 cu altă dată, C2 iese din fereastră.
- **Transpunerea:** nu e cazul, e regulament.
- **Criteriul (5):** aplicația afișează elementele pe care le dă fișa cu date de securitate a furnizorului. Nu clasifică produsul. **dedus**

**Starea de azi (pasul 3):**

| Aplicație | Dezvoltator | Lansată | Recenzii | Preț |
|---|---|---|---|---|
| gpsr-clp-hazard-labels | voidroot GmbH | 10.07.2026 | 1 | gratuit până la 5 produse; 9,99 $/lună sau 99 $/an |
| clp-hazard-info-display (CLPLens) | momiji-shop | 10.07.2026 | 0 | plan gratuit |
| gpsr-compliance-2 (GPSR & CLP Product Safety) | Shark Tech systems | 25.08.2026 | 0 | 9,99 $/lună |

Sursa: paginile aplicațiilor, `faza5/date/shopify/app3/`. **verificat în sursă**
- **WordPress.org:** govseer-hazard-labels, adăugat 10.11.2026, 0 instalări. **verificat în sursă**. Germanized nu menționează CLP. **verificat în sursă**
- **Platforma:** câmpul nativ Shopify „disclosures" (17.06.2026, vezi C1) poate ține un text de avertizare pe produs. Nu are pictograme GHS sau frazele H/P traduse. **verificat în sursă** (funcția), **dedus** (limita)
- **Valul nu a început.** Aplicațiile s-au lansat în iulie 2026, înaintea vechii date (1.07.2026), care fusese deja mutată în decembrie 2025. **verificat în sursă** (date), **dedus** (explicație)
- **Timp până la termen:** 13,5 luni. Fereastra de 3-6 luni se poate prinde, dacă data rămâne. **dedus**

---

## C3. UK: vârsta pentru vânzarea de tutun

- **Actul:** Tobacco and Vapes Act 2026, s.1 și s.175(3): „The following (which relate to the age of sale of tobacco etc) come into force on 1 January 2027 … (a) sections 1, 2, 5, 6 …". Confirmat de SI 2026/996, „Coming into force 1st January 2027". Surse: https://www.legislation.gov.uk/ukpga/2026/18/section/175 și SI 2026/996, `faza5/date/legal/uk_ukpga_2026_18_s175.html`, `uk_uksi_2026_996_*.html`. **verificat în sursă** (de agentul pentru calendarul național; nerecitit de mine)
- **Ce cere:** infracțiune vânzarea către o persoană „born on or after 1 January 2009"; amendă de nivel 4 (s.1(5)). Se aplică și vânzării online: **dedus** (legea nu numește vânzarea la distanță). Pentru vape-uri pragul rămâne 18 ani. **verificat în sursă**
- **Starea de azi:** nemăsurată. Proiectul de regulament pentru apărarea prin verificarea vârstei e încă proiect (de urmărit). **verificat în sursă**
- **Timp până la termen:** 1,5 luni. **Fereastra nu mai poate fi prinsă.** Nișă mică (doar vânzătorii de tutun din UK). **dedus**

---

## De urmărit (nevotate, fără dată sau cu data în schimbare)

| Ce | Stadiu citit | De ce contează |
|---|---|---|
| UK, abonamente (DMCCA 2024, Partea 4, Capitolul 2) | regulamentul de detaliu e proiect („1st January 2027"); niciun regulament de commencement pentru s.254; guvernul anunță „January 2027" (gov.uk, 9.08.2026) | element funcțional (ieșire online, notificări de reamintire, informații separate înainte de comandă), ca butonul de retragere; dar e teritoriul aplicațiilor de abonamente |
| CLP, Omnibus VI (2025/0531(COD)) | votat de PE 22.10.2026, așteaptă Consiliul | poate muta sau restrânge C2 |
| Germania, Tierhaltungskennzeichnungsgesetz § 10 (forma de creștere a animalelor, și la vânzarea la distanță) | în vigoare acum 1.1.2027; Drucksache 21/8974 (4.11.2026) propune 1.10.2027; vot final și BGBl **necunoscut** | carne proaspătă de porc vândută online; nișă |
| UK, vânzarea la distanță a cuțitelor (Crime and Policing Act 2026, s.32-43) | fără regulament de commencement | verificare cu act de identitate în checkout; nișă |
| Digital Fairness Act | propus de Comisie la 11.11.2026 | nu se va aplica în 2027-2028 |
| Detergenți, Regulamentul (UE) 2026/405, art. 20 | **adoptat**, dar se aplică din 23.09.2029 (art. 37), în afara ferestrei | singura obligație adoptată de afișare la vânzarea la distanță găsită pentru 2029 |
| Green Claims; Omnibus IV (instrucțiuni digitale); COM(2026) 565 (etichetare energetică digitală) | propuneri | afișări de produs |

## Respinse (pe scurt; detaliile în notele de lucru)

- **Date în afara ferestrei:** AI Act art. 50 (2.08.2026), credite de consum 2023/2225 (20.11.2026), 2024/825 (27.09.2026), dreptul la reparare (31.07.2026), jucării (1.08.2030), detergenți (23.09.2029), UK prețul pe unitate (6.04.2026), transpunerile naționale ale butonului de retragere și ale 2024/825 (2026), Spania Ley 10/2025 (2026). **verificat în sursă**
- **Fără element pe site (criteriul 2):** ambalaje 2025/40 (eticheta e pe ambalaj, iar data e condiționată de acte de punere în aplicare), baterii (pe produs; informarea online din 2025), muncă forțată (14.12.2027), taxa vamală de 3 EUR, noul Cod vamal, e-facturarea B2B în Germania (2027-2028) și Polonia (KSeF, 2027), BattDG și ElektroG (2027). **verificat în sursă**
- **Criteriul 3:** Franța, Loi 2026-602 (doar „mode ultra-express"), Ordonnance 2026-2 (servicii financiare prin telefon). **doar fragment** (Légifrance blocat la descărcare)
- **ESPR:** niciun act delegat cu cerințe de produs. **verificat în sursă**
- **Eticheta energetică a uscătoarelor (1.01.2027):** nimic nou de făcut pentru magazin. **verificat în sursă**
