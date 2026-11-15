# Faza 1: acoperire

Data: 2026-11-15. Toate cele 30 de domenii sunt terminate. Total: 139 de probleme scrise. 137 au minimum 2 surse deschise valide, iar 2 rămân sub prag din cauza datei (14-P5 și 26-P3, vezi mai jos). Lista completă e în INDEX.md.

## Desfășurare

- **Lotul 1 (01-05), prima rulare: eșuat.** Mediul cloud avea rețea limitată, fără niciun site permis, deci nu s-a putut deschide nicio pagină. Domeniile 01-04 au scris fișiere cu „nu am găsit”. Domeniul 05 a fost oprit înainte de final.
- **Repornire unică pentru 01-05: reușită.** Utilizatorul a trecut rețeaua mediului pe acces nerestricționat, iar domeniile 01-05 au fost repornite o singură dată, conform regulii.
- **Unealta de citire.** WebFetch a rămas blocat în sesiune, așa că toți subagenții au citit paginile cu curl simplu, printr-un script comun. Nu s-a folosit niciun user-agent fals, nicio oglindă (mirror) și nicio arhivă pentru ocolirea blocajelor.
- **Domeniile 06-30: o singură rulare**, câte 5 subagenți în paralel. Niciunul n-a eșuat, deci n-a fost nevoie de repornire.

## Surse blocate în toate domeniile

Aceste site-uri au blocat cititorii automați în toate domeniile. Nu sunt repetate în tabelul de mai jos.
- reddit.com: pagina vine goală, pentru că se încarcă prin JavaScript (inclusiv old.reddit.com și varianta .json).
- g2.com, trustpilot.com, upwork.com, producthunt.com: 403 sau verificare anti-bot.
- fiverr.com: 403 sau captcha.

Consecință: lipsesc sursele de tip Reddit, recenziile G2/Trustpilot, anunțurile Upwork/Fiverr și lansările Product Hunt. Sursele folosite în locul lor sunt forumuri de profil, Capterra, Hacker News, wordpress.org, Shopify App Store, Chrome Web Store, fluxul oficial de recenzii App Store, comunitățile vendorilor, presa și portaluri românești.

## Pe domenii

| Domeniu | Stare | Probleme | Surse blocate în plus față de cele comune |
|---|---|---|---|
| 01 cabinete medicale și stomatologice | terminat (după repornire) | 4 | dentaltown.com, forums.opendental.com (fără conexiune), bzi.ro (429), lassie.ai (conținut doar prin JavaScript) |
| 02 contabili | terminat (după repornire) | 4 | accountingweb.co.uk, forum.softpedia.com, etsy.com, central.xero.com (pagină goală) |
| 03 avocați și notari | terminat (după repornire) | 6 | clio.com |
| 04 agenți imobiliari | terminat (după repornire) | 5 | quora.com, indiehackers.com, inman.com |
| 05 constructori și meseriași | terminat (după repornire) | 4 | forums.mikeholt.com, getjobber.com/pricing, hvac-talk.com (lista de fire nu s-a putut extrage) |
| 06 arhitecți și designeri de interior | terminat | 4 | quora.com, indiehackers.com, forums.autodesk.com, thebuildingcodeforum.com, etsy.com, apps.apple.com (429), forum.softpedia.com, capital.ro (429), d5render.com/pricing |
| 07 restaurante și cafenele | terminat | 5 | etsy.com, community.toasttab.com (Cloudflare), comunitatea Square (pagini goale) |
| 08 pensiuni, hoteluri mici, gazde | terminat | 6 | apps.apple.com (404), căutarea internă airhostsforum |
| 09 magazine online mici | terminat | 5 | căutarea HTML community.shopify.com; un link Capterra a arătat alt produs |
| 10 vânzători pe marketplace-uri | terminat | 3 | community.etsy.com (pagină goală), forum.softpedia.com, căutarea apps.shopify.com, ecommercebytes.com (site închis) |
| 11 saloane și frizerii | terminat | 5 | salongeek.com, quora.com, indiehackers.com |
| 12 fitness și antrenori | terminat | 6 | etsy.com, payhip.com, ptroadmap.beehiiv.com, quora.com |
| 13 profesori, meditatori, cursuri | terminat | 6 | mumsnet.com, thestudentroom.co.uk, forum.softpedia.com, quora.com, indiehackers.com, glassdoor.ie |
| 14 părinți | terminat | 5 | mumsnet.com, etsy.com, axios.com, fastcompany.com, theeverymom.com, bzi.ro (429) |
| 15 studenți și cercetători | terminat | 4 | academia.stackexchange.com, techcommunity.microsoft.com |
| 16 freelanceri creativi | terminat | 4 | dpreview.com, fredmiranda.com, creativecow.net, indiehackers.com, quora.com, weddingwire.com |
| 17 creatori de conținut și podcasteri | terminat | 5 | payhip.com, campaignlive.com, saasworthy.com, freesound.org, gumroad.com (pagini goale) |
| 18 agenții de marketing și web | terminat | 4 | indiehackers.com, quora.com, forum.squarespace.com, sitepoint.com/community, searchengineland.com, community.framer.com (fără răspuns) |
| 19 recrutare și HR | terminat | 5 | indiehackers.com, etsy.com, snagajob.com, qsrmagazine.com și alte câteva site-uri de presă |
| 20 transportatori și logistică | terminat | 4 | overdriveonline.com, otrucking.com, carrier411.com |
| 21 service-uri auto | terminat | 4 | corvetteforum.com, gmtnation.com (406) |
| 22 fermieri | terminat | 3 | backyardchickens.com, agriland.ie, tractorbynet.com, thefarmingforum.co.uk (anti-bot), bzi.ro (429) |
| 23 evenimente și nunți | terminat | 5 | forumurile weddingwire, theknot, weddingbee, hitched.co.uk; mumsnet.com, boards.ie, quora.com, indiehackers.com, etsy.com |
| 24 ONG-uri și asociații de proprietari | terminat | 5 | forum.softpedia.com, capital.ro (429), blog.candid.org, brig.ro, xpertbloc.ro (fără răspuns) |
| 25 proprietari care închiriază | terminat | 5 | forums.landlordzone.co.uk, accountingweb.co.uk, etsy.com |
| 26 traducători și interpreți | terminat | 4 | proz.com (toate subdomeniile), community.rws.com (pagină goală), translatorscafe.com, atanet.org, multilingual.com, quora.com, indiehackers.com |
| 27 consultanți și coachi | terminat | 3 | indiehackers.com, skool.com, kit.com (captcha), blogul paperbell.com, etsy.com, gumroad.com |
| 28 dezvoltatori independenți | terminat | 5 | community.upwork.com, indiehackers.com, freelancing.stackexchange.com, quora.com |
| 29 căutători de loc de muncă | terminat | 5 | teamblind.com, indiehackers.com, forum.softpedia.com, addons.mozilla.org, jobscan.co/pricing, tealhq.com/pricing |
| 30 casa și banii personali | terminat | 6 | bogleheads.org, forum.mrmoneymustache.com, forum.softpedia.com, quora.com, indiehackers.com, money.stackexchange.com, quicken.com, discuțiile github.com, community.monarchmoney.com (fără conexiune) |

