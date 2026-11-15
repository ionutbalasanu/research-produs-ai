# Lot 03

Sursa SERP: Ubersuggest `serp_analysis` (language=ro, locId=2642, România), fără reîmprospătare. Pagini deschise cu curl (citeste.sh, peste https; peste http curl întorcea cod 000) și cu Playwright (iPhone 13 pentru verificarea pe telefon: scrollWidth <= innerWidth). Valori de test: salariu brut 5.000 lei, venit PFA 100.000 lei, note 8/9/10/7, număr auto inventat B100XYZ. Unde coloana „Funcționează?” spune „câmpuri văzute”, am văzut formularul, dar nu am obținut un rezultat (captcha sau lipsa unui test).

## calculator salariu net (volum: 90500, familie: 01)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 3), Related searches (poz. 11). SERP-ul are doar 6 rezultate organice (poz. 1, 2, 4, 5, 15, 17), deci lucrez cu 6.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | calculator-salarii.ro (/calcul-salariu-net/) | instrument funcțional | da: brut 5.000 → net 2.981 lei, CAS 1.250, CASS 500, impozit 269 | gratuit | actual („Actualizat 2026”, noiembrie 2026) | nu | da | da |
| 2 | salaria.ro | instrument funcțional | da: brut 5.000 → net 2.981, total taxe 2.132 | gratuit | actual (2026) | nu | da | da |
| 4 | salariile.ro | instrument funcțional | da: brut 5.000 → net 2.981; are și fluturaș PDF | gratuit | actual (2026, pagini pentru 2027) | nu | da | da |
| 5 | paylab.ro (/salariu-calculator) | instrument funcțional | da: brut 5.000 → net 3.028 RON (cu valorile implicite ale formularului) | gratuit (are și ofertă Paylab Business pentru firme) | actual (2026) | nu | da | da |
| 15 | play.google.com (com.calc.calculatorsalarii) | altul (aplicație Android) | neverificat (aplicație) | gratuită, „Contains ads” | neverificat | neverificat | neverificat | da (pagina din magazin) |
| 17 | play.google.com (aceeași aplicație, hl=ln) | altul (aplicație Android) | neverificat (aplicație) | gratuită | neverificat | neverificat | neverificat | da (pagina din magazin) |

- Ce apare azi: 4 instrumente web, 2 pagini ale aceleiași aplicații Android (doar 6 rezultate organice)
- Instrument gratuit funcțional: da (calculator-salarii.ro)
- Produs plătit și preț: niciunul găsit (paylab.ro promovează Paylab Business, fără preț pe pagină)
- Verdict: puternice (4 instrumente funcționale, actuale, fără cont, în primele 5 poziții)
- Riscuri: depinde de o instituție a statului (cotele CAS 25%, CASS 10%, impozit 10% și deducerea personală vin din Codul fiscal; după rezultatele calculatoarelor)
- Surse blocate: niciuna

## verificare rovinieta online (volum: 18100, familie: 04,06)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 1), Related searches (poz. 11). Doar 4 rezultate organice.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | roviniete.ro (/ro/info/verificare-rovigneta) | articol pe un magazin de roviniete | nu: textul descrie formularul (număr auto și serie de șasiu), dar pe pagină nu apare niciun câmp de verificare; singurul link „Verificare rovigneta” duce la un blog (inforovinete.blogspot.com) | gratuit (pagina); site-ul vinde roviniete, fără preț pe pagina deschisă | an 2026 în subsol | nu | nu (scroll orizontal 405 > 390) | da |
| 3 | roviniete.ro (/valabilitate-rovinieta-...) | articol pe un magazin de roviniete | nu (trimite la un formular prin link „AICI”) | idem | neclar | nu | nu (405 > 390) | da |
| 4 | cnadnr.ro (/ro/produseservicii/roviniete-0) | pagină a statului (CNAIR) | neverificat | – | – | – | neverificat | nu: eroare de conexiune la curl, 502 în browser; doar titlu din SERP |
| 5 | roviniete.ro (/ro/info/descarca-rovinieta) | altul (descărcare rovinietă după GUID pentru clienți) | nu este verificare | – | neclar | nu (cere GUID-ul tranzacției) | nu (405 > 390) | da |

