# Lot 01

Notă generală: SERP-urile vin din `serp_analysis` (Ubersuggest, România, limba română, fără refresh). La 7 din 12 căutări, unealta a întors o colectare din ziua de azi (2026-11-15, `newData: true`), deși nu am cerut refresh. Contorul de credite a rămas la 7/250 la toate apelurile. Unele dintre aceste colectări noi au goluri mari: lipsesc pozițiile 6-10, iar după ele vin direct aplicații Google Play aflate pe pozițiile 15-50. În tabele scriu poziția brută din SERP. Unde lista are mai puțin de 10 rezultate organice, sau unde rezultatele organice trec dincolo de poziția 10, spun asta explicit.
Paginile au fost deschise cu `citeste.sh`, peste HTTPS: adresele `http://` din SERP nu treceau prin proxy, așa că le-am rescris în `https://`. Instrumentele le-am testat cu Playwright, emulând un iPhone 13. „Telefon OK” înseamnă că scrollWidth <= innerWidth la lățimea de 390px. „Parțial” înseamnă că pagina s-a lățit peste 390px, iar browserul a micșorat-o ca să încapă.

## verificare rovinieta (volum: 135000, familie: 04,06)
- Data colectării SERP: 2026-11-15. Primul apel nu a întors nimic, al doilea a întors lista.
- Elemente care nu sunt organice: AI Overview (poz. 1)
- Rezultatele organice sunt doar 4 (poz. 2-5).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | rovineta.ro | altul (pagină goală de găzduire: „Something amazing will be constructed here…”) | nu | – | – | – | OK | da |
| 3 | fleety.ro | altul (pagina de prezentare a unui produs de management al flotei, „În construcție”, nu verifică rovinieta) | nu (fără verificare de rovinietă) | „Primul vehicul gratuit”, alt preț neafișat | 2026 | neclar | OK | da |
| 4 | gandul.ro | articol („ROVINIETA 2023…”) | nu | gratuit | învechit (2023 în titlu) | nu | neverificat | da |
| 5 | promotor.ro | articol (cum verifici online, amenzi) | nu | gratuit | an neclar în titlu | nu | neverificat | da |

- Ce apare azi: 2 articole (unul din 2023), 1 domeniu gol, 1 pagină de produs în construcție. Pe primele poziții nu e nici CNAIR (erovinieta.ro), nici vreun verificator.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit (fleety.ro nu afișează preț, doar „primul vehicul gratuit”)
- Verdict: SLABE (niciun instrument funcțional printre rezultate; căutarea cere un instrument, dar apar doar articole și pagini goale)
- Riscuri: depinde de o instituție a statului (după text: gandul.ro și promotor.ro trimit la erovinieta.ro, „site-ul celor de la CNAIR”, pentru verificare)
- Surse blocate: niciuna

## calculator tva (volum: 18100, familie: 01,11)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), Related searches (poz. 11)
- Rezultatele organice sunt doar 7, cu goluri: poz. 1, 3, 4, 5, 8, apoi 29 și 40.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | nexuserp.ro | instrument funcțional (pagină a unui furnizor de ERP) | da: test 100 + TVA → „121.00 = 100.00 + (21 X 100.00 / 100)” | gratuit | actual (cote 5/9/11/21) | nu | OK | da |
| 3 | cartiagricole.ro | articol (titlul anunță „Calculator si Formule”, dar în HTML nu apare niciun câmp de calcul, doar formule) | nu am găsit câmpuri | gratuit | 2021 în pagină | nu | OK | da |
| 4 | play.google.com | altul (aplicație Android „Calculator TVA”) | neverificat | neverificat | neverificat | neverificat | neverificat | doar titlu din SERP |
| 5 | contzilla.ro | articol (7 aug. 2025, cota de 21%) | nu | gratuit | actual | nu | neverificat | da |
| 8 | play.google.com | altul (aplicație „Calculator TVA: Net Brut”) | neverificat | neverificat | neverificat | neverificat | neverificat | doar titlu din SERP |
| 29 | play.google.com | altul (aplicație) | neverificat | neverificat | neverificat | neverificat | neverificat | doar titlu din SERP |
| 40 | play.google.com | altul (aplicație „VAT Calculator”) | neverificat | neverificat | neverificat | neverificat | neverificat | doar titlu din SERP |

