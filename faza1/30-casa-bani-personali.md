# Domeniu: Administrarea casei și a banilor personali (buget, facturi, abonamente, acte, garanții, sarcini casnice)

Notă despre date: paginile Hacker News afișează date relative („4 months ago”). Data exactă din listă provine din câmpul created_at al API-ului oficial de căutare HN (hn.algolia.com), folosit doar ca să găsim și să datăm itemii. Fiecare pagină a fost apoi deschisă direct pe news.ycombinator.com, cu HTTP 200.

## Problema 1: Abonamentele uitate continuă să fie plătite fără ca cineva din casă să le urmărească
- Cine o are: persoane fizice și familii cu multe abonamente digitale. Problema e mai mare când mai mulți membri ai familiei își fac abonamente separat.
- Cât de des apare: nu am găsit o măsurătoare independentă. Afirmațiile vendorilor: un autor spune că a găsit „$340/mo” în abonamente uitate, alt autor „$200/month”. Pagina ReSubs (vendor, 4 aprilie 2026) afirmă „Abonamentele uitate vă costă în medie 204 USD/an”, fără să arate sursa primară.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: oamenii descoperă abonamentul târziu și pierd bani. Exemplul din sursă: un abonament NYT Games nefolosit, cu un cost estimat de autor la „$100-$200”. Alte variante: scanează manual emailul, folosesc aplicații cu acces bancar (Rocket Money) sau aplicații cu introducere manuală.
- Soluții existente găsite, cu preț: Rocket Money, gratuit în varianta de bază și 6-12 USD/lună Premium (conform ReSubs). Unstar notează din recenzii negative că detecția automată ratează unele abonamente: „Subscription detection misses recurring charges.” Vexly (preț nevăzut), Inboxscan (rulează local, preț nevăzut), Tilla (Android, 2,99 USD pe viață), Bobby (iOS, achiziție unică), ReSubs (nivel gratuit + Premium).
- Surse deschise:
  - https://news.ycombinator.com/item?id=48860070 , 2026-07-10, „No one keeps track of their subscriptions.”
  - https://news.ycombinator.com/item?id=47353954 , 2026-03-12, „Built this after finding $340/mo in subscriptions I had forgotten about.”
  - https://news.ycombinator.com/item?id=45327265 , 2025-09-21, „I built Vexly after discovering I was wasting $200/month on forgotten subscriptions.”
  - https://resubs.app/ro/resources/best-apps-to-manage-recurring-payments , 2026-04-04 (vendor, folosit pentru prețuri), „Abonamentele uitate vă costă în medie 204 USD/an”
  - https://unstar.app/blog/ynab-rocket-money-monarch-everydollar-copilot-budget-apps-ranked-2026 , 2026-05-21, „Subscription detection misses recurring charges.”
- Doar fragment: comentariul HN 44535373 („Click-to-cancel rule is blocked”, 2025-07-11) despre „forgotten subscriptions”. Nu l-am deschis, deci nu se numără.

## Problema 2: Bonurile și termenele de garanție se pierd tocmai când produsul se strică
- Cine o are: persoane fizice și proprietari de locuințe cu electrocasnice și electronice în garanție.
- Cât de des apare: nu am găsit în surse. Afirmația „people lose thousands” aparține unui vendor și nu are sursă.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: oamenii nu găsesc bonul la nevoie. Unii folosesc un caiet: un comentator spune că un astfel de tool „can be replaced with a simple notebook”. Costul în bani sau timp nu l-am găsit în surse.
- Soluții existente găsite, cu preț: Good Til (gratuit cu introducere manuală, Pro $1.99/lună cu extragere AI din bon și scrisori de reclamație). Warrify (scanare AI și remindere, preț nevăzut). Stowly (inventar casnic cu garanții, preț nevăzut). Multe aplicații iOS apar doar în fragmente de căutare (vezi mai jos).
- Surse deschise:
  - https://news.ycombinator.com/item?id=47211106 , 2026-03-01, „I built Good Til because I could never find my receipts when I needed them”
  - https://news.ycombinator.com/item?id=45073262 , 2025-08-30, „people lose thousands because they forget warranty dates or can't find receipts”. Același fir, comentariu critic: „tool that can be replaced with a simple notebook”
  - https://news.ycombinator.com/item?id=49212442 , 2026-08-07, „Helps keep track of warranty information and alert you when it's coming up.”
