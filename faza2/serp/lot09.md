# Lot 09

Notă generală: SERP-urile vin din `serp_analysis` (Ubersuggest, România, limba română, locId 2642, limit 20, fără refresh). La 7 din 12 căutări unealta a întors o colectare din ziua de azi (2026-11-15, `newData: true`), deși nu am cerut refresh. Contorul de credite a rămas la 7/250 la toate apelurile. Am luat doar rezultatele organice de pe pozițiile 1-10. În tabele scriu poziția brută din SERP.
Paginile le-am deschis cu `citeste.sh`, iar adresele `http://` din SERP le-am deschis pe `https://`. Instrumentele le-am testat cu Playwright (Chromium, fără alte opțiuni), cu valori de test: 1.598 cm³ Euro 6 la impozit auto, 5.000 lei brut la salariu, 100 EUR la valută, CUI 160796 la verificare firmă, un PDF de test de o pagină la conversie și un URL de test la QR. „Telefon OK” înseamnă că, emulat pe iPhone 13, scrollWidth <= innerWidth. „OK (micșorat)” înseamnă că nu apare scroll orizontal, dar pagina are lățimea logică peste 390px, deci se afișează micșorată.

## calculator impozit auto 2026 (volum: 27100, familie: 01,06)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), People also ask (poz. 11)
- În pozițiile 1-10 sunt doar 5 rezultate organice (poz. 1, 3, 4, 5, 7). Poz. 1 și 7 sunt aceeași aplicație Google Play, listată cu alt parametru de limbă (hl=sw, hl=fil).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | play.google.com | altul (aplicație Android „Calculator Taxe Auto 2026”, HaraByte, 10+ descărcări, „NU este o aplicație oficială”) | neverificat (aplicație, nu se poate testa în browser) | gratuit, cu reclame | 2026 în nume și descriere | „fără cont” (după descriere) | aplicație Android | da (pagina Play, deschisă cu hl=ro) |
| 3 | kanald.ro | articol („Calculator Impozit Auto 2021”, publicat 23 feb. 2021, actualizat 22 iul. 2022) | nu (nu are câmpuri) | gratuit | învechit (2021) | nu | neverificat | da |
| 4 | evz.ro | articol (după titlu: noul impozit auto, mașini vechi) | – | – | – | – | – | nu (429, blocat) |
| 5 | upriserz.ro | instrument (după titlu: „Cat te costa de fapt masina ta – calculator practic”) | neverificat | – | – | – | – | nu (403 Cloudflare, blocat) |
| 7 | play.google.com | altul (aceeași aplicație ca la poz. 1) | neverificat | gratuit, cu reclame | 2026 | „fără cont” | aplicație Android | da (același id ca la poz. 1) |

- Ce apare azi: 1 aplicație Android (de 2 ori), 2 articole (unul din 2021, unul blocat), 1 calculator de cost auto blocat. Niciun calculator web de impozit testat.
- Instrument gratuit funcțional: nu (nu am confirmat niciunul; aplicația Play n-am putut-o testa, iar upriserz.ro e blocat)
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (verdict pe 5 rezultate organice; niciun instrument funcțional confirmat în primele 10, doar o aplicație netestată și articole, dintre care unul din 2021)
- Riscuri: depinde de o instituție a statului (după text: aplicația citează Codul fiscal, art. 470-474, iar kanald.ro spune că taxa diferă după hotărârile consiliilor locale); sezonier (după text: căutarea numește anul fiscal „2026”)
- Surse blocate: evz.ro (429), upriserz.ro (403 Cloudflare)

