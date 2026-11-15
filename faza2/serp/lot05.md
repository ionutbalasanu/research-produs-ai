# Lot 05

Sursa SERP: Ubersuggest `serp_analysis` (language=ro, locId=2642, limit=20, fără parametrul refresh). La unele căutări unealta a întors `newData: true` cu data de azi, deși nu am cerut reîmprospătare. Paginile au fost deschise pe 15.11.2026 cu curl simplu (citeste.sh, pe HTTPS, pentru că HTTP simplu nu trece prin proxy). Instrumentele au fost testate cu Playwright (valoare de test + verificare pe telefon, iPhone 13). Am luat primele 10 rezultate organice din listă. Când lista sare la poziții foarte îndepărtate (peste 20), le-am omis și am notat asta.

Legendă coloane: Funcționează? = am introdus o valoare de test și am primit un rezultat (da), am văzut câmpuri dar nu și un rezultat (câmpuri, rezultat neconfirmat), nu e instrument (—). Telefon = scrollWidth <= innerWidth pe iPhone 13.

---

## calculator salariu (volum: 60500, familie: 01)
- Data colectării SERP: 2026-10-08
- Elemente care nu sunt organice: AI Overview (poz. 2), Related searches (poz. 11)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | calculator-salarii.ro (/calcul-salariu-net/anul-2026/) | instrument funcțional | da (brut 6000 → net 3512 lei, angajator 6135) | gratuit | actual (2026, selector 2025–2027) | nu | da | da |
| 3 | leaveboard.com (/ro/calcul-salariu-it/) | instrument funcțional | da (brut 6000 → net 3510 RON) | gratuit (calculatorul); site-ul vinde un produs HR, cu meniu „Prețuri” | actual (2026) | nu | da | da |
| 4 | ducont.md (/calculator_salarii/) | instrument (Republica Moldova) | câmpuri negăsite la test automat; pagina are doar tabele cu cote MD 2025 | gratuit | parțial (titlu 2025, reguli din Moldova, nu din România) | nu | da | da |
| 5 | jobinfo.ro | instrument funcțional | da (brut 6000 → net 3.512,50 RON) | gratuit | actual (2026) | nu | da | da |
| 6 | calculator-salarii.ro (/anul-2025/) | instrument funcțional (același motor ca la poz. 1) | da (același formular) | gratuit | pagina e pentru 2025, dar selectorul merge până în 2027 | nu | neverificat separat (la poz. 1 da) | da |
| 7 | facebook.com (/calculatorsalariu) | altul (pagină de Facebook) | — | — | — | cere autentificare | neverificat | da (doar ecranul de logare) |
| 8 | contabss.ro (/calculator-salariu/) | instrument funcțional + pagină de firmă de contabilitate | da (brut 6000 → net 3510 lei) | gratuit | învechit în text („Actualizat 2025”, curs euro 2025) | nu | da | da |
| 9 | play.google.com (com.calc.calculatorsalarii) | aplicație mobilă | neverificat (nu am instalat aplicația) | gratuită, „Conține anunțuri” | neverificat | neverificat | — | da (fișa din magazin) |
| 10 | calculator-salarii.ro (/anul-2022/) | instrument funcțional (același motor) | da (același formular) | gratuit | pagina descrie anul 2022 („Actualizat pentru anul 2022”) | nu | neverificat separat | da |
| 12 | calculator-salarii.ro (/salariu-minim-pe-economie-2025/) | articol + același formular | da (același formular) | gratuit | titlu 2025 | nu | neverificat separat | da |

- Ce apare azi: 6 instrumente funcționale pe 3 domenii (dintre care 4 pagini calculator-salarii.ro), 1 instrument pentru Republica Moldova, 1 aplicație Android, 1 pagină de Facebook. Nu există pagini ale statului.
- Instrument gratuit funcțional: da (calculator-salarii.ro; tot funcționale: jobinfo.ro, leaveboard.com)
- Produs plătit și preț: niciunul găsit pe pagini (leaveboard.com are meniul „Prețuri” pentru produsul HR, nu pentru calculator)
- Verdict: PUTERNICE (3 instrumente funcționale, actualizate pentru 2026, fără cont, în primele 5 poziții: 1, 3, 5)
- Riscuri: depinde de o instituție a statului (calculul urmează cotele din Codul fiscal: CAS 25%, CASS 10%, impozit 10%, deducere personală, după textul calculatoarelor)
- Surse blocate: facebook.com (cere logare)