- Ce apare azi: 1 instrument web, 2 articole, 4 aplicații Google Play
- Instrument gratuit funcțional: da (nexuserp.ro)
- Produs plătit și preț: niciunul găsit (nexuserp.ro vinde ERP, dar prețul nu e afișat pe această pagină)
- Verdict: MEDII (un singur instrument web funcțional verificat în primele 5; celelalte sunt articole sau aplicații netestate)
- Riscuri: depinde de o instituție a statului (cotele de TVA sunt stabilite de Codul fiscal; contzilla menționează explicit cota generală de 21%)
- Surse blocate: niciuna

## cv online (volum: 9900, familie: 09)
- Data colectării SERP: 2026-08-27
- Elemente care nu sunt organice: Related searches (poz. 11)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | europass.europa.eu | pagină instituțională (UE): editor de CV | da: editorul se deschide („Creați-vă CV-ul… Începeți de la profilul dumneavoastră”); nu am completat date | gratuit | actual | opțional („Conectați-vă aici”), neverificat până la descărcare | OK | da |
| 2 | cvmaker.ro | produs plătit (generator de CV) | editorul cere cont („Continuând, creezi un cont”) | 5,99 RON / 14 zile, apoi 99,99 RON pe lună (pagina /preturi) | actual | da | OK | da |
| 3 | makemycv.com | produs plătit (generator de CV) | se ajunge la pagina de început a editorului („De la zero / Importă”) | 2,90 € / 7 zile, apoi 27,95 € la 4 săptămâni; sau 7,90 €/lună (94,80 €/an) | actual | neverificat | OK | da |
| 4 | ejobs.ro | instrument (portal de joburi, creare CV) | neverificat | neverificat | neverificat | neverificat | neverificat | blocat (403) |
| 5 | canva.com | instrument (CV Maker) | neverificat | neverificat | neverificat | neverificat | neverificat | blocat (403) |
| 6 | undelucram.ro | instrument (creare CV, portal de joburi) | butonul „Creează-ți CV-ul” nu a dus la editor în test | anunțat gratuit | 2026 | neclar | OK | da |
| 7 | delucru.md | instrument (portal de joburi din Republica Moldova) | duce la formularul de înregistrare | anunțat gratuit | actual | da | OK | da |
| 8 | cv-ro.com | instrument (generator de CV) | da: am văzut câmpurile (Prenume, Nume, E-mail) fără cont | „începeți gratuit”, preț neafișat (pagina de prețuri se încarcă prin JS) | actual | nu la început | OK | da |
| 9 | getyourcv.net | instrument (generator de CV) | se ajunge la pagina „Creează un CV nou”; câmpuri nevăzute | „Crearea și descărcarea CV-ului tău sunt gratuite” | 2026 | neclar („Conectare” opțional) | OK | da |
| 10 | jobseeker.com | instrument (generator de CV) | da: editorul s-a deschis fără cont, cu câmpuri (Prenume, Nume, e-mail…) | preț neafișat (pagina /ro/pricing se încarcă prin JS) | actual | nu la început | OK | da |

- Ce apare azi: 8 generatoare de CV (2 cu preț afișat), 2 site-uri blocate; Europass e pe locul 1
- Instrument gratuit funcțional: da (europass.europa.eu)
- Produs plătit și preț: cvmaker.ro: 5,99 RON / 14 zile, apoi 99,99 RON pe lună; makemycv.com: 2,90 € probă, apoi 27,95 € la 4 săptămâni
- Verdict: PUTERNICE (în primele 5 există cel puțin două instrumente funcționale și actuale: Europass și makemycv.com, plus cvmaker.ro cu cont; Europass nu cere cont)
- Riscuri: niciunul cu dovadă
- Surse blocate: ejobs.ro (403), canva.com (403)