## cod qr generator (volum: 9900, familie: 03)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 1), People also search / „Găsește produse și servicii similare” (poz. 6), Related searches (poz. 12)
- În pozițiile 1-10 sunt doar 4 rezultate organice (poz. 2-5).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | qrcode.tec-it.com | instrument funcțional (în engleză) | da: URL de test → imagine QR generată + link de descărcare | gratuit; „Subscribers can adjust up to 600 DPI” (preț neafișat) | actual | nu | OK | da |
| 3 | play.google.com | altul (aplicație Android „QR Code Generator – QRHyper”, 5M+ descărcări) | neverificat (aplicație) | gratuit, cu reclame și achiziții în aplicație (preț neafișat) | – | neverificat | aplicație Android | da |
| 4 | qrafter.app | instrument funcțional (în engleză) | da: URL de test → QR generat (PNG) + buton Download | gratuit | actual | nu | OK | da |
| 5 | jotform.com | instrument funcțional (în engleză, „for 2026”) | da: URL de test → QR afișat + Download / Copy Link | gratuit; unele opțiuni de design au lacăt, iar site-ul are „Pricing” (preț neafișat pe pagină) | actual (2026 în titlu) | nu pentru QR simplu | OK | da |

- Ce apare azi: 3 instrumente web funcționale (toate în engleză), 1 aplicație Android
- Instrument gratuit funcțional: da (qrcode.tec-it.com, qrafter.app, jotform.com)
- Produs plătit și preț: niciunul cu preț afișat (tec-it are abonament, jotform are planuri, aplicația Play are achiziții, dar fără prețuri pe paginile citite)
- Verdict: PUTERNICE (verdict pe 4 rezultate organice; 3 instrumente funcționale, actuale, fără cont, în primele 5)
- Riscuri: niciunul cu dovadă
- Surse blocate: niciuna

## calculator impozit auto (volum: 6600, familie: 01)
- Data colectării SERP: 2026-08-29
- Elemente care nu sunt organice: Related searches (poz. 11)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | impozitauto.ro | instrument (după titlu: „Impozit Auto 2026 și 2027”) | neverificat | – | 2026 în titlu | – | – | nu (403, blocat) |
| 2 | calculator-impozit-auto.ro | instrument funcțional | da: 1.598 cm³, Euro 6, Sector 1 → „132 lei … +65% față de anul 2025 (80 lei)”, conform HCGMB 514/2025 | gratuit | actual (actualizat 4 feb. 2026, OUG 78/2025) | nu | OK | da |
| 3 | serviciielectronice.brasovcity.ro | pagină a statului (calculator al Primăriei Brașov, după titlu) | neverificat | – | – | – | – | nu (403, blocat) |
| 4 | dfltgm.ro | pagină a statului, instrument funcțional (direcția fiscală locală Târgu Mureș) | da: categoria 1, E6, 1.598 cm³ → „Impozit estimat: 132 lei” | gratuit | actual (tarife pe 200 cm³ cu normă Euro) | nu | OK | da |
| 5 | impozitelocale2.ro | pagină a statului, instrument funcțional (DGITL Sector 2) | da: 1.598 cm³, E5 → „140,8 lei / An”, cu bonificație „127 lei” | gratuit | actual (tarife pe normă de poluare) | nu | OK (micșorat, 448px) | da |
| 6 | spfl.ro | pagină a statului, instrument funcțional (Ploiești, „2026”) | da: 1.598 cm³, Euro 6 → „Impozit anual: 132 lei” | gratuit | 2026 | nu | OK (micșorat, 1240px, fără viewport mobil) | da |
| 7 | dosar-auto.ro | instrument funcțional | da: 1.598 cm³, Euro 6, București → „Impozit estimat … 132 lei pe an” | gratuit | actual („Verificat conform Legii 239/2025”) | nu | OK | da |
| 8 | delta-inmatriculari.ro | instrument funcțional (pe site-ul unei firme de înmatriculări) | da: autoturism ≤1600, 1.598 cm³ → „Impozit anual estimat 132 lei” | gratuit | 2026 (HCGMB 514/2025) | nu | OK | da |
| 9 | autoklass.ro | articol (după titlu: „cât vei plăti în 2024”) | – | – | învechit după titlu (2024) | – | – | nu (403, blocat) |
| 10 | pint.ro | articol (blog al unui broker de asigurări, actualizat 16/01/2026) | nu | gratuit | actual | nu | neverificat | da |