- Ce apare azi: 3 pagini roviniete.ro (articole și descărcare) și 1 pagină CNAIR (nedeschisă); doar 4 rezultate organice
- Instrument gratuit funcțional: nu
- Produs plătit și preț: roviniete.ro vinde roviniete; pe paginile deschise nu e afișat niciun preț
- Verdict: slabe (niciun instrument de verificare funcțional în rezultatele organice)
- Riscuri: depinde de o instituție a statului (valabilitatea rovinietei vine din baza CNAIR; după textul roviniete.ro)
- Surse blocate: niciuna cu 403/captcha; cnadnr.ro inaccesibil (eroare de conexiune)

## calcul consum (volum: 8100, familie: 06)
- Data colectării SERP: –
- Elemente care nu sunt organice: –
- fără date SERP (serp_analysis a întors doar `{"location":"Global","language":null}`)
- Ce apare azi: fără date SERP
- Instrument gratuit funcțional: –
- Produs plătit și preț: –
- Verdict: – (fără date)
- Riscuri: –
- Surse blocate: –

## verificare itp online (volum: 6600, familie: 04,06)
- Data colectării SERP: 2026-08-29
- Elemente care nu sunt organice: Related searches (poz. 11)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | prog.rarom.ro (rarpol.asp) | pagină a statului (RAR), instrument | câmpuri văzute (serie CIV, nr. identificare, cod de verificare/captcha); rezultat neobținut din cauza captcha | gratuit | actual (sursa oficială) | nu | da | da |
| 2 | compara-asigurari.ro | articol (trimite la prog.rarom.ro) | nu e instrument | gratuit | 2026 | nu | da | da |
| 3 | itp.ro (/itp) | instrument | câmpuri văzute (VIN sau CIV + captcha); rezultat neobținut (captcha) | gratuit | an 2026 pe pagină | nu | da | da |
| 4 | evita-amenzi.ro (/verificare-itp) | instrument | câmpuri văzute (număr de înmatriculare); după trimitere rămâne „Se verifică...” (captcha Cloudflare Turnstile), fără rezultat | gratuit | 2026 | nu pentru verificare (site-ul are „Conectare/Creează cont”) | da | da |
| 5 | roviniete.ro (/verifica-online-rca-ul-itp-ul-si-rovinieta) | articol | nu e instrument | gratuit | neclar | nu | nu (405 > 390) | da |
| 6 | pret-asigurare.ro | articol (text despre verificare, fără formular pe pagină) | nu (0 câmpuri) | gratuit | 2026 | nu | da | da |
| 7 | vehio.ro | neverificat | neverificat | – | – | – | neverificat | nu: eroare de conexiune; doar titlu din SERP |
| 8 | itpautomoto.ro | articol pe blogul unei stații ITP (îndrumă spre registrul RAR) | nu e instrument | gratuit | actual (25 sept. 2026) | nu | da | da |
| 9 | asigurari.ro | articol | nu e instrument | gratuit | an 2026 în text | nu | neverificat (403 în browser) | da cu curl; 403 în Playwright |
| 10 | calculator-rca.ro (/verificare-itp/) | instrument (folosește serviciul public RAR, după text) | câmpuri văzute (număr, VIN); pentru B100XYZ nu a apărut niciun rezultat | gratuit, „fără cont” după text | 2026 | nu | da | da |

- Ce apare azi: 4 instrumente (RAR, itp.ro, evita-amenzi.ro, calculator-rca.ro), toate cu captcha sau fără rezultat la test; 5 articole; 1 nedeschis
- Instrument gratuit funcțional: parțial: prog.rarom.ro are formular gratuit, dar nu am obținut rezultat (captcha)
- Produs plătit și preț: niciunul găsit
- Verdict: medii (în primele 5 sunt 3 instrumente gratuite, fără cont, dar niciunul nu a dat un rezultat la test din cauza captcha)
- Riscuri: depinde de o instituție a statului (datele vin din baza RAR; după textul paginilor)
- Surse blocate: asigurari.ro (403 în browser; textul a fost citit cu curl); vehio.ro inaccesibil (eroare de conexiune)