- Doar fragment: listări App Store văzute doar în fragmentele WebSearch: WarrantyHub $4.99/lună sau $25.99/an, HousePulse premium $29.99/an, Valid $4.99/lună sau $39.99/an, Drawer $0.99 o singură dată, HomeFolio (date doar pe dispozitiv). Nu am găsit discuții de forum ale utilizatorilor, doar lansări de produse.

## Problema 3: În aplicațiile de buget, conexiunea la bancă se rupe des, iar oamenii ajung la import și reconciliere manuală
- Cine o are: persoane fizice și gospodării care își urmăresc banii în Rocket Money, Monarch, YNAB, Copilot sau GnuCash, mai ales cele cu multe conturi.
- Cât de des apare: Unstar a citit 4.000 de recenzii Google Play recente ale Rocket Money (2 decembrie 2025 - 10 septembrie 2026). Dintre cele 765 de recenzii negative consistente, 150 (19,6%) sunt despre conectarea băncii, iar 21 despre conexiuni care au mers și apoi s-au rupt. Un utilizator HN cu circa 20 de conturi spune că un cont i se deconectează „every few days”.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: reconectează conturile repetat. Un utilizator spune: „I spend more time re-linking my accounts than being able to actually use the app.” Altul face reconcilierea lunară manual pentru circa 30 de conturi și o descrie ca „takes a lot of time”. Folosește exporturi CSV acolo unde nu există API. Unii introduc manual datele, de exemplu un formular 1099 tastat de mână.
- Soluții existente găsite, cu preț: YNAB $109/an (ynab.com). Monarch $14.99/lună sau $99.99/an (Unstar). EveryDollar Premium $17.99/lună sau $79.99/an, necesar pentru sincronizarea bancară (Unstar). PocketLens, gratuit și self-hosted, cu cheile proprii Plaid (planul gratuit Plaid permite 10 conexiuni). SyncBank, plată unică (preț nevăzut). GnuCash, gratuit.
- Surse deschise:
  - https://unstar.app/blog/rocket-money-wont-link-bank-account-loop-reviews-2026 , 2026-09-12, „I spend more time re-linking my accounts than being able to actually use the app.”
  - https://news.ycombinator.com/item?id=47180709 , 2026-02-27, „my account gets disconnected every few days”
  - https://news.ycombinator.com/item?id=50122776 (comentariul utilizatorului jldugger), aprox. 2026-10-17, „Every month I sit down and compare the scheduled transactions with what actually happened”
  - https://news.ycombinator.com/item?id=49036872 , 2026-07-24, „Existing options either require manual csv imports, or route through paid relays”
  - https://www.ynab.com/pricing , dată nevizibilă (folosit doar pentru preț), „$109 USD* paid annually”
  - (același autor ca prima sursă, nu e numărată separat) https://unstar.app/blog/ynab-rocket-money-monarch-everydollar-copilot-budget-apps-ranked-2026 , 2026-05-21, „Bank connections break weekly, sometimes daily.”
- Doar fragment: pagina help.rocketmoney.com despre deconectări frecvente (articolul 10770707) și recenziile Trustpilot ale Rocket Money. Trustpilot e blocat, iar fragmentele de acolo sunt din 2024.

## Problema 4: Bugetul lunar nu prinde cheltuielile neregulate și nici momentul real în care pleacă banii din cont, așa că oamenii țin un tabel separat
- Cine o are: persoane fizice cu cheltuieli care variază de la o lună la alta, cu plăți anuale sau one-off (reparații, sărbători) și cu carduri de credit decontate luna următoare.
- Cât de des apare: nu am găsit în surse.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: un tabel separat pentru fluxul de numerar, pe lângă aplicația de buget. Un autor spune că ajustează lunar bugetul „until I pass”. Alt utilizator folosește tranzacții programate în GnuCash cu 90 de zile înainte. Costul în timp nu e cuantificat.
- Soluții existente găsite, cu preț: Stoke Money, redenumit Scone Money (abonament plătit, preț nevăzut). Bountisphere (preț nevăzut). GnuCash, gratuit (tranzacții programate și „Future Minimum Balance”). YNAB $109/an, criticat aici pentru că nu gestionează dimensiunea timpului.
- Surse deschise:
  - https://news.ycombinator.com/item?id=50122776 , aprox. 2026-10-16, „I've always had to maintain a separate spreadsheet to track my actual cash flow.” Tot de acolo: „My spending is rarely consistent month-to-month”. Întrebare în același fir: „how does the forecast handle one-off big expenses, like a car repair or Christmas?”
  - https://news.ycombinator.com/item?id=46671002 , 2026-01-18, „I find Zero-Based Budgeting (like YNAB) fails at handling Time”