- Ce apare azi: 6 instrumente (3 pe pagini ale direcțiilor fiscale locale), 2 articole, 2 instrumente blocate (impozitauto.ro, Primăria Brașov)
- Instrument gratuit funcțional: da (cel mai bun: calculator-impozit-auto.ro, cu localități și comparația cu 2025; apoi dosar-auto.ro)
- Produs plătit și preț: niciunul găsit
- Verdict: PUTERNICE (calculator-impozit-auto.ro, dfltgm.ro și impozitelocale2.ro sunt funcționale, actuale și fără cont, toate în primele 5)
- Riscuri: depinde de o instituție a statului (după text: tarifele vin din Legea 239/2025, OUG 78/2025 și hotărârile consiliilor locale, de exemplu HCGMB 514/2025; dfltgm.ro: „Impozitul datorat este cel stabilit de organul fiscal local”)
- Surse blocate: impozitauto.ro (403), serviciielectronice.brasovcity.ro (403), autoklass.ro (403)

## pdf in word convert (volum: 5400, familie: 05)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), Related searches (poz. 11)
- În pozițiile 1-10 sunt doar 4 rezultate organice (poz. 1, 3, 4, 5). Primele două pagini de instrument sunt în indoneziană și în rusă.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | pdf2doc.com | instrument funcțional (versiunea în indoneziană) | da: PDF de test încărcat → convertit, apare butonul „UNDUH” (descarcă) | gratuit | actual | nu | OK (micșorat, 506px) | da |
| 3 | tools.picsart.com | instrument (după URL; titlul din SERP e „Untitled”) | neverificat: pagina nu a afișat nimic nici la curl, nici în browser | – | – | – | neverificat | da (pagină goală) |
| 4 | tools.pdf24.org | instrument funcțional (versiunea în rusă) | da: PDF de test → „PDF24 конвертировал ваш файл PDF в DOCX”, test.docx 9,74 KB, buton de descărcare | gratuit („100% бесплатно”, cu reclame) | actual | nu („Регистрация не требуется”) | OK | da |
| 5 | youtube.com | video (tutorial în engleză) | – | – | – | – | – | nu (429/captcha, blocat) |

- Ce apare azi: 2 instrumente funcționale (pe pagini în indoneziană și rusă), 1 instrument care nu s-a încărcat, 1 video
- Instrument gratuit funcțional: da (cel mai bun: tools.pdf24.org)
- Produs plătit și preț: niciunul găsit
- Verdict: PUTERNICE (verdict pe 4 rezultate organice; pdf2doc.com și tools.pdf24.org sunt funcționale, actuale și fără cont, în primele 5, chiar dacă paginile nu sunt în română)
- Riscuri: niciunul cu dovadă
- Surse blocate: youtube.com (429/captcha)

## convertor valutar bnr (volum: 4400, familie: 05,12)
- Data colectării SERP: 2026-08-29
- Elemente care nu sunt organice: Related searches (poz. 11)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | cursbnr.ro | instrument funcțional | da: 100 EUR → 534,98 RON (curs BNR din 13.11.2026); are și calculator de TVA | gratuit | actual (13 nov. 2026) | nu | OK | da |
| 2 | bnr.ro | pagină a statului (convertorul BNR) | neverificat: la curl „This page can't be displayed”, în browser a rămas pe încărcare după 9 secunde | gratuit | – | nu | OK | da (nu s-a încărcat) |
| 3 | cursbnr.nxm.ro | instrument funcțional | da: 100 EUR → „534.98 RON” (+TVA 636,63) | gratuit | actual (13.11.2026) | nu | OK | da |
| 4 | bnr.ro | pagină a statului („Cursul de schimb”, fără convertor) | nu (pagină de informare) | gratuit | actual | nu | OK | da |
| 5 | cursvalutar.ro | instrument funcțional | da: 100 EUR → 534,9800 RON | gratuit | actual (13-11-2026) | nu | OK | da |
| 6 | cursvalutar.ro | instrument funcțional (pagina principală: tabel de curs + convertor) | da: câmpuri de conversie precompletate („1 → 5.3498”), același convertor ca la poz. 5 | gratuit | actual | nu | OK | da |
| 7 | cursbnr.nxm.ro | instrument funcțional (convertor EUR→RON) | da: aceleași câmpuri ca la poz. 3, precompletate cu 1 EUR; testul l-am făcut la poz. 3 | gratuit | actual | nu | OK | da |
| 8 | ing.ro | altul (pagina de curs valutar a băncii ING: curs ING, BNR, BCE) | parțial: are un selector de monedă și afișează cursul, dar nu am găsit un câmp pentru sumă | gratuit | actual (15 nov. 2026) | nu | OK | da |
| 9 | cursbnr.ro | instrument funcțional („Curs BNR azi” + „Convertor rapid”) | da: câmpurile au calculat 1 EUR → 5,35 RON, același motor ca la poz. 1 | gratuit | actual | nu | OK | da |
| 10 | curs-valutar-bnr.ro | instrument funcțional | da: 100 EUR → 534,9800 RON | gratuit | actual (13 nov. 2026) | nu | OK | da |

