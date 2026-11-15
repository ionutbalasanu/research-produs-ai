# Lot 08

Notă generală: listele vin din `serp_analysis` (Ubersuggest, România, limba română, fără refresh). La 8 din 12 căutări, unealta a întors o colectare de azi (2026-11-15, `newData: true`), deși nu am cerut refresh. Contorul de credite a rămas la 7/250 la toate apelurile. Celelalte 4 colectări sunt mai vechi: 2026-08-27, 2026-09-28, 2026-10-02 și 2026-10-03. Multe dintre colectările de azi au goluri: lipsesc pozițiile 6-10, iar după ele urmează direct aplicații Google Play de pe pozițiile 15-30. Respect precizarea primită: lucrez doar cu rezultatele organice de pe pozițiile 1-10 și nu completez cu rezultate de pe poziția 11 sau mai jos. În tabele trec poziția exact cum apare în SERP.

Paginile le-am deschis cu `citeste.sh`, pe https:// (adresele http:// din SERP le-am rescris). Instrumentele le-am testat cu Playwright, cu valori de test. Pentru telefon am emulat un iPhone 13, care are 390px lățime. „OK” înseamnă scrollWidth <= innerWidth și <= 390px. „Nu (Xpx)” înseamnă că pagina s-a lățit la X px, adică apare scroll orizontal sau browserul micșorează pagina. Scripturile sunt în `/tmp/claude-0/-home-user-research-produs-ai/ec306108-cf6b-596d-a2a6-189da6bc7c38/scratchpad/lot08scripts/`.

## calcul salariu net (volum: 33100, familie: 01)
- Data colectării SERP: 2026-09-28
- Elemente care nu sunt organice: AI Overview (poz. 2), Imagini (poz. 7)
- Rezultate organice în pozițiile 1-10: doar 5 (poz. 1, 3, 4, 5, 6). Lista se oprește la poziția 7.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | calculator-salarii.ro | instrument funcțional | da (5000 brut → 2981 net, cost complet 5113) | gratuit | 2026 (anii 2025-2027, curs BNR 5,3498) | nu | OK | da |
| 3 | manager.ro | instrument funcțional | da (5000 brut → 2968 net, CAM 113, cost total 5113) | gratuit; PDF-ul cu rezultatul cere e-mail și abonare la newsletter | 2026, dar ultima lună din listă e „Iulie 2026” | nu (doar PDF-ul cere e-mail) | nu (405px) | da |
| 4 | app.calculatorture.ro | instrument funcțional (salariu cu sporuri de tură) | da (5000 brut → 2.925 net, fără deducere personală) | gratuit | 2026 | nu | nu (512px) | da |
| 5 | calculator-salarii.ro | instrument funcțional (aceeași aplicație, pagina „6040 net → complet”) | da (afișează calculul precompletat) | gratuit | 2026 | nu | OK | da |
| 6 | calculator-salarii.ro | instrument funcțional (aceeași aplicație, „2018 brut → net”) | da (calcul precompletat) | gratuit | 2026 | nu | neverificat (aceeași aplicație ca la poz. 1) | da |

- Ce apare azi: 5 instrumente funcționale, din care 3 sunt pagini ale aceluiași site (calculator-salarii.ro). Din 5 rezultate organice.
- Instrument gratuit funcțional: da (calculator-salarii.ro)
- Produs plătit și preț: niciunul găsit
- Verdict: PUTERNICE (verdict pe 5 rezultate organice). În primele 5 sunt 3 instrumente funcționale, actuale, fără cont, de pe 3 domenii diferite.
- Riscuri: depinde de o instituție a statului. Rezultatul urmează regulile fiscale ale statului; după text: „CAS 25%, CASS 10%, impozit pe venit 10%”, „conform cu noile reglementari fiscale in vigoare”.
- Surse blocate: niciuna

