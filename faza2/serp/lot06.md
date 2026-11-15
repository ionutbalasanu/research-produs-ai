# Lot 06

Cum am lucrat: liste SERP din Ubersuggest `serp_analysis` (language=ro, locId=2642, limit=20, fără refresh). Am luat numai rezultatele organice aflate în primele 10 poziții SERP. Coloana „Poz” arată poziția SERP, iar în paranteză rangul organic. Paginile le-am deschis cu `citeste.sh` (curl simplu), pe https. Paginile încărcate prin JavaScript le-am deschis cu Playwright, iar afișarea pe telefon am verificat-o cu iPhone 13 (scrollWidth <= innerWidth). La unele calculatoare am introdus o valoare de test. „Primele 5” din verdict înseamnă primele 5 rezultate organice.

---

## cv europass (volum: 40500, familie: 09)
- Data colectării SERP: 2026-11-15 (primul apel n-a întors nimic, al doilea apel, tot fără refresh, a întors lista)
- Elemente care nu sunt organice: AI Overview (poz. 2), Imagini (poz. 3 și 12)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 (1) | fr.scribd.com — https://fr.scribd.com/document/297723850/eu-cv-en | document de descărcat (șablon Europass vechi, în engleză, pe Scribd) | nu e instrument | vizualizare gratuită; descărcarea cere cont Scribd | învechit (formatul vechi de CV Europass, cu „Insert photograph”) | da, pentru descărcare | neverificat | da (curl) |
| 4 (2) | it.scribd.com — https://it.scribd.com/document/481838985/Europass-CV-template-doc | document de descărcat (șablon Europass, DOC, pe Scribd) | nu e instrument | ca mai sus | an nevizibil | da, pentru descărcare | neverificat | da (curl) |
| 5 (3) | id.scribd.com — https://id.scribd.com/document/440141650/CV-Europass-RO | document de descărcat (CV Europass completat, în română, al unei persoane) | nu e instrument | ca mai sus | an nevizibil | da, pentru descărcare | neverificat | da (curl) |

- Ce apare azi: 3 documente pe Scribd (șabloane sau CV-uri încărcate de utilizatori). Editorul oficial Europass nu apare în primele 10 poziții.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit (Scribd cere cont pentru descărcare; prețul nu e afișat pe pagină)
- Verdict: SLABE (verdict pe 3 rezultate organice). La o căutare care cere un instrument apar doar documente pe Scribd.
- Riscuri: nu am găsit dovezi
- Surse blocate: niciuna

---

## calcul medie facultate (volum: 12100, familie: 08)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), Imagini (poz. 8 și 20)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 (1) | mojput.com — https://www.mojput.com/kalkulator-fakulteti | instrument funcțional, dar irelevant (calculator de puncte pentru admitere în Croația, în croată) | parțial: are pași și câmpuri (program, note, maturitate), dar nu l-am parcurs până la rezultat | gratuit; există un buton „PRO” | „Bodovne formule 2025”, reguli pentru Croația | nu pentru calculator | da (390 ≤ 390) | da (Playwright) |
| 3 (2) | mcpcalc.com — https://mcpcalc.com/education | director, agregator (index în engleză cu calculatoare GPA, „weighted grade” etc.) | pagina nu calculează nimic, are doar linkuri | gratuit | an nevizibil | nu | da | da |
| 4 (3) | mediacollege.com — https://www.mediacollege.com/misc/utilities/calculator.html | altul (pagină de „Calculator” generic, fără calculator vizibil) | nu: n-am văzut niciun câmp | — | an nevizibil | nu | da (409 ≤ 409) | da |
| 5 (4) | dynamicontent.net — https://dynamicontent.net/dcv2/indiv_calc.php?calc=38&key=nwcpa | instrument funcțional, dar irelevant (economii pentru facultate, SUA, USD) | da: are câmpuri și calculează (ex. „Total expenses $357,380.06”) | gratuit | an nevizibil | nu | da | da (Playwright) |

- Ce apare azi: 2 instrumente irelevante (Croația; economii pentru facultate în SUA), 1 director în engleză, 1 pagină goală. Niciun calculator românesc de medie.
- Instrument gratuit funcțional: nu (niciunul pentru media de la facultate în România)
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (verdict pe 4 rezultate organice). Niciun instrument funcțional pentru căutare; rezultatele sunt străine sau irelevante.
- Riscuri: nu am găsit dovezi
- Surse blocate: niciuna

---

