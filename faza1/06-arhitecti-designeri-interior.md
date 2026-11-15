# Domeniu: 06 arhitecți și designeri de interior

## Problema 1: Desenarea releveului (existentului) din planuri vechi scanate, PDF-uri sau scanări Matterport e lentă și manuală
- Cine o are: proiectanți rezidențiali și designeri care lucrează la renovări sau extinderi și pornesc de la planuri vechi pe hârtie, PDF-uri scanate sau scheme Matterport (utilizatori Chief Architect, AutoCAD).
- Cât de des apare: nu am găsit în surse o frecvență măsurată. În fereastra de 18 luni am găsit 3 fire distincte, pe 2 forumuri (ChiefTalk, CADTutor).
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: importă scanarea în programul CAD și redesenează peste ea, de mână. Un utilizator a încercat de mai multe ori („So far I have tried 2+ different attempts at the as-built”, ChiefTalk, 2025-08-28). Altul caută pe cineva plătit care să-i facă fișierul, iar un membru al forumului îl avertizează că „it could get expensive” (ChiefTalk, 2025-10-23). La CADTutor, alții convertesc PDF-ul vectorial, apoi aliniază manual entitățile pe o grilă. Pentru PDF-urile scanate, conversia nu funcționează. Nu am găsit în surse sume concrete.
- Soluții existente găsite, cu preț:
  - Ideatura: AI care redesenează în AutoCAD un plan pornind de la o captură de ecran. E în beta, după postarea din 2026-09-28 de pe CADTutor. Preț: nu am găsit în surse.
  - Houzz Pro: scanare a camerei cu iPhone-ul. Capterra afișează un preț de pornire de 399 $ pe lună, tarif fix. Un antreprenor scrie că „the scanning tool worked 10% of the time” (Capterra, 2025-07-24).
  - Scan2CAD: pagina de prețuri s-a deschis, dar prețul nu era vizibil în text. Preț: nu am găsit în surse.
  - Matterport: pagina de prețuri a întors 404. Preț: nu am găsit în surse.
  - Freelanceri pe Fiverr („convert PDF floor plan to AutoCAD”, de la circa 50 $): doar fragment, pentru că Fiverr e blocat.
- Surse deschise:
  - https://chieftalk.chiefarchitect.com/topic/47278-creating-an-as-built-of-a-multi-stepped-foundation-on-a-hill/ — 2025-08-28 — „We scanned the original blueprints, which I imported into Chief to draw off of.”
  - https://chieftalk.chiefarchitect.com/topic/47611-importing-cad-matterport-schematic-plan-into-chief-architect/ — 2025-10-22 — „I’m having trouble getting the data imported correctly into Chief Architect”
  - https://www.cadtutor.net/forum/topic/99332-ai-recreating-a-floor-plan-screenshot-in-autocad-feedback-welcome/ — răspuns din 2026-09-29 (firul a început pe 2026-09-28) — „Our biggest problem is historic records - scanned paper copies originally drawn in pen and ink”
  - Context deschis, dar în afara ferestrei de 18 luni (nu se numără): https://chieftalk.chiefarchitect.com/topic/45829-seeking-chief-drafter-for-a-7000-sq-ft-as-built/ — 2025-04-21 — „I’m looking to hire an experienced Chief Architect user to draft a detailed as-built”. https://chieftalk.chiefarchitect.com/topic/41463-imported-pdf-to-lines/ — 2024-03-04.
  - Context cu dată nevizibilă (nu se numără): https://forums.sketchup.com/t/translating-pdf-into-dwg-for-import/204601 — e din 2022, deci în afara ferestrei.
- Doar fragment: anunțuri Fiverr pentru conversie PDF→DWG (de exemplu fiverr.com/plantocadstudio/convert-pdf-or-image-floor-plan-to-autocad-drawing, „$50 … 1 day”); FloorAI (hunted.space), „turns floor plan images, scans, and PDFs into editable DXF”; pagini Scan2CAD despre conversia raster→vector.

## Problema 2: Randările AI modifică arhitectura, materialele și culorile proiectului și nu dau rezultate repetabile
- Cine o are: arhitecți, proiectanți rezidențiali și designeri care vor randări fotorealiste rapide pentru clienți, pornind din SketchUp sau Chief Architect.
- Cât de des apare: nu am găsit în surse o frecvență măsurată. În fereastră am găsit 4 fire distincte, pe 2 forumuri (SketchUp Community, ChiefTalk). Pagina de tag „diffusion” de pe forumul SketchUp mai listează și alte fire din 2025 și 2026.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp:
  - Randează o dată cu AI, apoi o dată fără clădire, și le combină în Photoshop („5 minute Photoshop merge”, forum SketchUp, 2025-08-11).
  - Scrie prompturi negative de tipul „do not change the materials or architecture” în ChatGPT sau Gemini (ChiefTalk, 2026-02-23). Corectează apoi în post-procesare.
  - Varianta clasică, cu motor de randare, ar dura „hours and hours”, după ChiefTalk (2026-04-23).