## calculator credit ipotecar (volum: 9900, familie: 01)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 1), Imagini (poz. 20, în afara primelor 10)
- Rezultate organice în pozițiile 1-10: doar 4 (poz. 2-5). Următorul rezultat organic e abia pe poziția 16 (Google Play) și nu l-am inclus.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | finance.imobiliare.ro | instrument funcțional (simulator plus formular de broker de credite) | da (90.000 €, avans 15%, 30 ani → „Rata lunară începând de la: 2.123 RON”, dobândă 4,7%) | gratuit („Serviciu gratuit conform OUG 52/2016”) | actual (campanie Black Friday 30.10-30.11) | nu | OK | da |
| 3 | bcr.ro | articol (blog: ce este simularea de credit) | nu | gratuit | an neclar | nu | neverificat | da |
| 4 | bcr.ro | altul (pagina produsului „Casa Mea Natura”, cu link spre simulatorul George) | nu pe pagină (are doar link) | – | actual (dobândă fixă 4,79%) | nu | neverificat | da |
| 5 | oferteimobiliare.ro | instrument funcțional | da (100.000 €, avans 15%, 6%, 30 ani → rată 510 €, dobândă totală 98.462 €) | gratuit | actual (curs BNR din 13.11.2026) | nu | OK | da |

- Ce apare azi: 2 instrumente, 1 articol de bancă, 1 pagină de produs bancar. Din 4 rezultate organice.
- Instrument gratuit funcțional: da (finance.imobiliare.ro)
- Produs plătit și preț: niciunul găsit. Băncile oferă credite, dar niciun instrument nu e plătit.
- Verdict: PUTERNICE (verdict pe 4 rezultate organice). În primele 5 sunt 2 instrumente funcționale, actuale, fără cont (poz. 2 și 5).
- Riscuri: depinde de o instituție a statului. După text, dobânda variabilă este „IRCC + 2,1%”, iar IRCC e indicele publicat de BNR.
- Surse blocate: niciuna

## verificare rovinieta dupa numar (volum: 8100, familie: 04,06)
- Data colectării SERP: 2026-08-27. Colectarea e dinaintea schimbării de sistem: după textul de pe erovinieta.net, din 1 octombrie 2026 rovinietele se emit prin TollRo, iar registrul public CNAIR nu mai funcționează din 7 octombrie 2026.
- Elemente care nu sunt organice: niciunul în pozițiile 1-10 (Related searches pe poz. 11)
- Rezultate organice: 10 (poz. 1-10)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | cnadnr.ro | pagină a statului (CNAIR) | neverificat | – | – | – | – | nu (curl: conexiune resetată; Playwright: 502 „upstream request failed”). Doar titlu din SERP. |
| 2 | erovinieta.net | instrument (verificare și vânzare de roviniete, serviciu privat) | parțial: la numărul-exemplu „B123ABC” răspunde „Nu am putut confirma… Registrul CNAIR nu răspunde azi” și trimite spre cumpărare | verificare gratuită; vinde rovinieta (taxă) | actualizat 5.11.2026 | nu | OK | da |
| 3 | evita-amenzi.ro | instrument (verificare după număr) | nu: după trimitere rămâne la „Se verifică...” și după 25 s; după prima verificare cere cont („Ai folosit verificarea gratuită de azi”) | gratuit, 1 verificare pe zi fără cont | 2026 (TollRo în titlu) | după o verificare, da | OK | da |
| 4 | roviniete.ro | altul (pagină informativă a unui vânzător; butonul duce la valabilitate.roviniete.ro, unde se cer nr., serie șasiu, serie certificat și cod captcha) | neverificat (cere seria de șasiu, seria certificatului și captcha) | gratuit | 2026 (categoriile de la 1.10.2026) | nu | nu (405px) | da |
| 5 | peco-online.ro | articol (cum verifici, amenzi, tarife) | nu | gratuit | actual (tarife pe norme Euro) | nu | OK | da |
| 6 | roviniete.ro | articol (comunicat de presă: „Verificare rovinieta online”) | nu | gratuit | vechi (trimite la serviciul CNADNR) | nu | nu (405px) | da |
| 7 | bucuresti.cnadnr.ro | pagină a statului (DRDP București) | neverificat | – | – | – | – | nu (curl: conexiune resetată). Doar titlu din SERP. |
| 8 | compara-asigurari.ro | articol (cu calculator de preț pentru rovinietă, nu de verificare) | nu pentru verificare (trimite la portalul CNAIR) | gratuit | actualizat 2.10.2026 | nu | OK | da |
| 9 | vignetim.com | articol (blog: de ce se cere seria de șasiu) | nu | gratuit | actualizat 1.10.2026 | nu | OK | da |
| 10 | verificarerovinieta.com | instrument funcțional (serviciu independent) | da: la „B123ABC” a răspuns „Rovinieta VALABILĂ… expiră la 15.04.2027”. Nu pot verifica dacă e corect; erovinieta.net spune că registrul public CNAIR nu răspunde. | gratuit | 2026 („din octombrie 2026, seria de șasiu nu mai este necesară”) | nu | OK | da |