## calcul salariu (volum: 4400, familie: 01)
- Data colectării SERP: 2026-08-28
- Elemente care nu sunt organice: Related searches (poz. 11)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | calculator-salarii.ro | instrument funcțional | da: 5.000 → 2.981 net | gratuit | actual (2026) | nu | da | da |
| 2 | impozitsalariu.ro | instrument funcțional | da: 5.000 → 2.981 RON net | gratuit | actual (2026) | nu | da | da |
| 3 | salaria.ro | instrument funcțional | da: 5.000 → 2.981 net | gratuit | actual (2026) | nu | da | da |
| 4 | salariile.ro | instrument funcțional | da: 5.000 → 2.981 net | gratuit | actual (2026) | nu | da | da |
| 5 | paylab.ro | instrument funcțional | da: 5.000 → 3.028 RON | gratuit | actual (2026) | nu | da | da |
| 6 | salarii.md | instrument funcțional, dar cu regulile Republicii Moldova (fond social 24%, impozit 12%) | da: 5.000 → 4.004 net (reguli MD) | gratuit | 2026 (MD) | nu | da | da |
| 7 | portalcontabilitate.ro (/calculator_salariu/) | produs plătit (portal cu abonament) | nu: pe pagină se văd doar căutare, login și formular de e-mail, calculatorul nu apare | „Variante de abonament”, preț neafișat pe pagină | titlu 2026 | da (login/abonament) | da | da |
| 8 | calculatoare-salarizare.ro (/salariu.php) | instrument (după HTML: fluturaș, câmpuri marcate ►) | neverificat: în browser apare „One moment, please...” (verificare anti-bot) | gratuit (după text) | 2026 (arhivă 2015-2025) | nu | neverificat | da cu curl; blocat în Playwright |
| 9 | undelucram.ro | instrument funcțional | da: 5.000 → 2.981 net | gratuit | actual (2026) | nu | da | da |
| 10 | portalcodulfiscal.ro (/calculator_salariu/) | produs plătit (portal cu abonament) | nu: calculatorul nu apare, doar căutare și login | „Beneficii si pret”, preț neafișat | titlu 2026 | da | da | da |

- Ce apare azi: 7 instrumente (unul cu reguli MD, unul neverificat din cauza anti-bot), 2 portaluri cu abonament, 0 articole
- Instrument gratuit funcțional: da (calculator-salarii.ro; și impozitsalariu.ro, salaria.ro, salariile.ro, paylab.ro, undelucram.ro)
- Produs plătit și preț: portalcontabilitate.ro / portalcodulfiscal.ro (abonament, preț neafișat pe pagină)
- Verdict: puternice (5 instrumente funcționale, actuale, fără cont, în primele 5)
- Riscuri: depinde de o instituție a statului (cotele din Codul fiscal, după rezultatele calculatoarelor)
- Surse blocate: calculatoare-salarizare.ro („One moment, please...” în browser; curl a mers)

## calculator medie (volum: 3600, familie: 08)
- Data colectării SERP: 2026-08-28
- Elemente care nu sunt organice: Related searches (poz. 11)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | calculator-medii.startcalc.com (medie facultate) | instrument | câmpuri văzute (18: materie, notă, credite) și buton; același site a dat rezultat la poz. 2 | gratuit | fără an relevant | nu | da | da |
| 2 | calculator-medii.startcalc.com (medie cu teză) | instrument funcțional | da: note 8, 9, 10, teza 7 → „8.99 ➔ 9” | gratuit | neclar (niciun an vizibil) | nu | da | da |
| 3 | diana-ionescu.ro (/calculator-medii/) | instrument | câmpuri văzute (butoane de note 10…5), test neefectuat | gratuit | actualizat conform Ordinului ME 4183/2022 (după text) | nu | da | da |
| 4 | osmcluj.ro (/calculator-medie/) | instrument (medie pe specializări și ani) | câmpuri văzute (specializări, ani, „Calculează”), test neefectuat | gratuit | neclar | nu | da | da |
| 5 | myunihub.ro | director de calculatoare (UMFCD, Drept UNIBUC, orice facultate) | pagina de start nu calculează, trimite la calculatoare | gratuit | neclar | nu | da | da |
| 6 | calculator-medii.startcalc.com (medie liceu) | instrument | câmpuri văzute (12), test neefectuat | gratuit | neclar | nu | da | da |
| 7 | medie-note.ro (/media-aritmetica) | instrument funcțional | da: 8, 9, 10, 7 → 8,5 | gratuit | n/a | nu | da | da |
| 8 | calculatorumfcd.ro | instrument | câmpuri de login; există „Calculează ca invitat”, test neefectuat | gratuit | neclar | opțional (mod invitat) | da | da |
| 9 | sorinborodi.ro (/Unelte/Media.html) | instrument (pagină cu frame-uri) | neverificat (textul nu se vede, 0 câmpuri detectate) | gratuit | neclar | nu | nu (pagină de desktop, 980 px) | da |
| 10 | play.google.com (net.oxdb.CalcMean) | altul (aplicație Android) | neverificat | gratuită, „Conține anunțuri” | neverificat | neverificat | neverificat | da (pagina din magazin) |

