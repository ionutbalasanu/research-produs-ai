# Lot 10

Notă generală: SERP-urile vin din `serp_analysis` (Ubersuggest, România, limba română, locId 2642, limit 20, fără refresh). Am folosit doar rezultatele organice de pe pozițiile 1-10. La 7 din 12 căutări, unealta a întors o colectare din ziua de azi (2026-11-15, `newData: true`), deși nu am cerut refresh. Contorul de credite a rămas la 7/250 la toate apelurile. Celelalte 5 au colectări din 30 august - 2 septembrie 2026. În tabele scriu poziția brută din SERP.
Paginile le-am deschis cu `citeste.sh`, pe https:// (adresele `http://` din SERP le-am rescris). Instrumentele le-am testat cu Playwright, introducând o valoare de test. Verificarea pe telefon am făcut-o cu emularea iPhone 13: „OK” înseamnă scrollWidth <= innerWidth. Patru domenii (dprp.gov.ro, finzoom.ro, afm.ro, economie.gov.ro) au resetat conexiunea, iar mfinante.gov.ro a închis-o fără răspuns, de două ori fiecare. Le-am trecut la „surse blocate” cu mențiunea „conexiune resetată” și le-am marcat „doar titlu din SERP”.

## verificare itp (volum: 27100, familie: 04,06)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), Related searches (poz. 11), Imagini (poz. 20)
- Rezultatele organice sunt doar 4 (poz. 1, 3, 4, 5).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | play.google.com | altul (aplicație Android „Acteo”, id ro.VerificRCA.app: monitorizează scadențele RCA/ITP/rovinietă după numărul de înmatriculare) | neverificat (aplicație, nu se poate testa pe web) | „Gratuito”, cu achiziții în aplicație; preț neafișat | actual (actualizată 15 nov. 2026) | neclar | neverificat | da |
| 3 | promotor.ro | articol („2024: ITP la autovehicule mai vechi de 10 ani”, 20 feb. 2024) | nu | gratuit | învechit (2024 în titlu) | nu | neverificat | da |
| 4 | digi24.ro | articol (29.11.2013, cum verifici dacă o mașină e garanție pentru un credit, nu despre ITP) | nu | gratuit | învechit (2013) | nu | neverificat | da |
| 5 | laborator.itp.ro | director, agregator (pagina unei stații ITP din București, cu prețuri: „Autoturisme 170 RON”; site-ul are în meniu „Verificare ITP”, dar pagina din SERP nu verifică nimic) | nu | – | actual (calendar noiembrie 2026) | nu | OK | da |

- Ce apare azi: 1 aplicație Android, 2 articole vechi (2013, 2024), 1 pagină de stație ITP. Niciun verificator web.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit (aplicația Acteo are „acquisti in-app”, fără preț afișat; laborator.itp.ro afișează prețul serviciului ITP, 170 RON, nu al unui produs digital)
- Verdict: SLABE (verdict pe 4 rezultate organice; niciun instrument web funcțional, iar căutarea cere o verificare)
- Riscuri: depinde de o instituție a statului (după text: promotor.ro spune că în unele situații ITP-ul „trebuie efectuată la Registrul Auto Român”; aplicația „verifică periodic” ITP-ul după numărul de înmatriculare)
- Surse blocate: niciuna

