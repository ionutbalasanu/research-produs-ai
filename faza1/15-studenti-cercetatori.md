# Domeniu: Studenți și cercetători

## Problema 1: Referințele bibliografice inventate de AI trebuie verificate manual, una câte una
- Cine o are: studenți la licență, master și doctorat care folosesc ChatGPT sau alte LLM-uri ca să găsească surse; recenzenți și coautori de articole științifice.
- Cât de des apare: un utilizator scrie că a primit referințe neverificabile de la primul prompt (community.openai.com, iul. 2026). Un fir de pe Physics Forums (apr.–oct. 2026, 13 răspunsuri, 7K vizualizări pe pagină) discută referințele „halucinate” din literatura științifică. The Decoder (mar. 2026) relatează că astfel de referințe au trecut de peer review la conferințe AI mari (NeurIPS, ACL). Nu am găsit în surse deschise o frecvență măsurată pentru studenți.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: caută manual fiecare referință. Utilizatorul de pe forumul OpenAI spune că asta l-a costat „significant time”. Pe forumul OpenAI, moderatorii recomandă verificarea manuală a fiecărei surse, una câte una. Un utilizator Physics Forums spune că a descoperit abia după o săptămână că o referință nu exista. Nu am găsit în surse costul în bani.
- Soluții existente găsite, cu preț: CiteAudit, aplicație web gratuită după înscriere cu e-mail, până la 500 de citări pe zi; peste limită folosești propria cheie API Gemini (the-decoder.com, deschis). Paperpal Reference Checker, check-hallucinations (PyPI), CheckIfExist și TrueCite (WisPaper) apar doar în fragmente de căutare; preț: nu am găsit în surse.
- Surse deschise:
  - https://community.openai.com/t/chatgpt-generated-unverified-academic-references-despite-explicit-instructions/1387692, 21 iulie 2026, „this cost me significant time because I had to manually check every citation”
  - https://www.physicsforums.com/posts/7318738/, 9 august 2026 (postarea #9 dintr-un fir început pe 21 aprilie 2026), „lo and behold, it it didn't exist”
  - https://the-decoder.com/hallucinated-references-are-passing-peer-review-at-top-ai-conferences-and-a-new-open-tool-wants-to-fix-that/, 8 martie 2026, „reference lists have ballooned over the years, making manual checking unrealistic for reviewers and co-authors”
- Doar fragment: arXiv 2602.15871 (CheckIfExist); casrai.org despre ce pot și ce nu pot face detectoarele de citări „halucinate” (2026); o analiză Nature citată în fragmente (2,6% dintre articolele din 2025 ar avea cel puțin o citare posibil halucinată, față de aproximativ 0,3% în 2024); GPTZero cu peste 50 de referințe halucinate în trimiterile la ICLR 2026 (cifră care apare și în articolul The Decoder, deschis); pypi.org/project/check-hallucinations; editage.com, ghid de verificare.

## Problema 2: Studenți semnalați fals de detectoarele AI (Turnitin) care trebuie să-și dovedească singuri nevinovăția
- Cine o are: studenți (inclusiv cei care folosesc doar corectura Grammarly) și profesori care trebuie să interpreteze scorul.
- Cât de des apare: un profesor de pe forumul Turnitin spune că „majoritatea” studenților cu care a discutat sunt șocați de scorul AI primit. Turnitin declară pe același forum o rată de rezultate fals pozitive sub 1%. Dataconomy (oct. 2025) relatează că, la Australian Catholic University, aproximativ un sfert din cazurile trimise spre investigare au fost respinse.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: studenții adună notițe scrise de mână și tastate, „dozens of pages”, plus istoricul complet de căutare pe internet (dataconomy). Pentru o studentă la nursing, investigația a durat 6 luni, timp în care foaia matricolă a purtat mențiunea „results withheld”, iar ea spune că a pierdut astfel un post de absolvent (dataconomy). Turnitin le recomandă profesorilor discuții cu studenții, fișe de reflecție și verificarea ciornelor (forumul Turnitin).
- Soluții existente găsite, cu preț: Grammarly Authorship înregistrează procesul de scriere în Word, Google Docs sau Grammarly Editor și generează un raport pe care studentul îl poate arăta. Pagina indică „Sign up It's free”; nu am găsit în surse prețul pentru planurile plătite.
- Surse deschise:
  - https://turnitin.forumbee.com/t/83ypqga, aproximativ decembrie 2025 (pagina afișează „11 mths ago”, într-un eveniment de pe forum care s-a desfășurat între 20 nov. și 20 dec. 2025), „students I’ve spoken to are shocked that the AI score they have is as high”
  - https://dataconomy.com/2025/10/13/how-a-universitys-ai-witch-hunt-derailed-a-students-career/, 13 octombrie 2025, „almost my entire essay was lit up in blue — 84 per cent”
  - https://www.grammarly.com/authorship (pagina soluției; dată nevizibilă, nu se numără ca dovadă a problemei), „AI detectors only guess from the final draft.”