## calculator credit nevoi personale (volum: 8100, familie: 01)
- Data colectării SERP: 2026-10-01
- Elemente care nu sunt organice: AI Overview (poz. 5), „People also search” (poz. 6)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 (1) | ing.ro — https://ing.ro/persoane-fizice/credite/ing-personal | instrument funcțional (calculator pe pagina de produs a băncii) | da: test cu 30.000 lei → „Rată lunară: 659,63 lei”, DAE 15,20%, total 41.769,26 lei | gratuit (calculatorul); creditul e produsul băncii | actual (dobânzi afișate azi; fără an) | nu | da (390 ≤ 390) | da (Playwright) |
| 2 (2) | bancatransilvania.ro — https://www.bancatransilvania.ro/credite/calculatorul-de-rate | instrument (după titlu) | neverificat | — | — | — | neverificat | nu: 403 „Acces blocat”, doar titlu din SERP |
| 3 (3) | brd.ro — https://www.brd.ro/calculatoare/calculatoare-de-credit/calculator-de-credit | instrument funcțional | da: rezultat afișat implicit (50.000 lei/5 ani → prima rată 1.043,07 lei, DAE 8,35%); are selectori. Nu am reușit testul cu altă valoare (câmpul e un slider) | gratuit | actual (dobânzi curente; fără an) | nu | da | da (Playwright) |
| 4 (4) | bcr.ro — https://www.bcr.ro/ro/persoane-fizice/calculatoare | director (pagină cu linkuri spre calculatoarele BCR) | pagina nu calculează nimic | gratuit | an nevizibil | nu | da | da |
| 7 (5) | raiffeisen.ro — …/credit-de-nevoi-personale-fara-ipoteca.html | produs (pagină de credit, după titlu) | neverificat | — | — | — | neverificat | nu: 403 „Just a moment”, doar titlu din SERP |
| 8 (6) | cec.ro — …/credit-online-de-nevoi-personale | produs (pagină de credit, după titlu) | neverificat | — | — | — | neverificat | nu: 403 CloudFront, doar titlu din SERP |
| 9 (7) | garantibbva.ro — https://www.garantibbva.ro/persoane-fizice/calculator-rate-credit/ | instrument funcțional | da: test cu 30.000 lei → „Valoarea ratei 1.420,90 RON/Lună”, DAE 13,85% | gratuit | actual (fără an) | nu | da | da (Playwright) |
| 10 (8) | finzoom.ro — https://www.finzoom.ro/ | agregator (după titlu) | neverificat | — | — | — | neverificat | nu: eroare de conexiune la curl, 502 la Playwright; doar titlu din SERP |

- Ce apare azi: 3 calculatoare de bancă funcționale (ING, BRD, Garanti BBVA), 1 pagină-director (BCR), 2 pagini de produs bancar blocate, 1 calculator de bancă blocat (BT), 1 agregator care n-a răspuns
- Instrument gratuit funcțional: da (ing.ro)
- Produs plătit și preț: calculatoarele sunt gratuite. Produsul vândut este creditul bancar: ING arată dobândă 5,99–11,49% și comision de analiză 200 lei; BRD arată dobândă între 5,70% și 20,68%
- Verdict: PUTERNICE (verdict pe 8 rezultate organice). În primele 5 organice sunt două calculatoare funcționale, fără cont, cu dobânzi curente (ING, BRD).
- Riscuri: nu am găsit dovezi (rezultatul depinde de oferta fiecărei bănci, nu de o instituție a statului)
- Surse blocate: bancatransilvania.ro (403), raiffeisen.ro (403 „Just a moment”), cec.ro (403 CloudFront), finzoom.ro (conexiune întreruptă / 502)

---