- Doar fragment: întrebările de pe money.stackexchange.com „How should an annual insurance payment be recorded in a monthly budget?” (2026-09-16) și „How should I structure a monthly budget when my expenses vary significantly from month to month?” (2026-08-16). Paginile au întors 403 (Cloudflare), deci nu se numără.

## Problema 5: Împărțirea sarcinilor casnice și a programului familiei: certuri despre cine face ce și informații împrăștiate în mai multe aplicații
- Cine o are: cupluri, colegi de apartament și părinți cu copii.
- Cât de des apare: nu am găsit în surse.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: folosesc aplicații de planificare a curățeniei (Sweepy, Tody) cu abonament. Un utilizator plătește „like 18€/year for us both” și preferă o alternativă open source. Alți părinți combină calendare, notițe și remindere. Majoritatea surselor sunt fondatori care lansează produse, iar vocea directă a utilizatorilor e puțină (un singur utilizator).
- Soluții existente găsite, cu preț: Sweepy (circa 18€/an pentru doi, conform utilizatorului). ChoresMates (gratuit pentru 1 grup, Pro $0.99/lună sau $19.99 pe viață). Roomsy (un an gratuit cu cod promoțional, apoi preț nevăzut). Mana (organizator de familie cu asistent AI, preț nevăzut). LifeOrder (preț nevăzut). Fairmo (împarte facturile și rotește sarcinile, preț nevăzut).
- Surse deschise:
  - https://news.ycombinator.com/item?id=44256916 , 2025-06-12, „this prevents conflicts and also frees the mind of having to keep track”
  - https://news.ycombinator.com/item?id=47203014 , 2026-03-01, „the "I do more around the house" argument.”
  - https://news.ycombinator.com/item?id=47349283 , 2026-03-12, „Many parents currently use multiple apps – calendars, notes, reminders – which quickly becomes chaotic.”
  - https://news.ycombinator.com/item?id=50071636 , 2026-10-13, „shared calendars, shopping lists, receipt scanners, meal planning, chores, and notes”
  - https://news.ycombinator.com/item?id=44748931 , 2025-07-31, „We wanted to quickly test the niche of home cleaning trackers”
- Doar fragment: articole de blog ale unor vendori de aplicații pentru cupluri despre „mental load” (cupla.app, pairplay, kidkarma). Nu le-am deschis.

## Problema 6: Familia nu știe ce conturi, acte și facturi are gospodăria dacă cel care le administrează moare sau nu mai poate
- Cine o are: persoana care administrează banii și actele familiei, partenerul ei și moștenitorii.
- Cât de des apare: nu am găsit în surse.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: soluții făcute de mână. Exemple: o broșură „ce faci când mor”, actualizată periodic; un inventar pe hârtie în două locuri; un fișier criptat cu instrucțiuni lăsate la avocat; o cutie de valori. Costul în timp nu e cuantificat. Autorul întrebării spune că managerii de parole nu rezolvă problema „what accounts do I even have?”.
- Soluții existente găsite, cu preț: Trustworthy („Family Operating System”). Pe pagina de prețuri am văzut planurile, dar nu și sumele în dolari. DocsOrb (iOS, preț nevăzut). DeadSwitch (Show HN 47225171, nedeschis).
- Surse deschise:
  - https://news.ycombinator.com/item?id=44888799 , 2025-08-13, „my family would have no idea how to access my banking and investment accounts”. Tot acolo, alt utilizator: „Keep a detailed , paper-based inventory of your stuff.”
  - https://news.ycombinator.com/item?id=46703585 , 2026-01-21, „should have a "what to do when I die" booklet.”
  - https://news.ycombinator.com/item?id=44352108 , 2025-06-23, „help people (ICP: families, students, expats) get on top of all their important documents”
  - https://www.trustworthy.com/pricing , dată nevizibilă (folosit doar pentru planuri, nu se numără), „AI Answers 10/month”
