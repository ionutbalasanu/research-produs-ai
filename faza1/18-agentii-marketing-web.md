# Domeniu: Agenții de marketing și web (mici)

## Problema 1: Raportul lunar către clienți se strică sau trebuie refăcut manual (Looker Studio, exporturi PDF, conectori)
- Cine o are: agenții mici și freelanceri de marketing (PPC, SEO, social) care trimit lunar fiecărui client un raport din Looker Studio sau din alt instrument de dashboard.
- Cât de des apare: lunar, la fiecare client, în „ziua raportului” („it is Reporting Day for my clients”, NickLift, 4 aug. 2025). Pe forumul Google mai multe fire separate despre aceeași defecțiune la export, pe tot intervalul mai 2025 – sept. 2026 (vezi sursele).
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: soluții improvizate: intră în Looker Studio de pe telefon, micșorează pagina la 50–75%, folosește modul „device toolbar” din browser; un utilizator ține „5 copies” ale unui raport de 11 pagini și adaugă „MANUALLY” fiecare cont nou (Jhana47, 10 iul. 2025). Altul: „I just spent an hour trying to figure it out” (Lakestone_Digital, 2 aug. 2025). Unii renunță la Looker și trec la un instrument plătit (recenzia Capterra din 12 aug. 2026, trecută de la Looker la AgencyAnalytics).
- Soluții existente găsite, cu preț:
  - AgencyAnalytics: 20 USD pe client pe lună, facturat anual (pagina de prețuri agencyanalytics.com/pricing, deschisă; dată nevizibilă).
  - DashThis: 44 USD/lună plătit anual sau 54 USD/lună lunar pentru planul „Individual” cu 3 dashboard-uri; următorul plan 139/164 USD/lună (dashthis.com/pricing, deschisă; dată nevizibilă).
  - ManageWP „Advanced Client Reports” (doar pentru site-uri WordPress): 1 USD pe site sau 25 USD pachet până la 100 de site-uri (managewp.com/pricing, deschisă; dată nevizibilă).
- Surse deschise:
  - https://discuss.google.dev/t/193899 — 10 iulie 2025 (Jhana47; răspunsuri din 9 sept. 2025) — „it's buggy and unreliable, I can't send that to my client.”
  - https://discuss.google.dev/t/247471 — 1–5 august 2025 (NickLift, Csmyth117 și alții) — „Please get this fixed ASAP Google, I have a 8 reports to finish.”
  - https://www.capterra.com/p/158746/Agency-Analytics/reviews/ — recenzie din 12 august 2026, secțiunea „Switched from Looker” — „Our Looker dashboards were always breaking.”
- Doar fragment:
  - Fragmente de căutare despre G2 (AgencyAnalytics): „High Costs” și „Expensive” printre aspectele negative, probleme de integrare în „25 reviews”. G2 blochează accesul, deci nu se numără.
  - Cifre de tipul „5–10 hours per client per month” sau „137 billable hours”: apar doar în bloguri ale vendorilor, citate din studiile AgencyAnalytics. Nu am deschis studiile originale.
  - Fire pe discuss.google.dev văzute doar în lista de rezultate a căutării: „Looker Studio Report Blank When Downloading PDF” (post din 17 mai 2025), „Scheduled PDF delivery intermittently renders one page blank” (22 sept. 2026), „My reports stopped showing up inside the email itself” (8 iul. 2025).

