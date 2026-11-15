# Domeniu: 01 cabinete medicale și stomatologice mici (partea administrativă)

> Stare: **nicio problemă nu îndeplinește regula de dovadă** (minimum 2 surse deschise, independente, din ultimele 18 luni).
> Motiv: în această sesiune nu s-a putut deschide nicio pagină web. WebFetch refuză toate domeniile încercate (DNS blocat de politica de rețea a sesiunii), iar curl primește 403 de la proxy la CONNECT. Singurul instrument care a funcționat este WebSearch, care întoarce doar titluri, URL-uri și rezumate. Conform regulilor, acestea sunt „doar fragment” și nu se numără.
> Mediul sesiunii are rețea „limited”, fără gazde permise (allowed_hosts gol). Ca să se poată reface colectarea, gazdele din secțiunea „Surse blocate” trebuie permise în setările de rețea ale mediului.

## Problema 1: nu am găsit (nicio sursă deschisă)
- Cine o are: nu am găsit în surse
- Cât de des apare: nu am găsit în surse
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: nu am găsit în surse
- Soluții existente găsite, cu preț: nu am găsit în surse
- Surse deschise: niciuna
- Doar fragment (nu se numără; teme pe care căutările le-au scos la suprafață, de verificat într-o rundă cu acces la rețea):
  - Verificarea asigurării dentare și a beneficiilor (insurance verification / breakdown) la cabinete dentare din SUA. Fragmentele provin aproape doar de pe bloguri de vânzători (Overjet, Curve Dental, RevenueWell, Zuub, Lassie, stealthagents.com, ainora.lt) și au cifre de marketing, neverificate. Nu am găsit niciun fir Reddit în rezultate.
    - https://www.overjet.com/blog/average-time-savings-ai-dental-insurance-verification-for-modern-dental-practices (doar fragment, dată în rezultat: 30 octombrie 2025)
    - https://www.dentalmanagers.com/blog/aadom-quickcast-why-insurance-verification-is-the-hidden-bottleneck/ (doar fragment, dată nevizibilă)
    - https://www.curvedental.com/blog/cut-insurance-verification-time (doar fragment, dată nevizibilă)
  - Verificarea asigurării externalizată către freelanceri: oferte de servicii pe Upwork și Fiverr, plus anunțuri pentru asistenți virtuali pe Workable și OnlineJobs.ph. Rezumatul căutării menționează tarife de circa 4,22–7 USD/oră; cifra nu e verificată pe pagină.
    - https://www.upwork.com/jobs/~022067110157780444776 (doar fragment, dată nevizibilă; deschiderea a eșuat)
    - https://fiverr.com/aresdan/do-dental-insurance-verification (doar fragment, dată nevizibilă; deschiderea a eșuat)
    - https://apply.workable.com/winning-assistants/jobs/view/F8F05457E9.md (doar fragment, dată nevizibilă; deschiderea a eșuat)
    - https://www.onlinejobs.ph/jobseekers/job/Virtual-Dental-Assistant-Insurance-Verification-Administrative-Support-1602109 (doar fragment, dată nevizibilă)
  - Autorizarea prealabilă (prior authorization) prin fax la cabinete medicale mici din SUA. Fragmentele citează un sondaj AMA din 13 mai 2026 și un brief MGMA 2026; nu am deschis niciunul. Tema e în mare parte de reglementare (CMS-0057-F).
    - https://www.medicaleconomics.com/view/electronic-prior-auths-are-coming-here-s-what-physicians-must-ask-their-ehr-and-billing-vendors (doar fragment, dată în rezultat: 12 octombrie 2026)
    - https://www.physicianspractice.com/view/6-ways-technology-can-ease-the-prior-authorization-burden (doar fragment, dată în rezultat: 26 noiembrie 2025)
    - https://mgma.com/getkaiasset/7a9ca2e8-061b-4378-a7a2-a1316dcd1765/MGMA%202026%20Prior%20Authorization%20Issue%20Brief%20%282%29.pdf (doar fragment, dată nevizibilă)
  - Neprezentarea pacienților la programare și remindere SMS (România). Fragmentele sunt doar pagini de vânzător (Zarina CRM). Am găsit un singur fir de forum românesc (Softpedia), dar acesta e despre hardware și CBCT, nu despre programări.
    - https://www.zarinacrm.ro/crm-cabinet-medical/programari-calendar/ (doar fragment, dată nevizibilă)
    - https://forum.softpedia.com/topic/1256829-sistem-pc-cabinet-stomatologie-cbct-uri/ (doar fragment, dată nevizibilă, nu e pe temă)

## Surse blocate
Toate încercările de deschidere au eșuat. WebFetch întoarce „getaddrinfo ENOTFOUND” sau „unable to fetch”, iar curl primește „CONNECT tunnel failed, response 403”.
- reddit.com și old.reddit.com (WebFetch: „unable to fetch”; curl: 403, inclusiv pe varianta .json)
- web.archive.org (WebFetch: „unable to fetch”)
- capterra.com (WebFetch și curl)
- g2.com (WebFetch și curl)
- trustpilot.com (WebFetch și curl)
- softwareadvice.com, getapp.com (curl)
- dentaltown.com, forumul de profil pentru stomatologi (WebFetch și curl)
- dentalmanagers.com, AADOM (WebFetch)
- upwork.com (WebFetch și curl)
- fiverr.com (WebFetch)
- apply.workable.com (WebFetch)
- producthunt.com (WebFetch și curl)
- wordpress.org (curl)
- play.google.com, apps.apple.com (curl)
- community.simplepractice.com (curl)
- news.ycombinator.com (WebFetch, test de control)

## Căutări făcute
- WebSearch: „reddit dental office manager insurance verification takes hours 2026”. Fără fire Reddit, doar bloguri de vânzători.
- WebSearch: „"is there a tool" dental front desk insurance breakdown reddit”. Fără fire Reddit, doar vânzători plus o ofertă Fiverr.
- WebSearch: „small medical practice prior authorization fax paperwork reddit 2026 private practice”. Fără fire Reddit, doar vânzători și presă de specialitate.
- WebSearch: „cabinet stomatologic programari pacienti neprezentare programare SMS forum”. Doar pagini de vânzător românesc, plus un fir Softpedia care nu e pe temă.
- WebSearch: „upwork dental insurance verification virtual assistant job 2026”. Oferte de freelanceri pe Upwork, anunțuri pe Workable și OnlineJobs.ph.
- WebFetch: reddit.com/r/Dentistry/search (blocat), web.archive.org pentru r/Dentistry (blocat), capterra.com Dentrix reviews (blocat), trustpilot.com getweave.com (blocat), dentaltown.com/messageboard (blocat), dentalmanagers.com articol AADOM (blocat), upwork.com job (blocat), apply.workable.com (blocat), g2.com Open Dental reviews (blocat), producthunt.com search „dental insurance” (blocat), fiverr.com gig (blocat), news.ycombinator.com (blocat, test).
- curl: reddit.com și old.reddit.com search.json, capterra, g2, trustpilot, dentaltown, upwork, producthunt, wordpress.org, play.google.com, apps.apple.com, community.simplepractice.com, softwareadvice, getapp. Toate au primit 403 de la proxy.