- Ce apare azi: 7 instrumente web, 1 director de calculatoare, 1 instrument neverificat, 1 aplicație Android
- Instrument gratuit funcțional: da (calculator-medii.startcalc.com; medie-note.ro)
- Produs plătit și preț: niciunul găsit
- Verdict: puternice (în primele 5: startcalc cu rezultat confirmat la poz. 2, iar poz. 1, 3 și 4 sunt calculatoare gratuite fără cont, cu formular vizibil)
- Riscuri: depinde de o instituție a statului (regulile de calcul al mediilor vin din regulamentul ME; după textul diana-ionescu.ro, Ordinul ME 4183/2022)
- Surse blocate: niciuna

## calculator ore (volum: 2900, familie: 01)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), Related searches (poz. 11), Imagini (poz. 20). Primele 10 organice sunt la poz. 1, 3, 4, 5, 7, 9, 12, 14, 16, 24.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | calculatodo.com (/ro/calculator-ore-si-minute) | instrument funcțional | da: două ore alese din liste → rezultat „22:00:00 / 22.00 / 1320 / 79200” | gratuit | n/a | nu | da | da |
| 3 | time.is (/ro/compare) | instrument (convertor de fus orar, alt scop) | câmpuri văzute în browser | gratuit | n/a | nu | da | parțial: 403 la curl |
| 4 | oralocala.timein.org (/timecalculator) | instrument (după titlu) | neverificat | – | – | – | neverificat | nu: eroare de conexiune / 502; doar titlu din SERP |
| 5 | play.google.com (Hours Calculator – Timesheet) | altul (aplicație Android) | neverificat | gratuită, cu reclame și achiziții în aplicație | neverificat | neverificat | neverificat | da (magazin) |
| 7 | play.google.com (Time Calculator, sternbach) | altul (aplicație Android) | neverificat | gratuită („Instalează”) | neverificat | neverificat | neverificat | da (magazin) |
| 9 | play.google.com (Time Calculator: Hours Minutes) | altul (aplicație Android) | neverificat | gratuită | neverificat | neverificat | neverificat | da (magazin) |
| 12 | play.google.com (Time Calculator, somdatt) | altul (aplicație Android) | neverificat | gratuită | neverificat | neverificat | neverificat | da (magazin) |
| 14 | play.google.com (Hour Calculator) | altul (aplicație Android) | neverificat | gratuită | neverificat | neverificat | neverificat | da (magazin) |
| 16 | play.google.com (Hours – Hours Calculator) | altul (aplicație Android) | neverificat | gratuită, „Conține anunțuri” | neverificat | neverificat | neverificat | da (magazin) |
| 24 | play.google.com (Time Calculator: Convert Hours) | altul (aplicație Android) | neverificat | gratuită, „Conține anunțuri” | neverificat | neverificat | neverificat | da (magazin) |

- Ce apare azi: 1 instrument web funcțional, 1 convertor de fus orar, 1 site nedeschis, 7 aplicații Android
- Instrument gratuit funcțional: da (calculatodo.com)
- Produs plătit și preț: niciunul găsit (o aplicație are achiziții în aplicație, fără preț afișat)
- Verdict: medii (un singur instrument web confirmat în primele 5; restul sunt alt tip de instrument, un site inaccesibil și aplicații)
- Riscuri: niciunul cu dovadă
- Surse blocate: time.is (403 la curl); oralocala.timein.org inaccesibil (eroare de conexiune)