## Problema 2: Întreținerea multor site-uri WordPress ale clienților: actualizări care strică site-uri, unelte de administrare nesigure
- Cine o are: agenții web și freelanceri care întrețin zeci sau sute de site-uri WordPress ale clienților, de obicei pe abonament de mentenanță.
- Cât de des apare: la fiecare val de actualizări de plugin sau temă („Almost every update turns into a headache”, recenzie Elementor, ≈ iunie 2026). Pe wordpress.org, pagina cu recenzii de 1 stea la Elementor are 24 de pagini; în ultimele ~5 luni apar titluri precum „Constantly Breaking Customer Websites” și „Elementor Updates Cause More Problems Than They Solve”.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: testează manual fiecare actualizare înainte s-o aplice; deschide și salvează din nou șabloanele ca să revină afișarea („pages require manually opening and re-saving templates”). Folosește panouri de administrare multi-site (ManageWP, MainWP), dar se plânge că site-urile se deconectează și că suportul răspunde după 3 săptămâni. Când gazda instalează automat un plugin nou, agenția trebuie să explice „100's of customers” ce e acel plugin.
- Soluții existente găsite, cu preț:
  - ManageWP: tarif per site și per modul, de regulă 1–2 USD/site/lună per modul (Backups 2 USD, Uptime 1 USD etc.) sau pachete de 25–75 USD pentru până la 100 de site-uri (managewp.com/pricing, deschisă; dată nevizibilă).
  - WP Umbrella: de la 1,99 € / 2,19 USD per site pe lună (wp-umbrella.com/pricing, deschisă; dată nevizibilă).
  - WPVibe Fleet Management (WPBeginner): actualizează mai multe site-uri dintr-un chat AI (ChatGPT, Claude). Se descrie drept „o alternativă gratuită la ManageWP” (wpbeginner.com/ro, articol deschis; dată nevizibilă).
- Surse deschise:
  - https://wordpress.org/support/topic/elementor-updates-cause-more-problems-than-they-solve/ — „5 months, 1 week ago” (≈ începutul lui iunie 2026), ascendinmotion — „be prepared to thoroughly test every update before deploying it.”
  - https://wordpress.org/support/topic/customer-support-site-connection-horrible/ — recenzie ManageWP Worker, „1 week, 4 days ago” (≈ 4 noiembrie 2026), Cyndi — „Unprofessional, unresponsive, and sites continually disconnect.”
  - https://wordpress.org/support/topic/auto-installed/ — recenzie „AI Agent by SiteGround”, „2 months, 2 weeks ago” (≈ începutul lui septembrie 2026), ianatkins — „We manage multiple client sites, auto-installing and having to explain a new plugin”
- Doar fragment:
  - Thread pe forumul Brizy, „Updates … have broken multiple site”. support.brizy.io a întors 403, deci nu se numără.
  - Recenzia Elementor „Version 3.26 broke many of the sites I maintain”: deschisă, dar e de acum „1 year, 11 months” (≈ dec. 2024), în afara intervalului. Nu se numără.
  - Recenzia Elementor „Constantly Breaking Customer Websites” (≈ iulie 2026): deschisă, dar textul conține doar „Best Client Experience”, fără conținut despre problemă. Nu se numără.

## Problema 3: Suspendări de profiluri Google Business ale clienților, greu de diagnosticat la scară
- Cine o are: agenții de SEO local și consultanți care administrează zeci sau sute de profiluri Google Business Profile (GBP) pentru clienți locali (meseriași, firme de servicii).
- Cât de des apare: un practician scrie că suspendările îi apar la conturile noi preluate „for about 3 weeks” (28 mai 2026). Search Engine Roundtable relatează în sept. 2025 că mulți specialiști SEO local raportează mai multe suspendări decât înainte.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: depune contestații una câte una, încetinește ritmul modificărilor, verifică starea fiecărui profil cu instrumentul Google de status al verificării. Instrumentul nu are căutare: „you have to scroll for days” când ai sute de profiluri. Agenția cu ~200 de profiluri spune că suspendările i-au oprit modelul de business și îi provoacă „sleepless nights”. Costul în bani: nu am găsit în surse.
- Soluții existente găsite, cu preț: instrumentul gratuit de status al verificării de la Google (support.google.com/business/workflow/12825603, recomandat de moderatorul forumului). Unelte plătite dedicate diagnosticării sau contestării suspendărilor, cu preț: nu am găsit în surse. GMBapi a lansat un rank tracker local cu scanări nelimitate (thread de vendor din 29 sept. 2026, fără preț afișat în thread), dar acesta nu tratează suspendările.
- Surse deschise:
  - https://localsearchforum.com/threads/help-suspensions-wrecking-our-agency.63237/ — 28 mai 2026, lonerangerseo — „It's killed our business model at the current moment”
  - https://localsearchforum.com/threads/suspended-disabled-or-unverified-profile-figuring-out-next-steps.63287/ — 6 iulie 2026, Stefan Somborac (moderator) — „If you manage hundreds or thousands of profiles, you have to scroll for days.”
  - https://www.seroundtable.com/google-business-profile-suspensions-increase-40169.html — 29 septembrie 2025, citează un practician — „almost every new GBP we create gets suspended within a couple of days”