- Soluții existente găsite, cu preț: SketchUp Diffusion / AI Render (inclus în SketchUp; pagina de prețuri s-a deschis, dar prețul nu era vizibil în text), ChatGPT, Gemini, Copilot, Krea AI, Adobe Firefly, D5 Render, Twinmotion, SoftPlan cu AI integrat. Toate sunt numite în firele ChiefTalk. Prețuri: nu am găsit în surse; pagina de prețuri D5 e blocată (403).
- Surse deschise:
  - https://forums.sketchup.com/t/so-close-to-being-great/337116 — postare din 2025-08-04 (firul a început pe 2025-08-03) — „It always modifies the building in ways I do not want it to.”
  - https://forums.sketchup.com/t/diffusion-wont-keep-colors-textures/339232 — 2025-08-21 — „Unfortunately, Diffusion always mucks with the color palette even when prompted not to.”
  - https://chieftalk.chiefarchitect.com/topic/48358-are-we-getting-built-in-ai-render-in-chief-anytime-soon-softplan-has-it-already/ — 2026-02-23 — „And yes, it still changed parts of the building.” Din același fir, tot pe 2026-02-23: „We. Need. Repeatable. Results.”
  - https://chieftalk.chiefarchitect.com/topic/48824-ai-llm-good-rendering-prompts/ — 2026-04-23 — „even with the help of TwinMotion would take hours and hours and never come close”
  - https://forums.sketchup.com/t/diffusion-no-longer-works-as-before-version-version-1-2025-9-28/340921 — 2025-10-10 — „Why is the result so different?”
- Doar fragment: VizBase (blog de vendor, martie 2026), după care designerii se plâng că tool-ul înlocuiește materialele specificate. Learnarchitecture.net, despre un client care a cerut AI-ului să modifice un element din randare și a primit un rezultat fără sens arhitectural. Ghidul de randare AI Luma (2026).

## Problema 3: Listele de produse (FF&E) cer introducere și actualizare manuală: clipper-e instabile, prețuri neactualizate, dubluri, status comenzi neurmărit
- Cine o are: designeri de interior, mai ales solo sau în studiouri mici, care fac selecții de mobilier și finisaje, bugete și comenzi pentru clienți.
- Cât de des apare: nu am găsit în surse o frecvență măsurată. Am găsit 5 recenzii Capterra din fereastră, de la autori diferiți, la 2 produse diferite (DesignFiles și Programa). Pe Gumroad se vând șabloane Excel și Notion pentru urmărirea selecțiilor și a comenzilor.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp:
  - Copiază produsele de pe site-uri cu un web clipper, apoi le introduce a doua oară în moodboard („I have to do it twice”, Capterra, 2025-10-29).
  - Urmărește comenzile separat, pentru că software-ul nu preia numărul de comandă sau de tracking (Capterra, 2025-10-27).
  - Ține prețurile la zi manual, pentru că „furniture sourcing doesn’t update automatically” (Capterra, 2025-06-30).
  - Timp sau bani pierduți: nu am găsit în surse cifre.
- Soluții existente găsite, cu preț:
  - DesignFiles: de la 35 $ pe lună, tarif fix (Capterra).
  - Houzz Pro: de la 399 $ pe lună, tarif fix (Capterra).
  - Programa: „Contact vendor” (Capterra).
  - Studio Designer: de la 54 € de utilizator pe lună (Capterra).
  - Șablon Gumroad „Interior Design Sourcing Tracker”: 9,99 $, data nu e vizibilă, 1 vânzare afișată.
  - Șablon Gumroad „Product & Material Selection tracker” (Excel, include „order progress tracker”): 14,99 $, data nu e vizibilă.