## cerere demisie (volum: 6600, familie: 02,09)
- Data colectării SERP: 2026-08-29
- Elemente care nu sunt organice: Imagini (poz. 1), Related searches (poz. 11)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | inspectiamuncii.ro | document de descărcat (PDF, 1 pagină) / pagină a statului | – | gratuit | an nevizibil | nu | – | da |
| 3 | demisie.net | instrument (generator de cerere + calculator de preaviz) | câmpuri văzute în generator (tip cerere, angajat, funcție, dată); generarea nu a fost testată până la capăt | gratuit | 2026 în pagină | nu | OK | da |
| 4 | lugera.ro | document de descărcat (DOCX, încărcat în 2022) | – | gratuit | 2022 | nu | – | da |
| 5 | papervee.com | document de descărcat (modele Word/PDF), pe site-ul unui produs HR | – | „Cost Gratuit”, cu confirmare prin email | „Actualizat conform Codului Muncii 2026” | email | OK | da |
| 6 | 8ore.ro | articol | – | – | 2026 în titlu | – | neverificat | blocat (403) |
| 7 | edenred.ro | articol cu model | – | gratuit | „Ghidul tau 2025” în titlu | nu | neverificat | da |
| 8 | cariera.ejobs.ro | articol | – | gratuit | neclar | nu | neverificat | da |
| 9 | cerere-demisie.ro | instrument funcțional (generator) | da: am introdus „Ion Popescu / Firma Test SRL” și am primit „CERERE DE DEMISIE Subsemnata Ion Popescu… ultima zi de lucru… 11 decembrie 2026” (genul selectat automat a fost „Feminin”) | gratuit | actual | nu | parțial (pagina se lățește la 468px) | da |
| 10 | hipo.ro | articol | – | gratuit | 2023 în pagină | nu | neverificat | da |

- Ce apare azi: 2 instrumente, 4 articole, 3 documente de descărcat (unul pe site-ul ITM)
- Instrument gratuit funcțional: da (cerere-demisie.ro, poz. 9; demisie.net, poz. 3, are câmpurile vizibile)
- Produs plătit și preț: niciunul găsit (papervee.com vinde software HR, dar pe pagină nu e afișat niciun preț)
- Verdict: MEDII (în primele 5 e un singur instrument, demisie.net; generatorul verificat complet e abia pe poz. 9)
- Riscuri: juridic (model de document cu efect juridic: încetarea contractului de muncă)
- Surse blocate: 8ore.ro (403)

## simulare credit ipotecar (volum: 5400, familie: 01)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 4), Related searches (poz. 11)
- Rezultatele organice sunt doar 5: poz. 1, 2, 3, 5, apoi 48.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | calculator-casa.raiffeisen.ro | instrument (calculator al băncii, după titlu) | neverificat | neverificat | neverificat | neverificat | neverificat | blocat (403) |
| 2 | ing.ro | instrument funcțional (simulator pe pagina produsului) | da: câmpurile valoare proprietate, avans, perioadă; afișează un calcul implicit („Valoare împrumutată 450.001,00 lei”) | gratuit | actual (dobândă fixă 4,79%-6,59%) | nu | OK | da |
| 3 | bancatransilvania.ro | instrument (după titlu, „Calculează-ți ratele”) | neverificat | neverificat | neverificat | neverificat | neverificat | blocat (403) |
| 5 | bcr.ro | director (pagină cu linkuri spre calculatoarele BCR) | nu pe această pagină | gratuit | 2026 | nu | OK | da |
| 48 | play.google.com | altul (aplicație Android) | neverificat | neverificat | neverificat | neverificat | neverificat | doar titlu din SERP |

- Ce apare azi: 3 calculatoare de bancă (2 blocate), 1 pagină cu linkuri BCR, 1 aplicație
- Instrument gratuit funcțional: da (ing.ro)
- Produs plătit și preț: niciunul găsit
- Verdict: MEDII (în primele 5 am verificat un singur instrument, ING; Raiffeisen și BT par instrumente după titlu, dar sunt blocate)
- Riscuri: niciunul cu dovadă (dobânzile afișate sunt ale băncii)
- Surse blocate: calculator-casa.raiffeisen.ro (403), bancatransilvania.ro (403)