## convertor mp3 (volum: 9900, familie: 05)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 3), Related searches (poz. 11)
- Rezultatele organice sunt doar 5 (poz. 1, 2, 4, 5, 10).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | ytmp3.gl | instrument (convertor YouTube → MP3) | câmpuri văzute („Paste your YouTube link” + „Convert”); conversie netestată, pentru că testul ar fi însemnat descărcarea unui clip de pe YouTube | gratuit („completely free”) | fără an vizibil | nu („no sign-up”) | OK | da |
| 2 | audiotranscriber.io | instrument (YouTube → MP3, parte dintr-o suită AI de transcriere) | câmpuri văzute (link + „Extract MP3”); conversie netestată, din același motiv | gratuit pentru conversie; restul suitei neverificat | fără an vizibil | nu pentru conversie („No sign-up”); există buton „Sign in for free” | OK | da |
| 4 | ytmp3.rent | instrument (după titlul din SERP) | – | – | – | – | – | nu, blocat: „One moment, please... your request is being verified” |
| 5 | cloudconvert.com | instrument funcțional (MP4 → MP3) | da: am încărcat un MP4 de test de 2 s și am primit „FINISHED test.mp3 · 20 KB · Download” | gratuit în test; pagina are link „Pricing”, preț neafișat pe pagină | actual (© 2026) | nu (în test) | OK | da |
| 10 | play.google.com | altul (aplicație Android „Video to MP3 Converter”, 50M+ descărcări) | neverificat (aplicație) | gratuit, „Contains ads” | actual (actualizată 8 oct. 2026) | neverificat | neverificat | da |

- Ce apare azi: 4 convertoare web (unul blocat de verificarea anti-bot), 1 aplicație Android.
- Instrument gratuit funcțional: da (cloudconvert.com, testat cu un fișier; ytmp3.gl și audiotranscriber.io au câmpurile, dar conversia nu am testat-o)
- Produs plătit și preț: niciunul cu preț afișat (cloudconvert.com trimite la „Pricing”)
- Verdict: MEDII (verdict pe 5 rezultate organice; în primele 5 am confirmat cu test un singur instrument, cloudconvert.com; celelalte două par funcționale, dar nu le-am testat, deci pragul de două confirmate nu e atins)
- Riscuri: niciunul cu dovadă (audiotranscriber.io afișează „Processing copyrighted music is prohibited”, dar asta nu intră în categoriile cerute)
- Surse blocate: ytmp3.rent (pagină de verificare „One moment, please...”)

## calculator pensie (volum: 6600, familie: 01)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), Imagini (poz. 6), Related searches (poz. 11)
- Rezultatele organice sunt doar 5 (poz. 1, 3, 4, 5, 8).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | ultimatecalculator.net | instrument funcțional (calculator american de pensie, în USD; titlul din SERP este „Application error: a client-side exception”, dar azi pagina merge) | da: cu valorile implicite + vârsta 65 → „$2,170,112 / $1,696,781” | gratuit | © 2025; reguli americane, nu românești | nu | OK | da |
| 3 | antena3.ro | articol (1 mar. 2016: CNPP a lansat o aplicație de calcul al vârstei de pensionare) | nu | gratuit | învechit (2016) | nu | neverificat | da |
| 4 | cost.ua | instrument (calculator ucrainean de pensie, în grivne) | câmpuri văzute (salariu, vârstă, sex, categorie, „Порахувати”); netestat | gratuit | reguli ucrainene | nu | OK | da |
| 5 | ekalkulator.pio.rs | pagină a statului (Serbia, fondul de pensii) | nu am putut testa: „E-kalkulator lične penzije zahteva registraciju i prijavu putem eID” | gratuit | reguli sârbești | da (eID) | neverificat | da |
| 8 | play.google.com | altul (aplicație „Retirement calculator”, pensie din investiții) | neverificat (aplicație) | gratuit | învechit (actualizată 16 dec. 2023) | neverificat | neverificat | da |

- Ce apare azi: 1 calculator american, 1 calculator ucrainean, 1 portal sârbesc cu cont, 1 articol din 2016, 1 aplicație Android. Niciun calculator pentru pensia românească.
- Instrument gratuit funcțional: da (ultimatecalculator.net, dar e în USD și nu se aplică pensiei din România)
- Produs plătit și preț: niciunul găsit
- Verdict: MEDII (verdict pe 5 rezultate organice; după definiție există un instrument funcțional, fără cont, în primele 5, dar e american; niciun rezultat nu calculează pensia românească)
- Riscuri: depinde de o instituție a statului (după text: antena3.ro trimite la aplicația Casei Naționale de Pensii pentru calculul vârstei de pensionare)
- Surse blocate: niciuna

