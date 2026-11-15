# Lot 07

Notă generală: SERP-urile vin din `serp_analysis` (Ubersuggest, România, limba română, locId 2642, limit 20, fără parametrul refresh). La 5 din 12 căutări unealta a întors o colectare din ziua de azi (2026-11-15, `newData: true`), deși nu am cerut refresh. Contorul de credite a rămas la 7/250 la toate apelurile. Aceste colectări noi au goluri mari: puține rezultate organice în primele 10 poziții, apoi direct aplicații Google Play pe pozițiile 13-54. În tabele trec doar rezultatele organice din pozițiile 1-10, cu poziția brută din SERP. Rezultatele organice de după poziția 10 le enumăr separat și nu le număr. Unde în primele 10 poziții sunt mai puțin de 10 rezultate organice, verdictul spune „(verdict pe N rezultate organice)”.
Paginile le-am deschis cu `citeste.sh`, cu adresele `http://` rescrise în `https://`. Instrumentele le-am testat cu Playwright (Chromium, fără opțiuni). Pentru telefon am emulat `iPhone 13`. „OK” înseamnă scrollWidth <= innerWidth la 390px. „Parțial” înseamnă că pagina nu are viewport mobil: scrollWidth = innerWidth, dar lățimea e de peste 390px, deci pagina se afișează micșorată. „NU” înseamnă scrollWidth > innerWidth.

## word in pdf (volum: 40500, familie: 05)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), Related searches (poz. 11)
- Rezultate organice în primele 10 poziții: 5 (poz. 1, 3, 4, 5, 8). După poz. 10, necontate, doar titlu din SERP: 4 aplicații Google Play (poz. 13, 21, 26, 45).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | swifdoo.com | articol (ghid „Convert Word to PDF… Online & Offline”, promovează programul desktop SwifDoo PDF, fără câmp de încărcare pe pagină) | nu (nu am găsit niciun input de fișier) | trial gratuit de 7 zile, butoane „Buy Now”/„Pricing”, preț neafișat pe pagină | „Updated on April 23, 2024” | – | OK | da |
| 3 | pdf.wondershare.com | instrument funcțional (convertor Word→PDF online) | da: am încărcat un .docx de test → „This task has been processed successfully / Download” | gratuit pentru conversie, cu buton „Go Premium” (preț neafișat) | actual | nu (fără login la conversie) | OK | da (Playwright) |
| 4 | youtube.com | video | – | – | – | – | neverificat | blocat (HTTP 429, captcha) |
| 5 | web.smallpdf.com/cn (redirect la smallpdf.com/cn) | instrument funcțional (convertor Word→PDF, pagina în chineză) | da: .docx de test → „test.pdf 18 kB – 1 页面 / 下载” (descărcare) | gratuit („免费”), cu buton de probă plătită (preț neafișat) | actual | nu | OK | da (Playwright) |
| 8 | play.google.com | altul (aplicație Android „Convert Word to PDF doc & docx”, 10K+ descărcări, „Conține anunțuri”) | neverificat (aplicație) | gratuit cu reclame | „Ultima actualizare 23 aug. 2022” | neverificat | neverificat | da (pagina din magazin) |

- Ce apare azi: 2 instrumente online funcționale, 1 articol (care vinde un program desktop), 1 video, 1 aplicație Android
- Instrument gratuit funcțional: da (pdf.wondershare.com; smallpdf.com funcționează la fel, dar pagina e în chineză)
- Produs plătit și preț: swifdoo.com (program desktop, trial 7 zile, preț neafișat), wondershare „Go Premium” (preț neafișat), smallpdf „免费试用” (preț neafișat)
- Verdict: PUTERNICE (verdict pe 5 rezultate organice): două convertoare funcționale, actuale și fără cont, pe poz. 3 și 5
- Riscuri: niciunul găsit
- Surse blocate: youtube.com (429, captcha)

## calculator medie facultate (volum: 12100, familie: 08)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), Imagini (poz. 6 și 17), Related searches (poz. 11)
- Rezultate organice în primele 10 poziții: 4 (poz. 1, 3, 4, 5). Niciunul după poz. 10.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | uniarea.github.io | instrument funcțional, dar pentru Portugalia („Simulador de Candidatura”, note 0-20 și examene 0-200) | are câmpuri și buton „Calcular”; nu se aplică sistemului românesc | gratuit | reguli „2020/21” în text | nu | parțial (782px) | da |
| 3 | mojput.com | altul (orientare școlară din Croația, „kalkulator-fakulteti”, listă de orașe și facultăți croate) | nu am văzut un calcul de medie | gratuit | neclar | nu | OK | da (Playwright) |
| 4 | facebook.com/studycalc | altul (pagină Facebook) | – | – | – | da (zid de login, conținutul nu se afișează) | neverificat | da (doar ecranul de login) |
| 5 | dynamicontent.net | instrument (College Savings Calculator, SUA: economii pentru facultate, în dolari) | are câmpuri; nu calculează media | gratuit | neclar | nu | OK | da |