## calculator impozit casa 2026 (volum: 5400, familie: 01,07)
- Data colectării SERP: 2026-10-01
- Elemente care nu sunt organice: „People also ask” (poz. 3)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 (1) | bizbrasov.ro — https://bizbrasov.ro/2025/12/22/brasov-impozite-casa-masina-2026/ | articol (impozite locale Brașov 2026) | nu e instrument | gratuit | actual (22.12.2025, despre 2026) | nu | neverificat | da |
| 2 (2) | digigov.ro — https://digigov.ro/calculatoare/pensie | instrument funcțional, dar irelevant (calculator de pensie) | da: are câmpuri (stagiu, salariu); n-am făcut test | gratuit (site-ul vinde documente) | 2026 | nu | da | da (Playwright) |
| 4 (3) | facebook.com — https://www.facebook.com/groups/580327073834748/posts/1373876014479846/ | forum (postare în grup Facebook, „Cum se calculează impozitul pe clădiri – 2026”) | nu e instrument | — | 2026 (titlu) | conținutul nu e vizibil fără cont | neverificat | parțial: doar titlul |
| 5 (4) | simulequa.com — https://www.simulequa.com/ro/blog/calcul-salariu-net-romania-2026-cas-cass-impozit-it | articol (despre salariul net, irelevant) | nu | gratuit | 2026 | nu | neverificat | da |
| 6 (5) | folositor.ro — https://folositor.ro/harta-site | director (hartă de site cu linkuri, inclusiv ghidul „Impozit locuință 2026 — calcul, termene…”) | pagina nu calculează nimic; n-am văzut în listă un calculator de impozit pe clădire | gratuit | 2026 | nu | neverificat | da |
| 7 (6) | capital.ro — https://www.capital.ro/impozitul-pe-locuinta-2026-… | articol (după titlu) | nu | — | 2026 (titlu) | — | neverificat | nu: 429, doar titlu din SERP |
| 8 (7) | steuergo.de — https://www.steuergo.de/ro/rechner/riester-rechner | instrument, dar irelevant (pensie Riester, Germania) | are câmpuri; n-am făcut test | site comercial („Prețuri”) | 2026 | nu pentru calculator | neverificat | da |
| 9 (8) | cronicavj.ro — https://cronicavj.ro/2025/12/14/cand-si-cat-vom-plati-impozitele-si-taxele-pe-2026/ | articol (după titlu) | nu | — | 2026 (titlu) | — | neverificat | nu: 502 la tunel, doar titlu din SERP |
| 10 (9) | facebook.com — https://www.facebook.com/groups/1287571791919418/posts/1744760402867219/ | forum (grup Facebook, „2.677 lei/mp la calcularea impozitului pe locuință”) | nu | — | an nevizibil | conținutul nu e vizibil fără cont | neverificat | parțial: doar titlul |

- Ce apare azi: 4 articole, 2 postări în grupuri Facebook, 1 director, 2 calculatoare irelevante (pensie RO, pensie Riester DE). Niciun calculator de impozit pe casă.
- Instrument gratuit funcțional: nu (niciunul pentru impozitul pe clădire)
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (verdict pe 9 rezultate organice). Niciun instrument funcțional pentru căutare; doar articole, grupuri și calculatoare pentru alte subiecte.
- Riscuri: depinde de o instituție a statului (impozitul pe clădiri se stabilește prin hotărârile consiliilor locale; după textul articolului bizbrasov și al titlurilor capital/cronicavj); sezonier (căutarea numește anul fiscal 2026, după text)
- Surse blocate: capital.ro (429), cronicavj.ro (502 la conexiune)

---

## calculator salariu brut net (volum: 4400, familie: 01)
- Data colectării SERP: 2026-08-28
- Elemente care nu sunt organice: niciunul în primele 10 („related searches” la poz. 11)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 (1) | calculator-salarii.ro — https://www.calculator-salarii.ro/calcul-salariu-net/ | instrument funcțional | da: test 6.000 brut → „salariu net de 3523 lei”, cost angajator 6.135 lei | gratuit | 2026 (selector 2025–2027) | nu | da (390 ≤ 390) | da (Playwright) |
| 2 (2) | salaria.ro — https://salaria.ro/ | instrument funcțional | da: test 6.000 brut → CAS 1500, CASS 600, impozit 377 | gratuit | 2026 („valabil din Iulie 2026”) | nu | parțial: pagina se lățește la 481 px, dar fără scroll orizontal (481 ≤ 481) | da (Playwright) |
| 3 (3) | impozitsalariu.ro — https://www.impozitsalariu.ro/ | instrument funcțional | da: test 6.000 → „Primești în mână 3.523 RON” | gratuit | 2026 | nu | da | da (Playwright) |
| 4 (4) | salariile.ro — https://salariile.ro/ | instrument funcțional | da: test 6.000 → „Salariu net 3.523 lei” | gratuit | 2026 | nu | da | da (Playwright) |
| 5 (5) | paylab.ro — https://www.paylab.ro/salariu-calculator | instrument (formular) | câmpuri văzute (brut, tichete, persoane în întreținere); rezultatul testului nu l-am putut citi | gratuit | 2026 | nu | da | da (Playwright) |
| 6 (6) | calculatorvenituri.sdworx.ro — https://www.calculatorvenituri.sdworx.ro/ | instrument (după titlu; titlul din SERP e „IIS Windows Server”) | neverificat | — | — | — | neverificat | nu: conexiune resetată / 502, doar titlu din SERP |
| 7 (7) | portalcontabilitate.ro — https://www.portalcontabilitate.ro/calculator_salariu/ | instrument (prin curl: pagină de portal pe abonament, cu iframe spre manager.ro/calculator-salariu) | neverificat (Playwright a primit verificarea Cloudflare) | portalul vinde abonamente; prețul calculatorului nu e afișat | titlu 2026 | neverificat | neverificat | parțial: curl 200, Playwright „Just a moment” |
| 8 (8) | undelucram.ro — https://www.undelucram.ro/ro/calculator-salariu-net-sau-brut-romania | instrument funcțional | da: test 6.000 → „3.510 Salariu Net” (impozit 390; diferă de celelalte calculatoare, care dau 3.523) | gratuit | 2026 (titlu) | nu | da | da (Playwright) |
| 9 (9) | calculatoare-salarizare.ro — https://www.calculatoare-salarizare.ro/salariu.php | instrument funcțional (foaie de calcul în iframe) | da: câmpuri (lună, brut, deduceri, tichete) cu valori și calcul afișat | gratuit | „Actualizat la 04.08.2026” | nu | parțial: iframe fix de 670 px, pagina se lățește la 685 px (685 ≤ 685) | da (Playwright) |
| 10 (10) | nexuserp.ro — https://www.nexuserp.ro/calculator-salariu-net | instrument (formular pe site-ul unui ERP) | câmpuri văzute (brut, monedă, dată 11-2026); rezultatul testului nu l-am putut citi | gratuit (calculatorul); site-ul vinde ERP | 2026 | nu | da | da (Playwright) |