## scrisoare de intentie (volum: 5400, familie: 09)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: Imagini (poz. 1), AI Overview (poz. 3)
- Rezultatele organice sunt doar 3 (poz. 2, 4, 5).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | cvida.io | articol (modele complete de scrisoare de intenție, cu butoane „Copiază textul” și „Scrie-o pe a ta în generator”; site de CV-uri) | articol funcțional; generatorul nu l-am testat | modelele gratuite; prețul generatorului neafișat pe pagină | fără an vizibil | nu pentru modele; generatorul neverificat | OK | da |
| 4 | ro.linkedin.com | articol („5 pași pentru a scrie o scrisoare de intenție”) | – | – | – | – | – | nu, blocat (403) |
| 5 | oar-bucuresti.ro | document de descărcat (PDF: scrisoarea de intenție a unui candidat anume la alegerile OAR, 12 mai 2018, nu un model) | nu | gratuit | învechit (2018) | nu | neverificat | da |

- Ce apare azi: 1 site de modele cu generator, 1 articol LinkedIn (blocat), 1 PDF personal din 2018.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul cu preț afișat (cvida.io are generator și „Creează primul tău CV”, fără preț pe pagină)
- Verdict: SLABE (verdict pe 3 rezultate organice; niciun instrument funcțional verificat în primele 10)
- Riscuri: niciunul cu dovadă
- Surse blocate: ro.linkedin.com (403)

## model cv angajare simplu (volum: 4400, familie: 03,09)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: Imagini (poz. 1), AI Overview (poz. 5), Related searches (poz. 11)
- Rezultatele organice sunt doar 3 (poz. 2, 3, 4).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | cariera.ejobs.ro | articol (18 iun. 2026, „Model CV 2026”, cu modele Word de descărcat: română, engleză, „Model CV Simplu”) | nu (descărcări) | gratuit | actual (2026) | nu | neverificat | da |
| 3 | pinterest.com | altul (pin cu imagine care trimite la factura-fiscala.com, „CV simplu – model ușor de completat (Word + exemple)”) | nu | gratuit | fără an | nu pentru pin | neverificat | da |
| 4 | ro.scribd.com | document de descărcat (CV necompletat de 1 pagină, cu rubrica „Stare civila”) | nu | descărcarea cere cont Scribd | fără an | da (pentru descărcare) | neverificat | da |

- Ce apare azi: 1 articol cu modele Word, 1 pin Pinterest, 1 document Scribd.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (verdict pe 3 rezultate organice; niciun instrument, doar modele de descărcat)
- Riscuri: niciunul cu dovadă
- Surse blocate: niciuna

## calcul pensie (volum: 2900, familie: 01)
- Data colectării SERP: 2026-08-30
- Elemente care nu sunt organice: AI Overview (poz. 3), People also ask (poz. 4)
- Rezultatele organice de pe pozițiile 1-10 sunt 8.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | cnpp.ro | pagină a statului (/varsta-pensionare) | nu am putut testa: cu curl, doar „My CNPP – Se încarcă contul tău”; în browser, redirecționează la my.cnpp.ro/conectare/simulare-pensie-publica, unde apare „Web Page Blocked!” | – | – | probabil da („conectare” în adresă) | – | parțial, blocat |
| 2 | cnpp.ro | pagină a statului (/calculul-pensiei) | nu: 404 „Pagina nu a fost găsită” | – | – | – | – | da (404) |
| 5 | caav.ro | pagină a unei case de pensii a avocaților (contribuții 2025, tipuri de pensii) | nu | gratuit | actual (2025) | nu | neverificat | da |
| 6 | lapensie.com | instrument („Program GRATUIT de calculare pensii”; calculul pensiei se face după logare: „Logati-va pentru Calcul Pensie”; are și pagini separate pentru vârsta de pensionare) | nu l-am testat (calculul principal e după cont) | gratuit (după text) | învechit („Valoarea Punctului de pensie: 2032.00 RON”, deși Legea 360/2023 a introdus punctul de referință de 81 lei) | da (pentru calculul pensiei) | parțial (scrollWidth 1703 > 1560: pagina e mai lată decât ecranul și browserul o micșorează) | da |
| 7 | cnas.gov.md | pagină a statului (Republica Moldova, calculatorul vârstei de pensionare) | – | – | – | – | – | nu, blocat („One moment, please... being verified”) |
| 8 | cnpp.ro | pagină a statului („Calculul punctajului de pensie potrivit legii nr. 19/2000”) | nu | gratuit | învechit (regulile Legii 19/2000) | nu | neverificat | da |
| 9 | finzoom.ro | instrument („Calculator Pensie Privata”, după titlu) | – | – | – | – | – | doar titlu din SERP (conexiune resetată) |
| 10 | papervee.com | articol (9 sept. 2024, „Cum se calculează pensia în 2024?”; site de software HR cu „Solicită demo”) | nu | gratuit | învechit (2024) | nu | neverificat | da |

