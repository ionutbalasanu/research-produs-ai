# 03. Cererile de retur gestionate manual în magazinele Shopify mici
Piață: magazinele Shopify mici (țări diferite: SUA, UK, Australia, Germania, Hong Kong) | Limbă: engleză | Verificat: 2026-11-16 | Verdict la pasul 1: INTRĂ | Curs folosit: 1 USD = 4,8428 lei (curs BNR comunicat în 13 noiembrie 2026, citit de pe https://www.cursbnr.ro/ în 2026-11-16; bnr.ro/nbrfxrates.xml a redirecționat spre pagina principală BNR, unde valorile se încarcă prin script și nu apar în HTML)

## 0. Întrebarea decisivă: ce include Shopify gratuit acum
Răspuns scurt: Shopify are acum, inclus în admin, un portal de retur „self-serve": clientul cere returul din contul de client, magazinul aprobă sau refuză, poate adăuga produse de schimb la aprobare și poate trimite eticheta. Regulile de retur (fereastră, „final sale", taxă de stocare la loc, taxă de transport la retur) sunt native. Lipsesc: încărcarea de poze, aprobarea automată, cererea fără cont de client (clienții „guest" ajung tot pe e-mail), schimbul cerut de client, etichete generate automat la tarifele proprii. Prin urmare golul rămas e îngust și e deja ocupat de aplicații mici noi (vezi secțiunea 3).

| Fapt | Link | Data | Marcaj |
|---|---|---|---|
| Clientul trimite cererea din pagina comenzii; magazinul aprobă sau refuză; la aprobare poate adăuga produse de schimb și trimite etichete | https://help.shopify.com/en/manual/fulfillment/managing-orders/returns/self-serve-returns | 2026-11-16 | verificat în sursă |
| Formularul poate cere „return reasons and product condition"; pagina nu menționează poze | același link | 2026-11-16 | verificat în sursă |
| Reguli: fereastră 14/30/90 zile sau personalizată, taxă de transport la retur, taxă de restocare, produse „final sale" | https://help.shopify.com/en/manual/fulfillment/managing-orders/returns/return-rules | 2026-11-16 | verificat în sursă |
| „Return fees aren't deducted from refunds automatically" (taxele se scad manual la rambursare) | același link (redare WebFetch) | 2026-11-16 | verificat în sursă |
| „You review and decide on every request." | https://help.shopify.com/en/manual/fulfillment/managing-orders/returns/self-serve-returns/setup | 2026-11-16 | verificat în sursă |
| „Exchanges can't be requested in self-serve returns" | același link | 2026-11-16 | verificat în sursă |
| „Legacy customer accounts don't display return or cancellation options." Clientul trebuie să folosească noua versiune a conturilor de client | același link | 2026-11-16 | verificat în sursă |
| Pagina de configurare nu menționează niciun cost și nu limitează funcția la un plan (doar activarea pe piețe separate cere Advanced/Plus); funcția e gratuită pe toate planurile | același link | 2026-11-16 | dedus (lipsa unui preț în pagină) |
| Portalul nativ nu are câmp de încărcare poze: „Currently there is no image upload field in the native return request flow." | https://community.shopify.com/t/allow-customers-to-upload-photos-when-submitting-a-return-request/637828 | 2026-06-17 | verificat în sursă (afirmație de comerciant, confirmată de mai mulți participanți) |
| Un participant pe forum: „Shopify’s self serve returns is free and already covers the customer requesting" | https://community.shopify.com/t/i-built-a-free-returns-and-exchanges-app-for-small-shopify-stores-and-need-blunt-feedback/674740 | 2026-08-31 | verificat în sursă (opinie pe forum) |

Consecință pentru ipoteză: produsul din TRIERE („formular de retur cu verificarea automată a eligibilității") e acoperit aproape în întregime gratuit de Shopify. Rămâne doar un plus: poze, cerere fără cont, aprobare automată.

## 1. Alternative actuale și prețuri
| Alternativă | Ce face | Preț văzut azi | Link | Data | Marcaj |
|---|---|---|---|---|---|
| Shopify self-serve returns (nativ) | portal de cerere, reguli de eligibilitate, aprobare manuală, etichetă încărcată de comerciant | preț neafișat; niciun cost menționat (vezi 0) | https://help.shopify.com/en/manual/fulfillment/managing-orders/returns/self-serve-returns/setup | 2026-11-16 | verificat în sursă / dedus (gratuit) |
| AfterShip Returns & Exchanges | portal, etichete automate, aprobare automată, reguli; 4,7 (1.547 recenzii) | Return Care gratuit (cu „Revenue share"); Essentials 19 $/lună cu 20 retururi, 0,50 $ per retur în plus; Premium 119 $/lună cu 100 retururi | https://apps.shopify.com/returns-center-by-aftership | 2026-11-16 | verificat în sursă |
| Return Prime | portal, schimburi, store credit; 4,8 (780) | Start gratuit cu 5 cereri; Grow de la 19,99 $/lună cu 60 cereri; Thrive AI 79,99 $; Scale 149,99 $ | https://apps.shopify.com/return-prime | 2026-11-16 | verificat în sursă |
| ReturnGO | soluție completă, aprobare automată; 4,9 (410) | Premium 147 $/lună cu 110 retururi; Pro 297 $/lună | https://apps.shopify.com/returngo | 2026-11-16 | verificat în sursă |
| Loop Returns | retururi, schimburi, etichete; 4,6 (450) | Checkout+ gratuit „for brands with 5k+ annual orders"; Returns de la 340 $/lună | https://apps.shopify.com/loop-returns | 2026-11-16 | verificat în sursă |
| Yanet Returns & Exchanges (capăt ieftin) | portal, reguli, store credit | Free 6 cereri/lună; Professional 9,99 $/lună cu 80 cereri; Ultimate 29,99 $ nelimitat, cu „Automation Approval" | https://apps.shopify.com/yanet-return-and-exchange | 2026-11-16 | verificat în sursă |
| Synctrack Returns & Exchanges | portal, etichete, reguli | Starter gratuit 5 cereri; 19,99 $/lună 60 cereri; 49,99 $ cu aprobare automată | https://apps.shopify.com/omega-returns-drive | 2026-11-16 | verificat în sursă |
| CWILL (ParcelPanel) Returns & Exchanges | portal, etichete | Free 6 retururi/lună; Essential 29 $/lună; Professional 99 $ | https://apps.shopify.com/parcel-panel-returns-exchanges | 2026-11-16 | verificat în sursă |
| Loopback Returns (dezvoltator solo, lansat 24.09.2026, 0 recenzii) | cerere de retur fără cont de client, aprobare într-un clic | 9 $/lună nelimitat | https://apps.shopify.com/loopback-returns | 2026-11-16 | verificat în sursă |
| Opus Returns & Exchanges (dezvoltator solo, lansat 14.08.2026, 0 recenzii) | portal pentru comenzi „guest", schimburi, dovezi foto | gratuit | https://apps.shopify.com/opus-returns-exchanges | 2026-11-16 | verificat în sursă |

Categoria „Returns and exchanges" din Shopify App Store afișează „285 apps": https://apps.shopify.com/categories/orders-and-shipping-returns-and-warranty-returns-and-exchanges/all (2026-11-16, verificat în sursă).

## 2. Nemulțumiri
| Sursă (link) | Data | Față de | Citat ≤15 cuvinte | Actualitate | Marcaj | Piață |
|---|---|---|---|---|---|---|
| https://apps.shopify.com/returns-center-by-aftership/reviews?ratings%5B%5D=1&sort_by=newest (8849 Official Website) | 2026-11-04 | AfterShip | „terrible UX, overly complicated setup, unintuitive design, and useless support" | ultimele 12 luni | verificat în sursă | Shopify, Hong Kong |
| același link (Kitty Kabana) | 2026-10-02 | AfterShip (preț pe funcții) | „not worth it if you're a small business" | ultimele 12 luni | verificat în sursă | Shopify, Australia |
| același link (Cotes of London) | 2026-10-28 (editat) | AfterShip | „Each stage they said I could not get what I wanted unless I upgraded." | ultimele 12 luni | verificat în sursă | Shopify, SUA |
| https://apps.shopify.com/loop-returns/reviews?ratings%5B%5D=1&sort_by=newest (H BAR C) | 2026-11-12 | Loop | „We had an onboarding error cost us thousands in refunds given in error." | ultimele 12 luni | verificat în sursă | Shopify, SUA |
| https://apps.shopify.com/loop-returns/reviews?ratings%5B%5D=2&sort_by=newest (SAINT SKEI) | 2026-02-02 | Loop | „I could not test the app, because an onboarding call is mandatory." | ultimele 12 luni | verificat în sursă | Shopify, Cipru |
| același link (HealthyFeetStore.com) | 2025-12-09 | Loop | „It took us weeks to setup...and we still haven't correctly configured it." | ultimele 12 luni | verificat în sursă | Shopify, SUA |
| https://apps.shopify.com/return-prime/reviews?ratings%5B%5D=1&sort_by=newest (ST. CLAIR) | 2026-05-18 | Return Prime | „Do not trust this app if you expect any level of customer service." | ultimele 12 luni | verificat în sursă | Shopify, UK |
| același link (EzyDog Australia) | 2026-04-22 (editat) | Return Prime | „Worst return portal we’ve used." | ultimele 12 luni | verificat în sursă | Shopify, Australia |
| https://apps.shopify.com/returngo/reviews?ratings%5B%5D=1&sort_by=newest (Moddo) | 2026-07-23 | ReturnGO | „BEWARE! THEY CANCEL LABELS WHILE ALREADY IN TRANSIT." | ultimele 12 luni | verificat în sursă | Shopify, SUA |
| https://community.shopify.com/t/feature-request-improve-self-serve-returns-for-merchants/644509 (twecoop) | 2026-07-01 | retururile native Shopify și aplicațiile terțe | „Right now, it doesn’t fully solve the returns workflow" | ultimele 12 luni | verificat în sursă | Shopify, țară necunoscută |
| https://community.shopify.com/t/allow-customers-to-upload-photos-when-submitting-a-return-request/637828 (același autor, twecoop; nu e sursă independentă) | 2026-06-17 | retururile native | „Currently there is no image upload field in the native return request flow." | ultimele 12 luni | verificat în sursă | Shopify, țară necunoscută |
| https://community.shopify.com/t/return-process-in-shopify/706400 (Jens_Hecker) | 2026-10-29 | retururile native (etichete la tarif propriu DPD) | „we need a third-party app with an appropriate pricing plan" | ultimele 12 luni | verificat în sursă | Shopify, Germania |
| https://community.shopify.com/t/suggest-return-and-exchange-apps-for-sm-businesses/631388 (shreyanshkr) | 2026-06-06 | aplicațiile de retur (contracte, comisioane) | „Annual contracts, transaction fees and bad customer service i see in negative reviews." | ultimele 12 luni | verificat în sursă | Shopify, țară necunoscută |
| https://community.shopify.com/t/recommendations-for-a-good-returns-exchanges-app-for-uk-based-stores/581197 (Shopcorblimey) | 2025-12-28 | proces manual în Shopify | „doing it manually in shopify is so clunky" | ultimele 12 luni | verificat în sursă | Shopify, UK |
| https://community.shopify.com/t/built-a-small-returns-app-for-stores-whose-customers-never-log-in-looking-for-honest-feedback/687215 (ahsandoesntcare) | 2026-09-25 | retururile native (clienți fără cont) | „guest-checkout orders end up as emails" | ultimele 12 luni | verificat în sursă | Shopify, țară necunoscută |

Total: 15 rânduri, 14 surse independente, toate din ultimele 12 luni. Atenție: aproape toate nemulțumirile față de aplicații sunt despre suport, configurare și preț, nu despre lipsa unei funcții pe care am putea-o adăuga noi.

## 3. Ipoteza de schimbare
Ipoteza: un magazin mic care azi face retururile pe e-mail ar instala o aplicație nouă, ieftină și simplă (cerere fără cont, poze, aprobare automată după reguli), în locul portalului gratuit Shopify sau al aplicațiilor existente.

### Ce o susține
- Portalul nativ nu are poze, nu acceptă comenzi de la clienți fără cont nou și cere aprobare manuală la fiecare cerere (secțiunea 0, verificat în sursă).
- Aplicațiile mari sunt criticate pentru configurare grea, apeluri obligatorii de onboarding și funcții blocate în planuri scumpe (secțiunea 2, 9 recenzii din ultimele 12 luni).
- Un comerciant cere explicit o variantă fără „transaction fees" și fără contracte anuale (631388, 2026-06-06).

### Ce o slăbește
- Shopify oferă gratuit nucleul fluxului: cerere, reguli de eligibilitate, aprobare, etichetă, schimb adăugat la aprobare (secțiunea 0).
- Capătul ieftin e plin: categoria are 285 de aplicații; Yanet, Synctrack, CWILL, Return Prime au planuri gratuite cu 5-6 cereri/lună; Yanet are 9,99 $/lună cu 80 cereri (secțiunea 1).
- Exact produsul propus a fost lansat de cel puțin doi dezvoltatori solo în august-septembrie 2026: Loopback Returns (9 $/lună, cerere fără cont) și Opus (gratuit, comenzi guest, dovezi foto). Ambele au 0 recenzii azi (verificat în sursă, 2026-11-16). Și LaunchTip și alți vânzători își promovează unelte similare în firul 637828 (2026-09-22, 2026-10-18).
- Comentariul pe forum la Loopback: „the work doesn’t end at approval" (687215, 2026-09-25): o aplicație de cerere nu scoate munca de rambursare și etichetă.
- Comerciantul din 644509 spune că a încercat aproape toate aplicațiile și vrea ca Shopify să rezolve nativ; nu caută încă o aplicație.
- Shopify dezvoltă activ funcția (anulări adăugate recent, conform 644509): golul se poate închide de la o lună la alta (dedus).

### Bariere de schimbare
- Încredere: o aplicație nouă, fără recenzii, cere acces la comenzi și date de client; Shopify impune cerințe de nivel 2 pentru nume, adresă, telefon, e-mail (https://shopify.dev/docs/apps/launch/protected-customer-data, 2026-11-16, verificat în sursă).
- Efort de configurare și teama de încă o aplicație care „nu merge" (644509).
- Clienții deja în fluxul nativ: comerciantul trebuie să mute linkul de retur și politica.

### Cumpărarea efectivă: se află doar din test.

## 4. Calea către cumpărători
Căutări (Ubersuggest, SUA, locație 2840, limba en, 2026-11-16; contor reports: 5/150 înainte de apeluri):
- „shopify returns": 480/lună, CPC 13,75 $ (keyword_overview).
- „shopify returns app": 110/lună, CPC 48,14 $ (match_keywords).
- „best shopify returns app": 40/lună, CPC 102,17 $ (match_keywords).
- „shopify self serve returns": 50/lună (keyword_overview).
Volum mic, CPC mare: cuvintele sunt disputate de aplicațiile mari (dedus din CPC).

Shopify App Store, reguli citite din shopify.dev (2026-11-16, verificat în sursă):
- Taxă de dezvoltator: „one-time fee of $19 USD per Partner account" (≈92 lei la cursul de mai sus). https://shopify.dev/docs/apps/launch/distribution/revenue-share
- Comision Shopify: „You keep 100% of your first $1,000,000 USD in lifetime gross app revenue" și 15% peste; plus „All billing is subject to a 2.9% processing fee" și taxe de vânzare; în unele țări, „Regulatory Operating Fee". Același link.
- Facturare obligatorie prin Shopify: „Apps that use off-platform billing cannot be distributed through the Shopify App store" (1.2). https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements
- Aplicația nu poate fi identică cu alte aplicații proprii publicate (1.1.5); modificările de temă doar prin theme app extensions (5.1.1); listarea cere screencast demo în engleză (4.5.3) și date de test (4.5.4); recenziile stimulate sunt interzise (1.3). Același link.
- Accesul la date protejate de client se cere separat și „isn't possible while the app is under review". https://shopify.dev/docs/apps/launch/app-store-review/submit-app-for-review
- Durata recenziei de către Shopify: necunoscut (nu apare în paginile citite).

Forum community.shopify.com: dezvoltatorii își prezintă aplicațiile cu dezvăluire („Disclosure: I built..."), dar mai multe postări promoționale apar „flagged by the community and is temporarily hidden" (631388, 637828, 711789). Regulile forumului despre autopromovare nu le-am citit: necunoscut.

## 5. Drumul până la 2.000 lei/lună (încasări brute)
2.000 lei / 4,8428 = 413 $ pe lună. Model: abonament lunar, deci contează clienții ACTIVI plătitori.
- La 9 $/lună (prețul Loopback): 413 / 9 = 45,9, deci 46 de clienți activi.
- La 9,99 $/lună (Yanet Professional): 413 / 9,99 = 41,3, deci 42 de clienți activi.
- La 19 $/lună (AfterShip Essentials, Synctrack, Return Prime Grow): 413 / 19 = 21,7, deci 22 de clienți activi.
- La 29 $/lună (CWILL Essential): 413 / 29 = 14,2, deci 15 clienți activi.
Costuri directe cunoscute, separat: 19 $ o dată la înregistrare (≈92 lei); 2,9% taxă de procesare pe încasări; 0% comision Shopify sub 1.000.000 $ (sursa: revenue-share, 2026-11-16). Găzduire: necunoscut. Rata de dezinstalare: necunoscut.
Context: două aplicații identice lansate acum 2-3 luni au 0 recenzii (secțiunea 1). Numărul lor de instalări e necunoscut.

## 6. Produsul restrâns
### Ce face (max 5 rânduri)
1. Pagină de retur pentru comenzi fără cont: număr comandă + e-mail.
2. Reguli de eligibilitate citite din comanda Shopify; poză obligatorie pentru motive alese de comerciant.
3. Aprobare automată pentru cererile care respectă regulile, restul într-o coadă.
4. Creează returul nativ în Shopify (ca rambursarea și restocarea să rămână în Shopify).

### Efort de construire (dedus)
3-4 săptămâni: aplicație embedded (App Bridge), theme app extension pentru pagină, stocare poze, Billing API, cerere de date protejate nivel 2, screencast și listare.

### Efort de operare lunar (dedus)
Suport pe e-mail pentru instalări și configurare; răspuns la recenzii; câteva ore pe lună dacă instalările sunt puține.

### Ce se poate strica lunar
Shopify adaugă poze sau cereri fără cont în portalul nativ (funcția e dezvoltată activ); schimbări de API și versiuni anuale; respingere sau întârziere la recenzia aplicației; cereri de suport legate de etichete și transportatori.

## 7. Presupunerea care omoară ideea
Că un magazin mic care face azi retururile pe e-mail va instala și plăti o aplicație nouă, fără recenzii, deși Shopify oferă gratuit portalul de retur și alte aplicații acoperă deja exact golul rămas (cerere fără cont, poze) gratis sau la 9 $/lună.

## 8. Surse blocate
- reddit.com: HTTP 200, dar pagina are doar titlul „Reddit", fără conținut (r/shopify, căutare „returns app"), 2026-11-16.
- g2.com: HTTP 403 (Loop Returns reviews), 2026-11-16.
- trustpilot.com: HTTP 403 (loopreturns.com), 2026-11-16.
- apps.shopify.com/search?q=returns: „We are having trouble loading your results"; am folosit în schimb pagina de categorie.
- bnr.ro/nbrfxrates.xml: redirecționează spre pagina principală BNR, unde cursul nu apare în HTML; am folosit cursbnr.ro.

## 9. Lista surselor decisive pentru verificarea independentă
1. https://help.shopify.com/en/manual/fulfillment/managing-orders/returns/self-serve-returns/setup, 2026-11-16, regulă/funcție nativă: „You review and decide on every request."
2. Același link, 2026-11-16, limită nativă: „Exchanges can't be requested in self-serve returns"
3. https://help.shopify.com/en/manual/fulfillment/managing-orders/returns/return-rules, 2026-11-16, funcție nativă: „Select a preset return window, or enter a custom number of days."
4. https://community.shopify.com/t/allow-customers-to-upload-photos-when-submitting-a-return-request/637828, 2026-11-16, nemulțumire: „Currently there is no image upload field in the native return request flow."
5. https://apps.shopify.com/returns-center-by-aftership, 2026-11-16, preț: „Includes 20 returns/month; $0.50 per extra return."
6. https://apps.shopify.com/yanet-return-and-exchange, 2026-11-16, preț: „80 free requests per month, only $0.2 per extra request"
7. https://apps.shopify.com/loopback-returns, 2026-11-16, preț și concurent direct: „Unlimited return requests"
8. https://apps.shopify.com/opus-returns-exchanges, 2026-11-16, concurent direct gratuit: „Guest-order return portal with customer-requested exchanges."
9. https://apps.shopify.com/categories/orders-and-shipping-returns-and-warranty-returns-and-exchanges/all, 2026-11-16, saturație: „285 apps"
10. https://apps.shopify.com/returns-center-by-aftership/reviews?ratings%5B%5D=1&sort_by=newest, 2026-11-16, nemulțumire: „terrible UX, overly complicated setup, unintuitive design, and useless support"
11. https://apps.shopify.com/loop-returns/reviews?ratings%5B%5D=2&sort_by=newest, 2026-11-16, nemulțumire: „I could not test the app, because an onboarding call is mandatory."
12. https://community.shopify.com/t/feature-request-improve-self-serve-returns-for-merchants/644509, 2026-11-16, nemulțumire: „Right now, it doesn’t fully solve the returns workflow"
13. https://community.shopify.com/t/built-a-small-returns-app-for-stores-whose-customers-never-log-in-looking-for-honest-feedback/687215, 2026-11-16, slăbește ipoteza: „the work doesn’t end at approval"
14. https://shopify.dev/docs/apps/launch/distribution/revenue-share, 2026-11-16, regulă de canal: „one-time fee of $19 USD per Partner account"
15. Același link, 2026-11-16, regulă de canal: „All billing is subject to a 2.9% processing fee"
16. https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements, 2026-11-16, regulă de canal: „Apps that use off-platform billing cannot be distributed through the Shopify App store"
17. https://www.cursbnr.ro/, 2026-11-16, curs: „1 USD = 4.8428 Lei"