## verificare rca online (volum: 14800, familie: 04,06)
- Data colectării SERP: 2026-09-28
- Elemente care nu sunt organice: AI Overview (poz. 2)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | calculrca.ro (/?page_id=332) | altul (pagină inexistentă) | nu (HTTP 404, „Pagina nu poate fi găsită”) | — | stricat | — | neverificat | da |
| 3 | asigurari-ieftine.ro (blog) | altul (404, trimite spre calculatorul RCA de pe prima pagină) | nu (404) | — | stricat | — | neverificat | da |
| 4 | myblog.ro | articol | — | — | învechit (titlul spune 2026, dar textul e din 6.11.2016 și pomenește CSA/CEDAM) | nu | da | da |
| 5 | politisti.ro | forum | — | — | neverificat | nu pentru citit | neverificat | da |
| 6 | bizlaw.md | articol (Republica Moldova, CNPF) | — | — | neverificat | nu | neverificat | da |
| 7 | hdsatelit.com | articol (URL din 2014) | — | — | probabil învechit (URL 2014) | — | — | nu (HTTP 508 „Resource Limit Is Reached”) |
| 8 | videotutorial.ro | articol/video tutorial | — | — | învechit (10 mai 2021) | nu | neverificat | da |
| 9 | wacasig.ro (blog) | altul (404) | nu (404) | — | stricat | — | neverificat | da |
| 10 | asigurareonline.ro (/verificare-itp) | articol (despre ITP, nu RCA), pe site de broker | nu are formular | — | neverificat | nu | da | da |
| 11 | pint.ro (blog) | articol scurt | — | — | învechit (02/02/2023) | nu | neverificat | da |

- Ce apare azi: 6 articole sau postări (1 forum), 3 pagini 404, 1 pagină indisponibilă (508). Niciun formular de verificare.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit (asigurari-ieftine.ro și wacasig.ro trimit spre un comparator RCA, dar paginile din SERP sunt 404 și nu au preț)
- Verdict: SLABE (niciun instrument funcțional în primele 10; primul rezultat e o pagină 404)
- Riscuri: depinde de o instituție a statului (verificarea se face în baza de date oficială a polițelor RCA; myblog.ro numește CEDAM/CSA, după text)
- Surse blocate: niciuna cu 403. Indisponibil: hdsatelit.com (HTTP 508)

## calculator consum (volum: 8100, familie: 06)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 6), Related searches (poz. 11). Lista are doar 6 rezultate organice până la poziția 20; aplicațiile Google Play de la pozițiile 28, 34, 51 și 54 au fost omise.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | peco-online.ro (/calculator.php) | instrument funcțional | da (300 km, 6 l/100 km, 8 lei/l → 18 l, 144 RON) | gratuit | fără an; formulă stabilă | nu | da | da |
| 2 | gps-online.webshow.ro | instrument funcțional | da (300 km → 18 litri, 180 RON) | gratuit | actual (titlu 2026, are și varianta electrică) | nu | da | da |
| 3 | calculatoare-utile.ro | instrument | câmpuri, rezultat neconfirmat la test automat (formula afișată pe pagină pare inversată: km/l × 100) | gratuit | fără an | nu | da | da |
| 4 | leaveboard.com (/ro/calculator-consum/) | instrument funcțional | da (valori implicite → 18,0 l, 135 RON) | gratuit | fără an | nu | da | da |
| 5 | dosar-auto.ro (/ro/planificator/) | instrument funcțional | da (300 km → costuri în lei, 0,59 lei/km) | gratuit | actual (2026, preț carburant precompletat 10,67) | nu | neverificat (formular desktop testat) | da |
| 15 | play.google.com (com.shpavda.fuel_calculator) | aplicație mobilă | neverificat | neverificat | neverificat | neverificat | — | doar titlu din SERP |