- Ce apare azi: 7 instrumente funcționale (pe 4 domenii), 2 pagini BNR (dintre care convertorul nu s-a încărcat), 1 pagină de bancă
- Instrument gratuit funcțional: da (cel mai bun: cursbnr.ro)
- Produs plătit și preț: niciunul găsit
- Verdict: PUTERNICE (cursbnr.ro, cursbnr.nxm.ro și cursvalutar.ro sunt funcționale, actuale și fără cont, în primele 5)
- Riscuri: depinde de o instituție a statului (după text: toate folosesc cursul de referință publicat de BNR, „preluate zilnic automat de la Banca Nationala a Romaniei”)
- Surse blocate: niciuna (bnr.ro nu a fost blocat, dar convertorul nu s-a afișat)

## calcul impozit auto (volum: 2900, familie: 01,06)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), Related searches (poz. 11)
- În pozițiile 1-10 sunt doar 4 rezultate organice (poz. 1, 3, 4, 5).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | delta-inmatriculari.ro | instrument funcțional | da: 1.598 cm³ → „Impozit anual estimat 132 lei” | gratuit | 2026 (HCGMB 514/2025) | nu | OK | da |
| 3 | inmatriculari-auto.com.ro | instrument (formular cu capacitate + procent de majorare pe județ, „Suma de plata”) | neverificat: la curl am văzut formularul și tabelul de majorări pe 2026 (de exemplu Alba 16,05%), dar în browser pagina a întors eroarea 500 | gratuit | 2026 în text | nu | neverificat (eroare 500 în browser) | da (curl) |
| 4 | lege5.ro | articol (fragment din Codul fiscal, „actualizat 2026”, pe un site de legislație cu abonament) | nu | fragment gratuit; site cu „Abonamente” (preț neafișat) | actual | nu pentru fragment | neverificat | da |
| 5 | impozitauto.ro | instrument (după titlu: „Impozit auto 2026 Bucuresti-Sector5”) | neverificat | – | 2026 în titlu | – | – | nu (403, blocat) |

- Ce apare azi: 1 instrument funcțional, 1 instrument care nu s-a încărcat în browser, 1 instrument blocat, 1 text de lege
- Instrument gratuit funcțional: da (delta-inmatriculari.ro)
- Produs plătit și preț: lege5.ro (abonament, preț neafișat pe pagină)
- Verdict: MEDII (verdict pe 4 rezultate organice; un singur instrument funcțional confirmat în primele 5)
- Riscuri: depinde de o instituție a statului (după text: HCGMB 514/2025, Codul fiscal, majorări stabilite de fiecare autoritate locală)
- Surse blocate: impozitauto.ro (403)