## test iq (volum: 4400, familie: 08)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2)
- Lista are goluri mari: doar 4 rezultate organice între pozițiile 1-5. Celelalte 6 sunt aplicații Play pe pozițiile 15-41.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | play.google.com | altul (aplicație „IQ Test: Intelligence Test”) | neverificat | neverificat | neverificat | neverificat | neverificat | doar titlu din SERP |
| 3 | mozgotren.com | instrument (după titlu) / articol: pagină în engleză și rusă, cu „Log in” și „Тарифы” | nu am găsit în pagină butonul de start al testului | neclar (are pagină de tarife) | 2021 în pagină | neclar | OK | da |
| 4 | play.google.com | altul (aplicație) | neverificat | neverificat | neverificat | neverificat | neverificat | doar titlu din SERP |
| 5 | britannica.com | articol (enciclopedie, în engleză) | – | – | – | – | neverificat | blocat (403) |
| 15 | play.google.com | altul (aplicație) | neverificat | neverificat | neverificat | neverificat | neverificat | doar titlu din SERP |
| 18 | play.google.com | altul (aplicație) | neverificat | neverificat | neverificat | neverificat | neverificat | doar titlu din SERP |
| 20 | play.google.com | altul (aplicație) | neverificat | neverificat | neverificat | neverificat | neverificat | doar titlu din SERP |
| 34 | play.google.com | altul (aplicație) | neverificat | neverificat | neverificat | neverificat | neverificat | doar titlu din SERP |
| 40 | play.google.com | altul (aplicație) | neverificat | neverificat | neverificat | neverificat | neverificat | doar titlu din SERP |
| 41 | play.google.com | altul (aplicație, titlu în arabă) | neverificat | neverificat | neverificat | neverificat | neverificat | doar titlu din SERP |

- Ce apare azi: 8 aplicații Google Play, 1 site străin cu test neconfirmat, 1 articol din enciclopedie (blocat); niciun site în română
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (niciun instrument web verificat ca funcțional; în primele 5 sunt aplicații Play netestate, un site în engleză/rusă fără test găsit și un articol)
- Riscuri: niciunul cu dovadă
- Surse blocate: britannica.com (403)

## calcul salariu net 2025 (volum: 2900, familie: 01)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 1)
- Rezultatele organice sunt doar 4 (poz. 2-5).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | portalinstitutiipublice.ro | instrument (calculator, „Noul Cod Fiscal 2026”) | câmpuri văzute în HTML; testul nu s-a încheiat, pentru că la trimitere a apărut o pagină de verificare anti-bot („Please wait while your request is being verified”) | gratuit | 2026 | nu | OK | da |
| 3 | comfincalc.com | instrument funcțional (în engleză) | da: 5000 brut → 2.943 RON net (cu deducere de 179) | gratuit („Free, No login”) | 2026 | nu | OK | da |
| 4 | smartpret.ro | articol (ghid „Actualizat: Iulie 2026”) | nu | gratuit | 2026 | nu | OK | da |
| 5 | salariuldupataxe.ro | instrument funcțional | da: 5000 brut → 2.925 RON net (fără deducere personală, cum scrie pe pagină) | gratuit | 2026 | nu | OK | da |

- Ce apare azi: 3 instrumente (toate pe reguli 2026, deși căutarea cere 2025), 1 articol
- Instrument gratuit funcțional: da (comfincalc.com; salariuldupataxe.ro)
- Produs plătit și preț: niciunul găsit
- Verdict: PUTERNICE (două instrumente funcționale, actuale, fără cont în primele 5: comfincalc.com și salariuldupataxe.ro)
- Riscuri: depinde de o instituție a statului (cotele CAS/CASS/impozit și deducerea vin din Codul fiscal); sezonier (după text: căutarea numește anul 2025, iar rezultatele sunt deja pe 2026)
- Surse blocate: niciuna. Pe portalinstitutiipublice.ro a apărut o pagină de verificare la trimiterea formularului; nu am ocolit-o.

## verificare iban (volum: 2900, familie: 04)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), Related searches (poz. 11)
- Lista are goluri: 4 rezultate organice între poz. 1-5, apoi aplicații Play pe poz. 18-51.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | iban.es | instrument (în spaniolă) | câmp și buton „Validar”; testul cu IBAN-ul RO de exemplu nu a dat un rezultat nou vizibil; banca și BIC „Disponible sólo para miembros” | gratuit pentru validarea de bază, detaliile cer abonament (preț neafișat pe pagină) | an nevizibil | da, pentru detalii | OK | da |
| 3 | remitly.com | instrument funcțional (pagina e în vietnameză) | da: „IBAN này có vẻ chính xác” (IBAN-ul pare corect) | gratuit | actual | nu | OK | da |
| 4 | banci-info.ro | director (bănci și coduri SWIFT, nu are verificator IBAN) | nu | gratuit | 2026 | nu | neverificat | da |
| 5 | ibankodu.com.tr | instrument (în turcă), demo gratuit cu limită | după un singur test: „Ücretsiz IBAN Doğrulama Servisi isteklerinin sayısını aştınız” (limita gratuită a fost depășită); trimite spre abonamentul IBAN Suite | demo gratuit limitat, abonament IBAN Suite (preț neafișat pe pagină) | 2026 | da, pentru mai mult | OK | da |
| 18 | play.google.com | altul (aplicație IBAN Checker) | neverificat | neverificat | neverificat | neverificat | neverificat | doar titlu din SERP |
| 32 | play.google.com | altul (aplicație BIN Checker) | neverificat | neverificat | neverificat | neverificat | neverificat | doar titlu din SERP |
| 40 | play.google.com | altul (aplicație) | neverificat | neverificat | neverificat | neverificat | neverificat | doar titlu din SERP |
| 47 | play.google.com | altul (aplicație) | neverificat | neverificat | neverificat | neverificat | neverificat | doar titlu din SERP |
| 51 | play.google.com | altul (aplicație) | neverificat | neverificat | neverificat | neverificat | neverificat | doar titlu din SERP |

