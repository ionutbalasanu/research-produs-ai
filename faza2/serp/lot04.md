# Lot 04

Note de metodă (valabile pentru tot lotul):
- SERP: Ubersuggest `serp_analysis`, language=ro, locId=2642 (România), limit=20, fără refresh. „Poz” = locul printre rezultatele organice (1–10), nu poziția brută din SERP.
- Pagini deschise cu `citeste.sh` (curl simplu, prin https). Instrumentele au fost verificate cu Playwright (chromium.launch() fără opțiuni, 3–5 s de așteptare). Telefon = `devices['iPhone 13']`, cu verificarea scrollWidth <= innerWidth.
- „da (test)” = am introdus o valoare de test și am primit un rezultat calculat. „câmpuri, netestat” = am văzut câmpurile, dar nu am cerut un rezultat. La verificările auto (RCA, rovinietă) nu am introdus numere de înmatriculare, ca să nu interoghez date despre vehicule reale.
- Telefon „da*” = fără scroll orizontal, dar pagina nu are layout de mobil: innerWidth raportat > 390 px, deci pagina se afișează micșorată.
- Valori de test folosite: salariu brut 5.000 lei (rezultatul corect după regulile din iulie 2026, confirmat de 6 site-uri: net 2.981 lei); consum: 200 km, 7 l/100 km, 8 lei/l (14 l, 112 lei); dobândă compusă: 1.000, 5 %, 10 perioade.

## verificare rca (volum: 90500, familie: 04,06)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 2), Related searches. **Doar 4 rezultate organice în SERP.**

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | economo.ro (/informatii-asigurari/verificare-rca) | articol (trimite la AIDA, apoi la calculatorul RCA Economo) | nu e instrument | gratuit | fără an vizibil; menționează AIDA „din 2018” | nu | neverificat | da |
| 2 | aida.info.ro (/en/polite-rca) | instrument (baza oficială AIDA/BAAR) | neverificat: blocat de anti-bot („Acces temporar restricționat”, HTTP 202) | – | – | – | neverificat | blocat |
| 3 | rca.ro | produs plătit (comparator și vânzare de polițe RCA; câmp pentru nr. auto) | câmpuri, netestat (calculează prețul, nu verifică valabilitatea) | comparare gratuită, poliță plătită; preț neafișat fără date | da | nu pentru comparare | da | da |
| 4 | groupama.ro (/persoane-fizice/asigurare-auto/asigurarea-rca) | produs plătit (pagina de produs a unui asigurător) | nu e instrument de verificare | preț neafișat | da | – | neverificat | da |

- Ce apare azi: 1 articol, 1 instrument oficial blocat (AIDA), 2 pagini comerciale de vânzare RCA (doar 4 rezultate organice)
- Instrument gratuit funcțional: nu (niciunul confirmat; AIDA probabil e funcțional, dar nu l-am putut verifica)
- Produs plătit și preț: rca.ro, groupama.ro: polițe RCA, prețul nu e afișat fără datele vehiculului
- Verdict: slabe (niciun instrument de verificare confirmat ca funcțional în SERP; singurul candidat, AIDA, e blocat pentru acces automat)
- Riscuri: depinde de o instituție/bază de date externă (AIDA, administrată de BAAR; economo.ro: „AIDA ... în coordonarea BAAR”)
- Surse blocate: aida.info.ro (pagină anti-bot, HTTP 202)

## calculator salariu brut (volum: 14800, familie: 01)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 3), Related searches. **Doar 5 rezultate organice în SERP.**

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | calculator-salarii.ro (/calcul-salariu-brut/) | instrument funcțional (net → brut) | da (test: net 3.000 → brut 5.036) | gratuit | da (2026, 2027 în listă) | nu | da | da |
| 2 | salaria.ro | instrument funcțional | da (test: brut 5.000 → net 2.981) | gratuit | da („valabil din Iulie 2026”) | nu | da* (481 px) | da |
| 3 | salariile.ro | instrument funcțional | da (test: net 2.981) | gratuit | da (2026) | nu | da | da |
| 4 | salariucalculator.ro | instrument funcțional | da (test: net 2.981) | gratuit | da (iulie–dec. 2026, minim 4.325) | nu | da | da |
| 5 | play.google.com (com.calc.calculatorsalarii) | altul (aplicație Android) | neverificat (aplicație) | gratuit, cu anunțuri | neverificat | – | – | da |