## model cv european (volum: 2900, familie: 03,09)
- Data colectării SERP: 2026-08-30
- Elemente care nu sunt organice: Imagini (poz. 1), Related searches (poz. 11)
- În pozițiile 1-10 sunt 9 rezultate organice (poz. 2-10).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | europass.europa.eu | instrument funcțional (editorul oficial de CV Europass, UE) | da, parțial verificat: editorul se deschide cu opțiunile „Începeți de la zero” și „Încărcați un CV”; nu am completat un CV întreg | gratuit | actual | opțional („Conectați-vă aici” e separat de „Începeți de la zero”; descărcarea fără cont nu am verificat-o) | OK | da |
| 3 | ubbcluj.ro | document de descărcat (.doc, „Model de Curriculum Vitae European”) | nu | gratuit | învechit (fișier Word creat în 2006) | nu | neverificat | da |
| 4 | anofm.ro | pagină a statului (link de descărcare a modelului din HG 1021/2004) | nu | gratuit | model din 2004 | nu | OK | da |
| 5 | social2.ro | document de descărcat (.doc, după URL; încărcat în 2019) | – | – | – | – | – | nu („One moment, please… request is being verified”, blocat) |
| 6 | hipo.ro | instrument (formular de CV Europass pe un site de joburi) | parțial: formular cu nume, email, telefon, oraș; CV-ul se trimite pe email, iar descărcarea cere cont („Intra in contul tau Hipo pentru a-ti descarca CV-ul European”) | gratuit | anii de naștere merg până la 2011 | da (cont / email) | OK (micșorat, 400px) | da |
| 7 | cariera.ejobs.ro | articol cu modele de descărcat („Model CV 2026”, 18 iun. 2026) | nu (descărcări de modele) | gratuit | 2026 | nu | neverificat | da |
| 8 | ro.scribd.com | document de descărcat („Model CV EUROPASS”, 2 pagini) | nu | descărcare după autentificare | vechi (rubrici fără diacritice corecte) | da pentru descărcare | neverificat | da |
| 9 | pinterest.com | altul (pin cu imagine, trimite la dpap.ro) | nu | gratuit | – | nu | neverificat | da |
| 10 | youtube.com | video („Cum să faci/editezi un CV Europass”) | – | – | – | – | – | nu (429/captcha, blocat) |

- Ce apare azi: 1 editor oficial UE, 1 formular de CV cu cont, 3 documente de descărcat (unul blocat), 1 pagină ANOFM, 1 articol, 1 pin Pinterest, 1 video
- Instrument gratuit funcțional: da (europass.europa.eu)
- Produs plătit și preț: niciunul găsit
- Verdict: MEDII (verdict pe 9 rezultate organice; în primele 5 e un singur instrument funcțional, editorul Europass; restul sunt documente vechi și pagini de descărcare)
- Riscuri: niciunul cu dovadă (CV-ul nu are efect juridic)
- Surse blocate: social2.ro (verificare anti-bot), youtube.com (429/captcha)

## calculator salariu net 2026 (volum: 2400, familie: 01)
- Data colectării SERP: 2026-09-02
- Elemente care nu sunt organice: People also ask (poz. 7), Related searches (poz. 12)
- În pozițiile 1-10 sunt 9 rezultate organice (poz. 1-6, 8-10).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | calculator-salarii.ro | instrument funcțional | da: 5.000 brut → „Salariu Net 2967” | gratuit | 2026 (anii 2025-2027) | nu | OK | da |
| 2 | salariile.ro | instrument funcțional (brut→net și net→brut) | da: 5.000 brut → „Salariu net 2.981 lei” | gratuit | 2026 | nu | OK | da |
| 3 | impozitsalariu.ro | instrument funcțional | da: 5.000 brut → „Primești în mână 2.981 RON” | gratuit | 2026 | nu | OK | da |
| 4 | salaria.ro | instrument funcțional | da: afișează un rezultat calculat implicit (4.325 brut → 2.699 net); completarea altei valori nu a mers în testul pe desktop | gratuit | 2026 și „2026 iul.” în listă | nu | OK (micșorat, 481px) | da |
| 5 | paylab.ro | instrument funcțional | da: 5.000 brut → „Salariul NET 3.028,00 RON” | gratuit | 2026 | nu | OK | da |
| 6 | calculatoare-salarizare.ro | instrument (fluturaș de salariu încărcat într-un iframe) | nu în test: iframe-ul calculatorului a întors 502 | gratuit | 2026 | nu | OK (micșorat, 685px) | da |
| 8 | undelucram.ro | instrument funcțional | da: 5.000 brut → „2.981 Salariu Net” | gratuit | 2026 | nu | OK | da |
| 9 | portalcodulfiscal.ro | instrument (calculator manager.ro încărcat într-un iframe, pe un site cu „Cont Premium”) | da prin curl: calculatorul din iframe (manager.ro) a dat la 5.000 brut „Salariu Net 2967”; în browser site-ul a cerut verificarea Cloudflare | calculator gratuit; abonament premium cu preț neafișat | 2026 | nu pentru calculator | neverificat (Cloudflare în browser) | da (curl) |
| 10 | jobinfo.ro | instrument funcțional | da: 5.000 brut → „Salariu Net 2.942,50 RON” | gratuit | 2026 | nu | OK | da |