- Ce apare azi: 10 calculatoare de salariu. 6 au dat rezultat la test sau au afișat un calcul, 2 au câmpuri dar rezultatul neconfirmat, 2 n-au putut fi verificate.
- Instrument gratuit funcțional: da (calculator-salarii.ro; la fel salaria.ro, impozitsalariu.ro, salariile.ro)
- Produs plătit și preț: niciunul găsit cu preț afișat (portalcontabilitate.ro vinde abonamente, prețul nu l-am văzut)
- Verdict: PUTERNICE. Patru calculatoare funcționale, actualizate pentru 2026 și fără cont în primele 4 poziții.
- Riscuri: depinde de o instituție a statului (cotele CAS/CASS/impozit sunt stabilite prin Codul fiscal; salaria.ro arată reguli „valabil din Iulie 2026”, iar rezultatele diferă între site-uri: 3.523 față de 3.510 lei)
- Surse blocate: calculatorvenituri.sdworx.ro (conexiune resetată / 502), portalcontabilitate.ro (Cloudflare „Just a moment” la Playwright)

---

## simulare credit nevoi personale (volum: 3600, familie: 01)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), „People also search” / „Găsește produse și servicii similare” (poz. 6), „related searches” (poz. 12)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 (1) | cec.ro — https://www.cec.ro/persoane-fizice/credite/credite-nevoi-personale | produs (pagină de credit, după titlu) | neverificat | — | — | — | neverificat | nu: 403 CloudFront, doar titlu din SERP |
| 3 (2) | 123credit.ro — https://123credit.ro/calculator/credit-nevoi-personale | instrument funcțional (comparator de credite / broker) | da: „Vezi ofertele” → listă de oferte cu dobândă și rată lunară | gratuit; câștigă din intermediere | 2026 (în text) | nu | nu: scroll orizontal (408 > 390) | da (Playwright) |
| 4 (3) | raiffeisen.ro — …/credite-de-nevoi-personale.html | produs cu calculator (după titlu: „Calculeaza-ti rata online”) | neverificat | — | — | — | neverificat | nu: 403 „Just a moment”, doar titlu din SERP |
| 5 (4) | icredit.ro — https://icredit.ro/ | instrument funcțional (calculator pe un site de credite / intermediar) | da: rezultat afișat (800 RON / 12 luni → rata 133,34 RON, total 1.600 RON) | gratuit (calculatorul); vinde credite | an nevizibil | nu | da (402 ≤ 402) | da (Playwright) |

- Ce apare azi: 2 instrumente funcționale (comparator 123credit, calculator icredit) și 2 pagini de bancă blocate
- Instrument gratuit funcțional: da (123credit.ro)
- Produs plătit și preț: creditele intermediate. 123credit arată dobânzi între 8,85% și 55% și DAE între 9,88% și 56%; icredit arată 800 RON → 1.600 RON de rambursat în 12 luni
- Verdict: PUTERNICE (verdict pe 4 rezultate organice). În primele 5 organice sunt două instrumente funcționale fără cont, fără semne că ar fi învechite (123credit pe telefon are scroll orizontal).
- Riscuri: nu am găsit dovezi
- Surse blocate: cec.ro (403 CloudFront), raiffeisen.ro (403 „Just a moment”)

---

