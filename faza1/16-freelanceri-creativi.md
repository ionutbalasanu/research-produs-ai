# Domeniu: Freelanceri creativi (design, foto, video)

## Problema 1: Sortarea (culling) a mii de fotografii pe ședință, mai ales alegerea celei mai bune dintre cadre aproape identice
- Cine o are: fotografi de nunți, evenimente, portret, cosplay, wildlife/păsări, jurnalism; fotografi cu aparate care trag rafale foarte rapide (ex.: 120 fps RAW).
- Cât de des apare: după fiecare ședință. Un fotograf de nunți vorbește de „thousands of images” per sesiune, iar un fotograf cu Sony A9 III de „thousands of photos per shoot” (surse mai jos). Firul oficial Adobe de feedback despre Assisted Culling avea 81 de răspunsuri și 4236 de vizualizări când l-am deschis. Nu am găsit o cifră independentă de frecvență.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: sortează manual sau cu Photo Mechanic, apoi editează în alt program. Un utilizator HN descrie „constant juggling with 3 apps”. Folosește funcția Assisted Culling din Lightroom (inclusă în abonament, conform FAQ-ului Adobe din fir), dar utilizatorii raportează că sare peste partea cea mai lentă: alegerea celui mai bun cadru dintr-o serie de cadre similare, toate clare și cu ochii deschiși. Mai raportează că funcția e reglată doar pentru oameni (nu pentru wildlife/sport), că marchează greșit cadre bune ca respinse și că blochează aplicația. Timp concret în ore: nu am găsit în surse deschise (cifrele de ore circulă doar pe bloguri ale vendorilor, văzute doar ca fragment).
- Soluții existente găsite, cu preț: Adobe Lightroom Assisted Culling (inclus în abonamentul Lightroom, conform FAQ-ului din firul Adobe); Aftershoot (de la 9,99 USD/utilizator/lună, conform Capterra); Photo Mechanic (preț negăsit în surse deschise); FirstPass (tool de culling pentru Mac, menționat de dezvoltatorul lui în firul Adobe, preț negăsit); o aplicație de culling cu clustering ML în curs de construire, menționată pe HN (preț negăsit). Imagen și FilterPixel au apărut doar în fragmente.
- Surse deschise:
  - https://community.adobe.com/questions-675/p-assisted-culling-feedback-thread-lrc-1627467/index4.html, 31 iul. 2026 (postarea christopherm49128357; în același fir: Philippe T, 21 iul. 2026, wildlife; DarkElfLX, 3 aug. 2026, cosplay; ScottLamers, 8 aug. 2026, crash-uri): „What this tool needs to do is look through images that are good”
  - https://news.ycombinator.com/item?id=47761911, 14 apr. 2026: „dealing with thousands of photos per shoot is a challenge”
  - https://news.ycombinator.com/item?id=46404127, 27 dec. 2025 (cineva care construiește un tool, nu un utilizator): „Photographers upload 1000+ images, ML clusters similar shots so clients can pick favorites faster”
  - https://www.capterra.com/p/10012022/Aftershoot/, dată nevizibilă (pagină de preț, nu se numără ca dovadă a problemei): „Starting price $ 9.99 Per User, Per Month”
- Doar fragment: G2 Aftershoot (recenzii despre AI care „occasionally keeps too many similar shots”), FilterPixel și Imagen (bloguri ale vendorilor, cu estimări de 4-6 ore pentru o nuntă de 3.000-4.000 de cadre), Photofocus „Aftershoot 2026 review”, ca.trustpilot.com Aftershoot.