- Ce apare azi: 9 instrumente, dintre care 7 confirmate funcționale în browser și unul confirmat doar prin curl. Pentru același brut de 5.000 lei, netul afișat diferă: 2.942,50 / 2.967 / 2.981 / 3.028 lei.
- Instrument gratuit funcțional: da (cel mai bun: salariile.ro sau impozitsalariu.ro)
- Produs plătit și preț: portalcodulfiscal.ro (abonament premium, preț neafișat)
- Verdict: PUTERNICE (verdict pe 9 rezultate organice; toate cele 5 rezultate din primele 5 sunt instrumente funcționale, actuale și fără cont)
- Riscuri: depinde de o instituție a statului (după text: CAS 25%, CASS 10%, impozit 10%, deducere personală și salariu minim din Codul fiscal și din HG; paylab.ro citează plafonul de 4.000 lei și salariul minim de 3.700 lei); sezonier (după text: căutarea numește anul fiscal „2026”, iar mai multe site-uri au variantă separată „2026 iul.”)
- Surse blocate: portalcodulfiscal.ro doar în browser (Cloudflare „Just a moment”); la curl s-a deschis

## verificare firma (volum: 2400, familie: 04)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), Related searches (poz. 11)
- În pozițiile 1-10 sunt doar 4 rezultate organice (poz. 1, 3, 4, 5).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | infoquick.ro | instrument funcțional (Coface InfoQuick) | da: CUI 160796 → „AUTOMOBILE-DACIA SA, J1991000081036, Mioveni, Argeș, functiune” | căutare gratuită; rapoarte cu plată („Cumpara InfoQuick”, preț neafișat în textul citit) | actual | nu pentru căutare | OK | da |
| 3 | datefirma.ro | instrument funcțional | da: CUI 160796 → Dacia, cifra de afaceri 29.919.900.100 RON, profit net, 10.556 angajați | gratuit | actual | nu | OK | da |
| 4 | nexuserp.ro | altul (pagina de căutare internă a unui furnizor de ERP: „175 rezultate găsite pentru: verificare firma”) | nu | gratuit | – | nu | OK | da |
| 5 | raport-firma.ro | produs plătit (căutarea e gratuită și arată date de bază, raportul complet PDF e cu plată) | da: CUI 160796 → „AUTOMOBILE-DACIA SA … ACTIVĂ Mioveni” | căutare gratuită; „Raport complet 50 RON”, fără TVA | actual | nu (email pentru comandă) | OK | da |

- Ce apare azi: 2 instrumente gratuite funcționale, 1 serviciu plătit cu căutare gratuită, 1 pagină de căutare a unui furnizor de ERP
- Instrument gratuit funcțional: da (cel mai bun: datefirma.ro, cu date financiare fără cont)
- Produs plătit și preț: raport-firma.ro, 50 RON per raport; infoquick.ro, rapoarte cu plată (preț neafișat)
- Verdict: PUTERNICE (verdict pe 4 rezultate organice; infoquick.ro și datefirma.ro sunt funcționale, actuale și fără cont pentru căutare, în primele 5)
- Riscuri: depinde de o instituție a statului (după text: „informatii de la Registrul Comertului si ANAF”, iar raport-firma.ro verifică ANAF, TVA și VIES)
- Surse blocate: niciuna