- Ce apare azi: 3 instrumente străine (spaniolă, vietnameză, turcă), 1 director românesc, 5 aplicații Play; niciun verificator în limba română
- Instrument gratuit funcțional: da (remitly.com, interfață în vietnameză)
- Produs plătit și preț: iban.es și ibankodu.com.tr au abonamente, dar nu afișează prețul pe pagina testată
- Verdict: MEDII (un singur instrument funcțional verificat în primele 5; celelalte două sunt limitate sau neconcludente)
- Riscuri: niciunul cu dovadă
- Surse blocate: niciuna

## contract inchiriere apartament (volum: 2400, familie: 07)
- Data colectării SERP: 2026-09-15
- Elemente care nu sunt organice: AI Overview (poz. 3), Imagini (poz. 5), Related searches (poz. 11)
- Rezultatul organic nr. 10 e pe poziția brută 13.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | skia.ro | document de descărcat (PDF, 9 pagini, „actualizat-2023”) | – | gratuit | învechit (2023) | nu | – | da |
| 2 | notariate.ro | document de descărcat (PDF, 3 pagini, încărcat în 2020) | – | gratuit | învechit (2020) | nu | – | da |
| 4 | evo-imobiliare.ro | articol (model 2026, clauze și anexe) | – | gratuit | 2026 | nu | neverificat | da |
| 6 | ro.scribd.com | document de descărcat (agregator) | – | neverificat | an neclar | probabil, la descărcare (neverificat) | neverificat | da |
| 7 | cncir.com.ro | document de descărcat (PDF, încărcat în 2025) | – | gratuit | 2025 | nu | – | da |
| 8 | startimob.ro | articol (agenție imobiliară) | – | gratuit | 2026 în pagină | nu | neverificat | da |
| 9 | notari.pro | articol / pagină de serviciu notarial (programare) | – | preț neafișat | 2026 | nu | parțial (398px) | da |
| 10 | lemonaid.ro | articol cu text de model (firmă de administrare imobile) | – | gratuit | an neclar | nu | neverificat | da |
| 12 | asirom.ro | articol (acte necesare) | – | gratuit | an neclar | nu | neverificat | da |
| 13 | contractinchiriere.ro | instrument (generator: „Gratuit · fără cont · descărcare PDF”) | pagina de start se încarcă; nu am ajuns la câmpurile formularului (neverificat) | gratuit | „Model 2026” | nu (după text) | OK | da |

- Ce apare azi: 4 documente PDF (2 din 2020-2023), 1 document pe Scribd, 4 articole sau pagini de model, 1 generator (pe poz. 13)
- Instrument gratuit funcțional: nu (contractinchiriere.ro, poz. 13, e neverificat)
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (niciun instrument funcțional verificat în primele 10; primele două rezultate sunt PDF-uri din 2023 și 2020)
- Riscuri: juridic (model de contract de locațiune cu efect juridic)
- Surse blocate: niciuna