## calcul pensie pe caz de boala (volum: 2400, familie: 01)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 1), Imagini (poz. 5), People also ask (poz. 6), Related searches (poz. 12). Doar 3 rezultate organice.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | pensii-botosani.ro (/calculul-pensiilor/) | pagină a statului (Casa Județeană de Pensii Botoșani), text despre calculul pensiei | nu e instrument | gratuit | mixt: 2023 apare de 59 de ori (legea nouă a pensiilor), 2026 de 4 ori | nu | da | da |
| 3 | lapensie.com (/forum/pensia-de-invaliditate2.php) | articol (site cu forum; site-ul anunță și un „Program GRATUIT de Calculare Pensii” pe altă pagină) | nu pe această pagină | gratuit | învechit? (cel mai nou an pe pagină: 2023) | nu | nu (pagină de desktop, 1043 px) | da |
| 4 | pensiidolj.ro (/pensia-de-invaliditate/) | pagină a statului (CJP Dolj) | nu e instrument | gratuit | 2024–2026 | nu | nu (pagină de desktop, 984 px) | da |

- Ce apare azi: 2 pagini ale caselor județene de pensii, 1 articol; doar 3 rezultate organice
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: slabe (niciun instrument în rezultatele organice, doar texte, la o căutare care cere un calcul)
- Riscuri: depinde de o instituție a statului (calculul pensiei de invaliditate urmează regulile CNPP/caselor de pensii; după textul paginilor CJP)
- Surse blocate: niciuna

## cv europass word (volum: 2400, familie: 09)
- Data colectării SERP: 2026-08-29
- Elemente care nu sunt organice: AI Overview (poz. 2), Imagini (poz. 8), Related searches (poz. 11). Primele 10 organice sunt la poz. 1, 3, 4, 5, 6, 7, 9, 10, 12, 13.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | europass.europa.eu (/ro/create-europass-cv) | instrument oficial UE (editor de CV) | pagina descrie editorul; „Mai întâi, va trebui să vă creați profilul Europass”; editorul nu a fost testat | gratuit | actual | da (profil Europass) | da | da |
| 3 | anofm.ro (/cv-europass/) | pagină a statului (ANOFM) | nu e instrument | gratuit | neclar (2017, 2020, 2026 pe pagină) | nu | da | da |
| 4 | social2.ro (CV-european-model.doc) | document de descărcat (DOC) | fișierul se descarcă (200) | gratuit | învechit (încărcat în 2019/04, după URL) | nu | neverificat | da (fișier binar .doc) |
| 5 | europass.europa.eu (/ro) | pagină oficială UE (acasă) | nu e instrument | gratuit | actual | site cu „Profilul meu” | da | da |
| 6 | hipo.ro (/locuri-de-munca/cveuropass) | instrument (formular CV cu „Salveaza CV & Download!”) | câmpuri văzute (email, nume, prenume, oraș, telefon…); download netestat | gratuit (fără preț afișat) | neclar (cel mai nou an: 2025) | cere e-mail în formular | da | da |
| 7 | interactive-cv.com (/en/blog/europass-cv-word) | articol în engleză (cu buton „Start Now” spre un generator de CV) | nu e instrument pe pagină | preț neafișat pe pagină | 2026 | nu | da | da |
| 9 | scribd.com (Model-CV-EUROPASS) | document de descărcat (pe Scribd) | buton „Download” vizibil, netestat | neclar | neclar | neverificat | da | da |
| 10 | cariera.ejobs.ro (/model-cv/) | articol cu modele de CV | nu e instrument | gratuit | 2026 | nu | da | da |
| 12 | ape.agenas.it (CVTemplate_it_IT.doc) | document de descărcat (DOC, în italiană) | fișierul se descarcă (200) | gratuit | neclar | nu | neverificat | da (fișier binar .doc) |
| 13 | ro.pinterest.com | altul (pin Pinterest) | nu | gratuit | neclar | da (login Pinterest afișat) | da | da |

- Ce apare azi: 2 pagini oficiale Europass (editorul cere profil), 1 pagină ANOFM, 3 documente DOC (unul din 2019, unul în italiană, unul pe Scribd), 2 articole, 1 formular CV (hipo.ro), 1 pin Pinterest
- Instrument gratuit funcțional: nu (Europass cere profil; formularul hipo.ro nu a fost testat până la download)
- Produs plătit și preț: niciunul găsit cu preț afișat
- Verdict: slabe (niciun instrument confirmat funcțional fără cont; restul sunt documente vechi sau străine și articole)
- Riscuri: niciunul cu dovadă
- Surse blocate: niciuna