- Surse deschise:
  - https://www.capterra.com/p/179202/DesignFiles/reviews/ — 2025-06-30, 1 stea — „Furniture sourcing doesn’t update automatically, creating unnecessary headaches.”
  - https://www.capterra.com/p/248518/Programa/reviews/?page=2 — 2025-10-24 — „also sometime the web clipper is a bit glitchy”
  - https://www.capterra.com/p/248518/Programa/reviews/ — 2025-10-29, 4 stele — „photos and links I import into the schedule could be automatically added”
  - https://www.capterra.com/p/248518/Programa/reviews/ — 2025-10-29, 5 stele — „Not being able to tell if I'm doubling up in the product library”
  - https://www.capterra.com/p/248518/Programa/reviews/?page=2 — 2025-10-27 — „If we were able to enter an order number or tracking number”
  - https://www.capterra.com/p/248518/Programa/reviews/?page=2 — 2025-10-24, 4 stele — „the inability to share the purchase status with clients”
  - Notă despre independență: recenziile Programa sunt de la autori diferiți, dar toate au fost postate între 24 și 29 octombrie 2025 și pot face parte dintr-o campanie de recenzii a vendorului. Sursa independentă de ele e recenzia DesignFiles.
- Doar fragment:
  - Specsources (blog de vendor, mai 2026) dă linkurile moarte și prețurile neactualizate drept erori frecvente în specificațiile făcute manual.
  - Pagina Fohlio afirmă completarea automată din URL; prețul de 99 $ de utilizator pe lună apare doar în fragment.
  - Listări Etsy cu șabloane FF&E (4–40 $): Etsy e blocat.

## Problema 4: Firmele mici de arhitectură nu găsesc un singur tool pentru pontaj, onorarii, facturare și managementul proiectelor; lucrează cu mai multe aplicații și introduc datele de două ori
- Cine o are: birouri de arhitectură mici și mijlocii (de la 4 la 20 de persoane în surse) care țin contabilitatea în QuickBooks.
- Cât de des apare: nu am găsit în surse o frecvență măsurată. Am găsit 1 fir AIA din 2026 cu mai mulți respondenți și 2 recenzii Capterra din fereastră.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp:
  - Combină aplicații, de exemplu Monograph pentru facturare cu sincronizare în QuickBooks Online, plus suport plătit (AIA, 2026-06-10). Alternativa e „I need to subscribe to other tools to make it complete” (Capterra, 2025-07-25).
  - Schimbă aplicația când una nu funcționează, ca ArchiOffice → BQE Core → Monograph (AIA, 2026-06-09). Un recenzent se întoarce la sistemul vechi după ce a pierdut „a ton of our time and energy” (Capterra, 2026-03-10).
  - Sume concrete: nu am găsit în surse.
- Soluții existente găsite, cu preț: Monograph („Contact vendor” pe Capterra), BQE Core, Factor, Deltek Ajera, QuickBooks Online (numite în firul AIA). Prețuri: nu am găsit în surse. Prețul Monograph Pro de 19 $ pe loc apare doar în fragment.
- Surse deschise:
  - https://communityhub.aia.org/discussion/software-for-accountingproject-tracking-1 — 2026-06-09 — „we had as many issues with it as we had benefits”. Postarea inițială, din 2026-05-28: „evaluating BQE Core for both accounting and project tracking”
  - https://www.capterra.com/p/178124/Monograph/reviews/ — 2026-03-10, 1 stea — „We wanted more integration of project management, time tracking, and invoicing.”
  - https://www.capterra.com/p/178124/Monograph/reviews/ — 2025-07-25, 4 stele — „The fact that I need to subscribe to other tools to make it complete.”
  - Context deschis, dar în afara ferestrei (nu se numără): https://communityhub.aia.org/discussion/project-management-and-crm-software-for-architects — 2025-03-03 — „hoping this would help eliminate duplicate entry of information”
  - Context cu dată nevizibilă (nu se numără): https://archinect.com/forum/thread/150198677/project-management-and-project-financial-software/0 — „everything seems to do one really well”
- Doar fragment: articolele Monograph și Noloco care compară Harvest, BQE și Factor (bloguri de vendor). Pentru firmele foarte mici, Noloco spune că urmărirea onorariilor „stays in a spreadsheet”.

## Surse blocate
- reddit.com: HTTP 200, dar pagina e goală (doar „Reddit”).
- g2.com: 403
- trustpilot.com: 403, cerere identificată ca bot
- upwork.com: 403, Cloudflare
- producthunt.com: 403, „Just a moment”
- fiverr.com: 403, verificare anti-bot („It needs a human touch”)
- quora.com: 403
- indiehackers.com: 403
- forums.autodesk.com: 403, „Just a moment”
- thebuildingcodeforum.com: 403
- etsy.com: 403
- apps.apple.com: 429
- forum.softpedia.com: 403
- capital.ro: 429
- d5render.com/pricing: 403
- Nu e blocat, dar nu am putut folosi: archinect.com se deschide (HTTP 200), însă firele de forum nu afișează data, deci nu le-am numărat. matterport.com/pricing a întors 404.