## declaratie pe proprie raspundere (volum: 2900, familie: 02)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: Imagini (poz. 1, „Declaratie-pe-proprie-raspundere - Titu Maiorescu University”), AI Overview (poz. 2)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 3 (1) | politiaromana.ro — https://politiaromana.ro/files/pages_files/26MODEL_Declaratie_proprie_raspundere_2503.pdf | document de descărcat (PDF, model al Poliției Române; pagină a statului) | nu e instrument | gratuit | an nevizibil | — | neverificat | nu: eroare de certificat TLS la server (n-am dezactivat verificarea), doar titlu din SERP |
| 4 (2) | de.scribd.com — https://de.scribd.com/document/413999291/declaratie-pe-propria-raspundere-4-pdf | document de descărcat (model generic „Subsemnatul…”, pe Scribd) | nu | vizualizare gratuită; descărcarea cere cont Scribd | an nevizibil | da, pentru descărcare | neverificat | da |
| 5 (3) | portal.just.ro — …/Declaratie pe propria raspundere pentru acces in instanta incepand cu 15 mai 2020.doc | document de descărcat (DOC, instanță; pagină a statului) | nu | gratuit | învechit (după titlu: acces în instanță din 15 mai 2020) | — | neverificat | nu: 403 „Just a moment”, doar titlu din SERP |
| 7 (4) | docs.google.com — https://docs.google.com/open?id=0Byhy5_7z7X8UZXg0dzhNdW5tNDg | document de descărcat (DOC pe Google Drive; declarație către Biroul Poliției Rutiere) | nu | gratuit | an nevizibil | nu (se vede și fără autentificare) | neverificat | da (Playwright) |

- Ce apare azi: 4 documente de descărcat (2 de pe site-uri ale statului, dintre care unul învechit, 1 pe Scribd, 1 pe Google Drive). Niciun generator.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (verdict pe 4 rezultate organice). Niciun instrument funcțional, doar modele statice de document.
- Riscuri: juridic (model de document cu efect juridic: declarația pe propria răspundere, dovadă în textul modelelor de pe Scribd și Google Drive); depinde de o instituție a statului (modelele sunt cerute de Poliție sau de instanță, după titluri și text)
- Surse blocate: portal.just.ro (403 „Just a moment”); politiaromana.ro nu e blocat, dar nu l-am deschis din cauza erorii TLS

---

## calculator impozit (volum: 2400, familie: 01)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 4), „related searches” (poz. 11)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 (1) | impozitauto.ro — https://impozitauto.ro/ | instrument (după titlu „Impozit Auto 2026 și 2027”) | neverificat | — | 2026 (titlu) | — | neverificat | nu: 403 „Just a moment” (curl și Playwright), doar titlu din SERP |
| 2 (2) | calculator-impozit-auto.ro — https://www.calculator-impozit-auto.ro/ | instrument funcțional (impozit auto) | da: test 1998 cmc, Euro 6, București → „251 lei”, conform HCGMB 514/2025 | gratuit (are reclame) | 2026 („actualizat 4 feb 2026”) | nu | da (390 ≤ 390) | da (Playwright) |
| 3 (3) | spit-ct.ro — https://www.spit-ct.ro/calculator-taxe-locale/ | instrument funcțional (pagină a statului: SPIT Constanța; salubrizare, clădiri, auto, teren) | da: test salubrizare 3 persoane → „Rezultat 1008 lei” | gratuit | an nevizibil pe pagină | nu | da | da (Playwright) |
| 5 (4) | dfltgm.ro — https://dfltgm.ro/file_fizice/calcul_impozit_auto.html | instrument funcțional (pagină a statului: DFL Târgu Mureș, impozit auto) | da: test 1998 cmc → „Impozit estimat: 195 lei” | gratuit | an nevizibil | nu | da | da (Playwright) |

- Ce apare azi: 4 instrumente (impozit auto și taxe locale), dintre care 2 pe site-uri ale direcțiilor fiscale locale și 1 blocat. Nu apare niciun calculator de impozit pe venit.
- Instrument gratuit funcțional: da (calculator-impozit-auto.ro)
- Produs plătit și preț: niciunul găsit
- Verdict: PUTERNICE (verdict pe 4 rezultate organice). În primele 5 organice sunt trei calculatoare funcționale fără cont. Doar unul arată explicit 2026; celelalte două nu au an vizibil și nici semne că ar fi învechite.
- Riscuri: depinde de o instituție a statului (impozitul local se stabilește prin hotărârile consiliilor locale; dovadă: „Conform: Hotărârea CGMB 514 din 23/12/2025”; dfltgm: „Impozitul datorat este cel stabilit de organul fiscal local”)
- Surse blocate: impozitauto.ro (403 „Just a moment”)

---