- Ce apare azi: 3 pagini CNPP (una blocată, una 404, una despre legea veche), 1 pagină a casei de pensii a avocaților, 1 program cu cont și date învechite, 1 calculator moldovenesc blocat, 1 calculator de pensie privată nedeschis, 1 articol din 2024.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul cu preț afișat (papervee.com are pagina „Preț”, dar articolul nu afișează prețul)
- Verdict: SLABE (niciun instrument funcțional verificat; singurul calculator românesc deschis, lapensie.com, cere cont și afișează un punct de pensie învechit)
- Riscuri: depinde de o instituție a statului (după text: pagina CNPP trimite la simularea din contul my.cnpp.ro; calculul urmează Legea 360/2023 și punctul de referință, conform papervee.com)
- Surse blocate: cnpp.ro/varsta-pensionare (browser: „Web Page Blocked!”), cnas.gov.md („One moment, please”), finzoom.ro (conexiune resetată)

## model scrisoare (volum: 2900, familie: 03)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: Imagini (poz. 1), AI Overview (poz. 3)
- Rezultatele organice sunt doar 3 (poz. 2, 4, 5).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | pinterest.com | altul (pin „My Creations (Letter Paper Design)”, design de hârtie de scrisori, fără text de model) | nu | – | fără an | nu | neverificat | da |
| 4 | fr.scribd.com | document de descărcat (prezentare PPTX de 21 de pagini pentru clasa I, „Scrisoarea”) | nu | descărcarea cere cont | fără an | da (pentru descărcare) | neverificat | da |
| 5 | studentiada.ro | articol (10 apr. 2025, „Cum scriem o scrisoare”) | nu | gratuit | actual (2025) | nu | neverificat | da |

- Ce apare azi: 1 pin Pinterest, 1 prezentare școlară pe Scribd, 1 articol.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (verdict pe 3 rezultate organice; niciun instrument și niciun model propriu-zis de scrisoare)
- Riscuri: niciunul cu dovadă
- Surse blocate: niciuna