## Problema 2: Găsirea și logarea cadrelor potrivite în ore întregi de filmare brută (footage), pentru editori video
- Cine o are: editori video freelanceri, documentariști, editori de nunți și evenimente care lucrează cu arhive locale mari.
- Cât de des apare: la fiecare proiect cu material mult. Un dezvoltator descrie arhive de „500GB+” prin care editorii caută manual. Nu am găsit o cifră independentă de frecvență.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: derulează manual materialul; transcrie în Premiere, exportă transcrierea, o lipește în ChatGPT împreună cu un cadru static și cere note de logare, clip cu clip (flux descris ca „clunky”, pentru că se face în afara Premiere). Timp: „hours manually scrubbing” (formularea dezvoltatorului RushShift; nu am găsit o măsurătoare independentă).
- Soluții existente găsite, cu preț: Jumper (căutare vizuală locală, plugin pentru Premiere/Resolve/Avid/Final Cut; licență lifetime sau abonament, dar suma nu apare în textul paginii); RushShift (lansat pe HN în sept. 2026, preț negăsit); căutarea Media Intelligence din Premiere (preț negăsit în surse deschise din interval). Eddie AI, Reduct, Transcriptive și Selects au apărut doar în fragmente.
- Surse deschise:
  - https://community.adobe.com/questions-729/ai-assisted-documentary-logging-in-premiere-is-anyone-integrating-chatgpt-or-other-tools-directly-into-workflow-1554329, 19 mar. 2026: „obviously the workflow is clunky because it lives outside Premiere”
  - https://news.ycombinator.com/item?id=49844088, 25 sept. 2026 („50 days ago” la deschidere; autorul își prezintă propriul produs): „Editors spend hours manually scrubbing through 500GB+ folders looking for specific shots”
  - https://news.ycombinator.com/item?id=44426396, 30 iun. 2025 (autorul își prezintă propriul produs): „a tool for video editors to do visual search on their footage”
  - https://getjumper.io/pricing, dată nevizibilă (pagină de preț, nu se numără): „Local AI video search for professional editors.”
- Doar fragment: firele Adobe despre panoul de căutare vizuală din Premiere (deschise, dar postările sunt din dec. 2024 - apr. 2025, deci în afara intervalului de 18 luni: utilizatorii cereau căutare pe bin/secvență și se plângeau de rezultate duplicate); cined.com și provideocoalition despre Eddie AI (NAB 2026); reduct.video; nofilmschool.com „Let AI log and organize footage”.

## Problema 3: Software-ul all-in-one pentru clienți (CRM, contracte, facturi) e prea scump sau prea greu de configurat pentru creativii care lucrează singuri
- Cine o are: fotografi, designeri grafici și de brand, editori video și mici agenții creative care folosesc HoneyBook sau Dubsado pentru oferte, contracte, facturi și automatizări.
- Cât de des apare: e o cheltuială lunară sau anuală recurentă. Pe paginile Capterra ale HoneyBook (paginile 2-3), prețul apare des ca principal minus în recenziile din 2025-2026. Nu am numărat sistematic toate recenziile.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: plătește abonamentul (în jur de 40 USD/lună pentru intrare la HoneyBook, după un designer grafic; Dubsado a urcat de la 200 la peste 300 USD/an, după o proprietară de agenție creativă); renunță după trial; rămâne blocat din cauza efortului de migrare („switching to another service became too much of a hassle”); sau își construiește singur sistemul în Notion + Typeform (recenzie Capterra HoneyBook, pagina 3, dată nevizibilă lângă text, deci nu o număr). Configurarea Dubsado e descrisă ca o curbă de învățare abruptă.
- Soluții existente găsite, cu preț: HoneyBook (cam 40 USD/lună la nivelul de intrare, conform unei recenzii Capterra din mar. 2026; prețurile oficiale pe planuri le-am văzut doar în fragmente de pe bloguri: 36/59/129 USD pe lună după scumpirea din feb. 2025); Dubsado (peste 300 USD/an pentru nivelul de bază, peste 500 USD/an pentru altele, conform unei recenzii Capterra din nov. 2026). Pixieset, Studio Ninja și 17hats au apărut doar ca alternative în fragmente.
- Surse deschise:
  - https://www.capterra.com/p/162588/HoneyBook/reviews/?page=2, 17 mar. 2026 (Ryan P., Graphic Designer): „the barrier to entry is around $40 a month”
  - https://www.capterra.com/p/162588/HoneyBook/reviews/?page=2, 27 aug. 2025 (Head Photographer and Owner; același site și aceeași pagină ca sursa de mai sus, autor diferit): „The thing that caused us to not be able do so was price”
  - https://capterra.com/p/206389/Dubsado/reviews/, 13 nov. 2026 (Isabelle D., Creative Agency Owner): „Going from $200 USD a year to over $300”
  - https://capterra.com/p/206389/Dubsado/reviews/, 6 nov. 2025 (Paola S., Owner, Video Editor, Content Producer): „Some of the features are clunky like scheduling, form design”
  - https://community.honeybook.com/business-talk-46/disappointed-by-recent-price-hikes-a-tough-blow-for-small-businesses-4320 și https://community.honeybook.com/money-talk-143/honeybook-your-direct-competitors-have-begun-taking-your-users-4068: deschise, dar datate 21 ian. 2025 și 12-17 dec. 2024, deci în afara intervalului. Nu le număr.