- Ce apare azi: 3 instrumente de verificare (unul răspunde, unul nu confirmă, unul blocat după prima verificare), 4 articole sau pagini informative, 1 pagină de vânzător cu link spre un formular cu captcha, 2 pagini CNAIR la care nu am ajuns.
- Instrument gratuit funcțional: da (verificarerovinieta.com, poz. 10, cu rezultat a cărui corectitudine nu am putut-o verifica)
- Produs plătit și preț: rovinieta propriu-zisă e o taxă, nu un instrument plătit. Tarifele afișate pe peco-online.ro pentru autoturism, 12 luni: 228 RON (electric) – 330 RON (Euro 0-III). Niciun instrument plătit găsit.
- Verdict: MEDII. Există un singur instrument care dă rezultat, pe poziția 10. În primele 5 nu e niciun instrument care să dea un rezultat confirmat.
- Riscuri: depinde de o instituție a statului. După text (erovinieta.net): „registrul public CNAIR (erovinieta.ro/vgncheck) nu funcționează din 7 octombrie 2026”, iar rovinietele se emit „în noul sistem CNAIR (TollRo)”.
- Surse blocate: niciuna cu 403/429/captcha. Nu am ajuns însă la cnadnr.ro și bucuresti.cnadnr.ro: conexiunea a fost resetată sau a dat 502 prin proxy.

## model cv angajare (volum: 5400, familie: 03,09)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: Imagini (poz. 1, „CV simplu – model ușor de completat (Word + exemple…)”), AI Overview (poz. 2), Related searches (poz. 11)
- Rezultate organice în pozițiile 1-10: doar 3 (poz. 3, 4, 5)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 3 | anofm.ro | pagină a statului, cu un document de descărcat (CV_in_format_european-1.doc) | nu (document .doc) | gratuit | învechit („modelul comun aprobat prin HG nr. 1021/2004”) | nu | OK | da |
| 4 | cvapp.ro | produs plătit (galerie de exemple de CV, cu editor) | editorul se deschide fără cont (alegerea șablonului); descărcarea nu am testat-o | majoritatea șabloanelor PREMIUM; probă 7 zile €2,95, apoi €19,95/lună; €44,95/6 luni; €74,95 (al treilea plan); plan gratuit cu câteva șabloane, doar PDF | actual | neclar pentru descărcare | OK | da |
| 5 | cvapp.ro | produs plătit (pagina „Modele de CV simple”, același editor) | la fel ca poz. 4 | la fel ca poz. 4 | actual | neclar | OK | da |

- Ce apare azi: 1 pagină a statului cu un .doc vechi, 2 pagini ale unui editor de CV freemium. Din 3 rezultate organice.
- Instrument gratuit funcțional: nu. Editorul cvapp.ro se deschide, dar aproape toate șabloanele sunt plătite, iar descărcarea nu am testat-o.
- Produs plătit și preț: cvapp.ro, €2,95 probă 7 zile, apoi €19,95/lună (sau €44,95 pe 6 luni)
- Verdict: MEDII (verdict pe 3 rezultate organice). Un singur editor, freemium, pe 2 poziții; în rest, un model de stat din 2004.
- Riscuri: niciunul cu dovadă
- Surse blocate: niciuna