- Ce apare azi: 4 instrumente web funcționale, 1 aplicație Android (doar 5 rezultate organice)
- Instrument gratuit funcțional: da (cel mai bun: salariucalculator.ro / salariile.ro; toate cele 4 au dat aceleași cifre corecte)
- Produs plătit și preț: niciunul găsit
- Verdict: puternice (4 instrumente funcționale, actuale, fără cont, pe pozițiile 1–4)
- Riscuri: depinde de o instituție a statului (reguli fiscale din Codul fiscal/ANAF; salariul minim s-a schimbat în iulie 2026, după textul salariucalculator.ro)
- Surse blocate: niciuna

## calcul salariu brut (volum: 8100, familie: 01)
- Data colectării SERP: 2026-10-01
- Elemente care nu sunt organice: AI Overview (poz. 10), Related searches

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | calculator-salarii.ro (/calcul-salariu-brut/) | instrument funcțional | da (test) | gratuit | da | nu | da | da |
| 2 | salariile.ro | instrument funcțional | da (test: 2.981) | gratuit | da | nu | da | da |
| 3 | impozitsalariu.ro | instrument funcțional | da (test: 2.981, iulie 2026) | gratuit | da | nu | da | da |
| 4 | salaria.ro | instrument funcțional | da (test: 2.981) | gratuit | da | nu | da* | da |
| 5 | paylab.ro (/salariu-calculator) | instrument funcțional | da (test: net 3.028, diferit de celelalte 6 site-uri; nota de pe pagină citează minimul de 3.700 lei, adică reguli vechi) | gratuit | parțial (opțiuni 2025/2026, dar notă cu reguli vechi) | nu | da | da |
| 6 | calculatoare-salarizare.ro (/salariu.php) | instrument (foaie Excel într-un iframe) | câmpuri văzute în iframe, netestat | gratuit | da („2026”, plus arhivă pe ani) | nu | da* (layout desktop, 1223 px) | da |
| 7 | salariucalculator.ro | instrument funcțional | da (test: 2.981) | gratuit | da | nu | da | da |
| 8 | forvismazars.com (/ro/.../salariu-net-vs-brut) | articol | nu e instrument | gratuit | neverificat | nu | neverificat | da |
| 9 | leaveboard.com (/ro/calculator-salariu/) | instrument funcțional (pe site-ul unui produs HR) | da (test: 2.981) | gratuit | da | nu | da* (405 px) | da |
| 10 | portalcontabilitate.ro (/calculator_salariu/) | instrument (după titlu: „Noul Cod Fiscal 2026”) | neverificat: Cloudflare „Just a moment” în browser (curl a primit doar textul paginii, cu fereastra de autentificare) | – | titlu 2026 | posibil (fereastră de login în pagină) | neverificat | parțial |

- Ce apare azi: 8 instrumente (7 testate funcționale, 1 netestat), 1 articol, 1 instrument blocat
- Instrument gratuit funcțional: da (cel mai bun: impozitsalariu.ro / salariile.ro)
- Produs plătit și preț: niciunul găsit (leaveboard.com e software HR cu pagină de prețuri, dar calculatorul e gratuit)
- Verdict: puternice (5 instrumente funcționale, actuale, fără cont, pe pozițiile 1–5)
- Riscuri: depinde de o instituție a statului (Cod fiscal/ANAF; paylab.ro arată deja o abatere de la regulile curente)
- Surse blocate: portalcontabilitate.ro (Cloudflare „Just a moment”)