## model demisie (volum: 2400, familie: 02,09)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: Imagini (poz. 1, „Cerere de demisie: model, tipuri și prevederi Codul Muncii”), AI Overview (poz. 3)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 (1) | templates.onlyoffice.com — https://templates.onlyoffice.com/pt/editor?…carta-de-demissao… | altul (editor online pentru un șablon de demisie în portugheză) | nu: textul și câmpurile nu s-au încărcat în 4–5 s | gratuit (după site) | an nevizibil | neverificat | da (390 ≤ 390, pagină goală) | da (Playwright; doar titlul „Carta de demissão”) |
| 4 (2) | es.scribd.com — https://es.scribd.com/document/61953374/cerere-demisie | document de descărcat (cerere de demisie în română, pe Scribd) | nu | vizualizare gratuită; descărcarea cere cont Scribd | an nevizibil | da, pentru descărcare | neverificat | da |
| 5 (3) | pdfcoffee.com — https://pdfcoffee.com/download/cerere-demisie-fara-preaviz-pdf-free.html | document de descărcat (după titlu) | nu | — | — | — | neverificat | nu: 403 „Just a moment”, doar titlu din SERP |

- Ce apare azi: 1 editor de șablon în portugheză (nu s-a încărcat), 2 documente pe site-uri de partajare (Scribd, pdfcoffee)
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (verdict pe 3 rezultate organice). Niciun instrument funcțional în română; doar documente și un șablon străin.
- Riscuri: juridic (model de document cu efect juridic: cererea de demisie din textul Scribd, adresată angajatorului, cu CNP și funcție)
- Surse blocate: pdfcoffee.com (403 „Just a moment”)

---

## formular cerere card european de sanatate (volum: 1900, familie: 02)
- Data colectării SERP: 2026-10-02
- Elemente care nu sunt organice: AI Overview (poz. 1), „related searches” (poz. 11)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 (1) | cardeuropean.ro — https://www.cardeuropean.ro/login/ | pagină a statului (portal de cerere online CEASS, după conținut; operator tehnic ProcessIT/Intellisoft) | formular de autentificare (e-mail, parolă); cererea nu am testat-o | gratuit | actual | da (cont cu e-mail) | da (390 ≤ 390) | da (Playwright) |
| 3 (2) | gw2.tirgumures.ro — …/Cerere_CardEU.pdf | document de descărcat (PDF, cerere-tip, pagină a primăriei) | nu | gratuit | învechit (folder „2012/05. Mai 2012”) | nu | neverificat | da (pdftotext) |
| 4 (3) | avocatnet.ro — …/articol_71396/… | articol (pași pentru obținerea online a cardului) | nu | gratuit | an nevizibil în extras | nu | neverificat | da |
| 5 (4) | cas.cnas.ro — https://cas.cnas.ro/casgj/cardul-european | pagină a statului (CAS Galați, formulare, după titlu) | nu | gratuit | — | — | neverificat | nu: conexiune resetată, doar titlu din SERP |
| 6 (5) | cardeuropean.ro — https://www.cardeuropean.ro/ | pagină a statului (informații și link „Depunere cerere”, după conținut) | nu e instrument (pagină de informare) | gratuit | actual | nu | da | da (Playwright) |
| 7 (6) | ro.scribd.com — https://ro.scribd.com/document/405847715/Cerere-Card-European-de-Sanatate | document de descărcat (cerere pe Scribd) | nu | vizualizare gratuită; descărcarea cere cont Scribd | an nevizibil | da, pentru descărcare | neverificat | da |
| 8 (7) | infocons.ro — https://infocons.ro/cardul-european-de-sanatate-online-… | articol (comunicat InfoCons) | nu | gratuit | 14 iunie 2025 | nu | neverificat | da |
| 9 (8) | for.casbt.ro — https://for.casbt.ro/viewtopic.php?t=14 | forum (forumul CAS Botoșani, după titlu) | nu | — | — | — | neverificat | nu: conexiune resetată, doar titlu din SERP |
| 10 (9) | ro.scribd.com — https://ro.scribd.com/document/697929626/Cerere-Eurocard | document de descărcat (cerere-tip CAS Bacău, pe Scribd) | nu | ca mai sus | an nevizibil | da, pentru descărcare | neverificat | da |

- Ce apare azi: 3 pagini ale statului (portalul de cerere online, care cere cont, pagina lui de informare și o pagină CAS), 4 documente de descărcat (3 pe Scribd, unul din 2012), 2 articole, 1 forum
- Instrument gratuit funcțional: nu (portalul oficial de cerere e gratuit, dar cere cont)
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (verdict pe 9 rezultate organice). Singurul instrument (cererea online) cere cont; restul sunt documente și articole.
- Riscuri: juridic (cererea-tip „reprezintă în același timp și o declarație pe propria răspundere”, după textul PDF-ului); depinde de o instituție a statului (cardul îl eliberează casele de asigurări de sănătate / CNAS, după text)
- Surse blocate: niciuna cu 403/429. Nu s-au putut deschide (conexiune resetată): cas.cnas.ro, for.casbt.ro