- Doar fragment: fstoppers.com „HoneyBook's Price Hike Is Coming” (dată nevizibilă în fragment); agiled.app „HoneyBook Review 2026” (preț 19→36 USD); prospeo.io (migrare spre Pixieset); the-runaway-club.beehiiv.com (blocat).

## Problema 4: Facturi întârziate sau neplătite și urmărirea manuală a plăților de la clienți
- Cine o are: freelanceri creativi care predau lucrarea înainte de plată (sursele deschise acoperă creativi în general, din UK, și o makeup artist; nu am găsit o sursă deschisă din interval scrisă strict de un fotograf, designer sau editor video).
- Cât de des apare: un articol pentru creativi spune că întârzierile sunt „common in creative work”. O freelancer creativă avea în aceeași săptămână o factură întârziată cu 66 de zile și alta cu aproape 160. Statistici generale (29% din facturi plătite cu întârziere, analiza Bonsai) am văzut doar în fragmente.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: trimite manual mementouri pe o scară de escaladare (înainte de scadență, la 1-7 zile, la 2-3 săptămâni), sună, adaugă dobândă legală (în UK, 8% peste rata de bază a Băncii Angliei, plus o compensație fixă de 40/70/100 GBP), merge la small claims, sau plătește pe altcineva să urmărească plățile („Pay a fellow freelancer or a no-nonsense friend to chase your payments twice a month”). Timp: nu am găsit o cifră în surse.
- Soluții existente găsite, cu preț: mementourile automate din CRM-urile HoneyBook/Dubsado (prețurile sunt la Problema 3); calculatorul de dobândă legală din UK, menționat în articolul Creative Lives in Progress (gratuit, nu l-am deschis). Bonsai, Moxie și ruul.io au apărut doar în fragmente.
- Surse deschise:
  - https://creativelivesinprogress.com/articles/chase-late-payment-uk-small-claims-interest, 28 apr. 2026: „Late payments are common in creative work”
  - https://ciaradoesmakeup.substack.com/p/booked-busy-and-broke-the-dark-side, 5 iun. 2025 (makeup artist freelancer, domeniu creativ apropiat, nu design/foto/video): „This week, I chased a client who’s now 66 days overdue.”
- Doar fragment: webdesignerforum.co.uk „Are late payments an issue for you?” (deschis, dar conținutul firului nu s-a încărcat); indiehackers.com „Why freelancers get paid late” (blocat); jobbers.io „Freelance invoice non-payment report 2026” (403); wall-street.ro și financialintelligence.ro despre Legea 72/2013 și termenul mediu de plată B2B de 144 de zile din România (ICAP CRIF, 2025).

