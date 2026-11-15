# Lot 02

Notă generală: SERP-urile vin din `serp_analysis` (Ubersuggest, România, limba română, locId 2642, limit 20, fără refresh). La 8 din 12 căutări, unealta a întors o colectare din ziua de azi (2026-11-15, `newData: true`), deși nu am cerut refresh. Contorul de credite a rămas la 7/250 la toate apelurile. Celelalte 4 căutări au colectări mai vechi (2026-08-31, 2026-09-02, 2026-10-02). Multe dintre colectările de azi au goluri mari: după pozițiile 1-5 vin direct aplicații Google Play aflate pe pozițiile 12-54. În tabele scriu poziția brută din SERP. Am luat primele 10 rezultate organice în ordinea poziției, chiar și atunci când unele sunt dincolo de poziția 10, și spun asta explicit.

Paginile au fost deschise cu `citeste.sh`, peste HTTPS: adresele `http://` din SERP întorceau HTTP 000 prin proxy, așa că le-am rescris în `https://`. Instrumentele le-am verificat cu Playwright (câmpuri vizibile și, unde am putut, o valoare de test), iar pe telefon le-am verificat emulând un iPhone 13. „OK” înseamnă că scrollWidth <= innerWidth la lățimea de 390px. „Nu (Xpx)” înseamnă că pagina s-a lățit la X px, adică peste lățimea ecranului. Aplicațiile Google Play nu pot fi testate în browser: le-am trecut ca „altul (aplicație Android)”, cu „neverificat” la „Funcționează?” și „n/a” la „Telefon”. Pentru ele, la „Actual”, trec data „Ultima actualizare” din Play.