---

## calculator concediu prenatal (volum: 1600, familie: 01,09)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 1)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 (1) | tpu.ro — https://www.tpu.ro/informatii-utilitare/cum-se-calculeaza-indemnizatia-de-85-pentru-cresterea-copilului/ | articol (cu întrebări ale cititorilor în comentarii) | nu e instrument | gratuit | învechit (citează Legea 19/2000; date din 2009) | nu | neverificat | da |
| 3 (2) | newsweek.ro — https://newsweek.ro/social/cum-calculezi-ce-indemnizatie-de-crestere-a-copilului-… | articol (despre indemnizația de creștere a copilului, nu despre prenatal) | nu | gratuit | învechit („Data actualizării: 18.11.2023”) | nu | neverificat | da |
| 4 (3) | smetni.bg — https://smetni.bg/en/calculators/financial/maternity/ | instrument, dar irelevant (calculator de maternitate pentru Bulgaria, în engleză) | neverificat prin test | gratuit | 2026 (titlu), reguli bulgărești | nu | da (390 ≤ 390) | da |
| 5 (4) | facebook.com — https://facebook.com/groups/8800084376684844/posts/29908817065384935/ | forum (postare în grup Facebook „CONCEDIU PRENATAL”) | nu | — | an nevizibil | conținutul nu e vizibil fără cont | neverificat | parțial: doar titlul |

- Ce apare azi: 2 articole învechite, 1 calculator bulgăresc, 1 postare în grup Facebook. Niciun calculator românesc.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (verdict pe 4 rezultate organice). Niciun instrument funcțional pentru România; articolele sunt învechite.
- Riscuri: depinde de o instituție a statului (indemnizația „este plătită din asigurările sociale de stat”, după textul tpu.ro)
- Surse blocate: niciuna

---

## creare cv (volum: 1600, familie: 09)
- Data colectării SERP: 2026-08-31
- Elemente care nu sunt organice: AI Overview (poz. 1), Imagini (poz. 5, link google.com/search udm=2), „related searches” (poz. 11)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 (1) | europass.europa.eu — https://europass.europa.eu/ro/create-europass-cv | instrument (editorul oficial UE de CV Europass) | parțial: editorul se deschide fără cont („Începeți de la zero”), dar n-am ajuns la câmpuri | gratuit | actual | nu pentru pornire (contul e opțional, pentru profil) | da (390 ≤ 390) | da (Playwright) |
| 3 (2) | cvmaker.ro — https://www.cvmaker.ro/ | produs plătit (generator de CV cu plan gratuit) | neverificat (butonul de pornire n-a deschis editorul) | plan 0 RON; Pro 99,99 RON/lună, probă 14 zile la 5,99 RON, cu reînnoire automată | actual | neverificat | da | da (Playwright) |
| 4 (3) | creare-cv.com — https://creare-cv.com/ | produs plătit (generator de CV) | parțial: se deschide pagina de pornire a editorului | TXT gratuit; „Descărcarea unui CV în format DOCX sau PDF necesită un abonament”, preț neafișat (pagina de checkout a arătat doar bannerul de cookie) | actual | neverificat | da | da (Playwright) |
| 6 (4) | ejobs.ro — https://www.ejobs.ro/cv-ul-meu | instrument (după titlu „Creare CV”) | neverificat | — | — | — | neverificat | nu: 403 Cloudflare „Sorry, you have been blocked”, doar titlu din SERP |
| 7 (5) | getyourcv.net — https://www.getyourcv.net/ro/ | instrument (generator de CV) | parțial: pornirea editorului se deschide fără cont („Crearea și descărcarea CV-ului tău sunt gratuite”), dar n-am ajuns la câmpuri | gratuit (un CV, PDF); Pro 19 USD o singură dată | actual | nu pentru pornire | da | da (Playwright) |
| 8 (6) | makemycv.com — https://makemycv.com/ro | produs plătit (generator de CV) | da: editor cu câmpuri (prenume, nume, e-mail, telefon…), fără cont | probă 2,90 € pentru 7 zile, apoi 27,95 € la 4 săptămâni; anual 7,90 €/lună (94,80 €) | actual | nu pentru editare | da | da (Playwright) |
| 9 (7) | cvwizard.com — https://www.cvwizard.com/ro | produs plătit (generator de CV) | neverificat (editorul nu s-a deschis la click) | 19,99 USD/lună, probă 14 zile la 0,99 USD | actual | neverificat | da | da (Playwright) |
| 10 (8) | undelucram.ro — https://www.undelucram.ro/ro/creare-cv-online-simplu-romana-si-descarca-modelul-completat-cv-pdf-gratuit | instrument ascuns după cont (linkul „Creează-ți CV-ul” duce la /ro/login) | nu fără cont | gratuit (după titlu) | actual | da | neverificat | da |