## calculator dobanda depozit (volum: 1900, familie: 01)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2). Primele 10 organice sunt la poz. 1, 3, 4, 5, 8, 9, 15, 22, 23, 27.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | calculator.bg (/2/deposit.html) | instrument în bulgară | neverificat (în browser nu am găsit câmpuri vizibile; 502 pe telefon) | gratuit | n/a | nu | neverificat (502) | da (curl 200, text scurt) |
| 3 | clientebancario.bde.es | instrument în spaniolă (Banco de España), cu reCAPTCHA | neverificat (câmpurile nu au fost detectate) | gratuit | n/a | nu | da | da |
| 4 | play.google.com (Simulasi Kalkulator Deposito) | altul (aplicație Android, indoneziană) | neverificat | gratuită, „Conține anunțuri” | neverificat | neverificat | neverificat | da (magazin) |
| 5 | msn.com (/es-es/... calculadora-de-ahorros) | instrument în spaniolă (după titlu) | neverificat (pagina se încarcă goală) | – | – | – | da | da (conținut gol) |
| 8 | play.google.com (Bank Deposit Calculator) | altul (aplicație Android) | neverificat | gratuită, „Conține anunțuri” | neverificat | neverificat | neverificat | da (magazin) |
| 9 | play.google.com (Bank Deposit Calculator, hl=en_AU) | altul (aplicație Android) | neverificat | gratuită, cu reclame și achiziții în aplicație | neverificat | neverificat | neverificat | da (magazin) |
| 15 | play.google.com (Banking Calculator, hl=sl) | altul (aplicație Android) | neverificat | gratuită | neverificat | neverificat | neverificat | da (magazin) |
| 22 | play.google.com (Bank Deposit Calculator, hl=sl) | altul (aplicație Android) | neverificat | gratuită | neverificat | neverificat | neverificat | da (magazin) |
| 23 | play.google.com (Deposit calculator, ru.mob.dps) | altul (aplicație Android) | neverificat | gratuită, „Conține anunțuri” | neverificat | neverificat | neverificat | da (magazin) |
| 27 | play.google.com (Deposit Calculator, qdav) | altul (aplicație Android) | neverificat | gratuită, „Conține anunțuri” | neverificat | neverificat | neverificat | da (magazin) |

- Ce apare azi: 3 instrumente străine (BG, ES, ES), 7 aplicații Android; niciun rezultat în română
- Instrument gratuit funcțional: nu (niciunul confirmat; niciunul în română)
- Produs plătit și preț: niciunul găsit
- Verdict: slabe (niciun instrument funcțional confirmat; rezultatele sunt străine sau aplicații)
- Riscuri: niciunul cu dovadă
- Surse blocate: niciuna cu 403; calculator.bg a întors 502 pe telefon

## verificare anaf persoane fizice (volum: 1900, familie: 04)
- Data colectării SERP: 2026-10-02
- Elemente care nu sunt organice: AI Overview (poz. 1), Related searches (poz. 11). Primele 10 organice sunt la poz. 2-10 și 12.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | anaf.ro (dgcvpf/prezentare.activitati) | pagină a statului (ANAF, despre verificarea situației fiscale personale) | nu e instrument (meniu cu autentificare SPV) | gratuit | neclar | site cu autentificare SPV | nu (pagină de desktop, 1106 px) | da |
| 3 | anaf.ro (/restante/) | pagină a statului, instrument (listă de debitori) | da: lista „Obligații fiscale restante la data de 30.09.2026” se afișează; are căutare după denumire (debitori cu cod fiscal, nu verificare personală) | gratuit | actual (30.09.2026) | nu | nu (scroll orizontal 2090 > 1560) | da |
| 4 | anaf.ro (selectarea persoanelor fizice pentru control fiscal) | pagină a statului | nu e instrument | gratuit | neclar | nu | neverificat | da (200, text scurt) |
| 5 | mfinante.gov.ro (info PJ după CUI) | pagină a statului (instrument pentru persoane juridice, după titlu) | neverificat | gratuit | – | – | neverificat | nu: eroare de conexiune; doar titlu din SERP |
| 6 | juridice.ro | articol | nu | gratuit | învechit? (cei mai frecvenți ani: 2015, 2012; apare și 2024) | nu | da | da |
| 7 | avocatnet.ro (/t16371/...) | forum | nu | gratuit | 2025–2026 | nu | da | da |
| 8 | ey.com | articol | nu | gratuit | 2022–2024 | nu | da | da |
| 9 | universuljuridic.ro | articol (după titlu) | – | – | – | – | – | nu: 403 Cloudflare („Attention Required!”) |
| 10 | anaf.ro (/RegistruTVA/) | pagină a statului, instrument (registru TVA, după cod fiscal + captcha) | câmpuri văzute; rezultat neobținut (captcha) | gratuit | neclar | nu | nu (pagină de desktop, 1023 px) | da |
| 12 | lupsa.ro | articol (după titlu) | – | – | – | – | – | doar titlu din SERP |

