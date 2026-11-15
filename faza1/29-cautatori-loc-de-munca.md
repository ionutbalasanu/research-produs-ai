# Domeniu: Persoane care își caută loc de muncă

## Problema 1: Aceleași date trebuie reintroduse manual în zeci de formulare de aplicare (Workday și alte ATS-uri)
- Cine o are: candidați care aplică la mai multe firme prin portaluri de carieră (Workday, Greenhouse, Wellfound); în surse apar ingineri software, profesioniști care își schimbă domeniul, candidați care aplică la volum mare.
- Cât de des apare: la fiecare aplicare. Un recenzent scrie de „40 forms a day”; un comentator HN spune că a completat întrebările Wellfound de peste 120 de ori.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: completează manual (creează cont separat pe fiecare portal Workday, încarcă CV-ul și apoi îl retastează); unii evită pur și simplu firmele care folosesc Workday; alții folosesc extensii de autocompletare (Simplify Copilot, LazyApply). Cost în timp exact: nu am găsit în surse.
- Soluții existente găsite, cu preț:
  - LazyApply (extensie Chrome + abonament): Basic 99 $/an (15 aplicări/zi), Premium 149 $/an, Ultimate 999 $/an (pagina de prețuri lazyapply.com/pricing, deschisă). Rating 3,4/5 din 215 evaluări pe Chrome Web Store; recenzii recente care spun că nu funcționează nici pentru clienții plătitori.
  - Simplify Copilot: extensie de autocompletare cu nivel gratuit, 4,8/5 din 3,9K evaluări, 500.000 utilizatori (Chrome Web Store); prețul nivelului plătit: nu am găsit în surse (pagina simplify.jobs/pricing a dat 404).
- Surse deschise:
  - https://nelson.cloud/i-hate-workday , 2026-02-18, „Why do I have to create a separate account for each company that uses Workday”
  - https://nelson.cloud/i-hate-workday , 2026-02-18, „upload my resume and then still prompt me to manually enter data?” (același autor; nu se numără separat)
  - https://chromewebstore.google.com/detail/pbanhockgagggenencehbnadejlgchfc/reviews?hl=en , recenzie Justin Graves, Nov 5, 2026, „saves gobs of time typing in the same stuff over and over!”
  - aceeași pagină, recenzie Aditya Rana, Nov 6, 2026, „given up just because how tiresome their career pages are”
  - https://chromewebstore.google.com/detail/lazyapply-job-application/pgnfaifdbfoiehcndkoeemaifhhbgkmm/reviews , recenzie Coinomi, Aug 3, 2026, „I'm just happy I’m not copy-pasting the same answers into 40 forms a day.”
  - aceeași pagină, recenzie Brian MacDonald, Sep 27, 2026, „Does not work even for paying customers.”
  - https://news.ycombinator.com/item?id=47988268 (Ask HN: Is the Job Market Actually Bad?, 2026-05-02, dată exactă din API-ul oficial HN), „120+ applications, 120+ times me answering filling out Wellfound's content questions”
- Doar fragment:
  - Un blog vendor (jobwizard.ai) susține că Workday eșuează la parsarea CV-ului în ~30% din cazuri; nedeschis, nenumărat.
  - Postare teamblind.com „hate making new workday accounts” (403, vezi Surse blocate).
  - feedback.simplify.jobs/p/workday-application-support a fost deschisă, dar e din 2024-10-01 / 2025-04-06, în afara celor 18 luni; nu se numără.

## Problema 2: Anunțuri „fantomă” și aplicări care nu primesc niciun răspuns
- Cine o are: candidați care aplică „la rece” prin job boards, în SUA și în România; în surse apar absolvenți, seniori, persoane care își schimbă domeniul.
- Cât de des apare: Resume Genius (1.000 de candidați din SUA): 67% au suspectat de câteva sau multe ori anunțuri false; Greenhouse: ~19% din anunțurile de pe job boards în T2 clasificate drept ghost jobs; sondaj Simplon România: 55,9% nu primesc răspuns la aplicări.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: aplică în continuare la volum mare (un comentator: 65 de aplicări într-o lună → 3 phone screens, 0 interviuri; altul: 500+ aplicări într-un an fără rezultat), ignoră anunțurile cu „100+ candidates have applied”, se bazează pe recomandări (referrals). Cost în bani: nu am găsit în surse.
- Soluții existente găsite, cu preț:
  - GhostJob – Ghost Job Detector (extensie Chrome pentru LinkedIn): scor de încredere 0–100 gratuit, cont Pro cu investigație automată; 44 utilizatori, fără evaluări; prețul Pro: nu am găsit în surse.
  - Alte extensii (Trouvr, Skip This Job, Subspace Ghost Job Scanner, Commit Ghost Job Tracker): doar fragment, preț negăsit.
  - Bestjobs (România) promovează asistentul AI „Bestie” care răspunde fiecărui candidat (pe partea angajatorului, nu a candidatului); preț: nu am găsit în surse.