## convertor pdf in word (volum: 4400, familie: 05)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 1), Related searches (poz. 11)
- Rezultate organice în pozițiile 1-10: doar 5 (poz. 2, 3, 4, 5, 9). Rezultatul de pe poz. 29 nu l-am inclus.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | ilovepdf.com | instrument funcțional (pagina în japoneză, /ja/) | da: am încărcat un PDF de test și am descărcat test08.docx | gratuit; există planuri plătite (preț neafișat pe pagină) | actual | nu | OK | da |
| 3 | convertio.co | instrument (pagina în portugheză, /pt/) | neconfirmat: fișierul s-a încărcat, după „Converter” nu am prins descărcarea | gratuit cu limită de fișier; „Preços” există, preț neextras | actual | nu | OK | da |
| 4 | tools.exyconn.com | instrument (conversie în browser, în engleză) | neconfirmat: fișierul s-a încărcat, „Convert & Download DOCX” nu a produs descărcare în 60 s | gratuit | actual | nu | OK | da |
| 5 | youtube.com | video („How to convert a PDF to Word using Microsoft Word”) | nu | gratuit | – | nu | neverificat | nu (429, captcha). Doar titlu din SERP. |
| 9 | play.google.com | altul (aplicație Android „PDF to Word Converter”, pagina în franceză) | neverificat (aplicație) | „Contient des annonces, Achats via l'appli” | 2026 în descriere | – | neverificat | da |

- Ce apare azi: 3 convertoare online (niciunul în română; unul confirmat funcțional), 1 video, 1 aplicație Android. Din 5 rezultate organice.
- Instrument gratuit funcțional: da (ilovepdf.com)
- Produs plătit și preț: niciun preț afișat pe paginile deschise. ilovepdf și convertio au planuri plătite, iar aplicația din Play are achiziții în aplicație.
- Verdict: MEDII (verdict pe 5 rezultate organice). În primele 5 am confirmat un singur instrument; alte două s-au încărcat, dar conversia nu a fost confirmată.
- Riscuri: niciunul cu dovadă
- Surse blocate: youtube.com (429, captcha)

## verificare rca auto (volum: 3600, familie: 04,06)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), Imagini (poz. 10), Related searches (poz. 11)
- Rezultate organice în pozițiile 1-10: doar 4 (poz. 1, 3, 4, 5)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | urgentasig.ro | instrument (formular de verificare la un broker) | neverificat: cere seria de șasiu, CNP/CUI și e-mail, iar „rezultatul verificarii il trimitem pe adresa ta email”; nu am trimis un CNP | gratuit (după text) | „2026 - 2027” | nu cont, dar cere e-mail și CNP | OK | da |
| 3 | economo.ro | articol (cum verifici RCA în baza AIDA, cu ofertă RCA) | nu | gratuit | parțial vechi (pomenește Euroins „în 2023”) | nu | neverificat | da |
| 4 | rca.ro | produs plătit (comparator și vânzare de polițe RCA, nu verificare) | neverificat (cere numărul de înmatriculare ca prim pas al ofertei) | prețul poliței, neafișat fără date | actual | nu pentru calcul („MyRCA” pentru poliță) | nu (393px, depășire de 3px) | da |
| 5 | europa.eu | pagină instituțională UE (valabilitatea asigurării auto în UE) | nu | gratuit | actual | nu | neverificat | da |

- Ce apare azi: 1 formular care trimite rezultatul pe e-mail și cere CNP, 1 articol, 1 comparator de polițe, 1 pagină UE. Din 4 rezultate organice.
- Instrument gratuit funcțional: nu (singurul formular de verificare nu l-am putut confirma)
- Produs plătit și preț: rca.ro, polițe RCA (prețul nu apare fără datele vehiculului)
- Verdict: SLABE (verdict pe 4 rezultate organice). Niciun instrument confirmat funcțional. Singurul formular, urgentasig.ro, cere CNP și e-mail și trimite rezultatul pe e-mail.
- Riscuri: niciunul cu dovadă de instituție a statului. După economo.ro, verificarea se face în baza AIDA, care a înlocuit CEDAM.
- Surse blocate: niciuna