## convertor valutar (volum: 110000, familie: 05,12)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 4), Related searches (poz. 11)
- Rezultatele organice sunt doar 7: patru în primele 10 (poz. 1, 2, 3, 5), apoi trei aplicații Google Play (poz. 28, 48, 52).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | [cursbnr.ro](https://www.cursbnr.ro/convertor-valutar) | instrument funcțional (convertor + calcul TVA) | da (test: 100 EUR → 534,98 RON) | gratuit | actual (curs BNR din 13.11.2026, TVA 21% din aug. 2025) | nu | OK | da |
| 2 | [cursvalutar.ro](https://www.cursvalutar.ro/convertor-valutar/) | instrument funcțional (convertor) | da (test: 100 → 534,98) | gratuit | actual (curs din 13-11-2026) | nu | OK | da |
| 3 | [bnr.ro](https://www.bnr.ro/23790-convertor-valutar) | pagină a statului (BNR) cu convertor | câmpuri văzute (valoare, dată, valute), dar valoarea de test nu a produs un rezultat lizibil | gratuit | actual (dată selectabilă) | nu | nu (638px) | da |
| 5 | [citfin.ro](https://www.citfin.ro/calculator-schimb-valutar/) | instrument (calculatorul unei case de schimb cehe, 16 valute, cursuri „orientative”) | câmpuri văzute în HTML; testul în browser a eșuat (HTTP 502) | gratuit | neclar | nu | neverificat (502) | da (curl), browser 502 |
| 28 | [play.google.com – Curs Valutar](https://play.google.com/store/apps/details?hl=en_GB&id=dev.thewebers.ro) | altul (aplicație Android) | neverificat | gratuit, cu achiziții în aplicație (preț neafișat) | actualizată 16 sept. 2025 | neverificat | n/a | da |
| 48 | [play.google.com – Currency Converter (Wontera)](https://play.google.com/store/apps/details?hl=ro&id=com.wontera.currency_converter) | altul (aplicație Android) | neverificat | gratuit, cu reclame | actualizată 19 feb. 2026 | neverificat | n/a | da |
| 52 | [play.google.com – Currency Converter - Exchange](https://play.google.com/store/apps/details?hl=ro&id=com.currency.currencyexchange) | altul (aplicație Android) | neverificat | gratuit, cu reclame | învechită (ultima actualizare 14 dec. 2020) | neverificat | n/a | da |

- Ce apare azi: 2 instrumente funcționale, 1 convertor al BNR (pagină a statului), 1 calculator al unei case de schimb, 3 aplicații Android (pe poz. 28-52)
- Instrument gratuit funcțional: da (cursbnr.ro)
- Produs plătit și preț: niciunul găsit (aplicația „Curs Valutar” are achiziții în aplicație, fără preț afișat)
- Verdict: PUTERNICE (cursbnr.ro și cursvalutar.ro, pe poz. 1-2, funcționează, sunt actuale, nu cer cont și merg pe telefon)
- Riscuri: depinde de o instituție a statului (după text: convertoarele folosesc „cursul BNR din data…”)
- Surse blocate: niciuna (citfin.ro a întors 502 în Playwright, dar 200 la curl)

## transforma jpg in pdf (volum: 18100, familie: 05)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2)
- Primele 10 organice: poz. 1, 3, 4, 5, 8, 10, apoi 12, 15, 17, 18. Opt din zece sunt aplicații Google Play.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | [play.google.com – JPG to PDF Converter (Quantum X)](https://play.google.com/store/apps/details?hl=ro&id=com.dev.sarfi.jpgimagetopdf) | altul (aplicație Android) | neverificat | gratuit, cu reclame | actualizată 14 iul. 2026 | neverificat | n/a | da |
| 3 | [shutterstock.com](https://www.shutterstock.com/ro/image-converter/jpeg-to-pdf) | instrument (după titlu: „Convertor gratuit din JPEG în PDF”) | neverificat | doar titlu din SERP | – | – | neverificat | nu (403) |
| 4 | [webcatalog.io](https://webcatalog.io/ro/apps/acrobat-jpg-to-pdf) | director (fișă care împachetează instrumentul Adobe într-o aplicație desktop de descărcat) | nu (nu convertește pe pagină) | neafișat pe pagină (are link „Pricing”) | neclar | neverificat | neverificat | da |
| 5 | [play.google.com – JPG to PDF (cubbbixapps)](https://play.google.com/store/apps/details?hl=ro&id=cubbbixapps.imagetopdf) | altul (aplicație Android) | neverificat | gratuit cu limită zilnică; abonament „Pro” lunar sau anual, preț neafișat | actualizată 19 oct. 2026 | nu („fără cont”, după text) | n/a | da |
| 8 | [play.google.com – image to pdf converter (Oxasoft)](https://play.google.com/store/apps/details?hl=ro&id=com.morosoft.imagetopdf) | altul (aplicație Android) | neverificat | gratuit | actualizată 13 iun. 2024 | neverificat | n/a | da |
| 10 | [play.google.com – JPG to PDF: Convert Files](https://play.google.com/store/apps/details?hl=ro&id=com.jpegconverter) | altul (aplicație Android) | neverificat | reclame + achiziții în aplicație, preț neafișat | actualizată 4 iun. 2026 | neverificat | n/a | da |
| 12 | [play.google.com – JPG to PDF Converter PDF Maker](https://play.google.com/store/apps/details?hl=ro&id=com.jpgtopdfconverter.pdfmaker.app) | altul (aplicație Android) | neverificat | reclame + achiziții în aplicație, preț neafișat | actualizată 1 mai 2026 | neverificat | n/a | da |
| 15 | [play.google.com – JPG to PDF Converter (Abro)](https://play.google.com/store/apps/details?hl=ro&id=com.abro.jpgtopdfconverter) | altul (aplicație Android) | neverificat | gratuit, cu reclame | actualizată 22 apr. 2026 | neverificat | n/a | da |
| 17 | [play.google.com – Image & JPG to PDF Converter](https://play.google.com/store/apps/details?hl=ro&id=com.nenotech.imagetopdf.converter) | altul (aplicație Android, 100 K+ descărcări) | neverificat | gratuit, cu reclame | actualizată 8 oct. 2026 | neverificat | n/a | da |
| 18 | [play.google.com – Image to PDF Converter (Appora)](https://play.google.com/store/apps/details?hl=ro&id=com.appora.imagetopdf) | altul (aplicație Android) | neverificat | gratuit, cu reclame | actualizată 16 ian. 2026 | neverificat | n/a | da |

- Ce apare azi: 8 aplicații Android, 1 convertor web blocat (Shutterstock), 1 director (WebCatalog)
- Instrument gratuit funcțional: nu (niciun convertor web verificat; Shutterstock a întors 403)
- Produs plătit și preț: play.google.com (cubbbixapps): abonament „Pro”, preț neafișat; alte două aplicații au achiziții în aplicație, tot fără preț
- Verdict: SLABE (niciun instrument web verificat ca funcțional în primele 10: singurul convertor web e blocat, restul sunt aplicații care nu pot fi testate)
- Riscuri: niciunul dovedit
- Surse blocate: shutterstock.com (403, „Please enable JS and disable any ad blocker”)

## model cv (volum: 9900, familie: 03,09)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: Imagini (poz. 1, „Model CV 2026. Downloadează aici modele de succes!”), AI Overview (poz. 2), People also search (poz. 6), Related searches (poz. 12)
- Rezultatele organice sunt doar 3 (poz. 3, 4, 5).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 3 | [harunpehlivan.arsigo.com](https://harunpehlivan.arsigo.com/en/cvassistant) | instrument? (URL „cvassistant”, fără titlu în SERP) | neverificat | doar titlu din SERP | – | – | neverificat | nu (403) |
| 4 | [pinterest.com](https://www.pinterest.com/pin/709528116288903638/) | altul (pin „Modern CV Template”) | nu | – | neclar | da (pagina afișează doar „Log in / Sign up”) | neverificat | da (conținut ascuns după cont) |
| 5 | [fr.scribd.com](https://fr.scribd.com/document/341281536/Curriculum-Vitae-Model-CV) | document de descărcat (CV completat de o persoană, format Europass vechi) | nu | descărcarea pe Scribd cere cont | neclar | da, pentru descărcare | neverificat | da |

- Ce apare azi: 1 document Scribd, 1 pin Pinterest ascuns după cont, 1 pagină blocată. Deasupra lor: un bloc de imagini și AI Overview.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (niciun instrument funcțional; singurul instrument posibil e blocat, restul sunt un document și un pin ascuns după cont)
- Riscuri: niciunul dovedit
- Surse blocate: harunpehlivan.arsigo.com (403 Forbidden)

## cv europass template (volum: 6600, familie: 09)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: Imagini (poz. 2 și 14), AI Overview (poz. 3), People also search (poz. 6), People also ask (poz. 7)
- Rezultatele organice sunt doar 3 (poz. 1, 4, 5).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | [es.scribd.com](https://es.scribd.com/document/481838985/Europass-CV-template-doc) | document de descărcat (CV Europass completat, DOC/PDF) | nu | descărcarea pe Scribd cere cont | neclar (format Europass vechi) | da, pentru descărcare | neverificat | da |
| 4 | [it.scribd.com](https://it.scribd.com/document/481838985/Europass-CV-template-doc) | document de descărcat (același document ca la poz. 1) | nu | idem | idem | da, pentru descărcare | neverificat | da |
| 5 | [europasscv.ai](https://europasscv.ai/europass-cv-template-word/) | altul (domeniu parcat la Hostinger) | nu (stricat) | – | – | – | neverificat | da |

- Ce apare azi: 2 copii ale aceluiași document Scribd, 1 domeniu parcat. Site-ul oficial Europass nu apare printre rezultate.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (niciun instrument funcțional; singurul site dedicat e un domeniu parcat)
- Riscuri: niciunul dovedit
- Surse blocate: niciuna

## verificare cui anaf (volum: 5400, familie: 04)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2)
- Rezultatele organice sunt doar 5 (poz. 1, 3, 4, 5, 8).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | [contabilitateprofit.ro](https://contabilitateprofit.ro/home/fiscalitate/217-cum-pot-verifica-situatia-contabila-a-unui-partener-comercial-din-romania.html) | articol (cum verifici un partener; trimite la ANAF/MFP) | nu | gratuit | an neclar | nu | neverificat | da |
| 3 | [mfinante.ro](https://mfinante.ro/domenii/informatii-contribuabili/institutii-publice/ucaapi/ghiduri-audit) | pagină a statului (după URL: ghiduri de audit, nu verificare CUI) | neverificat | doar titlu din SERP | – | – | neverificat | nu (conexiune resetată) |
| 4 | [avocatnet.ro](https://www.avocatnet.ro/articol_34711/Ghid-practic-Cum-poti-verifica-situatia-fiscala-a-firmei-tale-fara-sa-te-mai-deplasezi-la-ANAF.html) | articol (ghid situație fiscală) | nu | gratuit | an neclar | nu | neverificat | da |
| 5 | [cabinetexpert.ro](https://www.cabinetexpert.ro/2021-04-13/surse-culegere-informatii-2021-unde-verific-cui-ul-cif-ul-unei-firme-unde-verific-situatia-financiara-fiscala-a-unei-firme.html) | articol (listă de surse) | nu | gratuit | învechit („2021” în titlu) | nu | neverificat | da |
| 8 | [chromewebstore.google.com](https://chromewebstore.google.com/detail/verificare-cui-anaf-%E2%80%93-fir/ojahojeendieobiibpolgaoeblelgbcb) | altul (extensie Chrome Tapselo; caută CUI în API-ul ANAF PlatitorTvaRest v9; 4 utilizatori) | neverificat (cere instalarea extensiei) | preț neafișat | actuală (API v9, e-Factura) | neverificat | n/a | da |

- Ce apare azi: 3 articole (unul din 2021), 1 pagină a MFP fără legătură cu verificarea CUI, 1 extensie Chrome
- Instrument gratuit funcțional: nu (pe pagină nu există niciun verificator; singurul instrument e o extensie care trebuie instalată)
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (căutarea cere un instrument, dar în primele 5 apar doar articole; extensia de pe poz. 8 nu se poate folosi direct în pagină)
- Riscuri: depinde de o instituție a statului (după text: extensia folosește „datele publice ANAF (PlatitorTvaRest v9)”, iar articolele trimit la ANAF/MFP)
- Surse blocate: mfinante.ro (conexiune resetată de server, „Connection reset by peer”)

## calculator consum auto (volum: 3600, familie: 06)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 6), Related searches (poz. 11)
- Primele 10 organice: poz. 1-5, apoi patru aplicații Google Play (poz. 23, 36, 46, 54). În total sunt doar 9.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | [peco-online.ro](https://www.peco-online.ro/calculator.php) | instrument funcțional (cantitate / distanță / consum / cost) | da (test: 200 km, 7 l/100 km → 14,00 l, 149,94 RON) | gratuit | actual (preț precompletat 10,71 RON/l) | nu | OK | da |
| 2 | [gps-online.webshow.ro](https://gps-online.webshow.ro/calculator-consum.html) | instrument (termic, consum real, electric) | câmpuri văzute, cu valori implicite; necalculat de mine | gratuit | actual („2026” în titlu) | nu | OK | da |
| 3 | [calculatoare-utile.ro](https://www.calculatoare-utile.ro/calculator/consum-combustibil) | instrument (litri + km → l/100 km) | câmpuri și buton „Calculează” văzute; netestat | gratuit | neclar | nu | OK | da |
| 4 | [leaveboard.com](https://leaveboard.com/ro/calculator-consum/) | instrument funcțional (pe site-ul unui soft HR) | da (rezultat afișat: 100 km, 6 l/100 km → 6,0 l, 45 RON) | gratuit | neclar | nu | OK | da |
| 5 | [dosar-auto.ro](https://www.dosar-auto.ro/ro/planificator/) | instrument funcțional (cost drum, rută pe hartă, compară combustibili) | da (câmpuri; exemple calculate pe pagină) | gratuit | actual („prețuri actualizate azi, 15.11.2026”) | nu | OK | da |
| 23 | [play.google.com – Calculator de combustibil](https://play.google.com/store/apps/details?hl=ro&id=com.mg.simplelicznik) | altul (aplicație Android, 500 K+ descărcări) | neverificat | gratuit, cu reclame | actualizată 29 sept. 2024 | neverificat | n/a | da |
| 36 | [play.google.com – Fuel Consumption Calculator](https://play.google.com/store/apps/details?hl=ro&id=kb2.soft.fuelcalculator) | altul (aplicație Android) | neverificat | neafișat | actualizată 27 aug. 2025 | neverificat | n/a | da |
| 46 | [play.google.com – Gas Mileage Calculator](https://play.google.com/store/apps/details?hl=ro&id=com.nikk797tech.gas_mileage_calculator) | altul (aplicație Android) | neverificat | neafișat | actualizată 26 feb. 2026 | neverificat | n/a | da |
| 54 | [play.google.com – Fuel Average Calculator](https://play.google.com/store/apps/details?hl=ro&id=com.fuelaverage.calculator) | altul (aplicație Android) | neverificat | neafișat | actualizată 22 iul. 2026 | neverificat | n/a | da |

- Ce apare azi: 5 instrumente web (3 verificate ca funcționale), 4 aplicații Android (pe poz. 23-54)
- Instrument gratuit funcțional: da (peco-online.ro)
- Produs plătit și preț: niciunul găsit
- Verdict: PUTERNICE (peco-online.ro, leaveboard.com și dosar-auto.ro, în primele 5, funcționează, sunt gratuite, fără cont și merg pe telefon)
- Riscuri: niciunul dovedit
- Surse blocate: niciuna

## calculator credit (volum: 2900, familie: 01)
- Data colectării SERP: 2026-10-02
- Elemente care nu sunt organice: AI Overview (poz. 9), Related searches (poz. 11)
- Primele 10 organice: poz. 1-8, 10, 12.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | [bancatransilvania.ro](https://www.bancatransilvania.ro/credite/calculatorul-de-rate) | instrument (după titlu: „Calculator de rate”) | neverificat | doar titlu din SERP | – | – | neverificat | nu (403) |
| 2 | [ing.ro](https://ing.ro/persoane-fizice/credite/ipotecar) | instrument funcțional (simulator credit ipotecar, pe pagina produsului) | da (valoare proprietate, avans, perioadă → „Valoare împrumutată 450.001,00 lei”) | gratuit | actual (dobânzi 4,79%-6,59% afișate) | nu | OK | da |
| 3 | [brd.ro](https://www.brd.ro/calculatoare/calculatoare-de-credit/calculator-de-credit) | instrument funcțional (credit personal) | da (50.000 lei / 5 ani → prima rată 1.043,07 lei, DAE 8,35%) | gratuit | actual | nu | OK | da |
| 4 | [raiffeisen.ro](https://www.raiffeisen.ro/ro/persoane-fizice/produsele-noastre/credite.html) | altul (pagina de credite a băncii) | neverificat | doar titlu din SERP | – | – | neverificat | nu („Just a moment…”) |
| 5 | [bcr.ro](https://www.bcr.ro/ro/persoane-fizice/calculatoare) | director (pagină cu două linkuri spre calculatoarele BCR) | nu pe pagină (doar linkuri) | gratuit | neclar | nu | OK | da |
| 6 | [unicredit.ro](https://www.unicredit.ro/ro/persoane-fizice/Credite/credite-ipoteca/Calculator-ipotecare.html) | instrument (după titlu: „Calculator credit ipotecar”) | neverificat | doar titlu din SERP | – | – | neverificat | nu (403, „Request Failed”, BrightCloud) |
| 7 | [finzoom.ro](https://www.finzoom.ro/) | director (comparator, după titlu) | neverificat | doar titlu din SERP | – | – | neverificat | nu (conexiune întreruptă, HTTP/2 CANCEL) |
| 8 | [cec.ro](https://www.cec.ro/persoane-fizice/credite/credite-nevoi-personale/credit-online-de-nevoi-personale) | altul (pagina produsului „credit online de nevoi personale”) | neverificat | doar titlu din SERP | – | – | neverificat | nu (403 CloudFront) |
| 10 | [garantibbva.ro](https://www.garantibbva.ro/persoane-fizice/calculator-rate-credit/) | instrument funcțional | da (60.000 RON / 24 luni → rata 2.766,80 RON/lună, dobândă 7,20%) | gratuit | actual | nu | OK | da |
| 12 | [finance.imobiliare.ro](https://finance.imobiliare.ro/calculator/credite-ipotecare) | instrument funcțional (al unui broker de credite) | da (90.000 €, avans 15%, 30 ani → rata lunară de la 2.123 RON) | gratuit | actual | nu | OK | da |

- Ce apare azi: 4 instrumente funcționale (ING, BRD, Garanti, Imobiliare), 1 pagină cu linkuri (BCR), 5 pagini de bancă sau comparator blocate (BT, Raiffeisen, UniCredit, finzoom, CEC)
- Instrument gratuit funcțional: da (brd.ro)
- Produs plătit și preț: niciunul găsit (sunt simulatoare gratuite ale băncilor; nu se vinde niciun instrument)
- Verdict: PUTERNICE (ING pe poz. 2 și BRD pe poz. 3 funcționează, sunt actuale, fără cont și merg pe telefon)
- Riscuri: niciunul dovedit
- Surse blocate: bancatransilvania.ro (403 „Acces blocat”), raiffeisen.ro („Just a moment…”), unicredit.ro (403), cec.ro (403 CloudFront), finzoom.ro (conexiune întreruptă)

## adeverinta salariat (volum: 2400, familie: 09)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: Imagini (poz. 1, „Adeverinta de salariat”), AI Overview (poz. 2)
- Rezultatele organice sunt doar 3 (poz. 3, 4, 5).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 3 | [scribd.com](https://www.scribd.com/document/345417364/adeverinta-de-salariu-doc) | document de descărcat („Adeverință de salariu”, anexă bancară) | nu | descărcarea pe Scribd cere cont | învechit („Versiune: Noiembrie 2005”, B.I./C.I.) | da, pentru descărcare | neverificat | da |
| 4 | [tpu.ro](https://tpu.ro/legislatie-politic-social/pentru-ce-i-adeverinta-de-salariat-mai-pe-intelesul-fiecaruia-si-fara-copy-paste-daca-s-ar-putea-multumesc-in-avans/) | forum (întrebare din 16 ianuarie 2021) | nu | gratuit | învechit (2021) | da, pentru răspuns | neverificat | da |
| 5 | [thetaserv.ro](https://thetaserv.ro/product/kit-hr-adeverinte-salariati/) | produs plătit (kit HR: adeverințe de salariat, venit și vechime) | nu (produs de descărcat, nu generator) | 49,00 lei („Preț de intrare”) | actual (pomenește registrul electronic) | da (pagina are cont și coș de cumpărături) | neverificat | da |

- Ce apare azi: 1 document vechi pe Scribd (2005), 1 forum (2021), 1 kit plătit
- Instrument gratuit funcțional: nu
- Produs plătit și preț: thetaserv.ro, 49,00 lei
- Verdict: SLABE (niciun instrument și niciun model gratuit actual; doar un document din 2005, un forum și un produs plătit)
- Riscuri: juridic (model de document cu efect juridic, o adeverință emisă de angajator; după text, thetaserv.ro: „Adeverința de venit din kit este cea emisă de angajator”)
- Surse blocate: niciuna

## convertor valutar online (volum: 2400, familie: 05,12)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: casetă de conversie valutară Google (poz. 1), Related searches (poz. 12)
- Rezultatele organice sunt doar 8: patru în primele 10 (poz. 2-5), apoi patru aplicații Google Play (poz. 21, 35, 43, 54).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | [doviz.com](https://www.doviz.com/doviz-cevirici) | instrument funcțional (în turcă, centrat pe lira turcească) | da (câmpuri cu valori calculate afișate: 1.000 → conversii) | gratuit | actual | nu | OK | da |
| 3 | [lt.coinmill.com](https://lt.coinmill.com/) | instrument (în lituaniană) | câmpuri (sumă, din, în) și buton văzute; netestat | gratuit | actual (cursuri din 14 noiembrie 2026) | nu | OK | da |
| 4 | [solverspro.com](https://solverspro.com/finance/currency-converter/) | instrument (în engleză, după titlu) | nu (0 câmpuri randate în browser) | gratuit | neclar | nu | OK | da |
| 5 | [justcnw.com](https://justcnw.com/currency) | instrument (în engleză) | câmpuri și buton „Convert” văzute; netestat | gratuit | neclar | nu | nu (405px) | da |
| 21 | [play.google.com – Curs Valutar](https://play.google.com/store/apps/details?hl=en_GB&id=dev.thewebers.ro) | altul (aplicație Android) | neverificat | achiziții în aplicație, preț neafișat | actualizată 16 sept. 2025 | neverificat | n/a | da |
| 35 | [play.google.com – Currency Converter (Wontera)](https://play.google.com/store/apps/details?hl=ro&id=com.wontera.currency_converter) | altul (aplicație Android) | neverificat | gratuit, cu reclame | actualizată 19 feb. 2026 | neverificat | n/a | da |
| 43 | [play.google.com – Currency Converter - Exchange](https://play.google.com/store/apps/details?hl=ro&id=com.currency.currencyexchange) | altul (aplicație Android) | neverificat | gratuit, cu reclame | învechită (14 dec. 2020) | neverificat | n/a | da |
| 54 | [play.google.com – Exchange Rate Calculator](https://play.google.com/store/apps/details?hl=ro&id=com.currencyconverterworldwide) | altul (aplicație Android) | neverificat | reclame + achiziții în aplicație, preț neafișat | actualizată 5 nov. 2026 | neverificat | n/a | da |

- Ce apare azi: 1 instrument funcțional în turcă, 2 convertoare străine netestate (lituaniană, engleză), 1 pagină fără convertor randat, 4 aplicații Android. Deasupra lor: caseta de conversie a Google. Niciun site românesc printre rezultate.
- Instrument gratuit funcțional: da (doviz.com, în turcă)
- Produs plătit și preț: niciunul găsit (aplicațiile au achiziții în aplicație, fără preț afișat)
- Verdict: MEDII (am confirmat un singur instrument funcțional în primele 5, și acela în turcă; celelalte nu au fost confirmate)
- Riscuri: niciunul dovedit
- Surse blocate: niciuna

## calculator concediu medical (volum: 1900, familie: 01,09)
- Data colectării SERP: 2026-10-02
- Elemente care nu sunt organice: AI Overview (poz. 1)
- Primele 10 organice: poz. 2-11.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | [gatadecompletat.ro](https://gatadecompletat.ro/calculator-concediu-medical/) | articol (titlu „Calculator…”, dar pagina are 0 câmpuri) | nu | gratuit | an neclar | nu | OK | da |
| 3 | [contabilsef.md](https://www.contabilsef.md/baza-de-calcul-pentru-indemnizatia-de-concediu-medical) | articol (Republica Moldova, alte reguli) | nu | gratuit; site cu abonamente | neclar | nu | neverificat | da |
| 4 | [portalcodulmuncii.ro](https://www.portalcodulmuncii.ro/concediu-de-risc-maternal-baza-de-calcul-13219.htm) | articol (risc maternal) | nu | gratuit | neclar | nu | neverificat | da |
| 5 | [nexuserp.ro](https://www.nexuserp.ro/caut/concediu) | altul (pagina de căutare internă a unui soft ERP, 35 de rezultate) | nu | soft cu plată, preț neafișat pe pagină | 2026 (noutate din 14 apr. 2026) | nu | neverificat | da |
| 6 | [facebook.com](https://www.facebook.com/groups/salariiresurseumane/posts/26731083359893211/) | forum (grup „Salarizare & Resurse Umane”) | nu | – | neclar | da (se vede doar titlul) | neverificat | da (doar titlul) |
| 7 | [folositor.ro](https://folositor.ro/ghid/concediu-medical-vs-concediu-de-odihna-2026) | articol (ghid, concediu medical vs. de odihnă) | nu | gratuit | actual („Actualizat: 13 noiembrie 2026”) | nu | neverificat | da |
| 8 | [legislatiamuncii.manager.ro](https://legislatiamuncii.manager.ro/a/28406/baza-de-calcul-concediu-medical-de-maternaritate-cumul-pfa-si-venituri-din-salarii.html) | articol (maternitate, cumul PFA) | nu | gratuit | neclar | nu | neverificat | da |
| 9 | [workly.ro](https://workly.ro/en/utile/calculator-indemnizatie-concediu-medical-2026/) | instrument funcțional (pe site-ul unui soft HR; versiunea în engleză) | da (valori implicite 6.300 lei, 10 zile → indemnizație netă 965,25 lei, împărțită angajator/FNUASS) | gratuit | actual („2026 rates”) | nu | OK | da |
| 10 | [de.scribd.com](https://de.scribd.com/doc/75846784/nota-calcul-mzbci) | document de descărcat (formular gol „Notă calcul” CAS NT) | nu | descărcarea pe Scribd cere cont | învechit (document încărcat demult, ID 75846784) | da, pentru descărcare | neverificat | da |
| 11 | [reddit.com](https://www.reddit.com/r/AskUK/comments/1nlu8ur/where_to_find_average_holiday_pay_calculator_or/?tl=ro) | forum (r/AskUK, Marea Britanie, tradus automat) | nu | – | neclar | neverificat | neverificat | da (pagină goală la curl) |

- Ce apare azi: 1 instrument funcțional (poz. 9), 5 articole (unul din Moldova), 2 forumuri, 1 pagină de soft, 1 formular pe Scribd
- Instrument gratuit funcțional: da (workly.ro, poz. 9)
- Produs plătit și preț: niciunul cu preț afișat (nexuserp.ro și workly.ro sunt softuri HR cu plată, dar prețul nu apare pe paginile deschise)
- Verdict: MEDII (singurul instrument funcțional e pe poz. 9; restul sunt articole, inclusiv cel de pe poz. 2, care are „calculator” în titlu)
- Riscuri: depinde de o instituție a statului (după text: workly.ro împarte indemnizația între angajator și „FNUASS (from day 7)”, cu cotele CAS/CASS)
- Surse blocate: niciuna (facebook.com și reddit.com nu au arătat conținut la curl, dar nu au întors cod de blocare)

## verificare amenzi dupa cnp (volum: 1900, familie: 04,06)
- Data colectării SERP: 2026-08-31
- Elemente care nu sunt organice: AI Overview (poz. 1), People also ask (poz. 7), Related searches (poz. 12)
- Primele 10 organice: poz. 2-6, 8-11, 13.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | [hub.mai.gov.ro](https://hub.mai.gov.ro/serviciu/view?id=63) | pagină a statului (serviciu MAI: istoric sancțiuni, puncte, status permis) | serviciu real, dar doar după autentificare | gratuit („Taxe: Gratuit”) | actual (pagină actualizată 09.04.2026) | da („doar de către utilizatorii care au un cont de utilizator validat”) | OK (Playwright a întors HTTP 500) | da (curl) |
| 3 | [dosar-auto.ro](https://www.dosar-auto.ro/ro/verificare-amenzi-puncte/) | director (ghid cu linkuri spre HUB MAI, Ghișeul.ro, DGPCI) | nu („nu cere CNP-ul și nu face verificarea în locul instituției”) | gratuit | actual (titlu „2027”) | nu | OK | da |
| 4 | [ghiseul.ro](https://www.ghiseul.ro/) | pagină a statului (plăți online) | neverificat | doar titlu din SERP | – | – | neverificat | nu (403) |
| 5 | [youtube.com](https://www.youtube.com/watch?v=1AB0wPnjmVE) | video („Șoferii își pot verifica amenzile și punctele de penalizare online”) | nu | gratuit | neclar | nu | neverificat | da (doar titlul) |
| 6 | [mai.gov.ro](https://www.mai.gov.ro/faq/sunt-o-victima-a-violentei-in-familie-ce-trebuie-sa-fac/) | pagină a statului (FAQ „Cum poate fi obținut istoricul sancțiunilor rutiere?”) | nu | gratuit | neclar | nu | neverificat | da |
| 8 | [ditl5.ro](https://ditl5.ro/amenzi/) | pagină a statului (taxe locale Sector 5, amenzi) | nu | gratuit | neclar | nu | neverificat | da |
| 9 | [bpr.politiaromana.ro](https://bpr.politiaromana.ro/ro/informatii-utile/istoricul-de-sanctiuni-rutiere-prin-e-mail-sau-prin-posta) | pagină a statului (istoric sancțiuni prin e-mail sau poștă, după URL) | neverificat | doar titlu din SERP | – | – | neverificat | nu (refuzat, mesaj de securitate) |
| 10 | [ghiseul.ro](https://www.ghiseul.ro/ghiseul/public/amenzi) | pagină a statului („Plată amendă”) | neverificat | doar titlu din SERP | – | – | neverificat | nu (403) |
| 11 | [youtube.com](https://www.youtube.com/shorts/37v8rqJX7eU) | video (Short, același subiect) | nu | gratuit | neclar | nu | neverificat | da (doar titlul) |
| 13 | [taxeimpozite4.ro](https://www.taxeimpozite4.ro/amenzi/) | pagină a statului (DGITL Sector 4, amenzi) | nu | gratuit | neclar | nu | neverificat | da |

- Ce apare azi: 7 pagini ale statului (MAI, Poliția Română, Ghișeul.ro, DITL-uri; 3 blocate), 1 director, 2 video-uri
- Instrument gratuit funcțional: nu (singurul serviciu real, HUB MAI, cere cont; Ghișeul.ro a fost blocat)
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (niciun instrument funcțional fără cont; singurul serviciu verificat e ascuns după autentificare)
- Riscuri: depinde de o instituție a statului (după text: HUB MAI e „Furnizat de Poliţia Română”; dosar-auto.ro trimite la HUB MAI și Ghișeul.ro)
- Surse blocate: ghiseul.ro (403, ambele adrese), bpr.politiaromana.ro (refuz cu mesaj „how to fix it, please visit the web page mentioned above”)

## calculator salariu minim 2025 (volum: 1600, familie: 01)
- Data colectării SERP: 2026-09-02
- Elemente care nu sunt organice: AI Overview (poz. 3), People also ask (poz. 5), Related searches (poz. 12)
- Primele 10 organice: poz. 1, 2, 4, 6-11, 13.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | [calculator-salarii.ro](https://www.calculator-salarii.ro/calcul-salariu-net/anul-2025/) | instrument funcțional (brut → net, alegi anul 2025/2026/2027) | da (test: 4.050 brut, anul 2025 → net 2.574 lei) | gratuit | actual (anul 2025 cerut + 2026, „Actualizat 2026”) | nu | OK | da |
| 2 | [undelucram.ro](https://www.undelucram.ro/ro/calculator-salariu-net-sau-brut-romania) | instrument funcțional (brut / net / cost companie) | da (câmp precompletat cu 4.325 + tabel de rezultat) | gratuit | actual („2026”; arată și evoluția salariului minim) | nu | OK | da |
| 4 | [calculator-salarii.ro](https://www.calculator-salarii.ro/salariu-minim-pe-economie-2025/) | instrument funcțional (calcul precompletat pentru minimul din 2025) | da (4.050 brut, 2025 → tabel calculat: CAS 938, CASS 375, impozit 163) | gratuit | actual pentru 2025 | nu | OK | da |
| 6 | [salariile.ro](https://salariile.ro/) | instrument funcțional (brut ↔ net, anul 2024-2026, luna) | da (calculul rulează; exemplu afișat „net 2.455 lei”) | gratuit | actual (2026) | nu | OK | da |
| 7 | [salaria.ro](https://salaria.ro/) | instrument funcțional (mai multe tipuri de contract) | da (4.325 brut → 2.699 net, cost total 4.418) | gratuit | actual (2026, inclusiv „2026 iul.”) | nu | nu (481px) | da |
| 8 | [calculatoare-salarizare.ro](https://www.calculatoare-salarizare.ro/salariu.php) | instrument (fluturaș 2026; arhivă de calculatoare 2015-2025) | instrucțiuni văzute; în browser apare doar câmpul de căutare, calculatorul nu a fost găsit | gratuit | actual (2026) | nu | nu (1391px) | da |
| 9 | [impozitsalariu.ro](https://www.impozitsalariu.ro/) | instrument funcțional | da (câmp brut + „Calculează”; exemplu calculat 4.325 brut → 2.455 net) | gratuit | actual (2026) | nu | OK | da |
| 10 | [leaveboard.com](https://leaveboard.com/ro/calculator-salariu/) | instrument funcțional (pe site-ul unui soft HR) | da (4.325 brut → 2.699 net, afișat) | gratuit | actual (2026) | nu | nu (405px) | da |
| 11 | [nowium.com](https://nowium.com/calculator-de-salarii-2025/) | altul (pagina unei firme de contabilitate; în browser nu apare niciun calculator) | nu | – | după titlu, 2025 | nu | OK | da (curl a eșuat de două ori, Playwright a mers) |
| 13 | [jobinfo.ro](https://jobinfo.ro/) | instrument funcțional | da (precompletat 4.050 brut → net 2.553 RON) | gratuit | parțial: titlul spune „2026”, dar valoarea implicită 4.050 e minimul din 2025 | nu | OK | da |

- Ce apare azi: 9 calculatoare de salariu (8 verificate ca funcționale), 1 pagină de firmă fără calculator. Cele mai multe sunt la zi pentru 2026; poz. 1 și 4 au și anul 2025.
- Instrument gratuit funcțional: da (calculator-salarii.ro)
- Produs plătit și preț: niciunul găsit
- Verdict: PUTERNICE (calculator-salarii.ro, pe poz. 1 și 4, și undelucram.ro, pe poz. 2, funcționează, sunt actuale, fără cont și merg pe telefon)
- Riscuri: depinde de o instituție a statului (după text: salariul minim și cotele CAS 25%, CASS 10%, impozit 10% se schimbă „de la an la an, uneori și în iulie” — salariile.ro); sezonier (după text: căutarea numește anul fiscal „2025”)
- Surse blocate: niciuna

## Rezumat

| Căutare | Ce apare azi | Instrument gratuit funcțional | Produs plătit și preț | Verdict | Riscuri |
|---|---|---|---|---|---|
| convertor valutar | 2 instrumente, 1 convertor BNR, 1 calculator de casă de schimb, 3 aplicații Android | da (cursbnr.ro) | niciunul găsit | PUTERNICE | depinde de o instituție a statului (BNR) |
| transforma jpg in pdf | 8 aplicații Android, 1 convertor blocat, 1 director | nu | aplicație cubbbixapps: abonament Pro, preț neafișat | SLABE | – |
| model cv | 1 document Scribd, 1 pin Pinterest ascuns după cont, 1 pagină blocată (doar 3 organice) | nu | niciunul găsit | SLABE | – |
| cv europass template | 2 copii ale aceluiași document Scribd, 1 domeniu parcat (doar 3 organice) | nu | niciunul găsit | SLABE | – |
| verificare cui anaf | 3 articole, 1 pagină MFP (blocată), 1 extensie Chrome | nu | niciunul găsit | SLABE | depinde de o instituție a statului (ANAF) |
| calculator consum auto | 5 instrumente web, 4 aplicații Android | da (peco-online.ro) | niciunul găsit | PUTERNICE | – |
| calculator credit | 4 instrumente de bancă sau broker, 1 pagină cu linkuri, 5 pagini blocate | da (brd.ro) | niciunul găsit | PUTERNICE | – |
| adeverinta salariat | 1 document din 2005, 1 forum, 1 kit plătit (doar 3 organice) | nu | thetaserv.ro, 49,00 lei | SLABE | juridic |
| convertor valutar online | 1 instrument în turcă, 3 convertoare străine (netestate sau goale), 4 aplicații Android; caseta Google deasupra | da (doviz.com, în turcă) | niciunul găsit | MEDII | – |
| calculator concediu medical | 1 instrument (poz. 9), 5 articole, 2 forumuri, 1 pagină de soft, 1 formular | da (workly.ro, poz. 9) | niciunul cu preț afișat | MEDII | depinde de o instituție a statului (FNUASS) |
| verificare amenzi dupa cnp | 7 pagini ale statului (3 blocate), 1 director, 2 video-uri | nu (HUB MAI cere cont) | niciunul găsit | SLABE | depinde de o instituție a statului (MAI / Poliția Română) |
| calculator salariu minim 2025 | 9 calculatoare (8 funcționale), 1 pagină de firmă | da (calculator-salarii.ro) | niciunul găsit | PUTERNICE | depinde de o instituție a statului (salariu minim, cote); sezonier (anul 2025) |