- Ce apare azi: 5 pagini ANAF (2 cu instrumente pentru firme sau debitori), 1 pagină MF nedeschisă, 4 articole, 1 forum
- Instrument gratuit funcțional: nu pentru persoane fizice (anaf.ro/restante funcționează, dar listează debitori, nu verifică situația unei persoane)
- Produs plătit și preț: niciunul găsit
- Verdict: slabe (niciun instrument funcțional pentru verificarea unei persoane fizice; pagini ANAF informative și articole)
- Riscuri: depinde de o instituție a statului (datele și procedura VSFP sunt ale ANAF; după paginile anaf.ro)
- Surse blocate: universuljuridic.ro (403 Cloudflare); mfinante.gov.ro inaccesibil (eroare de conexiune)

## calculator taxe pfa 2025 (volum: 1600, familie: 01)
- Data colectării SERP: 2026-10-02
- Elemente care nu sunt organice: AI Overview (poz. 6), Related searches (poz. 11). Primele 10 organice sunt la poz. 1-5, 7-10 și 12.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | taxepfa.ro | instrument funcțional | da: venit 100.000, cheltuieli 20.000 → CASS 8.000, CAS 12.975, impozit 5.903, total 26.878 lei | gratuit (promovează SOLO) | pagina de start e pentru 2027 (există și /2026); nu e pentru 2025 cum cere căutarea | nu | da | da |
| 2 | solo.ro (/calculator-2025) | instrument al unui produs plătit (SOLO) | câmpuri văzute („Ex: 8000”); rezultatul nu a apărut în test | calculator gratuit; abonament SOLO (90% reducere la prima lună cu cod, preț neafișat pe pagina deschisă) | 2025, potrivit cu căutarea | nu | da | da |
| 3 | taxmentor.ro (/taxe-pfa/) | instrument funcțional | da (după acceptarea politicilor): 100.000 lei → tabel 2025 vs 2024 (CAS la 24 salarii minime de 4.050 / 3.300 lei) | gratuit | 2025, potrivit cu căutarea (textul pomenește și 2026) | nu (cere bifa de acord) | da | da |
| 4 | declaratiaunica.contapp.ro (/calculator) | instrument (în pași, cu descărcarea Declarației Unice) | câmpuri în pași; test neefectuat; contor „Calcule realizate 75 234” | gratuit (după text); ContApp are abonamente, preț neafișat | actual (actualizat 15 nov. 2026; „Taxe Venituri 2026”) | nu pentru calcul (site cu Autentificare/Înregistrare) | da | da |
| 5 | contabilitatepebune.ro | instrument (după text: calculator PFA sistem real 2026) | neverificat: în browser apare „One moment, please...” | gratuit (după text) | 2026 | nu | neverificat | da cu curl; blocat în Playwright |
| 7 | startco.ro (/calculator) | instrument funcțional | da: rezultat comparativ (SRL Micro / SRL Profit / PFA) | gratuit | neclar | nu | da | da |
| 8 | catramai.ro | instrument funcțional | da: 100.000 lei → CAS 24.300, taxe totale 40.870 lei | gratuit | 2026 (nu 2025) | nu | da | da |
| 9 | bono.ro (/calculator-taxe-2026) | instrument funcțional | da: comparație PFA/SRL, de exemplu 69.750 / 85.990 net | gratuit | 2026 (nu 2025) | nu | da | da |
| 10 | econta.ro | instrument funcțional + formular de contact („Sunați-mă”) | da: SRL profit, net final 65.700 lei | calculator gratuit; servicii plătite: Contabilitate PFA 39 €/lună, SRL 49 €/lună, înființare SRL 599 lei | 2026 | nu | da | da |
| 12 | zarinacrm.ro | instrument (după titlu) | – | – | – | – | – | doar titlu din SERP |