- Doar fragment:
  - Thread „Agency account suspended all profiles” (localsearchforum.com/threads/agency-account-suspended-all-profiles.62262/), despre ~20 de profiluri ale clienților suspendate odată: deschis, dar e din 28 feb. 2025, în afara intervalului. Nu se numără.
  - Thread „GBP Suspended – Deceptive Content – licensed plumber” (13 mai 2026): deschis, dar autorul e proprietar de firmă, nu agenție. Nu l-am numărat pentru această problemă.

## Problema 4: Preluarea și gestionarea accesului la conturile clienților (GA4, magazine Shopify) la început și la sfârșitul colaborării
- Cine o are: agenții și freelanceri care preiau clienți noi și au nevoie de acces la Google Analytics 4 sau la magazinul Shopify al clientului, apoi gestionează aplicațiile și facturarea pe mai multe magazine.
- Cât de des apare: la fiecare client nou și la fiecare încheiere de colaborare. Un practician spune că sub 5 magazine fluxul e simplu, dar peste 20 „the install and billing bookkeeping is the actual product” (5 sept. 2026). Frecvență măsurată: nu am găsit în surse.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: pentru GA4 abandonat, formularele de recuperare Google cer un cont Google Ads legat. Fără el, agenția nu poate recupera proprietatea și ia în calcul o proprietate nouă, pierzând datele istorice. Thread-ul a durat de pe 28 aug. până pe 26 sept. 2026 fără rezolvare. Pe Shopify, agenția cere aprobare scrisă pentru fiecare preț de aplicație ca să nu apară costuri neașteptate pe factura clientului. După retragerea accesului, aplicațiile rămân instalate și continuă să fie facturate. Cost în bani: nu am găsit în surse.
- Soluții existente găsite, cu preț: Leadsie, instrument pentru obținerea accesului la conturile clienților, 59 USD/lună sau 129 USD/lună facturat lunar (leadsie.com/pricing, deschisă; dată nevizibilă). Un articol Leadsie e recomandat în thread-ul GA4 ca pas de recuperare, fără succes.
- Surse deschise:
  - https://localsearchforum.com/threads/access-to-lost-ga4-property.63361/ — 28 august 2026 (continuat până pe 26 sept. 2026), RMortis — „Have a new client with no access to the account”
  - https://community.shopify.com/t/676879 — 5 septembrie 2026, lumine — „If your access is later removed the app keeps running and keeps billing”
- Doar fragment:
  - Thread „Are agencies allowed to hold Google Analytics account data hostage”: deschis, dar din 18 apr. 2019, în afara intervalului. Nu se numără.
  - Articole de vendori (connexify.io, webtonic.io, chatfuel.com) despre accesul la Meta Business Manager, Google Ads și GA4: doar fragmente de căutare, interes comercial.

## Surse blocate
- reddit.com (r/agency): HTTP 200, dar pagina goală (conține doar „Reddit”)
- g2.com: HTTP 403 („Please enable JS and disable any ad blocker”)
- trustpilot.com: HTTP 403 (blocat ca bot)
- upwork.com: HTTP 403 (Cloudflare)
- producthunt.com: HTTP 403 („Just a moment…”)
- fiverr.com: HTTP 403 (captcha „It needs a human touch”)
- indiehackers.com: HTTP 403 („Just a moment…”)
- quora.com: HTTP 403 („Just a moment…”)
- forum.squarespace.com: HTTP 403 („Just a moment…”)
- sitepoint.com/community: HTTP 403 („Just a moment…”)
- support.brizy.io: HTTP 403
- searchengineland.com: HTTP 403
- community.framer.com: fără răspuns (HTTP 000)
- discourse.webflow.com: redirecționează spre community.webflow.com; căutarea JSON nu a mai funcționat, n-am extras fire
- localsearchforum.com/search: nu întoarce rezultate fără autentificare (am folosit doar paginile de thread și pagina principală)