- Ce apare azi: 2 calculatoare din alte țări (Portugalia, SUA), 1 platformă croată, 1 pagină Facebook. Niciun rezultat românesc.
- Instrument gratuit funcțional: nu (nimic care să calculeze media la o facultate din România)
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (verdict pe 4 rezultate organice): niciun instrument pentru nevoia căutată; calculatoarele care apar sunt pentru alte țări și alte scopuri
- Riscuri: niciunul găsit
- Surse blocate: niciuna (Facebook cere login)

## verificare cui (volum: 8100, familie: 04)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2)
- Rezultate organice în primele 10 poziții: 5 (poz. 1, 3, 4, 5, 6). Niciunul după poz. 10.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | rrf.ro | neverificat (titlu: „Check Romanian companies”) | neverificat | neverificat | neverificat | neverificat | neverificat | blocat (403, „Just a moment…”); doar titlu din SERP |
| 3 | data.wedevelop.ro | instrument (DateFirme: căutare firme după denumire/CUI, date ONRC/MF/ANAF) | parțial: căutarea duce la o listă publică de firme cu CUI, CA, profit și stare („peste 10.000 firme găsite”). Filtrarea după CUI-ul de test nu s-a aplicat în test. | listă gratuită; „🔒 Export CSV”, pagină „Prețuri” (preț necitit) | © 2026 | nu pentru listă; funcțiile AI și exportul cer cont | OK | da (Playwright) |
| 4 | contabilitateprofit.ro | articol (cum verifici un partener comercial; firmă de contabilitate) | nu | gratuit | an neclar | nu | neverificat | da |
| 5 | data.wedevelop.ro/cont | altul (pagina de creare cont DateFirme) | nu (formular de înregistrare) | – | 2026 | da | OK | da |
| 6 | chromewebstore.google.com | altul (extensie Chrome „Verificare CUI ANAF”, Tapselo, 4 utilizatori) | neverificat (trebuie instalată) | gratuită (fără preț pe pagină) | folosește API ANAF v9 | nu (cere instalare în Chrome) | OK (pagina din magazin) | da |

- Ce apare azi: 1 platformă de date despre firme (cu pagina ei de cont pe încă o poziție), 1 extensie Chrome, 1 articol, 1 site blocat
- Instrument gratuit funcțional: da, parțial (data.wedevelop.ro: lista publică merge fără cont; filtrarea după CUI nu am confirmat-o)
- Produs plătit și preț: data.wedevelop.ro (export CSV blocat, pagină „Prețuri”, preț necitit)
- Verdict: MEDII (verdict pe 5 rezultate organice): un singur instrument în primele 5, și acela confirmat doar parțial; poz. 1 e blocată
- Riscuri: depinde de o instituție a statului (după text: „Surse: ONRC · Ministerul Finanțelor · ANAF”; extensia: „direct din datele publice ANAF”)
- Surse blocate: rrf.ro (403, Cloudflare „Just a moment…”)

## calculator salariu invatamant (volum: 5400, familie: 01)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 1), Video (poz. 8), Related searches (poz. 11)
- Rezultate organice în primele 10 poziții: 4 (poz. 2, 3, 4, 5). Niciunul după poz. 10.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | facebook.com (SalariiInvatamant) | video (reel „Calculator Salarii Invatamant”) | – | – | – | da (login) | neverificat | da (doar titlul) |
| 3 | salarii.invatamantpreuniversitar.ro | instrument funcțional | da: la încărcare calculează cu valorile implicite (Profesor, Grad I) → „Salariu baza 6773 (grila V.I. 1-5 ani pe OUG 128/2023)”, „Perioada: 01.06.2024 - ...” | gratuit | parțial actual: ultima perioadă din listă e „iun 2024 …”, fără mențiune 2025/2026 | nu | parțial (993px) | da (Playwright; am deschis pagina principală, nu URL-ul cu parametri din SERP) |
| 4 | mate.info.ro | instrument învechit (formular „Calculator de salarii pentru profesori”) | nu: formularul are câmpuri, dar clicul pe „Calculeaza” a eșuat în test | gratuit | învechit (trimite la L 128/97, L 108/2007, HG 281/93) | nu | parțial (555px) | da |
| 5 | salarizare.zed-zen.com (redirect la romaniatransparenta.eu) | instrument (calculator pe proiectul legii salarizării 2026, ghidat pas cu pas) | parțial: pornește („Pasul 1 – În ce sector lucrezi?”); rezultatul final nu l-am obținut | gratuit („calculul se face în browser-ul tău”) | 2026, dar pe un proiect „NEADOPTAT” (variantele 25 mai / 17 iul / 20 aug 2026) | nu | OK | da (Playwright) |