## Căutări făcute
- WebSearch: „interior designer forum "is there a tool" FF&E schedule spreadsheet 2025”
- WebSearch: „reddit r/InteriorDesign software for client proposals sourcing tracking frustrated 2025”
- WebSearch: „Houzz Pro review 1 star capterra 2025 interior designer”
- WebSearch: „archinect forum software small architecture firm fee proposal time tracking 2025”
- WebSearch: „Studio Designer reviews capterra cons purchase orders tracking interior design 2025”
- WebSearch: „Programa interior design software reviews capterra cons clipper”
- WebSearch: „capterra Mydoma Studio reviews”; „capterra Fohlio reviews interior design specification”; „capterra Monograph architecture reviews”
- WebSearch: „forums.sketchup.com convert pdf floor plan to sketchup model 2025”; „site:forums.sketchup.com pdf import trace floor plan 2025”
- WebSearch: „fiverr convert pdf floor plan to autocad dwg gig”
- WebSearch: „forums.autodesk.com convert scanned pdf floor plan to dwg 2025 raster”; „site:forums.autodesk.com pdf to dwg conversion lines broken AutoCAD 2026”
- WebSearch: „site:news.ycombinator.com architect "floor plan" pdf to CAD AI”
- WebSearch: „site:cadtutor.net pdf to dwg scanned drawing convert 2025”; „site:forum.vectorworks.net import pdf convert to lines scanned plans 2025”
- WebSearch: „chieftalk 2025 pdf plans convert trace existing house as-built”
- WebSearch: „forums.sketchup.com SketchUp Diffusion AI render changes geometry disappointed”; „"Diffusion Won't Keep Colors/Textures" sketchup”
- WebSearch: „AI rendering architecture tool ignores my design changes materials forum 2026 architects complain render”
- WebSearch: „chieftalk houzz pro leads worth it designers 2025”; „chieftalk client keeps asking revisions changes billing hourly scope creep 2025”
- WebSearch: „communityhub.aia.org discussion small firm software fee proposal 2026”; „communityhub.aia.org discussion AI tool code research permit 2025”; „communityhub.aia.org upcodes code research subscription”; „communityhub.aia.org specifications writing small firm spec tool expensive 2025 2026”
- WebSearch: „chieftalk plan review comments permit rejected corrections building department 2026”; „architect forum code research takes hours which code edition applies jurisdiction amendments tool 2025”; „news.ycombinator.com Show HN building code AI architects permit compliance”
- WebSearch: „news.ycombinator.com "interior designers" sourcing furniture spreadsheet Show HN”; „"interior designer" "is there a tool" OR "is there an app" product links spec sheet clients 2026”
- WebSearch: „interior design procurement tracker template etsy order tracking spreadsheet designers”
- WebSearch (RO): „forum arhitect designer interior program randare clienti "există un program" 2025”: doar bloguri de vendori și fire Softpedia din 2006–2008.
- WebSearch (RO): „arhitecți România birocrație autorizație de construire documentație timp pierdut 2026 OAR”: am deschis articolul Revista Biz (FIDES, despre OUG 31/2025), dar e despre dezvoltatori, nu despre arhitecți ca firme, iar data articolului nu e clară. capital.ro a fost blocat (429). Nu am construit o problemă din asta.
- Pagini citite direct (citeste.sh), pe lângă sursele de mai sus: recenziile Capterra Houzz Pro (paginile 1–12), DesignFiles (paginile 1–8), Programa (paginile 1–3), Mydoma Studio (paginile 1–3, fără recenzii din fereastră), Monograph (paginile 1–4), Studio Designer; paginile de produs Capterra pentru prețuri; produse Gumroad; firele AIA Community Hub despre AI și despre AHJ; firele Archinect despre coduri (fără dată vizibilă).
- Teme căutate, dar nu au ajuns în fișier din lipsă de 2 surse valide în fereastră:
  - Lead-uri slabe de pe platforme plătite (Houzz) pentru arhitecți: o singură recenzie de arhitect din fereastră (Capterra, 2025-06-02); firul AIA e din 2024 și martie 2025.
  - Cercetarea codurilor de construcție cu AI: un singur fir valid (AIA, 2026-02-03, „the content was not 100% accurate”); firele Archinect nu au dată, iar Building Code Forum e blocat.