## Căutări făcute
- WebSearch: „AgencyAnalytics reviews expensive client reporting agency complaints 2026”
- WebSearch: „"monthly client reports" agency hours wasted forum 2025”
- WebSearch: „web designer clients feedback revisions endless email chasing approval forum 2026” (doar bloguri de vendori)
- WebSearch: „discourse.webflow.com client content collection waiting for client content”
- WebSearch: „agency getting access to client Meta business manager Google Ads GA4 frustrating "access" clients forum 2026” (doar vendori)
- WebSearch: „wordpress.org support "client sites" plugin update broke 2026 agency manage multiple sites”
- WebSearch: „markup.io pricing change reviews 2025 agencies feedback tool alternative” (articolul launchthedamnthing.squarespace.com deschis, dar datat 11 feb. 2025, în afara intervalului; problema „feedback de la clienți pe site” nu a intrat în fișier, lipsesc 2 surse valide)
- WebSearch: „site:warriorforum.com agency clients reporting OR "client" 2026” (fără rezultate de pe forum)
- WebSearch: „European Accessibility Act agency client websites forum "EAA" web designer clients asking 2025” (doar vendori; neinclus)
- WebSearch: „social media manager clients slow to approve posts content calendar approval "clients" forum thread 2026” (doar vendori; neinclus)
- WebSearch: „capterra.com Planable reviews”
- WebSearch: „support.google.com/business/thread agency client profile suspended video verification manager 2026”
- WebSearch: „localsearchforum.com threads 2026 "clients" profiles suspended agency managing many GBP”
- WebSearch: „localsearchforum.com clients asking ChatGPT AI visibility tracking report 2026”. Am deschis martech.org (24 iul. 2026) și comunicatul AgencyAnalytics (30 iun. 2026): „66%” dintre agenții spun că serviciile de vizibilitate în căutarea AI sunt cel mai cerut serviciu nou. Ambele surse vin de la același vendor (AgencyAnalytics), deci nu sunt independente; problema nu a intrat în fișier.
- WebSearch: „"previous agency" won't give access Google Analytics GA4 Google Ads account help thread 2026”
- WebSearch: „support.google.com analytics thread "no admin" GA4 property former agency regain access 2026”
- WebSearch (RO): „agenție marketing digital rapoarte lunare clienți timp pierdut forum” (doar bloguri de agenții, fără forumuri românești)
- WebSearch (RO): „"există un tool" OR "exista vreun tool" administrare site-uri clienti wordpress actualizari agentie web”
- API Hacker News (hn.algolia.com), comentarii după 15.05.2025: „agency client reporting”, „marketing agency clients reports hours”, „agency client approvals feedback”, „agency clients wordpress maintenance” (doar anunțuri și autopromovări, nimic folosit)
- Căutare Discourse pe discuss.google.dev (după 15.05.2025): „looker studio agency clients reports connector”, „looker studio supermetrics expensive”, „client report broken connector”, „Looker Studio clients report agency”, „looker studio monthly report client”, „Report Blank When Downloading PDF”, „previous agency access GA4”, „client lost access analytics property admin left”, „agency access client account”
- Căutare Discourse pe community.shopify.com: „collaborator request code client store”, „agency clients stores manage multiple” (multe fire sunt postate de fondatori care își validează produsul; am folosit doar un răspuns de practician)
- wordpress.org, recenzii de 1 stea: ManageWP Worker, MainWP Child (0 recenzii de 1 stea), Elementor, Atarim (toate recenziile Atarim au 2+ ani, deci nu le-am folosit)
- Capterra: pagina de recenzii AgencyAnalytics (pagina 1 și pagina 4; pagina 4 are doar recenzii din 2017–2023)
- localsearchforum.com: pagina principală (lista de fire recente) și firele citate mai sus
- Pagini de prețuri deschise: managewp.com/pricing, wp-umbrella.com/pricing, agencyanalytics.com/pricing, dashthis.com/pricing, leadsie.com/pricing