## calcul concediu medical (volum: 1900, familie: 01,09)
- Data colectării SERP: 2026-10-02
- Elemente care nu sunt organice: AI Overview (poz. 1)
- Rezultatul organic nr. 10 e pe poziția brută 11.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | gandul.ro | articol (schimbări de calcul în 2025) | – | gratuit | 2025 | nu | neverificat | da |
| 3 | legislatiamuncii.manager.ro | articol (caz practic) | – | gratuit | an neclar | nu | neverificat | da |
| 4 | bundeangajat.olx.ro | articol | – | gratuit | an neclar | nu | neverificat | da |
| 5 | portalcodulmuncii.ro | articol (întrebare și răspuns) | – | gratuit | an neclar | nu | neverificat | da |
| 6 | universulfiscal.ro | articol | – | gratuit | 2021 frecvent în pagină | nu | neverificat | da |
| 7 | portalcontabilitate.ro | articol (întrebare și răspuns) | – | gratuit | 2025-2026 în pagină | nu | neverificat | da |
| 8 | avocatnet.ro | forum (discuție) | – | gratuit | 2021 în pagină | nu | neverificat | da |
| 9 | g4media.ro | articol de știri (indemnizație 55% din august) | – | gratuit | 2025-2026 | nu | neverificat | da |
| 10 | portalcodulmuncii.ro | articol | – | gratuit | an neclar | nu | neverificat | da |
| 11 | ro.scribd.com | document de descărcat („Calculatoare Salarizare - Calculator Concediu Medical”, PDF) | nu e instrument | neverificat | an neclar | neverificat | neverificat | da |

- Ce apare azi: 8 articole, 1 forum, 1 document Scribd; niciun calculator. Primul calculator dedicat, gatadecompletat.ro, apare abia pe poz. 14.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (doar articole și forum la o căutare care cere un calcul)
- Riscuri: depinde de o instituție a statului (după text: g4media și gandul descriu modificări legislative ale procentului indemnizației; regulile de calcul sunt stabilite prin lege)
- Surse blocate: niciuna

## scrisoare de intentie model (volum: 1900, familie: 09)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: Imagini (poz. 1), AI Overview (poz. 3)
- Rezultatele organice sunt doar 4: poz. 2, 4, 5, apoi 19.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | fr.pinterest.com | altul (pin în engleză, „Sample Letter Of Interest For A Job”) | – | – | an neclar | pentru navigare | neverificat | da (pagina întoarce doar câteva rânduri, „Log in / Sign up”) |
| 4 | es.scribd.com | document de descărcat (model în limba engleză) | – | neverificat | an neclar | probabil, la descărcare (neverificat) | neverificat | da |
| 5 | gatadecompletat.ro | document de descărcat + ghid (2 feb. 2025) | – | gratuit | 2025 | nu | neverificat | da |
| 19 | docs.google.com | document de descărcat (fișier Drive cu titlu „💀 Scrisoare De Intentie Model Word”, URL cu parametru ciudat; aspect de spam) | – | – | – | „Sign in” | neverificat | da (pagina nu arată conținut) |

- Ce apare azi: 3 documente sau pin-uri (2 în engleză), 1 fișier Drive suspect; niciun model românesc pe primele poziții, în afară de gatadecompletat.ro
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (niciun instrument funcțional în primele 10; rezultate puține, în limbă străină sau suspecte)
- Riscuri: niciunul cu dovadă (scrisoarea de intenție nu are efect juridic)
- Surse blocate: niciuna

## calculator salariu brut 2026 (volum: 1600, familie: 01)
- Data colectării SERP: 2026-09-02
- Elemente care nu sunt organice: Related searches (poz. 11)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | calculator-salarii.ro | instrument funcțional | da: 5000 brut → 2.981 net, CAM 113, cost total 5.113 | gratuit | 2026 (selectare an 2025-2027) | nu | OK | da |
| 2 | salariile.ro | instrument funcțional | da: 5000 → defalcare „Salariu brut 5.000 lei, CAS…” | gratuit | 2026 | nu | OK | da |
| 3 | salaria.ro | instrument funcțional | da: calcul afișat pentru valoarea implicită 4050 brut (CAS 938, sănătate 375, impozit 163); variantele „2026” și „2026 iul.” | gratuit | 2026 | nu | parțial (474px) | da |
| 4 | papervee.com | instrument funcțional (net → brut, pe site-ul unui produs HR) | da: 3000 net → 5.128 brut, cost 5.243 | gratuit | 2026 | nu | OK | da |
| 5 | paylab.ro | instrument funcțional | da: 5000 brut → 3.028 net | gratuit | 2026 | nu | OK | da |
| 6 | undelucram.ro | instrument funcțional | da: 5000 brut → 2.981 net | gratuit | 2026 | nu | OK | da |
| 7 | jobinfo.ro | instrument funcțional | da: 5000 brut → 2.942,50 net | gratuit | 2026 | nu | OK | da |
| 8 | calculatoare-salarizare.ro | instrument (fluturaș de salariu 2026) | câmpurile nu au fost găsite în testul automat (neverificat) | gratuit | 2026, cu arhivă 2015-2025 | nu | parțial (685px) | da |
| 9 | calculator-salarii.ro | instrument (pagina brut 2026, același motor ca poz. 1) | câmpuri văzute; la trimitere a apărut o pagină de verificare („Please wait while your request is being verified”) | gratuit | 2026 | nu | OK | da |
| 10 | portalcodulfiscal.ro | instrument (calculator, „Noul Cod Fiscal 2026”) | câmpuri prezente în HTML; testul automat a completat căutarea site-ului, nu calculatorul (neverificat) | gratuit | 2026 | nu | OK | da |