## verificare rovinieta fara serie sasiu (volum: 6600, familie: 04,06)
- Data colectării SERP: 2026-08-28
- Elemente care nu sunt organice: AI Overview (poz. 1), Related searches

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | erovinieta.net (/verificare-rovinieta) | instrument (serviciu privat; nr. auto, seria de șasiu „dacă ți-o cerem”) | câmpuri, netestat | gratuit (vinde și roviniete) | da („Actualizat: 5 noiembrie 2026”, TollRo) | nu („fără cont”) | da | da |
| 2 | evita-amenzi.ro (/verificare-rovinieta) | instrument (nr. auto, apoi confirmă VIN) | câmpuri, netestat | gratuit | da (TollRo 2026) | nu pentru verificare; cont gratuit pentru alerte | da | da |
| 3 | roviniete.ro (/ro/Comunicat-De-Presa/114/...) | articol + magazin de roviniete (textul cere nr. și seria de șasiu, plus cod) | formular de verificare nevăzut în browser | gratuit / roviniete plătite | fără dată | – | da (405 > 390: ușor scroll orizontal) | da |
| 4 | peco-online.ro (/promotii.php) | articol (trimite la CNAIR/erovinieta.ro, cere VIN) | nu e instrument | gratuit | parțial (spune că se verifică pe erovinieta.ro, care nu mai răspunde) | nu | da | da |
| 5 | compara-asigurari.ro (/verificare-rovinieta/) | articol + calculator de tarife (selectoare de categorie/durată) | nu verifică; calculează tariful | gratuit | da (2026) | nu | da | da |
| 6 | verificarerovinieta.com | instrument (câmpuri nr. auto + VIN) | câmpuri, netestat | gratuit | da („Din octombrie 2026, seria de șasiu nu mai este necesară”) | nu | da | da |
| 7 | erovinieta.ro (/vgncheck/) | pagină a statului (registrul CNAIR) | nu: HTTP 503; alte site-uri spun că nu mai merge din 7 oct. 2026 | – | învechit/oprit | – | – | da (503) |
| 8 | bucuresti.cnadnr.ro | pagină a statului | nedeschis (conexiune resetată) | – | – | – | – | doar titlu din SERP |
| 9 | 9695.ro (/verifica-rovinieta/) | articol (ghid) | nu e instrument | gratuit | neverificat | nu | da | da |
| 10 | cnadnr.ro (/ro/roviniete/intrebari-si-raspunsuri...) | pagină a statului (FAQ) | nedeschis (HTTP 502 „upstream request failed”) | – | – | – | – | doar titlu din SERP |

- Ce apare azi: 3 instrumente private (netestate), 4 articole (2 cu calculator de tarif sau magazin), 3 pagini ale statului (toate indisponibile la verificare)
- Instrument gratuit funcțional: neconfirmat (au câmpuri și pretind că funcționează: erovinieta.net, evita-amenzi.ro, verificarerovinieta.com; nu am cerut un rezultat)
- Produs plătit și preț: erovinieta.net și roviniete.ro vând roviniete; prețurile sunt tarifele legale, nu le-am notat de pe pagină
- Verdict: medii (3 instrumente actuale, fără cont, în primele 6, dar funcționarea lor nu e confirmată; registrul oficial e oprit)
- Riscuri: depinde de o instituție a statului (CNAIR/TollRo: „registrul public CNAIR (erovinieta.ro/vgncheck) nu funcționează din 7 octombrie 2026”, după textul erovinieta.net; erovinieta.ro a răspuns cu 503)
- Surse blocate: niciuna blocată anti-bot; inaccesibile: erovinieta.ro/vgncheck (503), bucuresti.cnadnr.ro (conexiune resetată), cnadnr.ro (502)

## calculator calorii (volum: 4400, familie: 12)
- Data colectării SERP: 2026-10-01
- Elemente care nu sunt organice: AI Overview (poz. 2), Imagini (poz. 19)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | apps.apple.com (CalTrack) | altul (aplicație iOS) | neverificat (aplicație) | „Gratis · Achiziții din aplicație” | da | – | – | da |
| 2 | body365.ro (/calculator-calorii-macronutrienti-si-hidratare-cbdy/) | articol (descrie „aplicația CBDY”; pe pagină nu există un calculator) | nu (fără câmpuri de calcul) | – | 09/03/2025 | – | da | da |
| 3 | play.google.com (NutriLens) | altul (aplicație Android) | neverificat | gratuit, cu anunțuri | actualizat 24.05.2026 | – | – | da |
| 4 | apps.apple.com (Rig: AI Calculator Calorii) | altul (aplicație iOS) | neverificat | „Gratis · Achiziții din aplicație” | da | – | – | da |
| 5 | calculator.cat (/calculator-de-calorii-pentru-retete/) | instrument (calorii pentru rețete, nu necesar caloric) | câmpuri prezente; testul nu a confirmat un rezultat | gratuit | 5 aug. 2026 | nu | da | da |
| 6 | trendyol.com (cântar calculator calorii) | produs plătit (cântar de bucătărie) | – | preț nevăzut | – | – | – | blocat (403) |
| 7 | apps.apple.com (Eat Track, listă „S-ar putea să vă placă”) | director (listă de aplicații) | – | – | – | – | – | da |
| 8 | play.google.com (KiloTrack) | altul (aplicație Android) | neverificat | anunțuri + achiziții în aplicație | da | „fără cont obligatoriu” | – | da |
| 9 | apps.apple.com (Mancare, listă „S-ar putea să vă placă”) | director (listă de aplicații) | – | – | – | – | – | da |
| 10 | play.google.com (TDEE Calculator Calorii) | altul (aplicație Android) | neverificat | anunțuri + achiziții în aplicație | da | „Fără cont” | – | da |