## model cerere demisie simpla (volum: 1900, familie: 02,09)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: Imagini (poz. 1, „Cerere de demisie: model, tipuri și prevederi Codul Muncii”), AI Overview (poz. 3)
- În pozițiile 1-10 sunt doar 3 rezultate organice (poz. 2, 4, 5).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 2 | modelacte.ro | articol (text de model: „Exemplu de scrisoare de demisie”, cu câmpuri goale) | nu (text de copiat, fără generator) | gratuit | fără an vizibil | nu | neverificat | da |
| 4 | cdn.prod.website-files.com | document de descărcat (PDF „Model cerere demisie fara preaviz pdf”: text amestecat engleză/română, cu un model de cerere la mijloc) | nu | gratuit | PDF creat în 2024 | nu | neverificat | da |
| 5 | es.scribd.com | document de descărcat (model de demisie cu preaviz, interfață în spaniolă, „Traducido por ScribdTranslations”) | nu | descărcare după autentificare | – | da pentru descărcare | neverificat | da |

- Ce apare azi: 1 articol cu model, 2 documente (un PDF de calitate slabă și un document Scribd)
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (verdict pe 3 rezultate organice; niciun instrument funcțional în primele 10, doar texte și documente de model)
- Riscuri: juridic (model de document cu efect juridic: cererea de demisie încetează contractul de muncă; PDF-ul vorbește de preaviz de „20 zile lucrătoare … și 45 de zile” după Codul Muncii); depinde de o instituție a statului: nu am găsit dovadă
- Surse blocate: niciuna

## calculator dividende 2025 (volum: 1600, familie: 01)
- Data colectării SERP: 2026-10-02
- Elemente care nu sunt organice: AI Overview (poz. 2)
- În pozițiile 1-10 sunt 9 rezultate organice (poz. 1, 3-10), toate pe termene.ro, pagini de profil ale unor firme.

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | termene.ro | director, agregator (profilul firmei „ARENA ADVERTISING KEY SRL”) | – | – | – | – | – | nu (403 „Just a moment”, blocat) |
| 3 | termene.ro | director, agregator (profilul „HEADMADE ADVERTISING S.R.L.”) | – | – | – | – | – | nu (403, blocat) |
| 4 | termene.ro | director, agregator („contourglobal solutions (ploiesti) srl”) | – | – | – | – | – | nu (403, blocat) |
| 5 | termene.ro | director, agregator („DOREL PLANT S.R.L.”) | – | – | – | – | – | nu (403, blocat) |
| 6 | termene.ro | director, agregator („GEMIDO DISTRIBUTION SRL”) | – | – | – | – | – | nu (403, blocat) |
| 7 | termene.ro | director, agregator („OBAM HOLDING S.R.L.”) | – | – | – | – | – | nu (403, blocat) |
| 8 | termene.ro | director, agregator („NEXT GEN ACCOUNTING S.R.L.”) | – | – | – | – | – | nu (403, blocat) |
| 9 | termene.ro | director, agregator („VICIUNAI BUCHAREST SRL”) | – | – | – | – | – | nu (403, blocat) |
| 10 | termene.ro | director, agregator („BALUBE S.R.L.”) | – | – | – | – | – | nu (403, blocat) |

- Ce apare azi: 9 pagini de profil de firmă pe termene.ro (după titluri). Niciun calculator de dividende în titluri.
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit (paginile sunt blocate)
- Verdict: SLABE (verdict pe 9 rezultate organice; niciun instrument în primele 10, după titlurile din SERP, la o căutare care cere un calculator)
- Riscuri: sezonier (după text: căutarea numește anul fiscal „2025”); depinde de o instituție a statului: nu am dovadă din pagini, pentru că toate sunt blocate
- Surse blocate: termene.ro (403 Cloudflare „Just a moment”, pe toate cele 9 URL-uri)