- Ce apare azi: 3 calculatoare (1 funcțional, 1 învechit/nefuncțional, 1 pe proiect de lege, nefinalizat în test), 1 video Facebook
- Instrument gratuit funcțional: da (salarii.invatamantpreuniversitar.ro)
- Produs plătit și preț: niciunul găsit
- Verdict: MEDII (verdict pe 4 rezultate organice): un singur calculator confirmat cu rezultat în primele 5; al doilea (romaniatransparenta.eu) calculează pe un proiect neadoptat și nu l-am dus până la rezultat
- Riscuri: depinde de o instituție a statului (după text: grilele „pe OUG 128/2023”, „Legea 284/2010”; zed-zen: proiect „MMFTSS”, „intrare în vigoare 1 decembrie 2026”)
- Surse blocate: niciuna

## cerere concediu (volum: 4400, familie: 02,09)
- Data colectării SERP: 2026-08-28
- Elemente care nu sunt organice: Imagini (poz. 1), Related searches (poz. 11)
- Rezultate organice în primele 10 poziții: 9 (poz. 2-10)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | euload.com | document de descărcat (PDF „5.3 Cerere de concediu odihna (CO)”), ascuns după abonament | nu: PDF-ul redirecționează (302) la „/under.subscription.php” | „Abonamentul EXTRA de la 150 RON” (150/3 luni, 200/6 luni, 300/12 luni) | neclar | da (abonament) | neverificat | da (pagina de abonament) |
| 3 | papervee.com | articol + model gratuit (blog al unui soft HR) | nu | gratuit; produsul are pagina „Preț” (preț necitit) | „15 Aprilie 2026” | nu | OK | da |
| 4 | ro.scribd.com | document de descărcat (cerere CO parțial, IMSP din R. Moldova) | nu | descărcarea pe Scribd | neclar | descărcarea cere cont Scribd | neverificat | da |
| 5 | timeoff.guru | articol + model (blog al unui soft de concedii) | nu | gratuit; produs cu „Prețuri” (preț necitit) | 2026 („10 ani de TIMEOFF.GURU”) | nu | OK | da |
| 6 | facebook.com (contabun.ro) | altul (postare „Model cerere concediu de odihna”) | – | – | – | da (login) | neverificat | da (doar titlul) |
| 7 | primariasantandrei.ro | document de descărcat (listă: „MODEL CERERE CONCEDIU ODIHNA 2018_2019.doc”) | nu | gratuit | învechit (2018-2019) | nu | neverificat | da |
| 8 | leaveboard.com | articol + model Word/PDF + calculator de zile de concediu | modelul se descarcă (.docx/.pdf); calculatorul are câmpuri de dată, netestat | gratuit; produs HR cu „Prețuri” (preț necitit) | neclar | nu | parțial (685px) | da |
| 9 | tooluri.ro | instrument funcțional (generator cerere CO, DOCX) | da: am introdus nume și angajator → previzualizarea s-a completat („Subsemnatul Ion Test, angajat al societății Firma Test SRL…”), buton „Descarcă DOCX” | gratuit | „2026” în titlu | nu | OK | da (Playwright) |
| 10 | factura-fiscala.com | articol + model Word/PDF de descărcat | nu (fișiere .docx/.pdf) | gratuit | „(2026)” în titlu | nu | OK | da |

- Ce apare azi: 1 generator funcțional, 5 articole sau pagini cu model descărcabil, 3 documente (unul după abonament, unul din 2018-2019), 1 postare Facebook
- Instrument gratuit funcțional: da (tooluri.ro, poz. 9)
- Produs plătit și preț: euload.com (abonament EXTRA, 150 RON / 3 luni); papervee.com, timeoff.guru și leaveboard.com sunt software HR plătit, cu preț necitit
- Verdict: MEDII: un generator funcțional, dar abia pe poz. 9; primele 5 sunt documente și articole
- Riscuri: juridic (model de cerere adresată angajatorului; după text: „art.144 din Codul Muncii”, „prevederile esențiale din Codul Muncii”)
- Surse blocate: niciuna