## model cv europass necompletat (volum: 2900, familie: 03,09)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: Imagini (poz. 1, „CV European Necompletat | PDF”), AI Overview (poz. 6), Related searches (poz. 11)
- Rezultate organice în pozițiile 1-10: doar 4 (poz. 2-5)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | europass.europa.eu | pagină instituțională UE, cu editor de CV (europa.eu/europass/eportfolio/screen/cv-editor) | da, parțial: editorul se deschide fără cont, cu „Începeți de la zero”; nu am generat un PDF | gratuit | actual | nu pentru editare; profilul și biblioteca cer cont | OK (pagina de prezentare) | da |
| 3 | anofm.ro | pagină a statului cu document .doc | nu (document de descărcat) | gratuit | învechit (model HG 1021/2004) | nu | OK | da |
| 4 | hipo.ro | instrument (formular de CV; CV-ul vine pe e-mail, creează cont pe Hipo) | neverificat: CV-ul se trimite pe e-mail, iar formularul creează cont | gratuit | anii de naștere se opresc la 2011 | da (e-mail, cont Hipo) | nu (400px) | da |
| 5 | sb.politiaromana.ro | document de descărcat (curriculum_vitae.doc, IPJ Sibiu) | nu (document) | gratuit | neverificat | nu | – | nu (eroare de certificat TLS la curl). Doar titlu din SERP. |

- Ce apare azi: 1 editor oficial Europass, 2 documente .doc (ANOFM și Poliția Sibiu), 1 formular care trimite CV-ul pe e-mail. Din 4 rezultate organice.
- Instrument gratuit funcțional: da (europass.europa.eu, editor deschis fără cont, dar nu am generat un CV)
- Produs plătit și preț: niciunul găsit
- Verdict: MEDII (verdict pe 4 rezultate organice). Un singur instrument fără cont în primele 5. Hipo cere e-mail și cont.
- Riscuri: niciunul cu dovadă
- Surse blocate: niciuna cu 403/429/captcha. sb.politiaromana.ro nu s-a deschis din cauza unei erori de certificat TLS.

## calculator rca fara date personale (volum: 2400, familie: 06)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 1), Related searches (poz. 11)
- Rezultate organice în pozițiile 1-10: doar 4 (poz. 2-5). Trei dintre ele sunt din Italia și Spania.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | assicurazioni.segugio.it | comparator de asigurări auto, Italia (în italiană) | neverificat | – | – | – | – | nu (403, „Please enable JS and disable any ad blocker”). Doar titlu din SERP. |
| 3 | lineadirecta.com | produs plătit (asigurător spaniol, calculator de preț în spaniolă) | neverificat (piață spaniolă) | preț personalizat | promoție „válida hasta el 31/12/2025” (învechită) | – | neverificat | da |
| 4 | unipol.it | produs plătit (asigurător italian, preventivator RCA) | neverificat (piață italiană) | preț personalizat | actual (Black Friday până la 30/11) | – | neverificat | da |
| 5 | troco.ro | produs plătit (comparator RCA românesc, pagina în maghiară /hu/) | neverificat: primul câmp e numărul de înmatriculare („B 111 AAA”), adică exact datele pe care căutarea vrea să le evite | prețul poliței, neafișat | actual | neverificat | OK | da |

- Ce apare azi: 3 asigurători sau comparatoare străine (IT, ES), 1 comparator românesc în limba maghiară. Niciun rezultat în română. Din 4 rezultate organice.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: troco.ro, polițe RCA (preț neafișat fără datele vehiculului)
- Verdict: SLABE (verdict pe 4 rezultate organice). Niciun instrument funcțional relevant. Rezultatele sunt străine sau cer date ale vehiculului.
- Riscuri: niciunul cu dovadă
- Surse blocate: assicurazioni.segugio.it (403)

## verificare cnp (volum: 2400, familie: 04)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), Related searches (poz. 11), Imagini (poz. 18)
- Rezultate organice în pozițiile 1-10: 0. Singurele rezultate organice sunt aplicații Google Play, pe pozițiile 19 și 31, pe care nu le-am inclus.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| – | – | niciun rezultat organic în pozițiile 1-10 | – | – | – | – | – | – |

- Ce apare azi: niciun rezultat organic în primele 10. Colectarea are doar AI Overview și Related searches.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (verdict pe 0 rezultate organice). Colectarea nu conține niciun rezultat organic în primele 10, deci nici un instrument; probabil colectarea e incompletă.
- Riscuri: niciunul cu dovadă (nu există text de citat)
- Surse blocate: niciuna

