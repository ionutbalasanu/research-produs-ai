# Domeniu: Săli de fitness și antrenori personali

Notă de metodă: majoritatea surselor deschise sunt recenzii Capterra (pagini sortate „most critical" și „most recent", deschise cu HTTP 200) și comentarii Hacker News (deschise cu HTTP 200). Pe Capterra, multe recenzii poartă mențiunea „The reviewer received a gift card", adică recenzentul a primit o recompensă. Forumurile de profil (Reddit, Quora) și piețele de freelancing (Fiverr, Upwork) au blocat accesul. Datele HN sunt luate din câmpul `created_at` al API-ului oficial hn.algolia.com, pentru că pagina HN arată doar date relative („10 months ago").

## Problema 1: Datele de nutriție ale clienților nu ajung corect în aplicația antrenorului, care calculează mediile manual
- Cine o are: antrenori online și coach-i de nutriție care urmăresc macronutrienții clienților prin MyFitnessPal sau prin wearables, legate de Trainerize, My PT Hub sau Everfit.
- Cât de des apare: nu am găsit o frecvență măsurată. În paginile Capterra citite apare la 3 produse diferite (Trainerize, My PT Hub, Everfit), la recenzenți diferiți, între iulie 2025 și august 2026.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: intră în contul MyFitnessPal al fiecărui client și calculează mediile de mână („made my job longer and more tedious"). Alții se întorc în MyFitnessPal pentru fibre și micronutrienți, sau sincronizează manual datele din Fitbit. Nu am găsit în surse un număr de ore.
- Soluții existente găsite, cu preț: ABC Trainerize, între 9 $ și 248 $ pe lună în funcție de numărul de clienți (pagina oficială de prețuri, trainerize.com/pricing, deschisă); Everfit, de la 19 $ pe lună (Capterra); My PT Hub, de la 22,5 $ pe lună (Capterra). Toate au integrare cu MyFitnessPal, iar recenziile de mai jos sunt tocmai despre ea. Pe Etsy se vând trackere Google Sheets/Excel pentru antrenori (doar fragment, vezi mai jos).
- Surse deschise:
  - https://www.capterra.com/p/140262/Trainerize/reviews/?sort=most_critical, 3 iulie 2025 (recenzia „Okay Product"), „I have to individually go into each person MFP and calculate averages myself."
  - https://www.capterra.com/p/146651/My-PT-Hub/reviews/?sort=most_critical, 3 august 2026 (recenzia „Easy to use and very simple to get clients on board"), „clients have been unable to sync MyFitnessPal and other tracker apps."
  - https://www.capterra.com/p/202837/Everfit/reviews/?sort=most_critical, 27 ianuarie 2026 (recenzia „A Professional, Client-Friendly Platform That Elevates Nutrition Coaching"), „which means needing to refer to MyFitnessPal for more detailed nutrition data."
  - https://www.capterra.com/p/140262/Trainerize/reviews/?sort=most_critical, 16 decembrie 2025 (recenzia „Convenient app - all info in one place for training"), „doesn't always sync automatically with fitbit so have to manually do this"
- Doar fragment:
  - Etsy, „Personal Trainer Client Tracker V3, Coaching Spreadsheet" (https://www.etsy.com/listing/4563064957/): fragmentul de căutare dă un preț de 23,63 CA$ (redus de la 29,54 CA$). Pagina a fost blocată (403).
  - Payhip, „Personal Trainer Client Hub" pentru Excel (https://payhip.com/b/Uct49): fragmentul dă 24 $. Pagina a fost blocată (403).
  - Capterra Trainerize, recenzie din 12 mai 2023: antrenorul folosește Google Sheets pentru nutriție. Am citit-o, dar e mai veche de 18 luni, așa că nu se numără.

## Problema 2: Verificarea check-in-urilor săptămânale și analiza datelor clienților se fac manual și cresc odată cu numărul de clienți
- Cine o are: antrenori online cu mulți clienți la distanță, care primesc săptămânal formulare de check-in, jurnale de antrenament și date de progres.
- Cât de des apare: săptămânal, la fiecare client (ciclul obișnuit de check-in). Nu am găsit într-o sursă independentă câte ore îi ia unui antrenor.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: compară de mână ce a programat cu ce a făcut clientul și își petrece serile de duminică cerând clienților update-urile săptămânale (HN). Unii schimbă platforma ca să aibă check-in-uri mai structurate (TrueCoach). Nu am găsit în surse un cost în bani.
- Soluții existente găsite, cu preț: Everfit are „AI-powered Smart Response", adică ciorne de răspuns generate cu AI („AI-generated drafts that match your coaching tone", pe pagina oficială everfit.io/pricing, deschisă). Prețul planului care include funcția nu apare în textul paginii; Everfit pornește de la 19 $ pe lună (Capterra). CoachingPortal (lansat pe HN, martie 2026) are check-in-uri automate, preț negăsit. Koachi și TrainerCheck (Product Hunt / hunted.space) apar doar în fragmente.
- Surse deschise:
  - https://www.capterra.com/p/202837/Everfit/reviews/?sort=most_critical, 23 septembrie 2026 (recenzia „More Than a Coaching App"), „ability to quickly compare what I programmed versus what the client actually completed."
  - https://www.capterra.com/p/202837/Everfit/reviews/?sort=most_critical, 8 octombrie 2026 (recenzia „Everfit - ragnarok coaching perspective"), „the ability to analyse client data more intelligently"
  - https://www.capterra.com/p/155784/truecoach/reviews/?sort=most_critical, 22 august 2025 (recenzia „Excellent for 1:1 personal training – less suited for full online coaching"), „needing more automation around recurring habits, structured check-ins, and additional tools for nutrition coaching"
  - https://news.ycombinator.com/item?id=47428153, 18 martie 2026 (fondatorul CoachingPortal, despre un prieten antrenor), „manually copy-pasting updated programs into PDFs and chasing clients for weekly updates."