- Ce apare azi: 5 instrumente web (4 confirmate cu rezultat) și 1 aplicație Android. Sub 10 rezultate organice în SERP.
- Instrument gratuit funcțional: da (peco-online.ro)
- Produs plătit și preț: niciunul găsit
- Verdict: PUTERNICE (4 instrumente funcționale, fără cont, în primele 5: poz. 1, 2, 4, 5)
- Riscuri: niciun risc dovedit
- Surse blocate: niciuna

## calcul salariu invatamant (volum: 5400, familie: 01)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 1). Doar 4 rezultate organice.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | facebook.com (SalariiInvatamant, foto) | altul (postare pe Facebook a paginii „Calculator Salarii Invatamant”) | — | — | neverificat | cere autentificare (pagină goală) | neverificat | da (fără conținut) |
| 3 | portalinvatamant.ro (grila_salarizare_2023.pdf) | document de descărcat (PDF) | — | gratuit | învechit (MO 1197/29.XII.2023, salarii de la ianuarie 2024) | nu | — | da |
| 4 | facebook.com (SalariiInvatamant, foto) | altul (Facebook) | — | — | neverificat | cere autentificare | neverificat | doar titlu din SERP |
| 5 | ucv.ro (Salariu.pdf) | document de descărcat (PDF scanat, 1 pagină, fără text) | — | gratuit | 2025–2026 (după calea din URL) | nu | — | da (doar pe www.ucv.ro; ucv.ro fără www dă reset de conexiune) |

- Ce apare azi: 2 postări pe Facebook, 2 PDF-uri (o grilă din 2023 și un PDF scanat de la universitate). Sub 10 rezultate.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (niciun instrument funcțional; singurul „calculator” e pe Facebook, după logare)
- Riscuri: depinde de o instituție a statului (grilele de salarizare sunt publicate în Monitorul Oficial, după PDF-ul de la poz. 3)
- Surse blocate: facebook.com (cere logare)

## calculator rca (volum: 4400, familie: 06)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), People also search / „Găsește produse și servicii similare” (poz. 6), Related searches (poz. 12). Doar 4 rezultate organice.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | facile.it (Italia) | produs plătit (comparator de asigurări italian) | neverificat | titlul SERP: „da 131€” | — | — | — | nu (conexiune expirată/eroare HTTP/2) |
| 3 | independer.nl (Olanda) | articol/informații (NL) | — | — | neverificat | nu | neverificat | da |
| 4 | 1rca-ieftin.ro | altul (pagină goală) | nu (răspuns 200 fără conținut; nu are câmpuri nici după randare) | — | stricat | — | — | da |
| 5 | moneysupermarket.com (UK) | articol/comparator UK | neverificat | — | — | — | — | da (meniu și text) |

- Ce apare azi: 1 comparator italian, 1 pagină olandeză, 1 pagină din UK, 1 site românesc gol. Niciun rezultat românesc funcțional.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: facile.it, „da 131€” (doar din titlul SERP, pentru Italia)
- Verdict: SLABE (niciun instrument funcțional pentru România în primele 10; singurul site românesc e gol)
- Riscuri: niciun risc dovedit
- Surse blocate: facile.it (nu s-a putut deschide: timeout/eroare HTTP/2, nu 403)

## rovinieta online verificare (volum: 3600, familie: 06)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 1). Doar 4 rezultate organice.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | gandul.ro | articol | — | — | învechit („ROVINIETA 2023”) | nu | neverificat | da |
| 3 | e-viniete.ro (/vignette/ro/) | instrument funcțional + produs plătit (intermediar privat) | da (B123ABC → „Statut: Nevalidă”, apoi oferă cumpărare) | verificarea e gratuită; rovinieta costă 16,9 € (1 zi), 24,5 € (10 zile), 29,9 €, 38,9 €, 92,5 €, cu taxă de serviciu inclusă | actual (pomenește categoriile de la 1 octombrie 2026) | nu | da | da |
| 4 | roviniete.ro (/ru/info/alerte-de-expirare) | produs plătit (magazin de roviniete), pagină în rusă despre alerte de expirare | neverificat | preț neextras | neverificat | are „Войти” (logare) | neverificat | da |
| 5 | ecomunicate.ro | articol/comunicat | — | — | — | — | — | nu (HTTP 403) |