- Ce apare azi: 8 generatoare de CV: 1 oficial UE, 4 comerciale cu abonament sau probă plătită, 1 gratuit cu Pro opțional, 1 ascuns după cont, 1 blocat
- Instrument gratuit funcțional: parțial. Europass pornește editorul gratuit și fără cont, dar câmpurile nu le-am văzut; singurul cu câmpuri confirmate fără cont este makemycv.com, care la descărcare cere plată
- Produs plătit și preț: makemycv.com (2,90 € / 7 zile, apoi 27,95 € / 4 săptămâni); cvmaker.ro (5,99 RON / 14 zile, apoi 99,99 RON / lună); cvwizard.com (0,99 USD, apoi 19,99 USD / lună); getyourcv.net (Pro 19 USD o dată); creare-cv.com (abonament, preț neafișat)
- Verdict: MEDII (verdict pe 8 rezultate organice). În primele 5 organice, Europass și GetYourCV pornesc editorul fără cont, dar nu am confirmat câmpuri și rezultat; ejobs e blocat; restul sunt plătite.
- Riscuri: nu am găsit dovezi
- Surse blocate: ejobs.ro (403 Cloudflare)

---

## Rezumat

| Căutare | Ce apare azi | Instrument gratuit funcțional | Produs plătit și preț | Verdict | Riscuri |
|---|---|---|---|---|---|
| cv europass | 3 documente pe Scribd | nu | niciunul găsit | SLABE (pe 3 organice) | — |
| calcul medie facultate | 2 instrumente irelevante (HR, SUA), 1 director EN, 1 pagină goală | nu | niciunul găsit | SLABE (pe 4 organice) | — |
| calculator credit nevoi personale | 3 calculatoare de bancă funcționale, 1 director, 4 pagini blocate | da (ing.ro) | credite bancare: ING dobândă 5,99–11,49%, analiză 200 lei; BRD 5,70–20,68% | PUTERNICE (pe 8 organice) | — |
| calculator impozit casa 2026 | 4 articole, 2 grupuri FB, 1 director, 2 calculatoare irelevante | nu | niciunul găsit | SLABE (pe 9 organice) | depinde de o instituție a statului (consilii locale); sezonier (an fiscal 2026, după text) |
| calculator salariu brut net | 10 calculatoare de salariu (6 confirmate la test) | da (calculator-salarii.ro) | niciunul cu preț afișat | PUTERNICE | depinde de o instituție a statului (Codul fiscal) |
| simulare credit nevoi personale | 2 instrumente (comparator, calculator), 2 pagini de bancă blocate | da (123credit.ro) | credite intermediate: 123credit dobândă 8,85–55%, DAE 9,88–56% | PUTERNICE (pe 4 organice) | — |
| declaratie pe proprie raspundere | 4 documente (Poliție, instanță, Scribd, Google Drive) | nu | niciunul găsit | SLABE (pe 4 organice) | juridic; depinde de o instituție a statului (Poliție, instanță) |
| calculator impozit | 4 instrumente de impozit auto / taxe locale (1 blocat) | da (calculator-impozit-auto.ro) | niciunul găsit | PUTERNICE (pe 4 organice) | depinde de o instituție a statului (HCL, organ fiscal local) |
| model demisie | 1 șablon PT neîncărcat, 2 documente | nu | niciunul găsit | SLABE (pe 3 organice) | juridic |
| formular cerere card european de sanatate | 3 pagini ale statului (portal cu cont), 4 documente, 2 articole, 1 forum | nu (portalul cere cont) | niciunul găsit | SLABE (pe 9 organice) | juridic; depinde de o instituție a statului (CNAS/CAS) |
| calculator concediu prenatal | 2 articole învechite, 1 calculator bulgăresc, 1 grup FB | nu | niciunul găsit | SLABE (pe 4 organice) | depinde de o instituție a statului (asigurări sociale) |
| creare cv | 8 generatoare de CV (1 UE, 5 comerciale, 1 cu cont, 1 blocat) | parțial (Europass pornește fără cont, câmpuri neconfirmate) | makemycv 2,90 € / 7 zile, apoi 27,95 € / 4 săpt.; cvmaker 99,99 RON / lună; cvwizard 19,99 USD / lună; getyourcv Pro 19 USD | MEDII (pe 8 organice) | — |