## generator text (volum: 1900, familie: 03)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), Related searches (poz. 11)
- Rezultate organice în pozițiile 1-10: doar 4 (poz. 1, 3, 4, 5). Rezultatul de pe poz. 32 nu l-am inclus. Toate sunt în engleză și sunt generatoare de fonturi sau text stilizat, nu de text redactat.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | fontspace.com | instrument (generator de fonturi și text stilizat, după titlu) | neverificat | – | – | – | – | nu (403, „Just a moment…”). Doar titlu din SERP. |
| 3 | play.google.com | altul (aplicație Android „Stylish Text Generator”, 1K+ descărcări) | neverificat (aplicație) | gratuită (fără preț afișat) | – | „No registration required” | neverificat | da |
| 4 | capitalizemytitle.com | instrument (Fancy Text Generator, după titlu) | neverificat | – | – | – | – | nu (403, „Security Verification”). Doar titlu din SERP. |
| 5 | mixfont.com | produs plătit (generator de fonturi cu AI) | neverificat: generarea cere autentificare („Sign In with Google”) | Free: 50 de credite; Pro: $20/lună; Max: $200/lună | actual | da | OK | da |

- Ce apare azi: 2 instrumente blocate (neverificate), 1 aplicație Android, 1 produs plătit cu cont. Toate în engleză. Din 4 rezultate organice.
- Instrument gratuit funcțional: nu (cele două posibile instrumente gratuite au fost blocate, deci neverificate)
- Produs plătit și preț: mixfont.com, Pro $20/lună, Max $200/lună (Free: 50 de credite)
- Verdict: SLABE (verdict pe 4 rezultate organice). Niciun instrument confirmat funcțional. Singurul deschis cere cont. Rezerva: fontspace.com și capitalizemytitle.com sunt blocate și nu le-am putut verifica.
- Riscuri: niciunul cu dovadă
- Surse blocate: fontspace.com (403, „Just a moment…”), capitalizemytitle.com (403, verificare de securitate)

## calculator credit imobiliar (volum: 1600, familie: 01)
- Data colectării SERP: 2026-10-03
- Elemente care nu sunt organice: AI Overview (poz. 6), Related searches (poz. 11)
- Rezultate organice în pozițiile 1-10: 9 (poz. 1-5, 7-10)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | ing.ro | instrument funcțional (simulator pe pagina produsului) | da (precompletat: „Rata lunară primii 3 ani 2.468,23 lei”, „DAE: 8,73%”) | gratuit | actual (dobândă fixă 4,79%-6,59%) | nu | OK | da |
| 2 | calculator-casa.raiffeisen.ro | instrument (calculator Raiffeisen, după titlu) | neverificat | – | – | – | – | nu (403, „Just a moment…”). Doar titlu din SERP. |
| 3 | bancatransilvania.ro | pagină de produs cu calculator (după titlu) | neverificat | – | – | – | – | nu (403, „Acces blocat”). Doar titlu din SERP. |
| 4 | unicredit.ro | instrument (calculator ipotecar, după titlu) | neverificat | – | – | – | – | nu (403, „Request Failed”, BrightCloud). Doar titlu din SERP. |
| 5 | brd.ro | instrument funcțional (calculator pe pagina Habitat) | da (precompletat: 200.000 lei, 360 luni → „Prima rată 1.138,42 LEI, Total de plată 507.591 LEI, DAE 7,65 %”) | gratuit; formularul de contact separat cere nume și telefon | actual (4,99% fix 36 luni) | nu | OK | da |
| 7 | bcr.ro | altul (pagină-hub cu linkuri spre simulatorul George, george.bcr.ro) | nu pe pagină (doar linkuri) | gratuit | actual | nu | OK | da |
| 8 | finance.imobiliare.ro | instrument funcțional (simulator plus broker) | da („Rata lunară începând de la: 2.123 RON”) | gratuit | actual | nu | OK | da |
| 9 | cec.ro | pagină de produs (credit ipotecar în euro, după titlu) | neverificat | – | – | – | – | nu (403, CloudFront „Request blocked”). Doar titlu din SERP. |
| 10 | librabank.ro | altul (pagina produsului, cu exemplu reprezentativ și link spre /simulator_credit, unde e formularul) | nu pe pagină; formularul de pe /simulator_credit nu l-am trimis | gratuit | actual (IRCC + 2,15%, DAE 8,10%) | nu | OK | da |