- Ce apare azi: 1 instrument de verificare funcțional (pe site de intermediar), 1 magazin de roviniete (pagină în rusă), 2 articole (unul blocat). Sub 10 rezultate.
- Instrument gratuit funcțional: da (e-viniete.ro, verificare gratuită pe un site care vinde roviniete cu taxă de serviciu)
- Produs plătit și preț: e-viniete.ro: de la 16,9 € (1 zi) la 92,5 €, cu taxă de serviciu inclusă
- Verdict: MEDII (un singur instrument funcțional în primele 5)
- Riscuri: depinde de o instituție a statului (rovinieta e înregistrată în „sistemul central oficial”, iar prețurile depind de categoriile oficiale de la 1.10.2026, după textul e-viniete.ro)
- Surse blocate: ecomunicate.ro (403)

## cv europass model (volum: 2900, familie: 09)
- Data colectării SERP: 2026-10-02
- Elemente care nu sunt organice: Imagini (poz. 1), People also ask (poz. 8)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | ro.scribd.com (CV-Europass) | document de descărcat (Scribd, 2 pagini) | — | neverificat | neverificat | neverificat | neverificat | da |
| 3 | studocu.com | document de descărcat („Guideline 2007-2013”, după titlul SERP) | — | — | învechit după titlu (2007–2013) | — | — | nu (403 „Access Blocked”) |
| 4 | ro.pinterest.com | altul (pin cu imagine) | — | — | neverificat | nu pentru vedere | neverificat | da |
| 5 | gatadecompletat.ro | articol (ghid de completare) | — | — | neverificat | nu | neverificat | da |
| 6 | scribd.com (c-v-Model-European) | document de descărcat (3 pagini; „Download as DOC, PDF, TXT”) | — | neverificat | neverificat | neverificat | neverificat | da |
| 7 | studocu.com | document de descărcat | — | — | — | — | — | nu (403) |
| 9 | pinterest.com | altul (pin „Cv Europass format Word Romana”) | — | — | neverificat | nu pentru vedere | neverificat | da |
| 10 | ro.scribd.com (Copia Fișierului CV Europass) | document de descărcat | — | neverificat | neverificat | neverificat | neverificat | da |
| 11 | aosr.ro | document de descărcat (imagine JPEG cu CV Europass, din dosarul unui candidat) | — | — | neverificat | nu | — | da (fișier imagine) |
| 12 | ro.scribd.com (același URL ca la poz. 10) | document de descărcat (duplicat) | — | — | — | — | — | da |

- Ce apare azi: 6 documente (Scribd și Studocu, unul duplicat), 2 pin-uri Pinterest, 1 articol, 1 imagine. Niciun generator.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (niciun instrument funcțional în primele 10; doar documente încărcate de utilizatori și pin-uri)
- Riscuri: niciun risc dovedit
- Surse blocate: studocu.com (2 URL-uri, 403 „Access Blocked”)

## calculator dobanda legala (volum: 2400, familie: 01)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2). Doar 4 rezultate organice până la poziția 20 (aplicația Google Play de la poz. 29 a fost omisă).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | dosar-sina.ro (/en/tools/legal-interest-rate) | instrument (pagină în engleză) | câmpuri (sumă, scadență, data plății), dar niciun rezultat afișat după test (10000 RON, scadență 15.11.2025) | gratuit | afișează rata 14,5%/an (BNR 6,5% + 8 pp); © 2026 | nu | da | da |
| 3 | play.google.com (com.calculatord.calculatordobanda) | aplicație mobilă (după OG 13/2011) | neverificat | neverificat | neverificat; 10+ descărcări | neverificat | — | da (fișa din magazin) |
| 4 | coltuc.ro | articol (cabinet de avocat) | — | — | învechit (25 august 2013) | nu | neverificat | da |
| 5 | moisepaul.ro | articol (blog de avocat) | — | — | neverificat | nu | neverificat | da (prin Playwright; curl a întors doar titlul) |