- Doar fragment: spectrumlocalnews.com, caz de la University at Buffalo (14 mai 2025, în afara intervalului); popularai.org, „Turnitin false positives are a bigger problem than schools admit”; firul r/slatestarcodex din aprilie 2025 (apare doar prin oglinzi, nedeschis și în afara intervalului); workingeducators.org, cu o rată de rezultate fals pozitive de 31% la studenții ESL (testarea unui singur site). Articolul dailydot.com despre Grammarly și Turnitin a fost deschis, dar e din 3 iunie 2024, deci în afara intervalului; nu se numără.

## Problema 3: Software-ul de analiză calitativă (NVivo, ATLAS.ti) e greu de învățat, instabil și scump pentru doctoranzi
- Cine o are: doctoranzi și cercetători care codifică transcrieri de interviuri; coordonatori și profesori care îi ajută pe studenți cu programul.
- Cât de des apare: pe pagina Capterra a NVivo am găsit 3 recenzii de 1–3 stele din ultimele 13 luni (oct. 2025, apr. 2026, iul. 2026); pe Capterra UK, la ATLAS.ti, o recenzie de 3 stele din mar. 2026. Nu am găsit în surse o frecvență mai largă.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: învață programul din tutoriale („Requires A LOT of training. Training videos are not helpful.”, doctorand, apr. 2026). O echipă care a lucrat cu NVivo Collaboration Cloud descrie soluții manuale de ocolire și sincronizări repetate care au costat ore. Un profesor (recenzie fără dată vizibilă) spune că petrece mai mult timp depanând decât codificând. Costul în bani: nu am găsit în surse deschise o cifră datată.
- Soluții existente găsite, cu preț: NVivo, ATLAS.ti și MAXQDA (recenziile MAXQDA de pe Capterra din 2025–2026 sunt de 5 stele). Preț: nu am găsit în surse deschise. Fragmentele de căutare indică NVivo Project la 1.100 $ (licență perpetuă) și ATLAS.ti de la 10 $/lună (doar fragment).
- Surse deschise:
  - https://capterra.com/p/171501/NVivo/reviews/, 9 aprilie 2026 (Doctoral Candidate, 2/5), „Software is extremely hard to use as a novice. Not user friendly at all.”
  - https://capterra.com/p/171501/NVivo/reviews/, 19 iulie 2026 (Doctoral Writing Coach, 3/5), „often the students tasks with using the program do not have enough time”
  - https://capterra.com/p/171501/NVivo/reviews/, 30 octombrie 2025 (Assistant Professor, 1/5), „our team lost hours we can’t get back”
  - https://www.capterra.co.uk/reviews/171500/atlas-ti, 10 martie 2026 (cercetător, învățământ superior, 3/5), „the cloud, file management, backup, and user interface are horrible”
- Doar fragment: ratingul general NVivo pe Capterra (3,8 din aprox. 50 de recenzii, Customer Service 2,8); recenzii NVivo pe G2 și TrustRadius despre lentoare și suport slab; usercall.co, ghid „Best Thematic Analysis Tool for Dissertations in 2026” (vendor); lennartnacke.substack.com, care spune că AI-ul procesează în scurt timp transcrieri pentru care ar fi nevoie de săptămâni (afirmație nemăsurată). Recenzia ATLAS.ti despre transcriere „terrible, frustrating, slow” e din 8 mai 2025, în afara intervalului. Recenzia MAXQDA despre transcrierea neinclusă în pachetul pentru studenți e din 27 februarie 2025, în afara intervalului.