- Ce apare azi: 3 instrumente confirmate (ING, BRD, imobiliare.ro), 2 pagini-hub sau de produs cu link spre simulator, 4 pagini de bancă blocate. Din 9 rezultate organice.
- Instrument gratuit funcțional: da (ing.ro)
- Produs plătit și preț: niciunul găsit (băncile oferă credite, instrumentele sunt gratuite)
- Verdict: PUTERNICE (verdict pe 9 rezultate organice). În primele 5 sunt 2 instrumente funcționale, actuale, fără cont (ing.ro poz. 1 și brd.ro poz. 5).
- Riscuri: depinde de o instituție a statului. După text, dobânda variabilă este „IRCC + 2.1%” sau „IRCC + 2,29%”, iar IRCC e indicele publicat de BNR.
- Surse blocate: calculator-casa.raiffeisen.ro (403), bancatransilvania.ro (403), unicredit.ro (403), cec.ro (403)

## model contract vanzare cumparare auto (volum: 1600, familie: 02)
- Data colectării SERP: 2026-10-02
- Elemente care nu sunt organice: AI Overview (poz. 6), Related searches (poz. 11)
- Rezultate organice în pozițiile 1-10: 9 (poz. 1-5, 7-10)
- Context: după concreto.ro și compara-asigurari.ro, formularul ITL 054 s-a modificat pe 17.08.2026 („a fost introdus Chenarul D”). Coloana „Actual” compară fiecare model cu această modificare.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | impozitelocale2.ro | document de descărcat (PDF „Model 2026 ITL 054”, Anexa 2) | nu (document) | gratuit | actual (PDF creat pe 19.08.2026, „Model 2026 ITL 054”) | nu | – | da |
| 2 | contract-vanzare-auto.ro | document de descărcat (pagină cu PDF și Word) | nu (document) | gratuit | învechit: titlul spune 2026, dar PDF-ul descărcat este „Model 2016 ITL 054”, modificat în 2018 | nu | neverificat | da |
| 3 | compara-asigurari.ro | instrument (formular în 4 pași care generează contractul completat), plus PDF și Word necompletate | neconfirmat: formularul există, dar nu am ajuns cu datele de test până la PDF | gratuit („Gratuit, fără cont”, după text) | actual (PDF descărcat: „Model 2026 ITL 054”) | nu (după text) | nu (392px) | da |
| 4 | prefecturasibiu.ro | pagină a statului, document (formular de înstrăinare, după titlu) | neverificat | – | – | – | – | nu (curl: conexiune resetată). Doar titlu din SERP. |
| 5 | goldenauto.ro | articol cu PDF de descărcat | nu (document) | gratuit | învechit: titlul spune 2026, dar PDF-ul legat (încărcat în 2026/03) este „Model 2016 ITL 054” | nu | neverificat | da |
| 7 | avocatnet.ro | articol („DRPCIV pune la dispoziție un model oficial…”) | nu | gratuit | învechit (7 iulie 2020) | nu | neverificat | da |
| 8 | auto-schunn.ro | articol (blog al unui dealer auto) | nu | gratuit | publicat pe 23.02.2026, înainte de modificarea din august | nu | neverificat | da |
| 9 | ph.prefectura.mai.gov.ro | document de descărcat (PDF „Contract de vânzare-cumpărare pentru un vehicul folosit”, Prefectura Prahova) | nu (document) | gratuit | învechit (PDF din 2018, alt format decât ITL 054) | nu | – | da |
| 10 | concreto.ro | produs plătit (generator de contract, plus cereri de luare și scoatere din evidență) | neverificat (se plătește înainte de generare) | 25 lei per contract, plus 5 lei per cerere opțională | actual („actualizat conform ultimelor modificări din 17.08.2026”) | nu (după text) | neverificat | da |