- Ce apare azi: 1 instrument cu rezultat neconfirmat, 1 aplicație Android, 2 articole de avocat. Sub 10 rezultate.
- Instrument gratuit funcțional: nu (dosar-sina.ro are câmpuri, dar la test nu a afișat niciun rezultat)
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (niciun instrument confirmat funcțional în primele 10)
- Riscuri: depinde de o instituție a statului (rata se calculează din rata de referință BNR + 8 pp, după textul dosar-sina.ro și coltuc.ro)
- Surse blocate: niciuna

## model cv europass necompletat word (volum: 2400, familie: 03,09)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: Imagini (poz. 1, „CV European Necompletat | PDF”), AI Overview (poz. 2), People also search (poz. 3), Related searches (poz. 12). Doar 2 rezultate organice.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 4 | scribd.com (CV-European-Ro-RO-GOL) | document de descărcat (2 pagini, 3K vizualizări) | — | neverificat | neverificat | neverificat | neverificat | da |
| 5 | ro.scribd.com (Model-Cv-Europass-Ro) | document de descărcat (2 pagini) | — | neverificat | neverificat | neverificat | neverificat | da |

- Ce apare azi: 2 documente Scribd. Sub 10 rezultate.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (niciun instrument; doar 2 documente Scribd)
- Riscuri: niciun risc dovedit
- Surse blocate: niciuna

## cv online gratuit (volum: 1900, familie: 09)
- Data colectării SERP: 2026-10-02
- Elemente care nu sunt organice: AI Overview (poz. 1), People also search (poz. 6), Imagini (poz. 11, 17)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | reddit.com (r/resumes) | forum (traducere automată) | — | — | — | — | — | nu (pagina întoarce doar „Reddit”, fără conținut) |
| 3 | fliphtml5.com (blog ro) | articol | — | — | — | — | — | nu (403 „Just a moment...”) |
| 4 | es.pinterest.com (GetYourCV.net) | altul (profil Pinterest) | — | — | neverificat | nu pentru vedere | neverificat | da |
| 5 | moldova.org | articol (advertorial despre delucru.md, Republica Moldova) | — | — | neverificat | nu | neverificat | da |
| 7 | fliphtml5.com (blog ro) | articol | — | — | — | — | — | nu (403 „Just a moment...”) |
| 8 | play.google.com (com.status.cvcreator.resumemaker) | aplicație mobilă | neverificat | „Conține anunțuri”, „Achiziții în aplic.” (preț neafișat); 500K+ descărcări | neverificat | neverificat | — | da (fișa din magazin) |
| 9 | cvultau.ro (/creare-cv) | instrument (după titlu) | nu s-a putut deschide (certificat SSL care nu corespunde domeniului) | — | — | — | — | nu |
| 10 | reddit.com (r/recruitinghell) | forum | — | — | — | — | — | nu (fără conținut) |
| 12 | selfcv.com (/ro/politica-de-confidentialitate/) | altul (pagina de politică de confidențialitate a unui generator de CV; meniul are „Prețuri”) | — | preț neextras | politică actualizată 14/06/2024 | neverificat | neverificat | da |
| 13 | pinterest.com | altul (pin cu modele franceze de CV) | — | — | — | — | — | doar titlu din SERP |

- Ce apare azi: 2 discuții Reddit, 2 articole fliphtml5 (blocate), 2 pin-uri Pinterest, 1 advertorial din Moldova, 1 aplicație Android, 1 site cu certificat stricat, 1 pagină de politică de confidențialitate.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: aplicația Google Play „Constructor CV-uri” (achiziții în aplicație, fără preț afișat); selfcv.com are o pagină „Prețuri”, neextrasă
- Verdict: SLABE (niciun instrument funcțional verificat în primele 10 la o căutare care cere un instrument)
- Riscuri: niciun risc dovedit
- Surse blocate: fliphtml5.com (2 URL-uri, 403 „Just a moment...”); reddit.com (2 URL-uri, conținut neafișat fără JavaScript sau logare); cvultau.ro (eroare de certificat SSL)