## Probleme sub prag (scrise, dar fără 2 surse valide după regulă)

- **14-P5 (aplicații pentru părinți separați):** cele două recenzii App Store arată doar ziua și luna. Anul 2026 a fost dedus, deci sursele nu se numără.
- **26-P3 (oferte false pentru traducători):** o sursă are data vizibilă. A doua nu are data postării vizibilă și e datată doar printr-un e-mail din februarie 2026 citat în pagină.

## Criterii aplicate (de știut la triere)

- **Independență** = autori diferiți. Recenziile de pe aceeași pagină Capterra și firele diferite ale aceluiași forum au fost numărate separat dacă autorii diferă. Problemele care se sprijină pe un singur site sunt marcate în fișierele de domeniu, de exemplu 05-P3 (contractortalk), 11 (doar Capterra), 07-P1 și 07-P4 (doar Hacker News), 26-P4 (portalcontabilitate.ro).
- **Date relative.** BiggerPockets, forumul Amazon, Hacker News și Turnitin arată date de tipul „acum 2 luni”. Subagenții le-au transformat în date aproximative față de 2026-11-15 și au păstrat eticheta originală în fișier. La Hacker News, data exactă a fost luată de obicei din API-ul oficial.
- **Surse cu interes comercial.** Blogurile vendorilor și postările fondatorilor care își prezintă propriul tool sunt marcate în fișiere. Mai des apar în 02, 12, 16, 17, 19, 20, 22, 25, 28 și 30.
- **Obligații legale.** Au fost folosite cel mult o dată pe domeniu, în 11 domenii: 01, 07, 08, 13, 17, 19, 20, 24, 25, 26 și 28.
- **România.** Probleme cu surse românești există doar în 01, 07, 08, 13, 24 și 26. În celelalte domenii, căutările în română au întors mai ales pagini de vendori sau fire mai vechi de 18 luni, iar forum.softpedia.com a fost blocat.

## Verificarea citatelor (sesiunea principală)

După ce au terminat subagenții, un script a redeschis fiecare sursă numărată din toate cele 30 de fișiere și a căutat citatul în textul paginii.
- **Total surse numărate verificate: 531.**
- **522** au citatul găsit exact.
- **5** au fost confirmate manual: 3 recenzii App Store mutate pe pagina a doua a fluxului de recenzii (23) și 2 PDF-uri citite cu pdftotext (13, 14).
- **4** au citatul prescurtat cu „...” în fișier (08, 20, 29). Fragmentele dintre puncte apar în pagină.
- **0** citate negăsite.

Celelalte linii semnalate de script nu sunt surse numărate: pagini de prețuri, fragmente, site-uri blocate sau surse excluse pentru vechime.