## verificare anaf cnp (volum: 3600, familie: 04)
- Data colectării SERP: 2026-08-29
- Elemente care nu sunt organice: AI Overview (poz. 1), Related searches (poz. 11)
- Rezultate organice în primele 10 poziții: 9 (poz. 2-10)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | anaf.ro/VerifAdev | pagină a statului (formular „Verificare documente electronice eliberate în SPV”: nr. document, CNP/CIF, cod de validare) | neverificat: cere numărul unui document emis în SPV și captcha; nu verifică doar după CNP | gratuit | actual | nu pentru formular, dar documentul se obține din SPV (cont) | parțial (980px) | da |
| 3 | anaf.ro (DGCVPF) | pagină a statului (prezentare „Verificarea situației fiscale personale”) | nu (pagină informativă) | gratuit | actual | nu | neverificat | da |
| 4 | anaf.ro | pagină a statului (pagina principală, butoane de autentificare SPV) | nu | gratuit | actual | – | parțial (1101px) | da (Playwright) |
| 5 | anaf.ro (SPV) | pagină a statului („Înregistrare în Spațiul Privat Virtual”) | nu (procedura de creare cont) | gratuit | actual | da | neverificat | da |
| 6 | telework.ro | articol („Cum verific online istoricul la ANAF / SPV?”) | nu | gratuit | an neclar | nu | neverificat | da |
| 7 | anaf.ro/restante | pagină a statului (listă „Obligații fiscale restante”, căutare după denumire + cod de validare) | neverificat (captcha); listă pentru debitori persoane juridice, nu căutare după CNP | gratuit | „la data de 30.09.2026” | nu | NU (2090 > 1560) | da |
| 8 | anaf.ro/VerifAdev/verificareAdeverinta.do | pagină a statului (același formular ca la poz. 2) | neverificat (captcha) | gratuit | actual | nu (document din SPV) | parțial (980px) | da |
| 9 | anaf.ro | pagină a statului (descriere „Verification of electronic documents issued in SPV”) | nu | gratuit | actual | – | neverificat | da |
| 10 | contapp.ro | articol („SPV ANAF: cum te autentifici… în 2026”, blog al unui soft de contabilitate) | nu | articol gratuit; promoție „Black Friday ContApp: 15 luni la prețul a 12” (preț necitit) | 2026 | nu | neverificat | da |

- Ce apare azi: 7 pagini ANAF (2 formulare cu captcha, restul informative sau de autentificare), 2 articole
- Instrument gratuit funcțional: nu (nicio verificare doar după CNP fără cont SPV; formularele ANAF fără cont cer număr de document sau sunt liste pentru firme, cu captcha)
- Produs plătit și preț: contapp.ro (abonament, preț neafișat în textul citit)
- Verdict: SLABE: verificarea situației personale după CNP trece prin SPV (cont); formularele fără cont nu fac această verificare și nu le-am putut confirma (captcha)
- Riscuri: depinde de o instituție a statului (după text: toate verificările sunt pe anaf.ro, prin SPV)
- Surse blocate: niciuna

## model cerere (volum: 2900, familie: 02)
- Data colectării SERP: 2026-11-10
- Elemente care nu sunt organice: Imagini (poz. 1, „Model Cerere Tip | PDF”), AI Overview (poz. 3), Related searches (poz. 11)
- Rezultate organice în primele 10 poziții: 3 (poz. 2, 4, 5). Niciunul după poz. 10.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | anp.gov.ro | document de descărcat (PDF „CERERE-TIP – model”, L544/2001, Penitenciarul Mioveni) | – | gratuit | 2017 (după URL) | – | neverificat | nu (conexiunea resetată de două ori); doar titlu din SERP |
| 4 | pensiiconstanta.ro | document de descărcat (PDF „ANEXA 1… CERERE-TIP – model”) | – | gratuit | 2025 (timestamp în numele fișierului) | nu | neverificat | da (PDF descărcat, text neextras) |
| 5 | ru.scribd.com | document de descărcat (model cerere pentru indemnizația de instalare, HG 281/1993) | – | descărcarea pe Scribd | învechit (HG 281/1993) | descărcarea cere cont Scribd | neverificat | da |