## calcul pensie online (volum: 1600, familie: 01)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), Related searches (poz. 11). Doar 5 rezultate organice până la poziția 20 (aplicația Google Play de la poz. 54 a fost omisă).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | cjpiasi.ro | pagină a statului (Casa Județeană de Pensii Iași, explicația calculului) | — | gratuit | neverificat | nu | neverificat | da |
| 3 | lapensie.com (/virsta.php) | instrument funcțional (vârsta de pensionare, nu suma pensiei) | da (femeie, mai 1970 → „60 ani”, „după anul 2030 luna Mai”) | gratuit | probabil învechit: rezultatul de 60 de ani corespunde vechii Legi 19/2000 (pagina trimite separat la Legea 360/2023) | nu | nu (scroll orizontal 1703/1560) | da |
| 4 | cjpolt.ro | pagină a statului (CJP Olt) | — | — | — | — | — | nu (eroare la conectarea SSL) |
| 5 | estimez.ro (/calculator-varsta-pensionare/) | instrument (vârsta de pensionare) | câmpuri (sex, data nașterii, stagiu, condiții), rezultat neconfirmat la test automat | gratuit | actual (Legea 360/2023, „verificat pe 13 noiembrie 2026”) | nu | da | da |
| 9 | play.google.com (com.diemagd.pensioncalculator) | aplicație mobilă (calculator de investiții pentru pensie, nu sistemul public) | neverificat | neverificat; 50K+ descărcări | — | neverificat | — | da (fișa din magazin) |

- Ce apare azi: 2 pagini ale caselor de pensii (una nu se deschide), 2 calculatoare pentru vârsta de pensionare (unul confirmat, dar probabil pe legea veche), 1 aplicație Android generică. Niciun calculator pentru suma pensiei. Sub 10 rezultate.
- Instrument gratuit funcțional: da (lapensie.com, dar calculează vârsta, nu suma pensiei, iar rezultatul pare după legea veche)
- Produs plătit și preț: niciunul găsit
- Verdict: MEDII (un instrument funcțional în primele 5, dar nu sunt două instrumente actuale confirmate)
- Riscuri: depinde de o instituție a statului (regulile vin din Legea 360/2023 și de la casele de pensii/CNPP, după textul estimez.ro și cjpiasi.ro)
- Surse blocate: cjpolt.ro (eroare la handshake-ul SSL, nu 403)

## contract de inchiriere (volum: 1600, familie: 07)
- Data colectării SERP: 2026-10-03
- Elemente care nu sunt organice: Imagini (poz. 2, 14), AI Overview (poz. 3), Related searches (poz. 11)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | skia.ro (model-contract-inchiriere-actualizat-2023.pdf) | document de descărcat (PDF) | — | gratuit | „actualizat 2023” (în numele fișierului) | nu | — | da (PDF valid, 67 KB) |
| 4 | crosspoint.com.ro | articol (agenție imobiliară) | — | — | neverificat | nu | neverificat | da |
| 5 | cncir.com.ro (Model-contract-inchiriere.pdf) | document de descărcat (PDF) | — | gratuit | 2025 (în calea fișierului) | nu | — | da (PDF valid) |
| 6 | evo-imobiliare.ro | articol („Model contract inchiriere apartament 2026”) | — | — | actual (2026 în titlu) | nu | neverificat | da |
| 7 | notariate.ro (Contract-inchiriere-model.pdf) | document de descărcat (PDF) | — | gratuit | 2020 (în calea fișierului) | nu | — | da (PDF valid) |
| 8 | notari.pro | produs plătit (serviciu notarial) | — | tarif minim 0,3% din chiria pe toată perioada, minimum 50 lei, fără TVA | neverificat | nu | da | da |
| 9 | assets.primariatm.ro | document de descărcat (fișier binar, 166 KB) | — | gratuit | neverificat | nu | — | da (descărcat, nedeschis) |
| 10 | static.anaf.ro (Inchirierea.pdf) | pagină a statului / document (pliant ANAF) | — | gratuit | neverificat | nu | — | da (PDF valid, 1,3 MB) |
| 12 | lemonaid.ro | articol + model de descărcat („Descarca”) | — | gratuit | neverificat | nu | neverificat | da |
| 13 | lege5.ro | altul (textul Legii 114/1996, „actualizată 2026”) | — | gratuit pentru această pagină | actual | nu | neverificat | da |