- Ce apare azi: 4 documente de descărcat (2 actuale, 2 învechite), 3 articole (dintre care 2 cu PDF vechi), 1 generator gratuit neconfirmat, 1 generator plătit, 1 pagină de prefectură la care nu am ajuns. Din 9 rezultate organice.
- Instrument gratuit funcțional: nu (formularul de pe compara-asigurari.ro nu l-am confirmat)
- Produs plătit și preț: concreto.ro, 25 lei per contract (+5 lei per cerere opțională)
- Verdict: SLABE (verdict pe 9 rezultate organice). După definiție, în primele 10 nu am confirmat niciun instrument funcțional. Există totuși două modele oficiale actuale de descărcat (poz. 1 și 3), iar mai multe rezultate care scriu 2026 în titlu dau de fapt modelul din 2016.
- Riscuri: juridic (model de contract cu efect juridic, „contractul trebuie tiparit si semnat fizic de ambele parti”, după goldenauto.ro). Depinde de o instituție a statului: formularul tipizat ITL 054 e aprobat prin ordin ministerial (OMDRAP 1069/2016), a fost modificat pe 17.08.2026 și se vizează la DITL; după text, DRPCIV nu acceptă semnătura electronică.
- Surse blocate: niciuna cu 403/429/captcha. prefecturasibiu.ro nu s-a deschis (conexiune resetată).

## Rezumat

| Căutare | Ce apare azi | Instrument gratuit funcțional | Produs plătit și preț | Verdict | Riscuri |
|---|---|---|---|---|---|
| calcul salariu net | 5 instrumente (3 de pe calculator-salarii.ro), din 5 organice | da (calculator-salarii.ro) | niciunul găsit | PUTERNICE (pe 5 organice) | depinde de stat (reguli fiscale CAS/CASS/impozit) |
| calculator credit ipotecar | 2 instrumente, 1 articol BCR, 1 pagină de produs BCR, din 4 organice | da (finance.imobiliare.ro) | niciunul găsit | PUTERNICE (pe 4 organice) | depinde de stat (IRCC, BNR) |
| verificare rovinieta dupa numar | 3 verificatoare (1 dă rezultat), 4 articole sau pagini informative, 1 pagină de vânzător, 2 pagini CNAIR inaccesibile | da (verificarerovinieta.com, poz. 10) | niciun instrument plătit; rovinieta 228-330 RON/12 luni (taxă) | MEDII | depinde de stat (CNAIR/TollRo, registru public oprit din 7.10.2026) |
| model cv angajare | 1 .doc ANOFM din 2004, 2 pagini cvapp.ro freemium, din 3 organice | nu | cvapp.ro €2,95 probă, apoi €19,95/lună | MEDII (pe 3 organice) | niciunul |
| convertor pdf in word | 3 convertoare (1 confirmat), 1 video, 1 aplicație, din 5 organice | da (ilovepdf.com) | niciun preț afișat | MEDII (pe 5 organice) | niciunul |
| verificare rca auto | 1 formular cu CNP și răspuns pe e-mail, 1 articol, 1 comparator RCA, 1 pagină UE, din 4 organice | nu | rca.ro (polițe, preț neafișat) | SLABE (pe 4 organice) | niciunul cu dovadă |
| model cv europass necompletat | 1 editor Europass, 2 .doc, 1 formular Hipo cu cont, din 4 organice | da (europass.europa.eu) | niciunul găsit | MEDII (pe 4 organice) | niciunul |
| calculator rca fara date personale | 3 asigurători străini (IT/ES), 1 comparator RO în maghiară, din 4 organice | nu | troco.ro (polițe, preț neafișat) | SLABE (pe 4 organice) | niciunul |
| verificare cnp | 0 rezultate organice în primele 10 | nu | niciunul găsit | SLABE (pe 0 organice) | niciunul cu dovadă |
| generator text | 2 instrumente blocate, 1 aplicație, 1 produs AI cu cont; toate în engleză; din 4 organice | nu | mixfont.com $20/lună (Pro), $200/lună (Max) | SLABE (pe 4 organice) | niciunul |
| calculator credit imobiliar | 3 instrumente confirmate, 2 pagini cu link spre simulator, 4 bănci blocate, din 9 organice | da (ing.ro) | niciunul găsit | PUTERNICE (pe 9 organice) | depinde de stat (IRCC, BNR) |
| model contract vanzare cumparare auto | 4 documente (2 actuale), 3 articole, 1 generator gratuit neconfirmat, 1 generator plătit, din 9 organice | nu | concreto.ro 25 lei (+5 lei/cerere) | SLABE (pe 9 organice) | juridic; depinde de stat (ITL 054, DITL, DRPCIV) |