- Ce apare azi: 3 documente PDF/DOC (2 cereri-tip L544/2001 de pe site-uri ale statului, 1 pe Scribd)
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (verdict pe 3 rezultate organice): niciun instrument, doar documente de descărcat
- Riscuri: juridic (cereri-tip cu efect juridic; după text: „conform L544/2001”)
- Surse blocate: anp.gov.ro (conexiune resetată, nu 403/429; e trecut aici pentru că nu l-am putut deschide)

## calculator pensie online (volum: 2400, familie: 01)
- Data colectării SERP: 2026-10-02
- Elemente care nu sunt organice: AI Overview (poz. 1), Related searches (poz. 11)
- Rezultate organice în primele 10 poziții: 9 (poz. 2-10)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | my.cnpp.ro | pagină a statului (simulator CNPP „Simulare vârstă pensionare”) | neverificat | neverificat | neverificat | după cnpp.ro: „Nu este necesar cont” pentru simularea manuală | neverificat | blocat (HTTP 500 „Web Page Blocked! … Attack ID”); doar titlu din SERP |
| 3 | contabss.ro | instrument funcțional (Calculator Pensie 2026, cu tab-uri vârstă/estimare/anticipată/privată/impozit) | da: bărbat, născut 1980 → „VÂRSTĂ PENSIONARE 65 ani… ianuarie 2045”, stagiu minim 15, complet 35 | gratuit (site al unei firme de contabilitate) | „Actualizat 2026”, Legea 360/2023, VPR 2.032 lei | nu | OK | da (Playwright) |
| 4 | cnas.gov.md | instrument funcțional, dar pentru R. Moldova (calculatorul vârstei de pensionare, Legea nr. 156-XIV/1998) | da: 01-01-1980 → „Data estimată de pensionare: 01-01-2043, vârsta 63 ani” | gratuit | actual pentru Moldova, nu se aplică în România | nu | OK | da (Playwright) |
| 5 | cnpp.ro | pagină a statului (explică cele două simulări: manuală fără cont, automată cu SPV; trimite la my.cnpp.ro) | nu pe pagină (link „Începe acum” spre my.cnpp.ro, blocat) | gratuit | „Data ultimei modificări: 19.08.2026” | nu (simularea manuală) / da (automată) | OK | da |
| 6 | lapensie.com | instrument (program de calcul pensie) | neverificat: „Calcul pensie” cere logare (email + parolă, „Inregistrare/Cont nou”) | gratuit („Program GRATUIT”) | VPP 2032 RON, Legea 360/2023 | da (pentru calculul pensiei) | parțial (980px) | da |
| 7 | expertulbanilor.ro | instrument anunțat („Calculator pensie de stat”) | nu: în pagină nu apare niciun câmp de calcul, nici după acceptarea cookie-urilor | gratuit | neclar | nu | OK | da (Playwright) |
| 8 | finzoom.ro | instrument anunțat („Calculator Pensie Privata”) | neverificat | neverificat | neverificat | neverificat | neverificat | nu (eroare HTTP/2, conexiune resetată); doar titlu din SERP |
| 9 | cpmb.ro | pagină a statului (Casa de Pensii a Mun. București, „Calculul pensiei”, explicații) | nu | gratuit | 2026 în meniu („bilete tratament 2026”) | nu | OK | da |
| 10 | desprepensiiprivate.ro | instrument (calculator dată pensionare Pilon 2/3, formular „calculated fields”) | neverificat: câmpurile sunt în HTML; la a doua încărcare pagina nu s-a afișat complet | gratuit („Aplicații gratuite”); site cu „Zona Premium”/„Abonament” (preț necitit) | 2026 în titlu, Legea 360/2023 | nu | OK | da |

- Ce apare azi: 5 instrumente (2 confirmate: unul românesc, unul din Moldova; 1 cu cont; 1 fără câmpuri; 1 netestat), 3 pagini ale caselor de pensii (una blocată), 1 site neaccesibil
- Instrument gratuit funcțional: da (contabss.ro)
- Produs plătit și preț: niciunul găsit cu preț afișat (desprepensiiprivate.ro are „Abonament”/„Zona Premium”, preț necitit)
- Verdict: MEDII: în primele 5 e un singur instrument românesc confirmat (contabss.ro); cnas.gov.md funcționează, dar aplică legea din R. Moldova, iar simulatorul CNPP (poz. 2) e blocat pentru noi
- Riscuri: depinde de o instituție a statului (după text: „Legea 360/2023”, „VPR de 2.032 lei”, simulatorul oficial CNPP)
- Surse blocate: my.cnpp.ro („Web Page Blocked!”, firewall); finzoom.ro (conexiune resetată, nu 403/429; trecut aici pentru că nu s-a deschis)