- Ce apare azi: 5 documente de descărcat (4 PDF-uri și 1 fișier de la Primăria Timișoara), 3 articole (unul cu model), 1 serviciu notarial plătit, 1 text de lege.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: notari.pro: tarif minim notarial 0,3% din valoarea chiriei, minimum 50 lei, fără TVA
- Verdict: SLABE (niciun instrument sau generator funcțional în primele 10; doar documente statice și articole)
- Riscuri: juridic (model de contract cu efect juridic); depinde de o instituție a statului (în rezultate apare pliantul ANAF despre veniturile din chirii)
- Surse blocate: niciuna

---

## Rezumat

| Căutare | Ce apare azi | Instrument gratuit funcțional | Produs plătit și preț | Verdict | Riscuri |
|---|---|---|---|---|---|
| calculator salariu | 6 instrumente funcționale (3 domenii), 1 instrument MD, 1 aplicație, 1 Facebook | da (calculator-salarii.ro) | niciunul găsit | PUTERNICE | depinde de o instituție a statului (Cod fiscal) |
| verificare rca online | 6 articole/forum, 3 pagini 404, 1 pagină 508 | nu | niciunul găsit | SLABE | depinde de o instituție a statului (baza oficială RCA) |
| calculator consum | 5 instrumente web (4 confirmate), 1 aplicație; 6 rezultate | da (peco-online.ro) | niciunul găsit | PUTERNICE | niciunul dovedit |
| calcul salariu invatamant | 2 Facebook, 2 PDF; 4 rezultate | nu | niciunul găsit | SLABE | depinde de o instituție a statului (grilă în MO) |
| calculator rca | 3 site-uri străine (IT, NL, UK), 1 site RO gol; 4 rezultate | nu | facile.it „da 131€” (Italia, doar din titlu) | SLABE | niciunul dovedit |
| rovinieta online verificare | 1 instrument + magazin, 1 magazin, 2 articole; 4 rezultate | da (e-viniete.ro) | e-viniete.ro: 16,9 € (1 zi) până la 92,5 € | MEDII | depinde de o instituție a statului (sistemul oficial de roviniete) |
| cv europass model | 6 documente Scribd/Studocu, 2 Pinterest, 1 articol, 1 imagine | nu | niciunul găsit | SLABE | niciunul dovedit |
| calculator dobanda legala | 1 instrument neconfirmat, 1 aplicație, 2 articole; 4 rezultate | nu | niciunul găsit | SLABE | depinde de o instituție a statului (BNR) |
| model cv europass necompletat word | 2 documente Scribd; 2 rezultate | nu | niciunul găsit | SLABE | niciunul dovedit |
| cv online gratuit | 2 Reddit, 2 fliphtml5, 2 Pinterest, 1 advertorial MD, 1 aplicație, 1 site stricat, 1 politică | nu | aplicație Play cu achiziții în aplicație (fără preț); selfcv.com „Prețuri” (neextras) | SLABE | niciunul dovedit |
| calcul pensie online | 2 pagini CJP, 2 calculatoare de vârstă, 1 aplicație; 5 rezultate | da (lapensie.com, vârstă, probabil pe legea veche) | niciunul găsit | MEDII | depinde de o instituție a statului (Legea 360/2023, CNPP) |
| contract de inchiriere | 5 documente, 3 articole, 1 serviciu notarial, 1 text de lege | nu | notari.pro: 0,3% din chirie, minimum 50 lei | SLABE | juridic; depinde de o instituție a statului (ANAF) |