## calculator taxe notariale (volum: 2400, familie: 01)
- Data colectării SERP: 2026-08-30
- Elemente care nu sunt organice: Related searches (poz. 11)
- Rezultatele organice de pe pozițiile 1-10 sunt 10.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | notari.pro | instrument funcțional | da: 100.000 € → onorariu 7.096, OCPI 802, impozit 5.350, extras CF 40 (lei) | gratuit | actual („Actualizat: 5.08.2026”, curs BNR 13.11.2026) | nu | OK | da |
| 2 | notariate.ro | instrument funcțional (vânzare, donație, succesiune, partaj) | da: 100.000 € → onorariu 7.042 lei, intabulare 802 lei, impozit 5.350 lei | gratuit; oferă și „Expertize Grile Notariale”, preț neafișat | actual (Ordinul MJ 177/C/2024, curs BNR 15 noiembrie) | nu | OK | da |
| 3 | unu-imobiliare.ro | instrument funcțional | da: 500.000 € → onorariu 26.955 lei, intabulare 3.969 lei, impozit 26.749 lei etc. | gratuit | actual (OMJ 177/C/2024, TVA 21%, curs 13.11.2026) | nu | OK | da |
| 4 | notariatsignature.ro | instrument funcțional (5 calculatoare în acordeon) | da: 500.000 lei → onorariu 5.504,99 + TVA 1.156,05 = 6.661,04 lei, ANCPI 750 lei | gratuit | actual (curs 5,3498, TVA 21%) | nu | nu (scrollWidth 411 > 390) | da |
| 5 | notariatzarafiu.ro | instrument funcțional | da: 100.000 € → notar 7.115, ANCPI 803, impozit 5.350, total cumpărător 7.918 (lei) | gratuit | actual („2026”, curs 5,35) | nu | OK | da |
| 6 | imobiliare.net | instrument funcțional, dar cu date vechi | da: 100.000 € → onorariu 5.473 RON, intabulare 746 RON, impozit 1.424 RON | gratuit | învechit (curs EUR 4,9746; impozitul de 1.424 lei = 3% din ce depășește 450.000 lei, adică regula OUG 3/2017, nu cea de acum) | nu | OK | da |
| 7 | certum.ro | instrument funcțional | da: 500.000 lei → onorariu 5.504 + TVA 1.155,84 = 6.659,84, intabulare 750, impozit 5.000 (lei) | gratuit | actual (TVA 21%) | nu | OK | da |
| 8 | eurosibimobiliare.ro | instrument funcțional (agenție imobiliară) | da: 100.000 € → cumpărător 7.774 lei, vânzător 5.289 lei | gratuit | actual („2026”; curs afișat 5,2489, puțin diferit de BNR 5,3498) | nu | OK | da |
| 9 | ionut-popa.ro | instrument funcțional (birou notarial) | da: 500.000 lei → 5.504,99 + 1.156,05 = 6.661,04 lei, intabulare 750 lei | gratuit | parțial (calculul e cu TVA 21%, dar textul citează încă OMJ 46/C/2011) | nu | OK | da |
| 10 | notar-floresti.ro | instrument funcțional (birou notarial) | da: 500.000 lei → onorariu 6.716, ANCPI 750, impozit 5.000, extras CF 40 (lei) | gratuit | actual (curs 5,3498) | nu | OK | da |

- Ce apare azi: 10 calculatoare funcționale (6 de la birouri notariale sau site-uri de notariat, 3 de la site-uri imobiliare, 1 de la notari.pro); unul are curs și reguli de impozit vechi.
- Instrument gratuit funcțional: da (cel mai bun: notari.pro; și notariate.ro, unu-imobiliare.ro, notariatzarafiu.ro)
- Produs plătit și preț: niciunul cu preț afișat (notariate.ro vinde „Expertize Grile Notariale” fără preț pe pagină)
- Verdict: PUTERNICE (5 instrumente funcționale, actuale, fără cont, în primele 5)
- Riscuri: depinde de o instituție a statului (după text: onorariile urmează Ordinul MJ 177/C/2024, intabularea se plătește la ANCPI, iar cursul se ia de la BNR)
- Surse blocate: niciuna

## verificare firma anaf (volum: 2400, familie: 04)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), Related searches (poz. 11)
- Rezultatele organice sunt doar 4 (poz. 1, 3, 4, 5).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | listafirme.ro | instrument (după titlu: „Serviciul contribuabili - Firme conform MFinante”) | – | – | – | – | – | nu, blocat (403 „Just a moment...”) |
| 3 | mfinante.gov.ro | pagină a statului („Persoane juridice”, după titlu) | – | – | – | – | – | doar titlu din SERP (fără răspuns) |
| 4 | mfinante.gov.ro | pagină a statului (prima pagină a ministerului, după titlu) | – | – | – | – | – | doar titlu din SERP (fără răspuns) |
| 5 | anaf.ro | pagină a statului (lista bilanțurilor proprii ale Direcției Marilor Contribuabili, 2016 - sem. I 2022, nu o verificare de firmă) | nu | gratuit | învechit (ultimul bilanț listat: 2022) | nu | neverificat | da |