- Surse deschise:
  - https://www.cpapracticeadvisor.com/2026/04/30/ghost-jobs-still-haunting-67-of-job-seekers-report-finds/182536/ , 2026-04-30, „Have suspected this a few or many times: 67%”
  - https://allwork.space/2026/08/nearly-1-in-5-job-ads-may-be-fake-ghost-jobs/ , 2026-08-21, „about 19% of jobs advertised on digital job boards … classified as ghost jobs”
  - https://news.ycombinator.com/item?id=47988268 , 2026-05-02, „Most companies I apply to don’t respond at all”
  - același fir HN, alt comentator, „applied to 65 jobs in the last month and landed three phone screenings” (același fir; nu se numără separat)
  - https://startupcafe.ro/jumatate-candidati-nu-folosire-ai-cautare-job-aproape-6-10-nu-primesc-raspuns-aplicari-trimise-sondaj-105407 , 2026-08-20, „55,9% dintre respondenții sondajului spun că nu primesc răspuns la aplicări trimise”
  - https://startupcafe.ro/inteligenta-artificiala-bestie-bestjobs-300000-conversatii-candidati-toata-tara-septembrie-2026-107876 , 2026-10-05, „Tăcerea nu e neutră. Candidatul ignorat își amintește numele companiei” (articol despre soluția Bestjobs; nu e dovadă independentă de problemă)
  - https://chromewebstore.google.com/detail/clbbopifmidceplphamfdfapgacgbhnd (GhostJob), dată nevizibilă pe listare, „Click Scan on a supported job page to see a 0–100 Trust Score” (folosită doar pentru soluții existente)
- Doar fragment:
  - ResumeBuilder Ghost Jobs Report: 86% au întâlnit un ghost job (din fragmentul de căutare, nedeschis).
  - Studii Bestjobs: 87% au avut „interviu fantomă”, 80% nu au primit răspuns (fragmente, nedeschise).
  - https://revistacariere.ro/... „Unul din cinci anunțuri de angajare este fantomă” a fost deschisă, dar e din 2025-01-16, în afara celor 18 luni; nu se numără.

## Problema 3: Evidența aplicărilor și a versiunilor de CV trimise fiecărei firme se ține haotic (Excel, foldere, tab-uri)
- Cine o are: candidați care aplică la zeci de roluri și trimit versiuni diferite de CV.
- Cât de des apare: continuu pe durata căutării; un autor spune că „by week three of a job search, the process itself becomes the problem”.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: foi Excel/Google Sheets, șabloane Notion (unele vândute pe Gumroad), foldere cu fișiere CV aproape identice; aplicații de tracking ale căror extensii uneori nu salvează sau nu preiau datele, caz în care utilizatorul introduce manual sau revine la spreadsheet. Cost în timp: nu am găsit în surse.
- Soluții existente găsite, cu preț:
  - Huntr Pro: 40 $/lună, 90 $ la 3 luni sau 160 $ la 6 luni (huntr.co/pricing, deschisă).
  - Teal (extensie + aplicație), 4,9/5 pe Chrome Web Store; prețul Teal+: doar fragment (surse contradictorii: ~9 $/săptămână sau 29 $/lună), pagina de prețuri blocată.
  - Jobscan: Job Search Tracker (extensie Chrome); prețul abonamentului Jobscan: doar fragment (49,95 $/lună), pagina de prețuri blocată.
  - Șabloane Notion/Sheets: Spreadsheet Class oferă șablon gratuit Google Sheets (deschis); șabloane plătite pe Gumroad (~9 $, pachet 21 $): doar fragment.