## test iq gratuit (volum: 2400, familie: 08)
- Data colectării SERP: 2026-08-29
- Elemente care nu sunt organice: AI Overview (poz. 1), Related searches (poz. 11)
- Rezultate organice în primele 10 poziții: 9 (poz. 2-10)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | testiq.ro | instrument funcțional (test IQ, 30 de întrebări, 30 de minute) | da: am sărit peste toate întrebările → „Coeficientul dvs. de inteligenta este 72”, cu cod de test | gratuit („Aflarea rezultatului testului este acum gratuita”) | „© 2020-2025” | nu | OK | da (Playwright) |
| 3 | mensaromania.ro | instrument (test Mensa, inclus din test.mensa.no: 35 de întrebări, 25 de minute) | parțial: pornește (alegerea grupei de vârstă); rezultatul nu l-am obținut | gratuit | © 2026 | nu | OK | da (Playwright) |
| 4 | invatasingur.ro | instrument stricat (test de inteligență, 24 de întrebări) | nu: „Pornire test” → „Ne pare rău, dar ceva nu a funcționat” | gratuit | 2007-2026 | nu | OK | da (Playwright) |
| 5 | arealme.com | instrument funcțional (test IQ, varianta rapidă de 49 de întrebări) | da: răspunsuri „Nu știu” până la final → „SCORUL TĂU IQ 60”, cu profil și opțiunea de test complet | gratuit („Gratuit. Fără reclame, înregistrare sau plată.”) | „Actualizat 2026-11-03” | nu | OK | da (Playwright) |
| 6 | reddit.com | forum („Există cu adevărat teste IQ gratuite”) | – | – | – | – | neverificat | nu (curl a întors doar „Reddit”); doar titlu din SERP |
| 7 | international-iq-test.com | neverificat (titlu: „Test IQ gratuit 2026… fără înregistrare”) | neverificat | neverificat | neverificat | neverificat | neverificat | blocat (403); doar titlu din SERP |
| 8 | brain-testing.org | produs plătit (testul e gratuit, raportul cu IQ se plătește) | testul pornește; rezultatul e în raportul plătit | Raport de bază 12,99 $, Raport standard 19,99 $ | actual | nu | OK | da (Playwright) |
| 9 | giftededu.ro | altul (pagină „Testare IQ gratuita” a unui centru) | nu: HTTP 500, „A fost o eroare critică pe acest site web” | – | – | – | neverificat | da (eroare) |
| 10 | funqb.com | instrument (test IQ copii 9-16 ani, 60 de întrebări grilă) | parțial: câmpurile (nume, vârstă, variante radio) există; rezultatul nu l-am obținut | gratuit | neclar | nu | OK | da (Playwright) |

- Ce apare azi: 6 teste online (2 confirmate cu rezultat gratuit, 2 care pornesc, 1 stricat, 1 cu rezultat plătit), 1 forum, 1 site cu eroare, 1 site blocat
- Instrument gratuit funcțional: da (testiq.ro și arealme.com)
- Produs plătit și preț: brain-testing.org (12,99 $ / 19,99 $ pentru raportul IQ)
- Verdict: PUTERNICE: două teste funcționale, gratuite și fără cont în primele 5 (poz. 2 și 5), plus Mensa pe poz. 3
- Riscuri: niciunul găsit
- Surse blocate: international-iq-test.com (403); reddit.com (nu a întors conținut)

## generator logo (volum: 1900, familie: 03)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: Imagini (poz. 2 și 16), AI Overview (poz. 4), Related searches (poz. 11)
- Rezultate organice în primele 10 poziții: 3 (poz. 1, 3, 5). După poz. 10, necontate, doar titlu din SERP: 3 aplicații Google Play (poz. 28, 38, 54).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | creatorsai.me | neverificat (titlu: „Logos & Branding – CreatorsAI”, pagină de categorie) | neverificat | neverificat | neverificat | neverificat | neverificat | nu (certificat TLS care nu corespunde domeniului; nu am ocolit verificarea); doar titlu din SERP |
| 3 | fr.freelogodesign.org | instrument funcțional (creator de logo, în franceză) | da: nume „Test Firma” → app.freelogodesign.org/design, „24 résultats” cu butoane „ÉDITER” | gratuit (ofertă „Gratuit”); pachete plătite 44,99 $ (redus de la 65 $) și 59,99 $ (redus de la 95 $) | actual | nu pentru generare | OK | da (Playwright) |
| 5 | logotypemaker.com | instrument (generator de logo, în engleză) | parțial: numele duce la editor (/app?logo_name=…) cu galerie („Generate more logos”, ~110 SVG); nu am confirmat că numele apare în logo-uri | generare gratuită; fișiere „High Quality” 19,99 $, cu vector 49,99 $ | actual | neverificat la descărcare | OK | da (Playwright) |