- Ce apare azi: 6 aplicații mobile, 2 liste App Store, 1 articol, 1 instrument web de nișă (rețete), 1 produs fizic
- Instrument gratuit funcțional: nu (niciun calculator web de necesar caloric; calculator.cat neconfirmat)
- Produs plătit și preț: aplicații cu achiziții în aplicație (prețuri neafișate pe paginile deschise); trendyol.com, cântar (blocat)
- Verdict: slabe (niciun instrument web funcțional confirmat în primele 10; SERP dominat de magazine de aplicații)
- Riscuri: niciunul cu dovadă
- Surse blocate: trendyol.com (403)

## model cv europass (volum: 3600, familie: 03,09)
- Data colectării SERP: 2026-08-30
- Elemente care nu sunt organice: Imagini (poz. 1), Related searches

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | europass.europa.eu (/ro/create-europass-cv) | instrument funcțional (pagina UE, cu editor la europa.eu/europass/eportfolio/screen/cv-editor) | da (editorul se deschide cu opțiunea „start from scratch”); nu am completat un CV | gratuit | da | nu pentru a începe (login opțional) | da | da |
| 2 | social2.ro (.../2019/04/CV-european-model.doc) | document de descărcat (DOC) | – | gratuit | 2019 | nu | – | da |
| 3 | anofm.ro (/cv-europass/) | pagină a statului (link de descărcare, model după HG 1021/2004) | – | gratuit | model din 2004 | nu | neverificat | da |
| 4 | anp.gov.ro (.../2020/11/Model-de-CV-Europass.doc) | document de descărcat (DOC) | – | – | 2020 (după URL) | – | – | doar titlu din SERP (conexiune resetată) |
| 5 | hipo.ro (/locuri-de-munca/cveuropass) | articol + descărcare model | – | gratuit | neverificat | nu | neverificat | da |
| 6 | europass.europa.eu (/ro) | pagină oficială UE (acasă) | – | gratuit | da | – | neverificat | da |
| 7 | ubbcluj.ro (.../model_CV_european.doc) | document de descărcat (DOC) | – | gratuit | neverificat | nu | – | da |
| 8 | ro.scribd.com (/doc/244898811/Model-CV-EUROPASS) | document de descărcat (agregator) | – | descărcare după autentificare | neverificat | da pentru descărcare | neverificat | da |
| 9 | cariera.ejobs.ro (/model-cv/) | articol (modele de CV) | – | gratuit | 18 iun. 2026 | nu | neverificat | da |
| 10 | cvwizard.com (/ro/articol/europass-cv) | articol (de la un generator de CV comercial cu pagina „Costuri”) | – | preț neafișat în articol | 29 aprilie 2025 | – | neverificat | da |

- Ce apare azi: 1 instrument oficial (Europass), 3 DOC de descărcat, 1 pagină ANOFM, 1 pagină UE, 1 Scribd, 3 articole
- Instrument gratuit funcțional: da (europass.europa.eu)
- Produs plătit și preț: cvwizard.com (generator comercial; prețul nu e afișat pe pagina deschisă)
- Verdict: medii (un singur instrument funcțional, oficial; restul sunt modele DOC vechi și articole)
- Riscuri: niciunul cu dovadă (formatul Europass aparține Comisiei Europene, nu unei instituții românești din listă)
- Surse blocate: niciuna anti-bot; anp.gov.ro: conexiune resetată

## cerere concediu de odihna (volum: 2900, familie: 02,09)
- Data colectării SERP: 2026-08-30
- Elemente care nu sunt organice: Imagini (poz. 1), Related searches

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | euload.com (/model/5.3. Cerere de concediu odihna (CO).pdf) | document de descărcat (PDF) | linkul redirecționează la „under.subscription.php” | după abonament | – | da (abonament) | – | da (redirect) |
| 2 | facebook.com (postare contabun.ro) | altul (postare pe rețea socială) | – | – | – | – | – | da (doar titlul) |
| 3 | ru.scribd.com (Anexa 4 CERERE concediu de odihna) | document de descărcat (agregator, interfață în rusă) | – | descărcare după autentificare | neverificat | da | – | da |
| 4 | papervee.com (/ro/blog/cerere-concediu-de-odihna) | articol + model (de la un software HR plătit) | – | model gratuit; produs cu „Solicită demo”, fără preț afișat | 15 aprilie 2026 | nu | neverificat | da |
| 5 | leaveboard.com (/ro/modele-cereri/concediul-de-odihna/) | articol + model (software HR) | – | gratuit | neverificat | nu | neverificat | da |
| 6 | sdworx.ro (.../concediu-de-odihna-cerere-informatii-modele) | articol + modele | – | gratuit | 12 martie 2026 | nu | neverificat | da |
| 7 | primariasantandrei.ro (/documente.php?id=69) | document de descărcat (DOC „2018_2019”) | – | gratuit | 2019 | nu | – | da |
| 8 | nexuserp.ro (/blog/cerere-pentru-concediu-de-odihna) | document de descărcat (DOC/PDF) | – | gratuit | 10.08.2021 | nu | neverificat | da |
| 9 | form.jotform.com (/250934089371361) | instrument (formular al unei firme anume, „TENQ ONLINE SRL”) | formular funcțional, dar valabil doar pentru acea firmă | gratuit | – | nu | da | da |
| 10 | ro.scribd.com (cerere concediu de odihnă parțial) | document de descărcat (agregator) | – | descărcare după autentificare | neverificat | da | – | da |