## Surse blocate
- reddit.com (pagina r/freelance a întors HTTP 200, dar fără conținut: doar „Reddit”, 6 caractere)
- g2.com (403)
- trustpilot.com (403, blocare anti-bot)
- upwork.com (403, Cloudflare)
- producthunt.com (403, „Just a moment...”)
- fiverr.com (403, „It needs a human touch”)
- dpreview.com/forums (403, Cloudflare)
- fredmiranda.com forum (403, Cloudflare)
- indiehackers.com (403, Cloudflare)
- creativecow.net/forums (403, „Security Verification”)
- quora.com (403, Cloudflare)
- weddingwire.com forum (403, Access Denied)
- aftershoot.com/pricing (403, Cloudflare)
- jobbers.io (403)
- the-runaway-club.beehiiv.com (403, Cloudflare)
- Notă: am deschis capterra.com, community.adobe.com, news.ycombinator.com (și API-ul oficial de căutare hn.algolia.com), community.honeybook.com, liftgammagain.com, fstoppers.com (doar pagina principală), graphicdesign.stackexchange.com (doar pagina principală), wordpress.org (doar pagina principală). N-am folosit mirror-uri Reddit, deși au apărut în căutări.

## Căutări făcute
- WebSearch: „Aftershoot culling review problems 2026”
- WebSearch: „photographer forum culling takes hours wedding 2025”
- WebSearch: „HoneyBook price increase photographers alternative 2025 forum”
- WebSearch: „capterra HoneyBook reviews”
- WebSearch: „"is there a tool" client feedback revisions designers email chaos 2025”
- WebSearch: „video editor forum search hours of footage find clips transcript tool 2025 liftgammagain OR creativecow”
- WebSearch: „capterra.com Aftershoot reviews”
- WebSearch: „community.adobe.com Lightroom culling thousands of photos slow 2025”
- WebSearch: „community.adobe.com Premiere Pro find clip in hundreds of hours footage search visual 2026”
- WebSearch: „liftgammagain OR "creativecow" editors logging footage tedious assistant editor AI 2026”
- WebSearch: „photographers client gallery storage cost price increase Pixieset Pic-Time ShootProof complaint 2026” (fără dovezi utile din interval; direcție abandonată)
- WebSearch: „freelance designer clients not paying invoices chasing payment forum 2026”
- WebSearch: „photographer found my photos used without permission Pixsy Copytrack review 2025 forum” (singura recenzie critică deschisă, livingthedreamrtw.com despre Copytrack, era din 2022; direcție abandonată)
- WebSearch: „community.honeybook.com price increase 2026 photographer leaving”
- WebSearch: „fstoppers HoneyBook price hike photographers”
- WebSearch: „capterra Dubsado reviews”
- WebSearch: „Frame.io V4 complaints freelancers client review price storage 2025 2026 forum” (rezultatele relevante erau mirror-uri Reddit, neutilizate; direcție abandonată)
- WebSearch (RO): „fotograf nunta selectie poze dureaza ore forum 2025” (doar articole de presă despre prețuri, fără forum)
- WebSearch (RO): „designer freelancer client nu plătește factura ce fac forum România 2025” (fără fir de forum relevant)
- API-ul oficial de căutare Hacker News (hn.algolia.com), comentarii după 15.05.2025: „culling photos”, „photographer stolen photos copyright”, „freelance designer client revisions” (0 rezultate), „video editor footage search”
- Pagini deschise direct: firul Adobe Assisted Culling (index4), firul Adobe despre logarea documentarelor, firele Adobe despre căutarea vizuală din Premiere (index, index1, index2), Capterra HoneyBook (paginile 2 și 3), Capterra Dubsado, Capterra Aftershoot, firele HoneyBook Community (2), itemii HN 47761911, 46404127, 49844088, 44426396, getjumper.io/pricing, creativelivesinprogress.com, ciaradoesmakeup.substack.com, production-expert.com (despre freelanceri audio; conținutul articolului nu s-a extras), webdesignerforum.co.uk (conținutul firului nu s-a încărcat)