- Ce apare azi: 1 agregator blocat, 2 pagini ale Ministerului Finanțelor nedeschise, 1 pagină ANAF fără legătură directă cu verificarea firmelor.
- Instrument gratuit funcțional: nu (niciunul deschis)
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (verdict pe 4 rezultate organice; niciun instrument funcțional verificat; căutarea cere o verificare)
- Riscuri: depinde de o instituție a statului (după text: titlul listafirme.ro este „Firme conform MFinante”; restul rezultatelor sunt pagini MF și ANAF)
- Surse blocate: listafirme.ro (403, „Just a moment...”), mfinante.gov.ro (fără răspuns, 2 rezultate)

## proces verbal predare primire (volum: 1900, familie: 07)
- Data colectării SERP: 2026-08-31
- Elemente care nu sunt organice: Imagini (poz. 1), People also ask (poz. 6)
- Rezultatele organice de pe pozițiile 1-10 sunt 8.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | dprp.gov.ro | document de descărcat (DOCX „7. Model-Proces-Verbal-de-Predare-Primire”, încărcat 2025/03) | – | – | – | – | – | doar titlu din SERP (conexiune resetată) |
| 3 | lege5.ro | pagină de legislație (model de PV dintr-un act din 18.09.2012 despre penitenciare) | nu | fragment gratuit; „Cumpără forma actualizată 10 Lei cu TVA” sau abonament | învechit (2012, „nu include posibile modificări ulterioare”) | nu pentru fragment | neverificat | da |
| 4 | e-juridic.manager.ro | articol (2025, cu model .docx gratuit de descărcat) | nu | gratuit | actual (2025) | nu | neverificat | da |
| 5 | fr.scribd.com | document de descărcat (PV de 1 pagină, completat parțial cu datele unei firme din Iași) | nu | descărcarea cere cont | fără an | da (pentru descărcare) | neverificat | da |
| 7 | depozituldns.ro | articol (blogul unui magazin de papetărie, aug. 2026, cu structuri de PV și legături spre modelele DPRP și e-juridic) | nu | gratuit | actual (2026) | nu | neverificat | da |
| 8 | lugera.ro | articol (2025, PV pentru bunuri date angajaților; firmă de payroll) | nu | gratuit | actual (2025) | nu | neverificat | da |
| 9 | studocu.com | document de descărcat (după titlu) | – | – | – | – | – | nu, blocat (403 „Access Blocked”) |
| 10 | mefi.ro | altul (pagină inexistentă) | nu (404) | – | – | – | – | da (404) |

- Ce apare azi: 3 documente de descărcat (unul nedeschis, unul blocat), 3 articole, 1 pagină de legislație cu plată, 1 pagină 404.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: lege5.ro, „Cumpără forma actualizată 10 Lei cu TVA” (documentul actualizat) sau abonament Lege5 (preț neafișat)
- Verdict: SLABE (niciun instrument funcțional; doar modele de descărcat și articole)
- Riscuri: juridic (după text: e-juridic.manager.ro numește PV-ul „document oficial cu caracter juridic și probatoriu”)
- Surse blocate: studocu.com (403), dprp.gov.ro (conexiune resetată)