- Ce apare azi: 5 documente de descărcat (2 pe Scribd, 1 PDF după abonament), 3 articole cu model, 1 postare Facebook, 1 formular Jotform al unei firme anume
- Instrument gratuit funcțional: nu (niciun generator de cerere; formularul Jotform aparține unei singure firme)
- Produs plătit și preț: papervee.com (software HR, preț neafișat); euload.com (abonament, preț nevăzut)
- Verdict: slabe (niciun instrument funcțional general; doar modele și articole la o căutare care cere un document completat)
- Riscuri: juridic (model de document cu efect juridic: cerere de concediu conform art. 144 din Codul muncii, după titlul postării contabun.ro)
- Surse blocate: niciuna (euload.com cere abonament; Facebook a întors doar titlul)

## calculator dobanda compusa (volum: 2400, familie: 01)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 1)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | youtube.com (watch?v=L80yjKXtsCc) | video (în engleză) | – | – | – | – | – | blocat (429 / captcha) |
| 2 | simulatudo.com.br (/en/calculators/juros-compostos) | instrument funcțional (în engleză, R$) | da (test: suma finală R$2.531,87) | gratuit | da | nu | da | da |
| 3 | sarmaaya.pk (/calculator/compounding) | instrument funcțional (în engleză, pentru forex) | da (test: tabel pe perioade, 1.000 → 1.050 → 1.102,5…) | gratuit | da | nu | da | da |
| 4 | simplemarketsacademy.com (/investmentcalculator) | instrument funcțional (în engleză, $) | da (test: sold final calculat) | gratuit | da | nu | da | da |
| 5 | play.google.com (com.simulatore.pac, „FIRE Calculator”) | altul (aplicație Android) | neverificat | gratuit | – | – | – | da |
| 6 | play.google.com (com.investezen.app.calculator) | altul (aplicație Android) | neverificat | anunțuri + achiziții în aplicație | – | – | – | da |
| 7 | play.google.com (Calcular Interés Compuesto) | altul (aplicație Android) | neverificat | anunțuri | – | – | – | da |
| 8 | play.google.com (Calculator de dobândă compusă, JV CODE LAB) | altul (aplicație Android, în română) | neverificat | anunțuri | – | – | – | da |
| 9 | play.google.com (Compound Interest, SimpleEvo) | altul (aplicație Android) | neverificat | anunțuri | – | – | – | da |
| 10 | play.google.com (Compounding Calculator, UKM APPS) | altul (aplicație Android) | neverificat | anunțuri | – | – | – | da |

- Ce apare azi: 3 instrumente web străine (în engleză), 6 aplicații Android, 1 video; niciun site românesc
- Instrument gratuit funcțional: da (simulatudo.com.br; niciunul în română)
- Produs plătit și preț: niciunul găsit (aplicații cu anunțuri sau achiziții în aplicație, fără preț afișat)
- Verdict: puternice conform definiției (3 instrumente funcționale, actuale, fără cont, pe pozițiile 2–4), cu observația că niciunul nu e în română și nu folosește lei
- Riscuri: niciunul cu dovadă
- Surse blocate: youtube.com (429 / „unusual traffic”)