## model cv angajare pdf (volum: 1600, familie: 03,09)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: Imagini (poz. 1, „Model CV | PDF”), AI Overview (poz. 2), People also search / „Găsește produse și servicii similare” (poz. 3)
- În pozițiile 1-10 sunt doar 2 rezultate organice (poz. 4, 5).

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 4 | br.pinterest.com | altul (pin cu imagine „Exemple de CV avec Photo Gratuit à Télécharger”, în franceză, trimite la modeles-de-cv.com) | nu | gratuit | – | nu | neverificat | da |
| 5 | liveutmb.sharepoint.com | document de descărcat (document Word partajat pe SharePoint-ul unei instituții) | – | – | – | – | – | nu (403, blocat) |

- Ce apare azi: 1 pin Pinterest în franceză, 1 document SharePoint blocat
- Instrument gratuit funcțional: nu
- Produs plătit și preț: niciunul găsit
- Verdict: SLABE (verdict pe 2 rezultate organice; niciun instrument funcțional și niciun model românesc în primele 10)
- Riscuri: niciunul cu dovadă
- Surse blocate: liveutmb.sharepoint.com (403)

## Rezumat

| Căutare | Ce apare azi | Instrument gratuit funcțional | Produs plătit și preț | Verdict | Riscuri |
|---|---|---|---|---|---|
| calculator impozit auto 2026 | 1 aplicație Android (de 2 ori), 2 articole (unul din 2021), 1 calculator blocat; 5 organice | nu | niciunul găsit | SLABE (pe 5 organice) | depinde de o instituție a statului; sezonier |
| cod qr generator | 3 instrumente (în engleză), 1 aplicație Android; 4 organice | da (qrcode.tec-it.com, qrafter.app, jotform.com) | niciunul cu preț afișat | PUTERNICE (pe 4 organice) | – |
| calculator impozit auto | 6 instrumente (3 ale direcțiilor fiscale locale), 2 articole, 2 instrumente blocate | da (calculator-impozit-auto.ro) | niciunul găsit | PUTERNICE | depinde de o instituție a statului |
| pdf in word convert | 2 instrumente (în indoneziană și rusă), 1 instrument neîncărcat, 1 video; 4 organice | da (tools.pdf24.org) | niciunul găsit | PUTERNICE (pe 4 organice) | – |
| convertor valutar bnr | 7 instrumente (4 domenii), 2 pagini BNR, 1 pagină de bancă | da (cursbnr.ro) | niciunul găsit | PUTERNICE | depinde de o instituție a statului |
| calcul impozit auto | 1 instrument funcțional, 1 instrument cu eroare 500, 1 blocat, 1 text de lege; 4 organice | da (delta-inmatriculari.ro) | lege5.ro, abonament (preț neafișat) | MEDII (pe 4 organice) | depinde de o instituție a statului |
| model cv european | 1 editor UE, 1 formular cu cont, 3 documente, 1 pagină ANOFM, 1 articol, 1 pin, 1 video; 9 organice | da (europass.europa.eu) | niciunul găsit | MEDII (pe 9 organice) | – |
| calculator salariu net 2026 | 9 instrumente (7 confirmate în browser, 1 prin curl, 1 cu eroare 502); 9 organice | da (salariile.ro / impozitsalariu.ro) | portalcodulfiscal.ro, premium (preț neafișat) | PUTERNICE (pe 9 organice) | depinde de o instituție a statului; sezonier |
| verificare firma | 2 instrumente gratuite, 1 serviciu plătit, 1 pagină ERP; 4 organice | da (datefirma.ro) | raport-firma.ro 50 RON/raport; infoquick.ro (preț neafișat) | PUTERNICE (pe 4 organice) | depinde de o instituție a statului |
| model cerere demisie simpla | 1 articol cu model, 2 documente; 3 organice | nu | niciunul găsit | SLABE (pe 3 organice) | juridic |
| calculator dividende 2025 | 9 profiluri de firmă termene.ro (blocate); 9 organice | nu | niciunul găsit | SLABE (pe 9 organice) | sezonier |
| model cv angajare pdf | 1 pin Pinterest în franceză, 1 document blocat; 2 organice | nu | niciunul găsit | SLABE (pe 2 organice) | – |