## Problema 4: Pluginurile de citare pentru Word (Zotero, Mendeley Cite) se strică în documente mari de teză, aproape de termen
- Cine o are: studenți și doctoranzi care își scriu teza în Microsoft Word cu citări gestionate prin Zotero sau Mendeley.
- Cât de des apare: pe forumul Zotero apar mai multe fire separate despre pluginul de Word stricat în iunie–septembrie 2026 (de exemplu „Creating bibliography doesn't work”, 10 și 16 iunie 2026; „Word could not communicate with Zotero”, 30 iunie 2026; „Word repeatedly crashing”, 17 august 2026, toate văzute pe paginile forumului). Elsevier confirmă o problemă generală la Mendeley Cite, cauzată de o actualizare Microsoft Office (pagină actualizată pe 20 februarie 2026).
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: reinstalează pluginul, șterge Zotero.dotm, dezactivează antivirusul, mută documentul din OneDrive sau copiază tot conținutul într-un document nou. Un doctorand cu o teză de peste 400 de pagini se temea că va trebui să reinsereze manual aproape 1.000 de citări. O altă utilizatoare a pierdut muncă nesalvată din cauza blocărilor. Elsevier recomandă actualizarea Office.
- Soluții existente găsite, cu preț: Zotero și Mendeley sunt chiar instrumentele afectate; prețul lor: nu am găsit în surse. Nu am găsit o soluție dedicată reparării documentelor cu citări stricate.
- Surse deschise:
  - https://forums.zotero.org/discussion/132473/, 30 iunie 2026, „thesis document which contains almost a thousand existing citations across more than 400 pages”
  - https://forums.zotero.org/discussion/133241/, 17 august 2026, „I'm working against a deadline and have already lost some unsaved work”
  - https://www.elsevier.support/mendeley/answer/why-does-mendeley-cite-say-there-are-no-citations-in-this-document-even-though-there-are, 20 februarie 2026, „stops Mendeley Cite being able to read citations once they are inserted into the document”
- Doar fragment: zotero.org/support, potrivit căruia actualizările de securitate Windows din 9 iunie 2026 au stricat integrarea cu Word, iar Zotero 9.0.5 a reparat-o; forums.zotero.org/discussion/comment/514232 („{Citation} inserted instead of citation”); comment/513470 (pluginul nu face nimic pe macOS 26.5); paperguide.ai despre sincronizarea lentă în Mendeley (blog al unui vendor concurent); recenzii Mendeley pe G2.

## Surse blocate
- reddit.com: HTTP 200, dar pagina e goală (doar textul „Reddit”), deci blocată.
- g2.com: HTTP 403.
- trustpilot.com: HTTP 403 (mesaj anti-bot).
- upwork.com: HTTP 403 (Cloudflare).
- producthunt.com: HTTP 403 („Just a moment...”).
- fiverr.com: HTTP 403 („It needs a human touch”, captcha PerimeterX), la două pagini de servicii de formatare a tezelor.
- academia.stackexchange.com: HTTP 403 („Just a moment...”).
- techcommunity.microsoft.com: HTTP 403.
- capterra.com/p/233913/Mendeley/reviews/ și capterra.ca (Mendeley): 404 și 410; getapp.com.au (Mendeley): 404. Nu sunt blocări anti-bot, dar paginile nu s-au putut citi.
- atlasti.com/pricing și lumivero.com (paginile de prețuri NVivo): 404.

## Căutări făcute
- WebSearch: „Mendeley reference manager review 2025 frustrating sync broken”
- WebSearch: „falsely accused AI detector Turnitin student 2025 forum”
- WebSearch: „fiverr thesis formatting APA word table of contents gig” (gig-uri găsite, dar Fiverr blochează deschiderea)
- WebSearch: „"is there a tool" check reference list fake citations hallucinated references verify bibliography 2025”
- WebSearch: „forums.zotero.org check bibliography references exist hallucinated ChatGPT”
- WebSearch: „news.ycombinator.com hallucinated citations papers tool verify references 2025”
- WebSearch: „thesis Word formatting nightmare heading numbering captions table of contents broken 2026 forum”
- WebSearch: „learn.microsoft.com answers thesis word document caption numbering wrong chapter” (firul Microsoft Q&A deschis era din 2023, deci nu se numără)
- WebSearch: „formatare lucrare licenta Word anunt pret pagina 2026” (în română; au apărut doar ghidurile universităților, fără anunțuri)
- WebSearch: „thestudentroom Turnitin AI detection flagged my essay but I didn't use AI”
- WebSearch: „NVivo reviews cons expensive slow coding interviews capterra 2025”
- WebSearch: „Rayyan Covidence systematic review screening thousands of abstracts tedious alternative forum 2025”
- WebSearch: „PhD student coding interview transcripts takes weeks thematic analysis AI tool forum 2026”
- WebSearch: „ATLAS.ti reviews 2026 cons expensive student license capterra”
- WebSearch: „"Mendeley Cite" not working Word citations disappeared 2026”
- WebSearch: „forums.zotero.org Word plugin citations broken deadline thesis 2026”
- WebSearch: „msofficeforums.com thesis dissertation formatting page numbers roman sections table of contents 2026”
- WebSearch: „"is there a tool" OR "is there any tool" format thesis according to university guidelines automatically”
- WebSearch: „Covidence reviews capterra cons expensive” (pe pagina de prețuri Covidence, deschisă: 339 $/an pentru o recenzie și 907 $/an; nu am găsit plângeri ale utilizatorilor deschise și datate, așa că screeningul pentru recenzii sistematice nu a intrat ca problemă)
- Căutare internă pe forums.zotero.org: „bibliography doesn't work convert”
- Pagini citite cu citeste.sh: forums.zotero.org (lista de discuții, căutare, firele 132473, 133241 și comment/516840), community.openai.com, physicsforums.com, the-decoder.com, turnitin.forumbee.com, dataconomy.com, dailydot.com (din 2024, exclus), capterra.com (NVivo, MAXQDA și o recenzie MAXQDA), capterra.co.uk (ATLAS.ti), elsevier.support, grammarly.com/authorship, covidence.org/pricing, atlasti.com/student-licenses (fără prețuri vizibile).
- Formatarea tezei în Word, după ghidul universității, a fost căutată, dar n-a intrat ca problemă: am găsit doar gig-uri Fiverr (blocate), ghiduri universitare și un fir Microsoft Q&A din 2023, deci nicio sursă deschisă și datată după 15 mai 2025.