## cv online gratis (volum: 2400, familie: 09)
- Data colectării SERP: 2026-11-15
- Elemente care nu sunt organice: AI Overview (poz. 1), „People also search” / produse similare (poz. 4), Imagini (poz. 13). **Doar 3 rezultate organice în SERP.**

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | pinterest.com (pin „Créez un magnifique CV gratuitement”) | altul (pin în franceză) | – | – | – | – | – | da |
| 2 | kickresume.com (/dashboard/create/easy/) | instrument funcțional (editor de CV; în engleză) | da (editorul se încarcă ca „Guest User”, cu secțiuni editabile) | freemium: șablonul are „3 premium features”, prețul nu e afișat | da | nu pentru editare („Sign up to save your work!”) | neverificat | da |
| 3 | lambacv.com (/cv/free) | instrument (generator de CV în arabă, pentru Arabia Saudită) | neverificat | „gratuit” după text | – | neverificat | da | da |

- Ce apare azi: 1 editor de CV freemium (în engleză), 1 generator în arabă, 1 pin Pinterest (doar 3 rezultate organice)
- Instrument gratuit funcțional: da, parțial (kickresume.com: gratuit ca invitat, cu funcții premium; salvarea cere cont)
- Produs plătit și preț: kickresume.com (funcții premium; preț neafișat pe pagina deschisă)
- Verdict: medii (un singur instrument funcțional, în engleză, freemium; niciun rezultat românesc)
- Riscuri: niciunul cu dovadă
- Surse blocate: niciuna

## calculator pfa (volum: 1900, familie: 01)
- Data colectării SERP: 2026-10-02
- Elemente care nu sunt organice: AI Overview (poz. 2), Imagini (poz. 17)

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | contabilitatepebune.ro (.../calculator-taxe-pfa-2026-sistem-real_/) | altul (pagină de atașament aproape goală, doar titlul; fără calculator) | nu | – | titlu 2026 | – | da | da |
| 2 | play.google.com (Venit Net: Salariu PFA SRL) | altul (aplicație Android) | neverificat | gratuit | – | – | – | da |
| 3 | acte.mlb.ro (/calculator/freelancing) | instrument funcțional (angajat vs SRL/PFA) | da (test: net 5.000 lei / factură 10.000 lei → comparație calculată) | gratuit (site cu servicii plătite de documente) | da (2026, CAEN Rev. 3) | nu (login Google opțional) | da | da |
| 4 | contzilla.ro (/exemplu-calcul-simplu-taxe-pfa-in-sistem-real-2024/) | articol | – | gratuit | învechit (2024) | nu | neverificat | da |
| 5 | mnp.navy.mil (/group/performance/pfa-calculator) | altul (fără legătură: armata SUA, pagină de login) | – | – | – | da | – | da |
| 6 | ro.scribd.com (Calcul comparativ PFI-PFA 2023-2024) | document de descărcat | – | după autentificare | învechit (2023–2024) | da | – | da |
| 7 | facebook.com (postare Cristi Bărcan) | altul (postare: „Scrie VENIT ... îți trimit un calculator”) | – | – | – | – | – | da (doar textul postării) |
| 8 | keez.ro (/blog/category/pfa) | director (listă de articole de blog, de la un serviciu de contabilitate plătit) | – | preț neafișat pe pagină | da (CAEN Rev. 3, 2027) | – | da | da |
| 9 | apps.apple.com (PFRA & PFA Calculator, Air Force) | altul (fără legătură, aplicație militară SUA) | – | – | – | – | – | da |
| 10 | portalcontabilitate.ro (/pfa-calcul-cas-cass-si-impozit-pe-venit-pentru-2024-...) | articol | – | – | învechit (2024) | fereastră de login în pagină | neverificat | da (curl) |

- Ce apare azi: 1 instrument funcțional, 3 articole (2 din 2024), 1 document Scribd, 1 listă de blog, 1 aplicație Android, 1 postare Facebook, 2 rezultate fără legătură (armata SUA), 1 pagină goală
- Instrument gratuit funcțional: da (acte.mlb.ro)
- Produs plătit și preț: keez.ro (contabilitate, preț neafișat pe pagina deschisă); niciun preț văzut
- Verdict: medii (un singur instrument funcțional în primele 10; restul sunt articole vechi sau rezultate fără legătură)
- Riscuri: depinde de o instituție a statului (CAS/CASS/impozit după Codul fiscal/ANAF; articolele din 2024 sunt deja depășite)
- Surse blocate: niciuna