## calculator leasing auto (volum: 1600, familie: 01,06)
- Data colectării SERP: 2026-09-02
- Elemente care nu sunt organice: AI Overview (poz. 4), Related searches (poz. 11)
- Rezultatele organice de pe pozițiile 1-10 sunt 9.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | btleasing.ro | pagină a unei firme de leasing (prima pagină) | – | – | – | – | – | nu, blocat (403 „Acces blocat”) |
| 2 | raiffeisen-leasing.ro | instrument (după titlu: „Calculator rata leasing”) | – | – | – | – | – | nu, blocat (403 „Just a moment...”) |
| 3 | conso.ro | instrument funcțional | da: 20.000 € → grafic complet de rambursare, rată lunară în jur de 348,3 | gratuit | actual (© 2026) | nu | OK | da |
| 5 | brdleasing.ro | instrument funcțional | da: 20.000 € → valoare finanțată 17.000 €, rată 1.398,97 € + TVA (12 luni, avans 15%) | gratuit | fără an vizibil; nimic învechit observat | nu | OK | da |
| 6 | bdvautorulate.ro | instrument funcțional (dealer auto rulat) | da: câmpul a primit 2.000 (din 20.000 tastat) → rată 156 € + TVA, cost total 2.120 € + TVA | gratuit | © 2026 | nu | OK | da |
| 7 | porschefinance.ro | altul (listă de mărci care trimite la configuratorul fiecărei mărci, nu un calculator pe pagină) | nu pe această pagină | gratuit | fără an | nu | OK | da |
| 8 | unicreditleasing.ro | pagină a unei firme de leasing (autoturisme) | – | – | – | – | – | nu, blocat (403 „Request Rejected”) |
| 9 | finzoom.ro | instrument („Calculator DAE leasing”, după titlu) | – | – | – | – | – | doar titlu din SERP (conexiune resetată) |
| 10 | e-bcrleasing.ro | instrument (simulator BCR Leasing; continuarea cere cont: „Dacă vei continua vei avea nevoie de un cont de utilizator”) | nu în test: după prețul tastat, rata a rămas „EUR 0,00” | gratuit | © 2026 | simulare fără cont; cererea cu cont | OK | da |

- Ce apare azi: 3 calculatoare funcționale, 1 simulator care nu a dat rezultat, 1 pagină de trimitere la configuratoare, 4 site-uri blocate sau nedeschise (BT, Raiffeisen, UniCredit, Finzoom).
- Instrument gratuit funcțional: da (cel mai bun: conso.ro, cu grafic de rambursare și DAE)
- Produs plătit și preț: niciunul găsit
- Verdict: PUTERNICE (2 instrumente funcționale, actuale, fără cont, în primele 5: conso.ro poz. 3 și brdleasing.ro poz. 5)
- Riscuri: niciunul cu dovadă
- Surse blocate: btleasing.ro (403), raiffeisen-leasing.ro (403 „Just a moment...”), unicreditleasing.ro (403 „Request Rejected”), finzoom.ro (conexiune resetată)

## model imputernicire (volum: 1600, familie: 02)
- Data colectării SERP: 2026-09-02
- Elemente care nu sunt organice: Imagini (poz. 1), Related searches (poz. 11)
- Rezultatele organice de pe pozițiile 1-10 sunt 9.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | inspectiamuncii.ro | document de descărcat (DOC: împuternicire pentru un control ITM Ilfov) | nu | gratuit | fără an vizibil | nu | neverificat | da |
| 3 | tl.prefectura.mai.gov.ro | document de descărcat (DOC: „Anexa 38”, împuternicire pentru cazierul judiciar al unei persoane juridice; încărcat 2021/04) | nu | gratuit | an 2021 în adresă | nu | neverificat | da |
| 4 | afm.ro | document de descărcat (DOC, după titlu) | – | – | – | – | – | doar titlu din SERP (conexiune resetată) |
| 5 | rarom.ro | document de descărcat (DOCX: împuternicire pentru relația cu RAR: NNR, CIV, aplicații RAR) | nu | gratuit | fără an | nu | neverificat | da |
| 6 | economie.gov.ro | document de descărcat (DOCX „Anexa 12 – Model împuternicire”, după titlu; încărcat 2025/03) | – | – | – | – | – | doar titlu din SERP (conexiune resetată) |
| 7 | uatcomunaguravaii.ro | document de descărcat (DOCX: împuternicire pentru o licitație de concesionare, „Data: ____.2020”) | nu | gratuit | învechit (2020) | nu | neverificat | da |
| 8 | de.scribd.com | document de descărcat (împuternicire PJ pentru Registrul Comerțului) | nu | descărcarea cere cont | fără an | da (pentru descărcare) | neverificat | da |
| 9 | e-juridic.manager.ro | articol (30 ian. 2026, model de împuternicire pentru persoană juridică, DOC și PDF gratuite) | nu | gratuit | actual (2026) | nu | neverificat | da |
| 10 | filbo.ro | articol (blogul unui finanțator, publicat 09/12/2022, modificat 11/04/2025) | nu | gratuit | actual (2025) | nu | neverificat | da |

