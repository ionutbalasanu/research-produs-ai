# Domeniu: 05 constructori și meseriași (devize, oferte, programări)

> Stare: nu am putut deschide nicio pagină. Rețeaua acestei sesiuni permite doar registrele de pachete (npm, PyPI etc.) și nu are alte gazde permise (`allowed_hosts` gol). WebFetch și curl au eșuat pe toate site-urile încercate (lista e mai jos). WebSearch a funcționat, dar dă doar fragmente.
> Conform regulilor, o problemă intră în fișier doar cu minimum 2 surse deschise. Nu am nicio sursă deschisă, deci **nu am scris nicio problemă validă**.

## Problema 1: nu am găsit (nicio sursă deschisă)
- Cine o are: nu am găsit în surse
- Cât de des apare: nu am găsit în surse
- Ce face azi ca s-o rezolve și cât îl costă, în bani sau timp: nu am găsit în surse
- Soluții existente găsite, cu preț: nu am găsit în surse
- Surse deschise: niciuna
- Doar fragment: vezi secțiunea „Teme văzute doar în fragmente” de mai jos

## Teme văzute doar în fragmente (NU se numără, nu sunt probleme validate)
Le notez ca să poată fi verificate la o rundă cu acces la rețea. Niciun citat de aici nu a fost copiat dintr-o pagină deschisă. Datele lipsesc sau nu au fost verificate.

1. **Scrierea devizelor/ofertelor seara, după șantier.** Fragmente: rezumatul de căutare pentru handoff.ai/blog/remodeler-cut-20-hours-of-weekly-estimating-down-to-minutes (studiu de caz de vânzător, „close to 20 hours a week writing estimates”); mai multe postări dev.to ale aceluiași autor care promovează QuoteIQ (nu sunt independente). Sunt surse de marketing, nu voci de utilizatori.
2. **Clienți care dispar după ce primesc oferta (follow-up).** Fragment: un fir pe forumul comunității Jobber, „Why do clients disappear after asking for a quote?” (community.getjobber.com/discussions/operations-forum/why-do-clients-disappear-after-asking-for-a-quote/14304). Pagina e blocată, data nu se vede.
3. **Apeluri pierdute cât meseriașul e pe șantier.** Fragmente: doar bloguri de vânzători de recepționiști AI (callsphere.ai, vocphone.com, signpost.com etc.), cu cifre din sondaje pe care nu le-am verificat. Nu am găsit niciun fir de forum.
4. **Măsurători/cantități din planuri (takeoff) date în outsourcing.** Fragmente: anunțuri Upwork, de exemplu „Residential Material Takeoff: Framing & Windows for 3600 SF Home” și „Construction Estimator — Fast Turnaround, Residential Remodel (Photos/Field Measurements)”. Datele apar doar relativ („2 weeks ago”), deci sunt nevizibile.
5. **Șabloane Excel/Google Sheets de deviz vândute pe Etsy.** Fragmente: anunțuri Etsy (de exemplu 4583153611 „Remodeler Bundle…”, 827773435 „electrical contractor estimate template”). Prețurile apar doar în rezumatul căutării, deci nu sunt verificate.
6. **Aplicații deja lansate pentru oferte din poze sau voce.** Fragmente: Product Hunt „SnapQuote”; App Store „CostSnap”, „EZ Estimates AI”, „SimplyWise Cost Estimator”, „EchoBid”. Nu am verificat nici prețurile, nici datele.
7. **România: programe de devize și CRM pentru construcții.** Fragmente: zarinacrm.ro (licență lifetime, preț neverificat); un fir pe forum.softpedia.com, „calculator cost constructie casa la cheie” (pare din 2020, în afara intervalului).

## Surse blocate
Toate cererile au eșuat la nivel de rețea în sesiune: proxy-ul a răspuns cu 403 la CONNECT pentru curl, iar WebFetch a dat „getaddrinfo ENOTFOUND” sau „unable to fetch”.
- old.reddit.com (WebFetch: „unable to fetch”; curl: 403)
- www.reddit.com (curl, varianta .json: 403)
- community.getjobber.com (WebFetch: ENOTFOUND)
- www.capterra.com (WebFetch: ENOTFOUND; curl: 403)
- www.trustpilot.com (WebFetch: ENOTFOUND; curl: 403)
- www.contractortalk.com (WebFetch: ENOTFOUND; curl: 403)
- www.upwork.com (WebFetch: ENOTFOUND; curl: 403)
- www.producthunt.com (WebFetch: ENOTFOUND; curl: 403)
- curl a dat 403 și la: www.g2.com, apps.apple.com, play.google.com, www.fiverr.com, www.etsy.com, forum.softpedia.com, www.electriciantalk.com, dev.to, www.jlconline.com, wordpress.org, www.mumsnet.com, www.screwfix.com, community.screwfix.com, www.ukbusinessforums.co.uk, www.diynot.com, hn.algolia.com, news.ycombinator.com, www.plumbingzone.com

Ca runda să poată fi refăcută, aceste gazde trebuie permise în setările de rețea ale mediului cloud. Rețeaua mediului „Default” este „limited”, iar `allowed_hosts` e gol.

## Căutări făcute
Toate cu WebSearch. Au întors doar fragmente, nicio pagină deschisă.
- „contractor forum writing estimates takes hours every night 2025”
- „Jobber review "quotes" frustrating 2025 trustpilot”
- „"is there an app" contractors estimates from photos voice quote tradesman”
- „contractortalk.com estimating takes too long free estimates 2025”
- „tradesman missed calls while on job losing work forum 2025”
- „customers ghost after quote contractor forum follow up 2025”
- „program devize constructii firma mica pret forum 2025”
- „upwork construction estimator takeoff job posting 2025 residential”
- „contractor estimate template excel google sheets etsy”

Încercări de deschidere directă: old.reddit.com/r/Contractor/search (WebFetch); old.reddit.com și www.reddit.com search.json (curl); pagina de recenzii Jobber pe Capterra; recenziile Jobber pe Trustpilot (1-2 stele); pagina principală contractortalk.com; firul de pe forumul comunității Jobber; un anunț Upwork; SnapQuote pe Product Hunt. Toate au fost blocate.