- Ce apare azi: 10 instrumente (7 testate cu rezultat), niciun articol
- Instrument gratuit funcțional: da (calculator-salarii.ro)
- Produs plătit și preț: niciunul găsit (papervee.com vinde software HR, dar nu afișează preț pe această pagină)
- Verdict: PUTERNICE (cinci instrumente funcționale, actuale, fără cont în primele 5)
- Riscuri: depinde de o instituție a statului (cote și deducere din Codul fiscal); sezonier (după text: căutarea numește anul 2026). Observație: la același brut de 5000, rezultatele diferă de la un calculator la altul: 2.925, 2.942,50, 2.943, 2.981 sau 3.028 net.
- Surse blocate: niciuna. Pe a doua pagină calculator-salarii.ro a apărut o verificare la trimitere; nu am ocolit-o.

## Rezumat

| Căutare | Ce apare azi | Instrument gratuit funcțional | Produs plătit și preț | Verdict | Riscuri |
|---|---|---|---|---|---|
| verificare rovinieta | 2 articole (unul din 2023), 1 domeniu gol, 1 produs în construcție (doar 4 rezultate organice) | nu | niciunul găsit | SLABE | depinde de o instituție a statului (CNAIR) |
| calculator tva | 1 instrument web, 2 articole, 4 aplicații Play (7 rezultate organice) | da (nexuserp.ro) | niciunul găsit | MEDII | depinde de o instituție a statului (cote TVA) |
| cv online | 8 generatoare de CV, 2 blocate | da (europass.europa.eu) | cvmaker.ro 5,99 RON/14 zile, apoi 99,99 RON/lună; makemycv.com 2,90 €, apoi 27,95 €/4 săpt. | PUTERNICE | – |
| cerere demisie | 2 instrumente, 4 articole, 3 documente (PDF ITM, DOCX, Word/PDF) | da (cerere-demisie.ro, poz. 9) | niciunul găsit | MEDII | juridic |
| simulare credit ipotecar | 3 calculatoare de bancă (2 blocate), 1 pagină de linkuri, 1 aplicație | da (ing.ro) | niciunul găsit | MEDII | – |
| test iq | 8 aplicații Play, 1 site străin, 1 articol blocat | nu | niciunul găsit | SLABE | – |
| calcul salariu net 2025 | 3 instrumente (pe 2026), 1 articol (4 rezultate organice) | da (comfincalc.com) | niciunul găsit | PUTERNICE | depinde de o instituție a statului; sezonier (2025) |
| verificare iban | 3 instrumente străine, 1 director, 5 aplicații Play | da (remitly.com, în vietnameză) | iban.es și ibankodu.com.tr: abonament, preț neafișat | MEDII | – |
| contract inchiriere apartament | 4 PDF-uri, 1 Scribd, 4 articole sau modele, 1 generator pe poz. 13 | nu | niciunul găsit | SLABE | juridic |
| calcul concediu medical | 8 articole, 1 forum, 1 Scribd | nu | niciunul găsit | SLABE | depinde de o instituție a statului |
| scrisoare de intentie model | 3 documente sau pin-uri (2 în engleză), 1 fișier Drive suspect (4 rezultate organice) | nu | niciunul găsit | SLABE | – |
| calculator salariu brut 2026 | 10 instrumente | da (calculator-salarii.ro) | niciunul găsit | PUTERNICE | depinde de o instituție a statului; sezonier (2026) |