## calcul consum combustibil (volum: 1600, familie: 06)
- Data colectării SERP: 2026-09-02
- Elemente care nu sunt organice: Related searches

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | peco-online.ro (/calculator.php) | instrument funcțional | da (test: 14,00 l, 112,00 RON) | gratuit | fără an (calcul fără date variabile) | nu | da | da |
| 2 | calculatoare-utile.ro (/calculator/consum-combustibil) | instrument funcțional | da (test: 200 km / 14 l → „Consum: 7.00%”, cu unitatea afișată greșit) | gratuit | da | nu | da | da |
| 3 | pretcarburant.ro (/calculator) | instrument funcțional | da (test: 7,0 l/100 km; cost la 100 km cu prețul din 15 nov. 2026) | gratuit | da (prețuri la zi) | nu | da | da |
| 4 | gps-online.webshow.ro (/calculator-consum.html) | instrument funcțional | da (test: 14 l, 112 RON) | gratuit | da (2026) | nu | da | da |
| 5 | calculat.org (/ro/energie-combustibil/consum-combustibil/) | instrument funcțional | da (test: 14,0 l, 112,00 lei) | gratuit | da | nu | da* (553 px) | da |
| 6 | leaveboard.com (/ro/calculator-consum/) | instrument funcțional | da (test: 14,0 l, 112 RON) | gratuit | da | nu | da | da |
| 7 | dosar-auto.ro (/ro/planificator/) | instrument funcțional | da (test: 200 km, 14 l, motorină 149 lei la prețul zilei) | gratuit | da (prețuri 15.11.2026) | nu | neverificat | da |
| 8 | ladnefelgi.pl (Consumul de combustibil al unei mașini) | articol (magazin polonez) | – | – | neverificat | nu | neverificat | da |
| 9 | safefleet.eu (/ro/consum-combustibil/) | produs plătit (monitorizare consum pentru flote) | – | „Încearcă gratuit / Solicită ofertă”, preț neafișat | da | – | neverificat | da |
| 10 | icredit.ro (/stiri/cum-se-calculeaza-consumul-de-combustibil) | articol | – | gratuit | 05.08.2022 | nu | neverificat | da |

- Ce apare azi: 7 instrumente funcționale, 2 articole, 1 produs pentru flote
- Instrument gratuit funcțional: da (cel mai bun: pretcarburant.ro, cu prețuri la zi; dosar-auto.ro asemănător)
- Produs plătit și preț: safefleet.eu (preț neafișat, „Solicită ofertă”)
- Verdict: puternice (5 instrumente funcționale, actuale, fără cont, pe pozițiile 1–5)
- Riscuri: niciunul cu dovadă
- Surse blocate: niciuna

## calculator taxe pfa 2026 (volum: 1600, familie: 01)
- Data colectării SERP: 2026-10-02
- Elemente care nu sunt organice: AI Overview (poz. 2), Related searches

| Poz | Domeniu | Tip | Funcționează? | Gratuit/preț | Actual | Cont | Telefon | Deschis? |
|---|---|---|---|---|---|---|---|---|
| 1 | startupcafe.ro (/pfa-lovite-masuri-fiscale-analiza-htm-24018) | articol | – | gratuit | neverificat | nu | neverificat | da |
| 2 | contabilitate-timisoara.ro (/calculator-salariu/) | instrument funcțional, dar pentru salariu, nu pentru PFA | da (test: 2.981) | gratuit | da (2026) | nu | neverificat | da |
| 3 | contabilul.manager.ro (/a/29765/declaratia-unica-s-a-modificat...) | articol (Declarația unică 2026) | – | – | da (2026) | – | neverificat | da |
| 4 | medium.com (@Misulik112, „A Free 2026 Tax Calculator...”) | articol | – | – | – | – | – | blocat (403) |
| 5 | taxe.azisunt.com | produs plătit + calculator SRL (micro vs profit) | câmpuri prezente; testul nu a schimbat rezultatul, deci neconfirmat | abonament PFA 49 RON / 3 luni, SRL 99 RON / 3 luni | da (2026) | „Testează în contul tău” | neverificat | da |
| 6 | contabilitatepebune.ro (/model-decont-de-cheltuieli-2/) | altul (model de decont, fără legătură cu căutarea) | – | – | – | – | neverificat | da |
| 7 | icalculator.ro (/calculator-taxe-chirie.html) | instrument funcțional, dar pentru chirie, nu pentru PFA | da (test: chirie 2.000 × 12 → impozit 1.920 RON) | gratuit | da (2026) | nu | neverificat | da |
| 8 | calcfinch.com (/ro/salarii-si-taxe) | director (listă de calculatoare, inclusiv „Calculator taxe PFA 2026 (sistem real)” și „normă de venit”) | hub; calculatoarele PFA nu au fost testate | gratuit | da (2026) | nu | da | da |
| 9 | contapp.ro (/blog/page/19/) | director (pagină de blog a unui software de contabilitate plătit) | – | ofertă Black Friday „15 luni la prețul a 12”, preț neafișat | da | – | neverificat | da |
| 10 | salariile.ro (/noutati/pfa-sau-srl-2026) | articol | – | gratuit | 2 sept. 2026 | nu | neverificat | da |