- Ce apare azi: 2 generatoare de logo (în franceză și engleză), 1 site neaccesibil; niciun rezultat în română
- Instrument gratuit funcțional: da (fr.freelogodesign.org; descărcarea la calitate mare se plătește)
- Produs plătit și preț: freelogodesign.org (44,99 $ / 59,99 $), logotypemaker.com (19,99 $ / 49,99 $)
- Verdict: MEDII (verdict pe 3 rezultate organice): un singur generator confirmat în primele 5; al doilea doar parțial; poz. 1 neaccesibilă
- Riscuri: niciunul găsit
- Surse blocate: creatorsai.me (eroare TLS, nu 403/429; trecut aici pentru că nu s-a deschis)

## calculator consum combustibil (volum: 1600, familie: 06)
- Data colectării SERP: 2026-09-02
- Elemente care nu sunt organice: Related searches (poz. 11)
- Rezultate organice în primele 10 poziții: 10

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | peco-online.ro | instrument funcțional | da: 150 km, 7 l/100 km, 7,5 lei → „Necesar combustibil 10.50 l, Cost calatorie 78.75 RON” | gratuit | actual (fără reguli datate) | nu | OK | da (Playwright) |
| 2 | calculatoare-utile.ro | instrument | neconfirmat: după 40 l / 500 km și „Calculează” nu a apărut niciun rezultat în textul paginii | gratuit | actual | nu | OK | da (Playwright) |
| 3 | gps-online.webshow.ro | instrument funcțional (termic, invers, electric) | da: 150 km, 7 l, 7,5 lei → „Consum Total 10.5 Litri, Cost Total 78.75 RON” | gratuit | „2026” în titlu | nu | OK | da (Playwright) |
| 4 | calculat.org | instrument funcțional | da: 150 km → „10,5 ℓ, 78,75 lei” | gratuit | actual | nu | parțial (553px) | da (Playwright) |
| 5 | leaveboard.com | instrument funcțional (pe site-ul unui soft HR) | da: 150 km, 7, 7,5 → „Consum total 10.5 Litri, Preț călătorie 79 RON” | gratuit | actual | nu | OK | da (Playwright) |
| 6 | dosar-auto.ro | instrument funcțional (cost drum, prețuri la zi, rovinietă, pod) | da: 150 km → „Motorină 58 lei, 150 km · 8 L” (consum implicit 5,5) | gratuit | „prețuri actualizate azi, 15.11.2026” | nu | OK | da (Playwright) |
| 7 | pretcarburant.ro | instrument funcțional | da: 500 km, 35 l → „Consum real 7,0 l/100 km… Cost pe 100 km 66,6 lei” | gratuit | „prețul mediu din 15 noiembrie 2026” | nu | OK | da (Playwright) |
| 8 | icredit.ro | articol („Cum se calculează consumul”, pe site de credite rapide) | nu | gratuit | an neclar | nu | neverificat | da |
| 9 | distanta.com | neverificat (titlu: „Distanțe Rutiere… Planificator, Consum”) | neverificat | neverificat | neverificat | neverificat | neverificat | blocat (403); doar titlu din SERP |
| 10 | play.google.com | altul (aplicație „Calculator de combustibil”, „Conține anunțuri”) | neverificat (aplicație) | gratuit cu reclame | „Ultima actualizare 29 sept. 2024” | neverificat | neverificat | da (pagina din magazin) |

- Ce apare azi: 7 calculatoare (6 confirmate), 1 articol, 1 aplicație Android, 1 site blocat
- Instrument gratuit funcțional: da (peco-online.ro; la fel gps-online.webshow.ro, calculat.org, leaveboard.com, dosar-auto.ro, pretcarburant.ro)
- Produs plătit și preț: niciunul găsit
- Verdict: PUTERNICE: patru calculatoare funcționale, actuale și fără cont în primele 5 (poz. 1, 3, 4, 5)
- Riscuri: niciunul găsit
- Surse blocate: distanta.com (403)