- Doar fragment: Benzinga („Gold Plan: Starting at $240 per year”) și Quicken (plan gratuit Trustworthy cu 2 GB). Pagina Quicken a întors 403.

## Surse blocate
- reddit.com: HTTP 200, dar pagina conține doar cuvântul „Reddit”, fără conținut. O considerăm blocată.
- trustpilot.com: 403 („identified as coming from a bot”).
- g2.com: 403.
- upwork.com: 403 (Cloudflare).
- producthunt.com: 403 („Just a moment...”).
- fiverr.com: 403.
- etsy.com (căutare de șabloane Notion/binder): 403.
- bogleheads.org: 403 (Cloudflare).
- forum.mrmoneymustache.com: 403 (Cloudflare).
- forum.softpedia.com: 403 (Cloudflare).
- quora.com: 403 (Cloudflare).
- indiehackers.com: 403 (Cloudflare).
- money.stackexchange.com, paginile de întrebări: 403 (Cloudflare). Pagina principală a mers, întrebările nu.
- quicken.com (blog): 403.
- github.com discussions: 403 (calea nu e permisă în sesiune).
- community.monarchmoney.com: fără conexiune (HTTP 000).
- capterra.com: 404 la URL-ul încercat. Nu am mai încercat alte URL-uri.
- apps.apple.com: pagina de recenzii Tody s-a deschis, dar afișează doar recenzii vechi (2016 etc.), fără recenzii din ultimele 18 luni. Nu am folosit-o.

## Căutări făcute
- WebSearch: „app to track warranties and receipts household forum 2026”
- WebSearch: „Rocket Money review bank connection keeps disconnecting 2026”
- WebSearch: „"is there an app" track all household bills due dates forum”
- WebSearch: „chore app partner won't use it mental load household tasks forum 2026”
- WebSearch: „unstar.app Sweepy OR Tody OR OurHome OR Flatastic reviews”
- WebSearch: „unstar.app blog Monarch Money OR YNAB OR Cozi OR Splitwise reviews 2026”
- WebSearch (RO): „aplicație evidență facturi utilități abonamente garanții forum 2026”. N-a dat niciun forum românesc, doar pagini de vendori și contapp.ro (contabilitate PFA, în afara domeniului).
- WebSearch: „Trustworthy family operating system pricing documents passwords estate”
- Hacker News (căutare hn.algolia.com, comentarii și articole după 2025-05-15): „warranty receipts app”, „household paperwork organize”, „forgotten subscriptions”, „chore app partner”, „bill due dates tracking”, „warranty”, „household admin”, „paperwork”, „chores”, „subscriptions”, „YNAB”, „Monarch Money”, „home inventory”, „bills”, „mental load household”, „household chores app”, „family organizer app”, „shared family calendar chores”, „home maintenance reminders”, „if I die wife accounts”, „spouse doesn't know accounts”, „important documents family”, „paperless-ngx household”, „scan mail documents home”
- Stack Exchange (căutare money.stackexchange.com după 2025-05-15): „receipts”, „subscription”, „bills”, „track expenses”, „documents”, „budget spreadsheet”. Am găsit titluri, dar paginile au fost blocate.
- Lemmy (lemmy.world, căutare): „warranty receipts”, „household documents organize”, „subscription tracker”, „chore app”, „bill tracker”, „budget app”. Rezultate irelevante.
- Tildes (tildes.net/search): „chores”, „household bills”. Rezultate irelevante.
- Pagini de prețuri deschise: trustworthy.com/pricing, ynab.com/pricing, monarch.com/pricing (fără preț vizibil în text), sweepy.com (fără preț vizibil), goodtil.com (fără preț vizibil în afara demo-ului), resubs.app (comparație de prețuri).