- Ce apare azi: 9 instrumente (6 confirmate funcționale, 3 cu câmpuri văzute sau neverificate), 1 nedeschis; 0 articole
- Instrument gratuit funcțional: da (taxepfa.ro; taxmentor.ro pentru anul 2025)
- Produs plătit și preț: econta.ro: Contabilitate PFA 39 €/lună, SRL 49 €/lună, înființare SRL 599 lei; solo.ro: abonament, preț neafișat
- Verdict: puternice (taxepfa.ro și taxmentor.ro sunt funcționale, fără cont, în primele 5; taxmentor are anul 2025, taxepfa.ro are 2026/2027)
- Riscuri: depinde de o instituție a statului (CAS/CASS/impozit după Codul fiscal și Declarația Unică ANAF; după textul paginilor); sezonier (căutarea numește anul fiscal 2025; după text)
- Surse blocate: contabilitatepebune.ro („One moment, please...” în browser; curl a mers)

## Rezumat

| Căutare | Ce apare azi | Instrument gratuit funcțional | Produs plătit și preț | Verdict | Riscuri |
|---|---|---|---|---|---|
| calculator salariu net | 4 instrumente, 2 pagini ale unei aplicații Android (6 organice) | da (calculator-salarii.ro) | niciunul găsit | puternice | depinde de o instituție a statului (Cod fiscal) |
| verificare rovinieta online | 3 pagini roviniete.ro, 1 pagină CNAIR nedeschisă (4 organice) | nu | roviniete.ro vinde roviniete, preț neafișat | slabe | depinde de o instituție a statului (CNAIR) |
| calcul consum | fără date SERP | – | – | – | – |
| verificare itp online | 4 instrumente (toate cu captcha sau fără rezultat), 5 articole, 1 nedeschis | parțial (prog.rarom.ro, captcha) | niciunul găsit | medii | depinde de o instituție a statului (RAR) |
| calcul salariu | 7 instrumente, 2 portaluri cu abonament | da (calculator-salarii.ro) | portalcontabilitate.ro / portalcodulfiscal.ro, preț neafișat | puternice | depinde de o instituție a statului (Cod fiscal) |
| calculator medie | 7 instrumente, 1 director, 1 neverificat, 1 aplicație | da (startcalc.com, medie-note.ro) | niciunul găsit | puternice | depinde de o instituție a statului (regulament ME) |
| calculator ore | 1 instrument, 1 convertor de fus orar, 1 nedeschis, 7 aplicații | da (calculatodo.com) | niciunul găsit | medii | niciunul cu dovadă |
| calcul pensie pe caz de boala | 2 pagini CJP, 1 articol (3 organice) | nu | niciunul găsit | slabe | depinde de o instituție a statului (CNPP) |
| cv europass word | 2 pagini Europass, 1 ANOFM, 3 DOC, 2 articole, 1 formular, 1 Pinterest | nu | niciunul găsit | slabe | niciunul cu dovadă |
| calculator dobanda depozit | 3 instrumente străine, 7 aplicații Android | nu | niciunul găsit | slabe | niciunul cu dovadă |
| verificare anaf persoane fizice | 5 pagini ANAF, 1 MF, 4 articole, 1 forum | nu | niciunul găsit | slabe | depinde de o instituție a statului (ANAF) |
| calculator taxe pfa 2025 | 9 instrumente, 1 nedeschis | da (taxepfa.ro, taxmentor.ro) | econta.ro 39 €/lună (PFA), 49 €/lună (SRL); solo.ro preț neafișat | puternice | depinde de o instituție a statului (ANAF/Cod fiscal); sezonier (anul 2025) |