- Surse deschise:
  - https://chromewebstore.google.com/detail/teal-free-job-search-cont/opafjjlpbiaicbbgifbejoochmmeikep/reviews , recenzie James Kessenich, Oct 24, 2026, „track my job search and different versions of my resume in an Excel spreadsheet”
  - aceeași pagină, recenzie Tyler McDonald, Aug 18, 2026, „Probably going back to just tracking my jobs in a spreadsheet.” (aceeași pagină; nu se numără separat)
  - https://chromewebstore.google.com/detail/jobscan-job-search-tracke/apppjobnbahbomhgmcgolplkpigjlofl/reviews , recenzie Jiang Kai, May 29, 2026, „It does NOT populate job information from LinkedIn. I had to manually enter myself.”
  - https://dev.to/shaishav_patel_271fdcd61a/a-free-job-application-tracker-that-also-tailors-your-resume-no-signup-runs-in-your-browser-3h6p , 2026-06-14 (atribut datetime din pagină), „Most people end up juggling a spreadsheet, a folder of near-identical resume files” (autorul își promovează propriul tool)
  - https://huntr.co/pricing , dată nevizibilă, „The monthly plan is billed at $40 per month.” (folosită doar pentru preț)
- Doar fragment:
  - Liste Gumroad cu șabloane Notion „Job Application Tracker” (pagina designedbylinda.gumroad.com s-a deschis dar a returnat doar titlul, fără preț sau dată).
  - Gig-uri Fiverr care livrează aplicări + foaie Google Sheets cu evidența (fiverr.com blocat).

## Problema 4: Adaptarea CV-ului pentru fiecare anunț ca să treacă de filtrele ATS consumă timp și produce anxietate
- Cine o are: candidați care aplică online prin ATS; în surse: absolvenți („bloodbath”), profesioniști experimentați respinși automat.
- Cât de des apare: la fiecare aplicare; 67% dintre candidații din sondajul Resume Genius se tem că CV-ul le va fi respins înainte să-l vadă un om.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: rescrie manual CV-ul pentru fiecare rol („re-tailor from scratch every time”), optimizează pe cuvinte-cheie, folosește unelte de scanare/potrivire (Jobscan, Simplify, Teal). Un comentator HN descrie respingere automată la 20 de minute după aplicare. Cost exact în timp: nu am găsit în surse.
- Soluții existente găsite, cu preț:
  - Jobscan (scor de potrivire CV–anunț): preț doar fragment (49,95 $/lună sau 89,95 $ la 3 luni); pagina de prețuri blocată.
  - Simplify (scor ATS și „tailoring” în extensie): preț negăsit (404 pe pagina de prețuri).
  - Instrumente gratuite de tip „résumé-to-job tailoring” (ex. cel promovat în articolul dev.to): gratuit, conform autorului.
- Surse deschise:
  - https://news.ycombinator.com/item?id=47988268 , 2026-05-02, „I need to do something to ATS optimize my resume and plan otherwise I'll be unemployed”
  - același fir HN, alt comentator, „The best people I know are sending hundreds of tailored job applications” (același fir; nu se numără separat)
  - https://www.cpapracticeadvisor.com/2026/04/30/ghost-jobs-still-haunting-67-of-job-seekers-report-finds/182536/ , 2026-04-30, „Worry their resume will be rejected before a person sees it: 67%”
  - https://dev.to/shaishav_patel_271fdcd61a/a-free-job-application-tracker-that-also-tailors-your-resume-no-signup-runs-in-your-browser-3h6p , 2026-06-14, „You re-tailor from scratch every time, you lose track of what you sent where”
  - https://chromewebstore.google.com/detail/jobscan-job-search-tracke/apppjobnbahbomhgmcgolplkpigjlofl/reviews , recenzie Tom Vaesen, Oct 2, 2025, „Makes the process of pulling job descriptions & tailoring substantially easier!”
- Doar fragment:
  - Articole dev.to/careercheck care citează „Reddit says 30-60 minutes per resume” (nedeschise; blog vendor).
  - Recenzii Trustpilot Jobscan despre preț și facturare după anulare (trustpilot.com blocat).

## Problema 5: Oferte de muncă false și escrocherii (task scams, recrutori falși, reshipping) care țintesc candidații
- Cine o are: persoane care caută joburi remote/de acasă, inclusiv în România (mesaje pe WhatsApp/Telegram).
- Cât de des apare: BBB: aproape 50.000 de persoane au raportat escrocherii de angajare în ultimii trei ani; pierderile au crescut de la 90 mil. $ (2020) la 501 mil. $ (2024), conform articolului Fortune republicat de Allwork.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: verifică manual compania și recrutorul pe site-ul oficial, caută „scam” + numele firmei, trimite mesajul la un verificator (Bitdefender Scamio). Costul pentru victime: pierderi agregate de mai sus; cost individual: nu am găsit în surse.
- Soluții existente găsite, cu preț:
  - Bitdefender Scamio (analizează mesaje, linkuri, capturi de ecran cu oferte suspecte); preț: nu am găsit în surse.
  - Extensii „ghost/scam job detector” (Trouvr etichetează anunțurile legitimate/ghost/scam): doar fragment, preț negăsit.
