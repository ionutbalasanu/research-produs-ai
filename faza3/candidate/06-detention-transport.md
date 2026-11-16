# 06. Dovada timpului de așteptare (detention) refuzată de brokeri
Piață: SUA, șoferi proprietari-operatori și transportatori mici care lucrează prin brokeri | Limbă: engleză | Verificat: 2026-11-16 | Verdict la pasul 1: INTRĂ | Curs folosit: 1 USD = 4,8428 lei (curs BNR din 13 noiembrie 2026, citit de pe https://www.cursbnr.ro/ în 2026-11-16; https://www.bnr.ro/nbrfxrates.xml a întors o pagină „Error")

## 0. Întrebarea decisivă (doar pentru candidatele din „de clarificat")
Nu se aplică: candidata a intrat direct. Contraargumentul cerut în prompt („hard sell at any price") e verificat în secțiunea 3, „Ce o slăbește".

Constatare importantă pentru tot fișierul: două dintre cele trei fire TruckersReport folosite ca dovadă în faza 1 au fost pornite de oameni care testau o idee de aplicație, nu de șoferi care se plângeau spontan:
- firul din 20.04.2026 („Lost detention pay again because broker said "no proof""): autorul scrie „Before I build anything I want to know if this is actually useful to real drivers." (https://www.thetruckersreport.com/truckingindustryforum/posts/13451555/ , citit 2026-11-16, **verificat în sursă**). Un răspuns: „This dude ain't even a truck driver." (același link, **verificat în sursă**).
- firul-sondaj din 12.08.2025: autorul (ron.oruganti) scrie „The tool I'm envisioning isn't a new billing system." (https://www.thetruckersreport.com/truckingindustryforum/threads/whats-the-1-reason-your-detention-claims-get-denied.2529156/page-2 , citit 2026-11-16, **verificat în sursă**); alt participant întreabă „Is RO an AI?" (pagina 3, **verificat în sursă**).
- un al treilea fir, din 25.05.2026 („Detention claim process from your side"), e tot o cercetare: „Is there a tool out there that can help that you used" (https://www.thetruckersreport.com/truckingindustryforum/posts/13474722/ , **verificat în sursă**).

Concluzie: sondajul (7 din 13 voturi „They just ignore my request") și citatul „broker refused to pay" vin din fire de validare a unor aplicații concurente. Ele arată că alți constructori au văzut aceeași problemă înaintea noastră, nu că există cerere plătitoare (**dedus**).

## 1. Alternative actuale și prețuri
Căutare făcută prin API-ul public iTunes (https://itunes.apple.com/search?term=detention+pay&country=us&entity=software și variante, 2026-11-16). Numărul de evaluări și datele vin din API-ul de căutare (https://itunes.apple.com/lookup?id=...), citit 2026-11-16.

| Alternativă | Ce face | Preț văzut azi | Link | Data | Marcaj |
|---|---|---|---|---|---|
| Detention Pay - DMRG (DMRG LLC) | înregistrare a timpului de așteptare după locație, alerte la praguri; 4 evaluări, ultima versiune 06.05.2025 | gratuit, achiziții în aplicație: „Per Load $0.99", „Monthly $39.99" | https://apps.apple.com/app/id6502769929 | 2026-11-16 | verificat în sursă |
| RigRight (QC Pro Apps Ltd) | aplicație pentru șofer cu „Detention Tracker - one-tap clock, evidence builder and claim generator"; lansată 10.04.2026, 0 evaluări afișate | Driver Pro 24,99 $/lună sau 299,99 $/an; Fleet Owner 69,99 $/lună | https://apps.apple.com/us/app/rigright/id6761784949 | 2026-11-16 | verificat în sursă |
| GetDockPay (GetDockPay LLC) | ore de sosire și plecare cu GPS, calcul detention, factură PDF trimisă brokerului; prima versiune 22 sept., ultima 6 nov. 2026; fără evaluări | Pro 24,99 $/lună sau 239,99 $/an | https://apps.apple.com/us/app/id6807165625 | 2026-11-16 | verificat în sursă |
| SherHaul: Detention Pay (dezvoltator individual) | cerere de detention în PDF cu ore și poze, trimisă pe e-mail; verificare MC a brokerului; 1 evaluare | „Sherhaul Pro" 29,99 $ și 199,99 $ (tipul achiziției neclar: descrierea spune că nu are abonament) | https://apps.apple.com/us/app/id6760150378 | 2026-11-16 | verificat în sursă |
| Detention Timer: Load Tracking (Dace, Inc.) | GPS, detectare automată sosire/plecare, cronometru cu timp liber, poze BOL/POD; versiunea 0.5.0 din 19 aug.; fără evaluări | gratuit; achiziții neafișate | https://apps.apple.com/us/app/id6760627678 | 2026-11-16 | verificat în sursă |
| Trucker Tools (aplicația gratuită de urmărire a încărcăturii, folosită de brokeri) | brokerul primește alertă când așteptarea trece de 2 ore; șoferul trimite captură de ecran a traseului | aplicația e descrisă ca „free app for load tracking" (articol din 26.08.2021) | https://www.truckertools.com/three-ways-to-get-detention-pay/ | 2026-11-16 | verificat în sursă (prețul pentru șofer); actualitate neverificată |
| Hey Bubba! (bubba.ai) | urmărește așteptarea din geofence-ul ELD, compară cu termenii încărcăturii, înregistrează cererea; ținte: owner-operatori, flote 2-10 camioane | preț neafișat („Start FREE") | https://bubba.ai/solutions/detention-management | 2026-11-16 | verificat în sursă |
| ELD Motive | ELD-ul înregistrează ora și locul; pe blogul Motive nu apare o funcție dedicată de detention (3 articole, 2018-2019) | preț neafișat pe pagina de prețuri (pagina s-a încărcat fără sume) | https://gomotive.com/pricing/ ; https://gomotive.com/blog/tag/detention-time/ | 2026-11-16 | verificat în sursă (lipsa prețului și a funcției pe aceste pagini) |
| TruckLogics (TMS pentru owner-operatori) | contabilitate și dispecerat; cuvântul „detention" nu apare pe pagina de prețuri | Owner Operator 35,96 $/lună (anual) sau 39,95 $/lună | https://www.trucklogics.com/pricing | 2026-11-16 | verificat în sursă |

Dispărute din App Store: „Detention Source" (id6444958697) și „Detention Source Lite" (id6480213112), menționate în faza 1, întorc 404 în SUA și Canada, iar API-ul lookup nu le mai găsește (2026-11-16, **verificat în sursă**). Că au fost retrase de dezvoltator e **dedus**, motivul e **necunoscut**.

Doar fragment, fără preț: Detention Pay Tracker (pagină Notion, se încarcă prin script și a ieșit goală), GeoStamp de la WiseTech în marketplace-ul Motive (403), FleetOptos (Geotab).

Ce înseamnă: în 2026 au apărut cel puțin 4 aplicații iOS noi pentru exact acest produs (RigRight aprilie, SherHaul aprilie, Detention Timer iunie, GetDockPay septembrie), toate cu 0-1 evaluări; cea mai veche (DMRG, din 2024) are 4 evaluări. Două aplicații mai vechi au dispărut (**dedus** din datele de mai sus). Prețul de referință pe piață: 24,99-39,99 $/lună.

## 2. Nemulțumiri
Fluxul RSS oficial de recenzii (https://itunes.apple.com/us/rss/customerreviews/id=<ID>/sortby=mostrecent/json) a întors 0 recenzii pentru MacroPoint, Trucker Tools, Carrier 360, MySpot, SherHaul, DMRG și chiar pentru U-Haul (control), deci fluxul nu funcționa azi. Am citit recenziile afișate pe paginile aplicațiilor.

| Sursă (link) | Data | Față de (alternativă/proces manual) | Citat ≤15 cuvinte | Actualitate | Marcaj | Piață |
|---|---|---|---|---|---|---|
| https://www.thetruckersreport.com/truckingindustryforum/threads/detention-and-our-obligations.2543082/ | 30.06.2026 | broker/agent care tace | „I'm getting no response from the broker or agent concerning detention." | ultimele 12 luni | verificat în sursă | SUA |
| același fir, Diesel Dave | 30.06.2026 | proces manual: renunță | „I would take the lose and learn from it." | ultimele 12 luni | verificat în sursă | SUA |
| https://www.thetruckersreport.com/truckingindustryforum/threads/pathmark-transportation-mc-number-168257.2543523/ | 13.07.2026 | broker care refuză | „They then refused to pay any layover or detention." | ultimele 12 luni | verificat în sursă (relatare unilaterală, fără documente) | SUA |
| https://www.thetruckersreport.com/truckingindustryforum/posts/13474722/ (FloridaRetired) | 26.05.2026 | un broker mare | „TQL were masters at NOT paying detention in my experience." | ultimele 12 luni | verificat în sursă | SUA |
| https://www.thetruckersreport.com/truckingindustryforum/posts/13457459/ (pagina 2 a firului din faza 1; chimbotano) | 21.04.2026 | brokeri necinstiți, indiferent de dovadă | „is not going to pay to you no matter what." | ultimele 12 luni | verificat în sursă (fir pornit de un dezvoltator, vezi 0) | SUA |
| același link (FloridaRetired) | 29.04.2026 | broker care nu vrea | „The biggest problem with detention is when your broker doesn't want to pay it." | ultimele 12 luni | verificat în sursă | SUA |
| https://apps.apple.com/us/app/id1097181984 (Carrier 360 by J.B. Hunt, recenzie) | 12.08.2020 | proces: oră lipsă pe BOL | „forget to put the in an out time on the BOL and I get denied" | actualitate neverificată | verificat în sursă | SUA |
| https://apps.apple.com/us/app/id362413088 (Trucker Tools, recenzie „Could be better.") | 22.02.2022 | urmărirea continuă cu GPS | „with it always tracking it drains the battery down on your phone quick" | actualitate neverificată | verificat în sursă | SUA |
| https://www.thetruckersreport.com/truckingindustryforum/threads/whats-the-1-reason-your-detention-claims-get-denied.2529156/page-2 (Lennythedriver) | 12.08.2025 | brokeri, în general | „Detention pay is one of the biggest cat mouse games in this industry." | cu 3 luni înainte de fereastra de 12 luni | verificat în sursă (fir pornit de un dezvoltator) | SUA |

Număr: 6 citate din ultimele 12 luni, dar din doar 4 fire, toate pe același forum (TruckersReport), iar două fire sunt pornite de constructori de aplicații. Independente și spontane: 3 fire (Detention and our obligations, Pathmark, Detention claim process). Niciuna nu se plânge de lipsa unei aplicații; toate se plâng de brokeri care nu vor să plătească (**dedus**). Hacker News (Algolia, „trucking detention", 2026-11-16): niciun rezultat relevant.

## 3. Ipoteza de schimbare
Ipoteza: șoferul pierde bani pentru că dovada lui (notă pe BOL, poze) e respinsă; o aplicație care generează automat o dovadă cu ore GPS și o trimite brokerului ar recupera bani, deci ar plăti ~25 $/lună.

### Ce o susține
- Recenziile DMRG (doar 4, din 2024): un proprietar de flotă mică spune că încasările din detention s-au dublat într-o lună; altul: cererile săptămânale durează ~10 minute (https://apps.apple.com/app/id6502769929 , 2026-11-16, **verificat în sursă**, actualitate neverificată).
- Dovada contează uneori: refuz pentru că ora de intrare/ieșire lipsea pe BOL (recenzia Carrier 360, 2020, **verificat în sursă**).
- Faptul că alți 4-5 dezvoltatori au lansat aplicații în 2026 arată că problema e vizibilă (**dedus**; nu arată că se vinde).

### Ce o slăbește
Contraargumentul „hard sell at any price" e confirmat de mai multe surse care spun că dovada nu schimbă decizia sau că dovada există deja gratuit:
- Dovada nu schimbă decizia: „when a broker is shady , dishonest and unethical, is not going to pay to you no matter what." (chimbotano, 21.04.2026, https://www.thetruckersreport.com/truckingindustryforum/posts/13457459/ , **verificat în sursă**). „The biggest problem with detention is when your broker doesn't want to pay it." (FloridaRetired, 29.04.2026, același link). „What actually works is learning who to work with" (86scotty, 28.05.2026, https://www.thetruckersreport.com/truckingindustryforum/posts/13474722/ , **verificat în sursă**).
- Contractul decide, nu dovada: „Can only file what the rate con is for." (wichris, 05.05.2026, pagina 2 a firului din aprilie, **verificat în sursă**). „Unless the rate con/contract specifies TONU/Detention the bond won't pay." (wichris, 28.02.2025, https://www.thetruckersreport.com/truckingindustryforum/posts/13133074 , **verificat în sursă**, în afara celor 12 luni). Sfatul repetat e „Don't load next time till you get a revised rate con." (30.06.2026, firul „Detention and our obligations", **verificat în sursă**).
- Dovada există deja gratuit: „Your ELD will show everything you need." și „Why try to make an app when you already have that info?" (wichris, 20.04.2026, https://www.thetruckersreport.com/truckingindustryforum/posts/13451555/ , **verificat în sursă**). „The answer is not an app," (Opendeckin, 21.04.2026, pagina 2, **verificat în sursă**). „You are creating a solution for a problem that does not exist" (Blu_Ogre, 20.04.2026, **verificat în sursă**). „The big-time brokers have tracking apps to download." (bryan21384, 20.04.2026, pagina 2). Trucker Tools trimite brokerului alertă după 2 ore și e gratuită pentru șofer (vezi secțiunea 1).
- Majoritatea refuzurilor ar fi cereri nedepuse, nu dovezi respinse: „Most unpaid detention is unclaimed rather than refused." (https://bubba.ai/problems/broker-wont-pay-detention , actualizat 07.10.2026, **verificat în sursă**; pagină de vânzare a unui concurent, fără date).
- Mulți șoferi spun că încasează fără probleme: „Never had a problem collecting detention pay from the vast majority of brokers out there." (rollin coal, 20.04.2026, pagina 2, **verificat în sursă**).
- Piața de aplicații arată tracțiune slabă: 4 aplicații noi din 2026 cu 0-1 evaluări, DMRG cu 4 evaluări în doi ani, două aplicații retrase (secțiunea 1, **dedus**).

### Bariere de schimbare
- Gratuitul existent: ELD-ul (obligatoriu, deja plătit) și aplicațiile de urmărire cerute de brokeri (MacroPoint, Trucker Tools) produc deja ore și locații (**verificat în sursă** în firele citate; costul ELD-ului: **necunoscut** din pagini oficiale).
- Încă o aplicație pe telefon care urmărește în fundal: risc de baterie (recenzia Trucker Tools, 2022) și oboseala față de aplicații (articolul Overdrive despre „app overload" a fost blocat, vezi 8).
- Încredere: pe forum, cine propune o aplicație e luat drept „not even a truck driver" sau „AI" (secțiunea 0).
- Brokerul trebuie să accepte documentul: nicio sursă nu arată un broker care acceptă un PDF dintr-o aplicație terță ca dovadă mai bună decât ELD-ul (**necunoscut**).

### Cumpărarea efectivă: se află doar din test.

## 4. Calea către cumpărători
Căutări (Ubersuggest, SUA, locId 2840, limba en, 2026-11-16; contor „reports" înainte de primul apel: 14 din 150; 6 apeluri făcute):

| Căutare | Volum lunar | CPC | Intenție | Marcaj |
|---|---|---|---|---|
| detention pay | 390 | 0 | informațională | verificat în sursă (Ubersuggest) |
| what is detention pay | 170 | 0 | informațională | idem |
| truck driver detention pay | 140 | 0 | informațională | idem |
| detention pay trucking | 140 | 0 | informațională | idem |
| trucking detention | 140 (110-170 în ultimele 13 luni) | 0 | informațională | idem |
| detention pay calculator trucking | 0 | 0 | - | idem |
| detention time app | 0 | 0 | - | idem |
| truck detention tracker | 0 | 0 | - | idem |
| detention invoice / detention letter to broker | fără date | - | - | idem |

Nimeni nu caută o aplicație pentru asta; căutările sunt de tipul „ce este detention pay" (**dedus**).

Canale și regulile lor:
- **TruckersReport** (unde stă toată dovada de cerere): Regula 2 din Termeni: „No Advertising.", iar promovarea site-ului sau a firmei duce la blocarea contului (https://www.thetruckersreport.com/truckingindustryforum/help/terms , 2026-11-16, **verificat în sursă**). Firul „Forum Rules" (2009, editat 2014): „Promoting your website or businesses will result in your account being banned." (https://www.thetruckersreport.com/truckingindustryforum/threads/forum-rules.98668/ , **verificat în sursă**). Deci forumul nu e un canal de vânzare; există un link „Advertise with Us", prețul reclamei: **necunoscut**. Pe forum, linkurile din cuvinte ca „GPS" duc la Hammer App, apărând și în fire fără legătură, deci sunt inserate de site (**dedus**).
- **App Store** (cerințe pentru o aplicație cu localizare în fundal, din https://developer.apple.com/app-store/review/guidelines/ , 2026-11-16, **verificat în sursă**):
  - 2.5.4: „Multitasking apps may only use background services for their intended purposes: VoIP, audio playback, location, task completion" (localizarea în fundal e permisă, dar doar pentru scopul declarat).
  - 2.4.2: „Apps should not rapidly drain battery, generate excessive heat"
  - 5.1.5: „Use Location Services in your app only when it is directly relevant to the features" și trebuie notificat și cerut acordul înainte de colectare.
  - 5.1.1(iv): dacă utilizatorul refuză localizarea, aplicația trebuie să ofere o alternativă (ex. introducerea manuală a adresei).
  - 5.1.2(i): partajarea datelor cu terți (aici: locația trimisă brokerului) cere permisiune explicită.
  - 4.3(b): „Don't submit apps that are indistinguishable from what's already widely available." Cu 5-6 aplicații aproape identice, riscul de respingere există (**dedus**).
  - 3.1.1: abonamentul se vinde obligatoriu prin achiziție în aplicație.
  - Taxă: „The Apple Developer Program is 99 USD per membership year" (https://developer.apple.com/programs/whats-included/ , **verificat în sursă**). Comision redus „15% on paid apps and Apple In-App Purchases" pentru dezvoltatori sub 1 milion USD (https://developer.apple.com/app-store/small-business-program/ , **verificat în sursă**).
- Reclame: CPC 0 la toate căutările înseamnă că nimeni nu licitează; costul real al unui clic: **necunoscut**. Facebook/TikTok pentru șoferi: cost **necunoscut**.
- Android: nu am verificat Google Play; ponderea șoferilor pe Android: **necunoscut**.

## 5. Drumul până la 2.000 lei/lună (încasări brute)
2.000 lei / 4,8428 = 412,98 USD/lună. 3.000 lei = 619,48 USD/lună. [corectat la verificarea independentă, pasul 4]

Abonament (clienți ACTIVI plătitori în fiecare lună):
- la 24,99 $/lună (RigRight, GetDockPay): 412,98 / 24,99 = 16,5, deci **17 abonați activi** (pentru 3.000 lei: 24,8, deci 25).
- la 39,99 $/lună (DMRG): 412,98 / 39,99 = 10,3, deci **11 abonați activi**.
- la 0,99 $ per cursă (DMRG): 412,98 / 0,99 = 417,2, deci 418 curse plătite pe lună. [corectat la verificarea independentă, pasul 4]

Plată unică (cumpărători NOI în fiecare lună):
- la 29,99 $ (SherHaul, dacă e achiziție unică; neclar): 412,98 / 29,99 = 13,8, deci **14 cumpărători noi în fiecare lună**.

Costuri directe cunoscute, separat: comisionul Apple 15% (la 17 × 24,99 $ = 424,83 $ brut rămân 361,11 $ net); 99 $/an programul de dezvoltator (≈ 8,25 $/lună). Găzduire pentru trimiterea PDF-ului pe e-mail: **necunoscut** (probabil mică, **dedus**). Costul de achiziție al unui abonat: **necunoscut**.

Pentru comparație: cea mai veche aplicație dedicată (DMRG) are 4 evaluări după doi ani, iar cele 4 lansate în 2026 au 0-1 (secțiunea 1). Nu știm câți abonați au (**necunoscut**), dar nimic din ce am văzut nu arată vreuna cu 17 abonați activi.

## 6. Produsul restrâns
### Ce face (max 5 rânduri)
Aplicație de telefon pentru șofer: la sosirea la depozit (geofence sau o atingere) pornește cronometrul, notează ora și locul, cere o poză cu foaia de intrare; la plecare calculează orele peste timpul liber din rate con și tariful pe oră; generează un PDF cu cronologia și îl trimite pe e-mail brokerului, cu mesaj de anunțare la începutul detention-ului. Fără integrare ELD în prima versiune.

### Efort de construire (dedus)
3-5 săptămâni pentru iOS (React Native/Expo sau Swift): localizare în fundal cu regiuni, PDF, e-mail, abonament prin achiziție în aplicație. Agenția lucrează pe web, deci localizarea în fundal și trecerea prin App Review sunt partea cea mai incertă. Android ar mai adăuga 1-2 săptămâni.

### Efort de operare lunar (dedus)
Suport pentru „aplicația n-a prins sosirea", întrebări despre baterie, actualizări la fiecare versiune iOS, conținut și reclame. 5-10 ore/lună fără reclame; necunoscut cu reclame.

### Ce se poate strica lunar
- Schimbări Apple la permisiunile de localizare sau respingere la actualizare pe 4.3(b) sau 5.1.x.
- Telefoane care opresc localizarea în fundal (economie de baterie) și ratează sosirea, deci dovada lipsește exact când trebuie.
- Un broker contestă PDF-ul și clientul anulează abonamentul.
- Aplicațiile gratuite ale brokerilor (Trucker Tools, MacroPoint) sau ELD-urile adaugă aceeași funcție.

## 7. Presupunerea care omoară ideea
Că banii se pierd din cauza dovezii. Sursele citite spun că brokerul plătește sau nu după rate con și după cât de cinstit e, iar dovada (ELD, aplicațiile de urmărire ale brokerilor) există deja gratuit. Dacă e așa, un PDF mai bun nu schimbă rezultatul, iar șoferul nu plătește 25 $/lună pentru el.

## 8. Surse blocate
- https://www.overdriveonline.com/detention-parking-app-overload-hot-button-issues-for-owner-ops-explored-in-the-context-of-techs-sometime-salve : 403 (WebFetch și curl), 2026-11-16.
- https://www.thetruckersreport.com/truckingindustryforum/posts/13413923 (fir „Avoid --- Titanium American Logistics"): 403 (WebFetch și curl), 2026-11-16. Celelalte pagini TruckersReport s-au deschis.
- reddit.com (căutare r/Truckers): 403, 2026-11-16.
- https://marketplace.gomotive.com/app/geostamp-by-wisetech-global : 403, 2026-11-16.
- Pagina Notion „Detention Pay Tracker": se încarcă prin script, conținut gol la citire.
- https://gomotive.com/pricing/ : s-a deschis, dar fără prețuri (doar o fereastră de bun venit).
- Fluxul RSS iTunes de recenzii: răspuns valid, dar 0 recenzii pentru toate aplicațiile încercate, inclusiv una de control (U-Haul), 2026-11-16.
- https://www.bnr.ro/nbrfxrates.xml : pagină „Error"; am folosit cursbnr.ro.
- Nu e blocare, ci dispariție: paginile App Store ale „Detention Source" și „Detention Source Lite" (404 în SUA și Canada).

## 9. Lista surselor decisive pentru verificarea independentă
1. https://www.thetruckersreport.com/truckingindustryforum/posts/13451555/ , 2026-11-16, fir de validare al unui dezvoltator / contraargument: „Before I build anything I want to know if this is actually useful to real drivers."; „Your ELD will show everything you need."
2. https://www.thetruckersreport.com/truckingindustryforum/posts/13457459/ , 2026-11-16, contraargument (dovada nu schimbă decizia): „is not going to pay to you no matter what."; „The answer is not an app,"
3. https://www.thetruckersreport.com/truckingindustryforum/threads/whats-the-1-reason-your-detention-claims-get-denied.2529156/page-2 , 2026-11-16, sondajul din faza 1 e pornit de un dezvoltator: „The tool I'm envisioning isn't a new billing system."
4. https://www.thetruckersreport.com/truckingindustryforum/threads/detention-and-our-obligations.2543082/ , 2026-11-16, nemulțumire: „I'm getting no response from the broker or agent concerning detention."
5. https://www.thetruckersreport.com/truckingindustryforum/threads/pathmark-transportation-mc-number-168257.2543523/ , 2026-11-16, nemulțumire: „They then refused to pay any layover or detention."
6. https://www.thetruckersreport.com/truckingindustryforum/posts/13474722/ , 2026-11-16, nemulțumire: „TQL were masters at NOT paying detention in my experience."
7. https://bubba.ai/problems/broker-wont-pay-detention , 2026-11-16, contraargument (vânzător): „Most unpaid detention is unclaimed rather than refused."
8. https://apps.apple.com/app/id6502769929 , 2026-11-16, preț: „Per Load $0.99" / „Monthly $39.99"
9. https://apps.apple.com/us/app/rigright/id6761784949 , 2026-11-16, preț și funcție: „Detention Tracker" / Driver Pro „$24.99"
10. https://apps.apple.com/us/app/id6807165625 , 2026-11-16, preț: GetDockPay Pro „$24.99" lunar, „$239.99" anual
11. https://www.thetruckersreport.com/truckingindustryforum/help/terms , 2026-11-16, regulă de canal: „No Advertising."
12. https://developer.apple.com/app-store/review/guidelines/ , 2026-11-16, regulă de canal: „Don't submit apps that are indistinguishable from what's already widely available."; 2.5.4 „background services for their intended purposes"
13. https://developer.apple.com/app-store/small-business-program/ , 2026-11-16, cost: „reduced commission rate of 15% on paid apps and Apple In-App Purchases"
14. https://www.truckertools.com/three-ways-to-get-detention-pay/ , 2026-11-16, alternativă gratuită: „free app for load tracking"
