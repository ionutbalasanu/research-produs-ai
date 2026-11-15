# Domeniu: 03 avocați și notari (partea administrativă)

Nu am găsit nicio problemă care să îndeplinească regula de dovadă (minimum 2 surse deschise, independente, din ultimele 18 luni). Motivul: în această sesiune, rețeaua nu permitea deschiderea niciunei pagini externe. WebFetch a întors „getaddrinfo ENOTFOUND” pentru fiecare domeniu încercat, iar curl a primit „CONNECT tunnel failed, response 403” de la proxy. Mediul cloud („Default”) are rețea limitată și lista de domenii permise e goală. Singura unealtă care a funcționat a fost WebSearch, care întoarce doar fragmente și rezumate. După reguli, fragmentele nu se numără.

Din acest motiv nu am scris secțiuni „Problema N”. Mai jos sunt doar pistele întâlnite în fragmente, toate marcate „doar fragment”. Niciuna nu e verificată și niciuna nu se numără ca dovadă.

## Piste neconfirmate (doar fragment, nu se numără)
- Recenzii Clio (G2/Capterra): rezumatul căutării menționează plângeri despre facturare („billing issues ... high costs for basic features”) și dorința de „a standalone and simple desktop app for time tracking”. Nu am putut deschide paginile, iar datele nu se pot verifica. Linkuri: https://www.g2.com/products/clio/reviews ; https://www.capterra.com/p/105428/Clio/reviews/
- Urmărirea documentelor lipsă de la clienți la avocații care lucrează singuri: există un articol California Lawyers Association despre „missing document follow-up”, care nu a fost deschis. Link: https://calawyers.org/solo-small-firm/reducing-missing-document-follow-up-in-a-california-solo-practice/
- Notari / loan signing agents: e-mailul, calendarul, kilometrajul și registrul (journal) sunt ținute separat, iar datele se tastează de mai multe ori. Singura sursă e pagina de vânzare a unui furnizor (nexasphere.io), deci nu e o mărturie de utilizator. Prețuri din fragment, nedeschise: NotaryNext „starting at $15 a month”, SigningOS gratuit cu niveluri Pro/Elite (după closewise.com). Linkuri: https://nexasphere.io/products/iphone/signerledger-ai ; https://www.closewise.com/best-notary-apps-for-signing-agents-2026/
- România, monitorizarea termenelor din portal.just.ro: în fragmente apar instrumente existente (LexForce de la Wolters Kluwer, Termene.ro, aplicațiile iOS „Agenda Juridică” și „Monitor Dosare”), fără prețuri vizibile. Nu am găsit plângeri de utilizator, nici măcar în fragmente. Linkuri: https://www.wolterskluwer.com/ro-ro/solutions/lexforce ; https://termene.ro/solutie-avocati ; https://apps.apple.com/us/app/-/id1498634602
- Upwork: în fragmente apar anunțuri din 2026 pentru „Legal Data Entry & Intake Assistant” (firme de vătămare corporală și de planificare succesorală din SUA), cu sarcini de introducere de date despre dosare și clienți. Linkuri: https://www.upwork.com/freelance-jobs/apply/Remote-Legal-Data-Entry-Intake-Assistant-Full-Time_~022085440703519328313/ ; https://www.upwork.com/freelance-jobs/apply/Remote-Legal-Intake-Admin-Assistant-Texas-Estate-Planning-Law-Firm_~022065975550446653379/

## Surse blocate
- old.reddit.com și www.reddit.com: proxy 403 la curl (inclusiv varianta .json), iar WebFetch spune „unable to fetch from old.reddit.com”
- www.capterra.com: WebFetch ENOTFOUND, curl 403
- www.g2.com: curl 403
- www.trustpilot.com și ca.trustpilot.com: WebFetch ENOTFOUND, curl 403
- www.getapp.com: curl 403
- wordpress.org: WebFetch ENOTFOUND
- news.ycombinator.com: WebFetch ENOTFOUND
- www.upwork.com: WebFetch ENOTFOUND
- apps.apple.com: WebFetch ENOTFOUND
- forum.notarycafe.com: WebFetch ENOTFOUND
- Cauză comună: mediul sesiunii are rețea „limited” și nu are niciun domeniu permis. Ca să se poată repeta colectarea, domeniile de mai sus trebuie permise în setările de rețea ale mediului.

## Căutări făcute
- curl: old.reddit.com/r/LawFirm/search.json?q=billable time tracking (blocat)
- curl: www.reddit.com/r/LawFirm/.json și old.reddit.com/r/LawFirm/.json (blocat)
- WebFetch: old.reddit.com/r/LawFirm/new/ (blocat)
- WebSearch: „Clio reviews time tracking billing complaints 2026” (doar fragmente)
- WebFetch: capterra.com/p/105428/Clio/reviews/ și trustpilot.com/review/clio.com (blocat)
- curl: capterra, g2, trustpilot (com și ca), getapp, pagini de recenzii Clio (blocat)
- WebFetch: wordpress.org/plugins/search/law+firm/ și news.ycombinator.com (blocat)
- WebSearch: „reddit r/LawFirm solo attorney "is there a tool" client intake documents chasing” (doar fragmente, niciun fir Reddit în rezultate)
- WebSearch: „reddit notary loan signing agent journal invoicing app frustrating 2026” (doar fragmente, niciun fir Reddit în rezultate)
- WebSearch: „avocat termene dosare portal.just.ro notificari aplicatie monitorizare dosare” (doar fragmente)
- WebSearch: „upwork job legal assistant data entry law firm intake repetitive 2026” (doar fragmente)
- WebFetch: anunț Upwork, pagina App Store „Monitor Dosare”, fir forum.notarycafe.com (blocat)
- Nu am încercat Fiverr, Product Hunt, Chrome Web Store și piețele de șabloane Notion/Etsy, pentru că toate domeniile externe testate erau blocate la nivel de rețea.