- Ce apare azi: 4 articole (1 blocat), 2 instrumente funcționale pentru alte calcule (salariu, chirie), 1 calculator SRL plătit sau neconfirmat, 2 directoare, 1 pagină fără legătură
- Instrument gratuit funcțional: nu (niciun calculator PFA funcțional pe paginile din primele 10; calcfinch.com doar trimite spre unul)
- Produs plătit și preț: taxe.azisunt.com (OFA): 49 RON / 3 luni pentru PFA, 99 RON / 3 luni pentru SRL; contapp.ro (preț neafișat)
- Verdict: slabe (niciun calculator de taxe PFA funcțional în primele 10; instrumentele care merg calculează salariu sau chirie)
- Riscuri: depinde de o instituție a statului (ANAF/Codul fiscal: „Declaratia unica s-a modificat ... conform noului Ordin ANAF nr. 2736/2025”, după textul contabilul.manager.ro); sezonier (după text: căutarea numește anul fiscal 2026)
- Surse blocate: medium.com (403)

---

## Rezumat

| Căutare | Ce apare azi | Instrument gratuit funcțional | Produs plătit și preț | Verdict | Riscuri |
|---|---|---|---|---|---|
| verificare rca | 1 articol, 1 instrument oficial blocat (AIDA), 2 pagini comerciale RCA (doar 4 organice) | nu (AIDA neverificabil) | rca.ro, groupama.ro: polițe RCA, preț neafișat | slabe | depinde de AIDA/BAAR |
| calculator salariu brut | 4 instrumente, 1 aplicație (doar 5 organice) | da (salariucalculator.ro) | niciunul găsit | puternice | depinde de o instituție a statului (Cod fiscal/ANAF) |
| calcul salariu brut | 8 instrumente (7 testate), 1 articol, 1 blocat | da (impozitsalariu.ro) | niciunul găsit | puternice | depinde de o instituție a statului (Cod fiscal/ANAF) |
| verificare rovinieta fara serie sasiu | 3 instrumente private netestate, 4 articole, 3 pagini ale statului indisponibile | neconfirmat (erovinieta.net, evita-amenzi.ro, verificarerovinieta.com) | vânzare de roviniete (erovinieta.net, roviniete.ro), tarife legale | medii | depinde de o instituție a statului (CNAIR/TollRo; registrul oprit din 7 oct. 2026) |
| calculator calorii | 6 aplicații, 2 liste App Store, 1 articol, 1 instrument de rețete, 1 produs fizic | nu | aplicații cu achiziții în aplicație (fără preț); trendyol (blocat) | slabe | – |
| model cv europass | 1 instrument oficial, 3 DOC, 1 pagină ANOFM, 1 pagină UE, 1 Scribd, 3 articole | da (europass.europa.eu) | cvwizard.com (preț neafișat) | medii | – |
| cerere concediu de odihna | 5 documente, 3 articole cu model, 1 Facebook, 1 Jotform al unei firme | nu | papervee.com (fără preț), euload.com (abonament) | slabe | juridic |
| calculator dobanda compusa | 3 instrumente străine (EN), 6 aplicații Android, 1 video | da (simulatudo.com.br, în engleză) | niciunul găsit | puternice (conform definiției; niciunul în română) | – |
| cv online gratis | 1 editor freemium (EN), 1 generator în arabă, 1 Pinterest (doar 3 organice) | da, parțial (kickresume.com, freemium) | kickresume.com premium (preț neafișat) | medii | – |
| calculator pfa | 1 instrument, 3 articole (2 din 2024), 1 Scribd, 1 blog, 1 aplicație, 1 Facebook, 2 fără legătură, 1 pagină goală | da (acte.mlb.ro) | keez.ro (preț neafișat) | medii | depinde de o instituție a statului (ANAF/Cod fiscal) |
| calcul consum combustibil | 7 instrumente, 2 articole, 1 produs pentru flote | da (pretcarburant.ro) | safefleet.eu (preț neafișat) | puternice | – |
| calculator taxe pfa 2026 | 4 articole, 2 instrumente pentru alte calcule, 1 calculator SRL plătit, 2 directoare, 1 fără legătură | nu | taxe.azisunt.com: 49 RON / 3 luni (PFA), 99 RON / 3 luni (SRL) | slabe | depinde de o instituție a statului (ANAF); sezonier (an fiscal 2026, după text) |
