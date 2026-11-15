# Domeniu: Dezvoltatori software independenți (freelanceri, indie hackers, consultanți tehnici solo; partea de business și operațiuni)

## Problema 1: Găsirea clienților pe platforme inundate de aplicări automate, cu „connects" plătite
- Cine o are: dezvoltatori freelanceri (inclusiv seniori cu conturi vechi pe platforme) care caută proiecte pe Upwork, Fiverr, Freelancer, Guru.
- Cât de des apare: subiectul revine în mai multe fire Hacker News independente între 2025-06 și 2026-09 (4 autori diferiți citați mai jos). Frecvența exactă: nu am găsit în surse.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: cumpără „connects" pe Upwork pentru fiecare ofertă și plătește apoi procent din câștig dacă primește proiectul („You pay for connects and most proposals aren't even read.", răspuns în firul HN 45307270, 2025-09-20); alternativ, se bazează pe recomandări și rețea personală sau trimite clipuri Loom personalizate (sfaturi din firul HN 49856000). Sumele exacte cheltuite pe connects: nu am găsit în surse.
- Soluții existente găsite, cu preț:
  - Vollna (alerte și licitare automată pe Upwork): $24/lună sau $16/lună la plata anuală (https://vollna.com/pricing, pagină deschisă).
  - GigRadar (automatizare oferte Upwork): ofertă „lifetime" $1,697 o singură dată, „~2,100 proposals · ~$0.81 per proposal" (https://gigradar.io/pricing, pagină deschisă).
  - GigsAlert (alerte pentru joburi urgente pe platforme freelance, lansat pe HN 2025-08-26): preț nevăzut, site-ul nu a răspuns.
- Surse deschise:
  - https://news.ycombinator.com/item?id=49856000, 2026-09-26, „I cannot land a gig because automated platforms have flooded clients’ attention"
  - https://news.ycombinator.com/item?id=45307270, 2025-09-19, „it's just not worth having to purchase "connects" to initiate a bid proposal"
  - https://news.ycombinator.com/item?id=44201313, 2025-06-06, „I only really use fiverr because the connects are too expensive."
  - https://news.ycombinator.com/item?id=47327385, 2026-03-10, „I need help finding gigs, this year has been one of a kind."
- Doar fragment: articol fiscalitatea.ro (ghid 2026) cu fraza „instabilitatea veniturilor este, fără îndoială, cel mai mare stres al vietii de freelancer" (doar fragment de căutare, nu se numără).

## Problema 2: Plăți întârziate și urmărirea facturilor neplătite
- Cine o are: consultanți și dezvoltatori care facturează direct clienții (B2B), inclusiv contractori pe proiecte cu etape (milestones).
- Cât de des apare: un comentator dintr-o firmă mică de consultanță raportează, pe baza a „around 2,000 invoices sent over the last 5 years", o întârziere medie de 23 de zile și „About 1% of contracts tend to fully or partially default" (HN 47660286). Alte cifre: nu am găsit în surse.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: clauze contractuale de penalități și dobândă, oprirea livrării până la plată, livrabile doar în mod vizualizare până la achitare, facturi sub pragul procedurii simplificate; cerere în instanță în UK „costs something like 80 quid" (toate din firul HN 47660286). Un fondator fost freelancer estimează că petrecea „20% of my time" pe administrare, inclusiv urmărirea facturilor (HN 46839109; afirmație a unui vânzător de soluție).
- Soluții existente găsite, cu preț:
  - Trustora (contract + plată în escrow pe etape, prin Stripe Connect): comision plafonat la $150 fix, conform postării autorului pe HN 46839109.
  - Alte instrumente dedicate de recuperare/urmărire automată a facturilor pentru freelanceri: nu am găsit în surse deschise.
- Surse deschise:
  - https://news.ycombinator.com/item?id=47660286, 2026-04-06, „our average delay due to late payment is 23 days."
  - https://news.ycombinator.com/item?id=46839109, 2026-01-31, „drafting contracts, compliance, and chasing invoices."
  - https://news.ycombinator.com/item?id=47327385, 2026-03-10, „the client is finding it difficult to even pay for what has been done."
- Doar fragment: nimic relevant.

## Problema 3: Evidența timpului facturabil și facturarea: unelte scumpite brusc, fragmentate, timer uitat
- Cine o are: freelanceri și consultanți solo care facturează la oră și țin evidența timpului pe mai mulți clienți.
- Cât de des apare: după preluarea Harvest de către Bending Spoons, mai multe fire HN din 2026 (iulie, august, noiembrie) adună relatări de scumpiri; firul „RIP, Harvest" are 445 de puncte și 147 de comentarii. Uitatul timerului apare în recenzii Capterra la Toggl Track. Frecvența exactă: nu am găsit în surse.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: plătește prețul nou (un utilizator: de la circa $150 la peste $1100 pe an), migrează la altă unealtă sau își scrie singur o aplicație cu AI („had Claude vibecode a fully-featured clone in a single evening", HN 48849810); combină unealta de timp cu o unealtă separată de facturare („using a separate system is still necessary", recenzie Toggl 2026-03-30); corectează manual înregistrările uitate.
- Soluții existente găsite, cu preț:
  - Harvest: „$0 forever" și „$9 seat/month" (https://www.getharvest.com/pricing, pagină deschisă; utilizatorii HN descriu taxe suplimentare după utilizare).
  - Toggl Track: plan „Free $0" pentru număr limitat de utilizatori (https://toggl.com/track/pricing/, pagină deschisă); facturarea e descrisă ca „quite minimal" de un recenzent.
  - Zebu (alternativă Harvest, cu migrare): €5 pe lună / €60 pe an (https://zebu.work, pagină deschisă).
  - Hourbun (timp + facturare, lansat pe HN 2026-11): preț nevăzut pe pagina deschisă.
  - Wave (Waveapps): menționat ca gratuit dacă nu încasezi plăți prin el (comentariu HN 50420035; neverificat pe site-ul vânzătorului).
- Surse deschise:
  - https://news.ycombinator.com/item?id=50420035, 2026-11-09, „raise my annual charge to over $1100, from the $150 or so"
  - https://news.ycombinator.com/item?id=48849810, 2026-07-09, „They took my ~$100/yr Harvest time-tracking Solo plan, increased the price by 2.5x"
  - https://news.ycombinator.com/item?id=49374920, 2026-08-20, „Harvest hikes bills by 1500% after purchased by Bending Spoons"
  - https://www.capterra.com/p/247745/Toggl/reviews/?page=2, 2026-03-30 (recenzie 4 stele, „A simple but reliable time tracking tool for freelancers"), „during busier periods—when I forgot to start it."
- Doar fragment: sinteză G2 despre Toggl Track („users often forgetting to start timers and encountering syncing delays"), doar fragment, nu se numără; G2 blocat.

## Problema 4: Transformarea discuțiilor cu clientul în propuneri, oferte și modificări de scop (scope creep)
- Cine o are: freelanceri și consultanți solo care lucrează pe ofertă fixă sau pe propuneri scrise; deosebit de vizibilă la proiectele cu preț fix.
- Cât de des apare: un fondator fost freelancer spune că petrecea „two hours after every call" pe această muncă (HN 47019829, afirmație de vânzător). Alte cifre: nu am găsit în surse.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: scrie manual propunerea, formatează scopul, exportă PDF, urmărește semnătura și factura în unelte separate (HN 47019829); unii își construiesc singuri un flux cu AI pentru propuneri (HN 47076607); la scope creep trec contractul pe oră sau taxează suplimentar fiecare modificare („I charge another 0.5 hours just for the trouble", HN 48830015).
- Soluții existente găsite, cu preț:
  - Artifact (propuneri din notițe de apel + urmărire până la plată): preț nevăzut, site-ul nu a răspuns.
  - Bonsai (propuneri, contracte, facturare, conform unei recenzii Capterra din 2025-08-10): pagina de prețuri arată „$9 /user/month" și „$19 /user/month" (https://www.hellobonsai.com/pricing, pagină deschisă).
  - Calculator „Scope Creep" freepaycalc: gratuit, conform autorului (HN 48830015); site neverificat.
- Surse deschise:
  - https://news.ycombinator.com/item?id=47019829, 2026-02-15, „I'd spend two hours after every call doing the work around the work."
  - https://news.ycombinator.com/item?id=47076607, 2026-02-19, „I hate writing proposals. It's the most mind numbing and repetitive work"
  - https://news.ycombinator.com/item?id=46490660, 2026-01-04, „many projects go way over budget when a client is actively involved"
  - https://news.ycombinator.com/item?id=48830015, 2026-07-08, „I got tired of the friction associated with scoping engineering modifications on fixed-fee"
- Doar fragment: articol dev.to „How to spot scope creep in fixed-price projects" și mai multe calculatoare de scope creep (pagini promoționale), doar fragment; Product Hunt „scopeguard" blocat.

## Problema 5: Vânzarea propriului software global: taxe (TVA/sales tax) și acces la un „merchant of record" (sursă de tip obligație legală)
- Cine o are: indie hackers și dezvoltatori solo care vând SaaS sau aplicații către clienți din mai multe țări.
- Cât de des apare: un comentator spune că respingerea fără motiv la Lemon Squeezy „seems to be a fairly common experience based on other founders' reports" (HN 49353072). Cifre: nu am găsit în surse.
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: folosește un merchant of record (Paddle, Lemon Squeezy, FastSpring, Stripe) care preia taxele, plătind comision pe tranzacție; așteaptă aprobarea produsului (o lună de așteptare raportată, HN 48369065) sau mută contul la alt furnizor; cere sfatul contabilului (HN 49540833).
- Soluții existente găsite, cu preț:
  - Paddle: „5% + 50¢" pe tranzacție, fără taxă lunară (https://www.paddle.com/pricing, pagină deschisă).
  - Lemon Squeezy: „5% + 50¢" pe tranzacție (https://www.lemonsqueezy.com/pricing, pagină deschisă); autorul articolului din HN 49540833 spune că dezvoltarea e oprită după preluarea de către Stripe.
  - Stripe (serviciu MoR), FastSpring, tiun: preț nevăzut.
- Surse deschise:
  - https://news.ycombinator.com/item?id=49540833, 2026-09-03, „every state has their own sales tax rules"
  - https://news.ycombinator.com/item?id=49353072, 2026-08-18, „Lemon Squeezy rejected my store application after review with no specific reason given"
  - https://news.ycombinator.com/item?id=48369065, 2026-06-02, „It's been a month since I submitted my product for review and I'm still waiting."
- Doar fragment: blog agiled.app afirmă că uneltele fiscale Bonsai sunt făcute pentru persoane fizice autorizate din SUA, iar utilizatorii internaționali plătesc pentru ele fără să le poată folosi (doar fragment, sursă a unui concurent).

## Surse blocate
- reddit.com (HTTP 200, dar pagina goală: doar „Reddit")
- g2.com (HTTP 403)
- trustpilot.com (HTTP 403, blocare anti-bot)
- upwork.com și community.upwork.com (HTTP 403, Cloudflare)
- producthunt.com (HTTP 403, „Just a moment...")
- indiehackers.com (HTTP 403, „Just a moment...")
- freelancing.stackexchange.com (HTTP 403, „Just a moment...")
- fiverr.com (HTTP 403)
- quora.com (HTTP 403, „Just a moment...")
- gigsalert.com, artifact.app (nu au răspuns, HTTP 000)
- Capterra, pagina veche Toggl (p/146916): HTTP 404; folosită pagina curentă p/247745

## Căutări făcute
- WebSearch: „freelance developer scope creep estimating fixed price project tool hacker news 2025"
- WebSearch: „Bonsai freelance software review capterra 2025 cons"
- WebSearch: „forum programator freelancer clienti găsesc proiecte 2026 PFA IT" (rezultate românești: doar ghiduri fiscale SRL/PFA și un fir avocatnet fără conținut util; nu am găsit discuții românești despre probleme de business cu dovezi deschise)
- WebSearch: „capterra Toggl Track reviews forget to start timer"
- Căutarea Hacker News (hn.algolia.com, căutarea oficială legată din subsolul HN), comentarii după 2025-05-15: „freelance invoice late payment", „freelance client won't pay", „freelancing chasing invoices", „freelance scope creep", „freelancing is dead", „finding freelance clients", „upwork connects", „freelance proposal AI spam", „unprofitable freelance clients", „time tracking freelance forgot", „forgot to track time billable", „time tracking clients billable hours", „toggl", „invoicing freelance tool", „harvest time tracking", „writing proposals clients consulting", „estimate fixed price freelance underestimated", „scope creep client", „contract template freelancer", „statement of work consultant", „lemon squeezy", „merchant of record indie", „paddle rejected", „sales tax solo saas"
- Căutarea Hacker News, povești: „freelance", „freelancer", „consulting clients"
- Capterra: recenzii Bonsai (pagina 1) și Toggl Track (paginile 1–3)
- Pagini de prețuri deschise: Paddle, Lemon Squeezy, Harvest, Bonsai, Zebu, Hourbun, Trustora, Vollna, GigRadar, Toggl Track