- Ce apare azi: 7 documente de descărcat (5 de la instituții, unele nedeschise), 2 articole cu modele.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (niciun instrument funcțional; doar modele DOC/DOCX, fiecare pentru altă instituție)
- Riscuri: juridic (după text: modelul ITM spune că împuternicitul semnează „pentru si in numele meu actele de control… semnatura persoanei imputernicite fiindu-mi opozabila”); depinde de o instituție a statului (după text: modelele sunt specifice unei instituții: ITM, RAR, cazierul judiciar, ORC)
- Surse blocate: afm.ro, economie.gov.ro (conexiune resetată)

## Rezumat

| Căutare | Ce apare azi | Instrument gratuit funcțional | Produs plătit și preț | Verdict | Riscuri |
|---|---|---|---|---|---|
| verificare itp | 1 aplicație Android, 2 articole vechi, 1 pagină de stație ITP | nu | niciunul găsit | SLABE (verdict pe 4 rezultate organice) | depinde de o instituție a statului (RAR) |
| convertor mp3 | 4 convertoare web (1 blocat), 1 aplicație | da (cloudconvert.com) | niciunul cu preț afișat | MEDII (verdict pe 5 rezultate organice) | – |
| calculator pensie | calculatoare străine (SUA, Ucraina, Serbia cu eID), 1 articol 2016, 1 aplicație | da (ultimatecalculator.net, în USD, nu pentru România) | niciunul găsit | MEDII (verdict pe 5 rezultate organice) | depinde de o instituție a statului (CNPP) |
| scrisoare de intentie | 1 site de modele cu generator, 1 articol blocat, 1 PDF personal din 2018 | nu | niciunul cu preț afișat | SLABE (verdict pe 3 rezultate organice) | – |
| model cv angajare simplu | 1 articol cu modele Word, 1 pin, 1 document Scribd | nu | niciunul găsit | SLABE (verdict pe 3 rezultate organice) | – |
| calcul pensie | 3 pagini CNPP (blocată / 404 / lege veche), 1 program cu cont și date vechi, 1 blocat, 1 nedeschis, 2 articole | nu | niciunul cu preț afișat | SLABE | depinde de o instituție a statului (CNPP) |
| model scrisoare | 1 pin, 1 prezentare școlară, 1 articol | nu | niciunul găsit | SLABE (verdict pe 3 rezultate organice) | – |
| calculator taxe notariale | 10 calculatoare funcționale (1 cu curs și impozit vechi) | da (notari.pro) | niciunul cu preț afișat | PUTERNICE | depinde de o instituție a statului (MJ, ANCPI, BNR) |
| verificare firma anaf | 1 agregator blocat, 2 pagini MF nedeschise, 1 pagină ANAF fără legătură | nu | niciunul găsit | SLABE (verdict pe 4 rezultate organice) | depinde de o instituție a statului (ANAF/MF) |
| proces verbal predare primire | 3 documente, 3 articole, 1 pagină de legislație cu plată, 1 pagină 404 | nu | lege5.ro: 10 lei cu TVA (forma actualizată) | SLABE | juridic |
| calculator leasing auto | 3 calculatoare funcționale, 1 simulator fără rezultat, 1 pagină de trimitere, 4 blocate sau nedeschise | da (conso.ro) | niciunul găsit | PUTERNICE | – |
| model imputernicire | 7 documente DOC/DOCX, 2 articole | nu | niciunul găsit | SLABE | juridic; depinde de o instituție a statului |