## model cerere demisie fara preaviz (volum: 1600, familie: 02)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: Imagini (poz. 1, „Demisia fara preaviz: Ghidul tau 2025 cu model de cerere”), AI Overview (poz. 8)
- Rezultate organice în primele 10 poziții: 4 (poz. 2, 3, 4, 5). Niciunul după poz. 10.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | modelacte.ro | articol cu model (text de copiat cu câmpuri „[Numele complet]”) | nu (nu e generator) | gratuit | an neclar | nu | OK | da |
| 3 | demarches.tn | document de descărcat (PDF în franceză, „modèle de lettre de démission sans préavis”, Tunisia) | nu | gratuit | 2025/09 (după URL); legislație străină | nu | neverificat | da (PDF, text neextras) |
| 4 | gatadecompletat.ro | articol + model .docx („Model_Cerere_Demisie_La_Zi.docx”) | nu | gratuit | 2025/06 (după URL-ul fișierului) | nu | OK | da |
| 5 | infovaslui.ro | articol + model PDF („Formular_demisie.pdf”) | nu | gratuit | „26 ianuarie 2025” | nu | OK | da |

- Ce apare azi: 3 articole cu model (text, DOCX, PDF), 1 PDF străin
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (verdict pe 4 rezultate organice): niciun instrument sau generator, doar articole și documente; unul e pentru Tunisia
- Riscuri: juridic (model de demisie cu efect juridic; după text: „Codul Muncii prevede un termen de preaviz de 20 de zile lucrătoare”)
- Surse blocate: niciuna

## Rezumat

| Căutare | Ce apare azi | Instrument gratuit funcțional | Produs plătit și preț | Verdict | Riscuri |
|---|---|---|---|---|---|
| word in pdf | 2 instrumente, 1 articol, 1 video, 1 aplicație (5 organice) | da (pdf.wondershare.com, smallpdf.com) | swifdoo / wondershare / smallpdf, prețuri neafișate | PUTERNICE (verdict pe 5 rezultate organice) | – |
| calculator medie facultate | 2 calculatoare din alte țări, 1 platformă croată, 1 Facebook (4 organice) | nu | niciunul găsit | SLABE (verdict pe 4 rezultate organice) | – |
| verificare cui | 1 platformă de date (+ pagina de cont), 1 extensie, 1 articol, 1 blocat (5 organice) | da, parțial (data.wedevelop.ro) | data.wedevelop.ro (export blocat, preț necitit) | MEDII (verdict pe 5 rezultate organice) | depinde de instituție (ONRC, MF, ANAF) |
| calculator salariu invatamant | 3 calculatoare (1 confirmat, 1 învechit, 1 pe proiect de lege), 1 video (4 organice) | da (salarii.invatamantpreuniversitar.ro) | niciunul găsit | MEDII (verdict pe 4 rezultate organice) | depinde de instituție (grile OUG/lege salarizare) |
| cerere concediu | 1 generator, 5 articole/modele, 3 documente, 1 Facebook | da (tooluri.ro, poz. 9) | euload.com 150 RON / 3 luni; soft HR fără preț afișat | MEDII | juridic |
| verificare anaf cnp | 7 pagini ANAF, 2 articole | nu | contapp.ro (preț neafișat) | SLABE | depinde de instituție (ANAF) |
| model cerere | 3 documente (3 organice) | nu | niciunul găsit | SLABE (verdict pe 3 rezultate organice) | juridic |
| calculator pensie online | 5 instrumente (2 confirmate, unul din Moldova), 3 pagini ale caselor de pensii, 1 neaccesibil | da (contabss.ro) | niciunul cu preț afișat | MEDII | depinde de instituție (CNPP, Legea 360/2023) |
| test iq gratuit | 6 teste (2 confirmate), 1 forum, 1 eroare, 1 blocat | da (testiq.ro, arealme.com) | brain-testing.org 12,99 $ / 19,99 $ | PUTERNICE | – |
| generator logo | 2 generatoare (FR/EN), 1 neaccesibil (3 organice) | da (fr.freelogodesign.org) | freelogodesign 44,99 $ / 59,99 $; logotypemaker 19,99 $ / 49,99 $ | MEDII (verdict pe 3 rezultate organice) | – |
| calculator consum combustibil | 7 calculatoare (6 confirmate), 1 articol, 1 aplicație, 1 blocat | da (peco-online.ro și alții) | niciunul găsit | PUTERNICE | – |
| model cerere demisie fara preaviz | 3 articole cu model, 1 PDF străin (4 organice) | nu | niciunul găsit | SLABE (verdict pe 4 rezultate organice) | juridic |