- Surse deschise:
  - https://www.live5news.com/2026/07/15/bbb-warns-fake-remote-job-offers-are-rise/ , 2026-07-15, „when they attempt to cash out, they are told to send money first”
  - https://www.bitdefender.com/ro-ro/blog/hotforsecurity/task-scam-job-online-fals , 08 Octombrie 2026, „victima trebuie să depună propriii bani pentru a continua sau pentru a retrage”
  - https://allwork.space/2026/07/can-you-spot-a-fake-recruiter-increasingly-sophisticated-hiring-scams-are-costing-job-seekers-millions/ , 2026-07-12, „losses from employment scams grew from $90 million to $501 million”
  - https://news.ycombinator.com/item?id=47988268 , 2026-05-02, „increasingly difficult to get past the fake jobs, the resume harvesting”
- Doar fragment:
  - BBB Scam Tracker: 22.000 plângeri de escrocherii de angajare în 2025 față de 11.000 în 2024 (din fragmentul de căutare; în articolul Live5 deschis cifra nu apare).
  - Monster 2026 Job Scam Report: 95% au întâlnit oferte suspecte (fragment, nedeschis).
  - Notă: această problemă se sprijină parțial pe avertizări oficiale (BBB, DNSC), nu pe obligații legale.

## Surse blocate
- reddit.com (r/jobs: HTTP 200 dar pagină goală, doar „Reddit”)
- trustpilot.com (403, mesaj anti-bot) – recenzii Jobscan, LazyApply, Teal, Workday
- g2.com (403)
- producthunt.com (403 „Just a moment...”)
- upwork.com (403 Cloudflare)
- fiverr.com (403 „It needs a human touch”) – gig-uri „apply to jobs for you”
- addons.mozilla.org (pagină „Client Challenge”) – recenzii Simplify Copilot cu 1–2 stele
- teamblind.com (403)
- indiehackers.com (403 „Just a moment...”)
- forum.softpedia.com (403 „Just a moment...”) – firul „Cei care sunteți fără job de multe luni”
- jobscan.co/pricing (403), tealhq.com/pricing (403 Cloudflare)
- simplify.jobs/pricing (404, pagină inexistentă – nu blocare)

## Căutări făcute
- WebSearch: „job seekers ghost jobs fake postings frustration 2026 forum”
- WebSearch: „LazyApply reviews auto apply tool complaints”
- WebSearch: „"is there a tool" track job applications spreadsheet tailoring resume each application”
- WebSearch: „Simplify Copilot chrome extension reviews autofill workday”
- WebSearch: „news.ycombinator.com Ask HN job search 2026 applications no response”
- WebSearch: „Workday application "create an account" every company job seekers hate re-enter resume forum”
- WebSearch: „job application tracker template Etsy Notion Google Sheets job search”
- WebSearch: „ejobs bestjobs aplicat nu primesc raspuns forum angajatori ghosting candidati”
- WebSearch: „ghost job detector chrome extension LinkedIn posting age”
- WebSearch: „Teal job tracker chrome extension reviews”
- WebSearch: „Jobscan reviews capterra expensive subscription resume tailoring”
- WebSearch: „fiverr "apply to jobs" on your behalf job application assistant gig”
- WebSearch: „tailoring resume for every job application takes hours exhausting forum 2026”
- WebSearch: „workplace.stackexchange.com job offer scam recruiter 2026”
- WebSearch: „BBB scam tracker fake job offer remote 2026 lost money”
- WebSearch: „țeapă ofertă de muncă falsă WhatsApp job like-uri 2026 forum reclamatii”
- WebSearch: „Jobscan chrome extension reviews chromewebstore”
- WebSearch: „ResumeWorded OR Rezi OR Kickresume reviews chrome web store "cancel" subscription resume AI”
- WebSearch: „forum.softpedia.com caut job luni aplicat zeci CV-uri niciun raspuns”
- Pagini deschise cu citeste.sh: Chrome Web Store (LazyApply, Simplify Copilot, Teal, Jobscan Tracker, GhostJob), Hacker News (item 47988268; dată din API-ul oficial HN), nelson.cloud, feedback.simplify.jobs, cpapracticeadvisor.com, allwork.space (2 articole), startupcafe.ro (2 articole), revistacariere.ro, live5news.com, bitdefender.com/ro-ro, dev.to, capterra.com (Jobscan – o singură recenzie, fără conținut util), huntr.co/pricing, lazyapply.com/pricing, spreadsheetclass.com, designedbylinda.gumroad.com