- Doar fragment:
  - coachway.io (vendor de software): estimează 10–12,5 ore pe săptămână de check-in-uri la 50 de clienți. Pagina nu a fost deschisă, iar cifra e de marketing.
  - Koachi pe Product Hunt (https://www.producthunt.com/p/koachi/koachi-2): fragmentul spune „the time taken to receive feedback and the clients experience inputting feedback". Pagina a fost blocată (403).
  - Un fir pe r/personaltraining despre check-in-urile clienților online. Reddit a fost blocat.

## Problema 3: Programele de antrenament se introduc greu în aplicațiile de coaching, așa că antrenorii le scriu în altă parte și le transferă de mână
- Cine o are: antrenori personali și online care scriu programe individualizate (serii, repetări, progresii) și le livrează prin aplicații precum My PT Hub, Everfit sau Trainerize.
- Cât de des apare: ori de câte ori antrenorul scrie sau actualizează programul unui client. Nu am găsit o frecvență măsurată.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: scrie antrenamentul în câmpul de note când aplicația nu acceptă intervale de repetări. Ține programele în foi de calcul sau în aplicații generice, le copiază în PDF-uri, sau le construiește în Claude și le trimite apoi în aplicație. Un recenzent Everfit spune că un import sau o înlocuire în masă „would save hours" (fără cifră exactă). Pe Fiverr există multe oferte de încărcare a programelor în Trainerize, Everfit și TrueCoach (doar fragmente; Fiverr a blocat accesul).
- Soluții existente găsite, cu preț: Everfit are „AI Workout Builder" (pagina oficială de prețuri, deschisă). Un recenzent spune că poate lipi un antrenament în text și aplicația îl construiește. Everfit pornește de la 19 $ pe lună (Capterra). KeegNation duce programele scrise în Claude într-o aplicație de fitness, preț negăsit. Gymlocity (în dezvoltare, ianuarie 2026), preț negăsit.
- Surse deschise:
  - https://www.capterra.com/p/146651/My-PT-Hub/reviews/?sort=most_critical, 8 mai 2026 (recenzia „Great app for a great coached and coaching experience."), „end up having to write the actual workout in the notes section"
  - https://www.capterra.com/p/146651/My-PT-Hub/reviews/?sort=most_critical, 21 iulie 2026 (recenzia „Best personal trainer app"), „it does not allow for easy seamless change when progressing clients."
  - https://www.capterra.com/p/202837/Everfit/reviews/?sort=most_critical, 2 noiembrie 2026 (recenzia „The backbone of my online coaching business"), „A bulk upload or bulk-replace option would save hours."
  - https://news.ycombinator.com/item?id=46579190, 11 ianuarie 2026 (Gymlocity, în „Ask HN: What are you working on?"), „trainers still use spreadsheets or generic apps"
  - https://news.ycombinator.com/item?id=48131487, 14 mai 2026 (KeegNation), „personal trainers could stay in Claude while they create programming for their clients"
- Doar fragment:
  - Fiverr: cel puțin 20 de oferte apărute la căutare, de tipul „I will setup and upload workout plans on trainerize, truecoach, everfit and mypthub" (https://fiverr.com/fred_gittens/...). Toate au fost blocate (403); prețurile nu se văd în fragmente.

## Problema 4: Pentru sălile mici și antrenorii independenți, software-ul all-in-one de management e prea scump și prea complicat
- Cine o are: proprietari de săli mici, studiouri, boxe CrossFit și academii de arte marțiale, plus antrenori independenți care trec la Mindbody, Wodify sau soft similar.
- Cât de des apare: continuu, prin abonamentul lunar, comisioanele la plăți și contractul pe termen lung. Nu am găsit o frecvență măsurată.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: plătește un Customer Success Manager și un Technical Account Manager ca să poată folosi sistemul (Mindbody, noiembrie 2026). Plătește comisioane de procesare a cardurilor peste abonament (Wodify). Rămâne blocat în contract (Mindbody, octombrie 2026). Unii revin la soluții simple, cum ar fi Square sau Excel. Pierderea de timp pe administrație e menționată și de fondatori care construiesc alternative (HN).
- Soluții existente găsite, cu preț: Mindbody, de la 79 $ pe lună; Wodify, de la 99 $ pe lună; PushPress, de la 159 $ pe lună (toate sunt prețuri de pornire afișate pe Capterra). Glofox nu afișează preț pe Capterra („Contact vendor for pricing"). Alternative mai simple în dezvoltare: Gymlocity și MatGoat (HN), preț negăsit.
- Surse deschise:
  - https://www.capterra.com/p/40229/MINDBODY/reviews/?sort=most_critical, 5 noiembrie 2026 (recenzia „Outstanding Customer Success Support That Helps Us Get More Out of Mindbody"), „it's expensive to keep paying for on an ongoing basis as a small gym owner."
  - https://www.capterra.com/p/40229/MINDBODY/reviews/?sort=most_critical, 12 octombrie 2026 (recenzia „Do not sign Contract"), „found the interface confusing and unnecessarily complicated"
  - https://www.capterra.com/p/159663/Wodify/reviews/?sort=most_critical, 22 septembrie 2026 (recenzia „10+ Years, Thousands of WODs, Still Wodifying!"), „The monthly fees are relatively high, especially for a smaller CrossFit affiliate"
  - https://news.ycombinator.com/item?id=46579190, 11 ianuarie 2026 (Gymlocity), „The big players (Mindbody, etc.) are overkill and expensive for this market."
  - https://news.ycombinator.com/item?id=49691324, 14 septembrie 2026 (MatGoat), „saw how much time instructors lose to admin work"
- Doar fragment:
  - Recenziile Software Advice despre Mindbody: „prices have continued to increase" (din rezumatul căutării, necitit direct).
  - Blogurile concurenților WellnessLiving și Glofox despre creșterile de preț Mindbody. Sunt surse interesate și nu au fost deschise.

## Problema 5: Proprietarii de săli segmentează greu membrii și configurează greu automatizările de marketing, actualizările în masă și rapoartele
- Cine o are: proprietari și manageri de săli și studiouri care folosesc Wodify sau Mindbody pentru lead-uri, retenție și comunicarea cu membrii.
- Cât de des apare: la fiecare campanie, segment nou sau raport. Nu am găsit o frecvență măsurată.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: cere echipei de suport să construiască automatizările („their customer support team will build out any automation for you", Wodify, 1 noiembrie 2026). Verifică rapoartele de mână ca să se potrivească cu propriile cifre (Wodify, 8 octombrie 2026). Nu am găsit în surse un cost.
- Soluții existente găsite, cu preț: Mindbody „AI Concierge" și „Marketing Suite", menționate în recenzia din 10 noiembrie 2026 (Mindbody pornește de la 79 $ pe lună pe Capterra; prețul modulelor nu l-am găsit). Wodify are un asistent AI, menționat în recenzia din 4 noiembrie 2026 (Wodify pornește de la 99 $ pe lună pe Capterra).
- Surse deschise:
  - https://www.capterra.com/p/159663/Wodify/reviews/?sort=most_critical, 1 noiembrie 2026 (recenzia „Perfect for a CrossFit gym"), „Creating segments or automations is beyond hard."
  - https://www.capterra.com/p/40229/MINDBODY/reviews/?sort=most_critical, 6 noiembrie 2026 (recenzia „Great Lead Management, but Contracts and Contact Lists Are Cumbersome"), „Setting up of contracts and creating contact lists can be very cumbersome"
  - https://www.capterra.com/p/40229/MINDBODY/reviews/?sort=most_critical, 12 noiembrie 2026 (recenzia „Strong Scheduling and Marketing Insights, Though Bulk Updates Need Work"), „I'd liked bulk client updates in Mindbody to be easier."
  - https://www.capterra.com/p/159663/Wodify/reviews/?sort=most_critical, 8 octombrie 2026 (recenzia „10/10 onboarding, and teaming with Wodify"), „The reports could be easier to navigate."
- Doar fragment: nu am găsit în surse.

## Problema 6: Aplicațiile pentru săli și antrenori nu sunt disponibile în limba membrilor sau a clienților
- Cine o are: săli și antrenori din țări unde clienții nu vorbesc engleza (exemplele din surse: Honduras, o țară vorbitoare de germană, Norvegia).
- Cât de des apare: permanent, pentru fiecare membru sau client care nu știe engleza. Nu am găsit o frecvență măsurată.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: proprietarul acceptă limitarea de la început („we were aware of this before switching"). Personalul care nu știe engleza se descurcă greu cu platforma. Nu am găsit în surse un cost.
- Soluții existente găsite, cu preț: nu am găsit în surse.
- Surse deschise:
  - https://www.capterra.com/p/159663/Wodify/reviews/?sort=most_critical, 27 octombrie 2026 (recenzia „I Am Lares CrossFit - WODIFY - Honduras"), „i have not been able to set it up in spanish"
  - https://www.capterra.com/p/159663/Wodify/reviews/?sort=most_critical, 2 noiembrie 2026 (recenzia „2 Years Wodify experience"), „The app is not offered in German"
  - https://www.capterra.com/p/146651/My-PT-Hub/reviews/?sort=most_critical, 31 martie 2026 (recenzia „Overall very pleased 😊"), „I would request more languages for these clients - ex Norwegian"
- Doar fragment: nu am găsit în surse.

## Surse blocate
- reddit.com: HTTP 200, dar pagina conține doar cuvântul „Reddit", fără conținut (firul r/personaltraining despre check-in-uri).
- trustpilot.com (ie.trustpilot.com, recenzii Trainerize): HTTP 403, „identified as coming from a bot".
- g2.com: HTTP 403, „Please enable JS and disable any ad blocker".
- upwork.com: HTTP 403, Cloudflare.
- producthunt.com: HTTP 403, „Just a moment..." (Koachi).
- fiverr.com: HTTP 403, provocare anti-bot PerimeterX (oferte de încărcare a programelor în Trainerize).
- etsy.com: HTTP 403 (trackere Google Sheets pentru antrenori).
- payhip.com: HTTP 403, Cloudflare (Personal Trainer Client Hub).
- ptroadmap.beehiiv.com (newsletter pentru antrenori, despre anulările târzii): HTTP 403, „Just a moment...". Din acest motiv problema anulărilor și a neprezentărilor nu a putut fi documentată.
- quora.com: HTTP 403, „Just a moment...".
- Neblocat, dar indisponibil: un șablon Zapier pentru check-in-uri în Google Sheets a dat HTTP 404.

## Căutări făcute
- WebSearch: „personal trainer spending hours on client check-ins every week online coaching forum 2025"
- WebSearch: „Trainerize review 1 star capterra 2025"
- WebSearch: „"is there an app" OR "is there a tool" personal trainer track clients nutrition macros google sheets 2025"
- WebSearch: „Mindbody review 2025 small studio owner price increase complaint"
- WebSearch: „fiverr personal trainer workout program writing trainerize setup gig"
- WebSearch: „news.ycombinator.com personal trainer software Show HN coaches 2025"
- WebSearch: „gym owner forum chasing failed payments members declined cards hours every month" (doar bloguri de vendori)
- WebSearch: „indiehackers personal trainers pain point app check-ins programming"
- WebSearch (română): „antrenor personal programări clienți excel aplicație abonamente sală fitness forum" (doar pagini comerciale, niciun forum românesc relevant)
- WebSearch: „personal trainer "no-shows" late cancellations clients policy forum 2025 trainers" (bloguri și șabloane; sursa de la antrenori, ptroadmap, e blocată)
- WebSearch: „online coach "check-ins" overwhelmed too many clients forum thread 2026" (doar bloguri de vendori)
- WebSearch: „wordpress.org plugin gym membership booking reviews "one star" OR "doesn't work" fitness classes" (nimic relevant)
- WebSearch: „apps.apple.com Mindbody Business app"
- WebSearch: „capterra.com TrueCoach reviews Everfit reviews Glofox reviews PushPress reviews", „capterra Glofox reviews page", „capterra PushPress reviews gym owner"
- WebSearch: „personal trainer client tracker google sheets template coaches macro check-in template sale"
- Capterra, pagini de recenzii deschise (sortare most_critical și/sau most_recent): ABC Trainerize, My PT Hub, Mindbody, TrueCoach, Everfit, PTminder (fără recenzii recente extrase), ABC Glofox, PushPress, Wodify. Am deschis și pagina Software Advice pentru Trainerize (HTTP 200, neutilizată).
- Capterra, pagini de produs (prețuri de pornire): PushPress, Wodify, Mindbody, Everfit, My PT Hub, Glofox.
- Pagini oficiale de prețuri: trainerize.com/pricing, everfit.io/pricing.
- Hacker News, API oficial hn.algolia.com (comentarii după 15.05.2025): „personal trainer clients", „gym owner software", „fitness coach spreadsheet", „my gym members", „coaches check-ins", „fitness coaches", „trainers spreadsheets", „nutrition coach clients", „studio owners mindbody", „no-shows studio". Am deschis paginile HN 46579190, 49691324, 48131487 și 47428153.
