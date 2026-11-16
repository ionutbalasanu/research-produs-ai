# Faza 3, pasul 4: verificare independentă

Data: 2026-11-16. Au verificat doi subagenți noi, care nu au lucrat la pasul 3: unul pentru candidatele 01-04, altul pentru 05-08. Fiecare a redeschis sursele decisive ale fișelor (prețuri, nemulțumiri, reguli de canal, cursul BNR) cu `curl -sL` simplu. WebFetch a fost folosit doar unde curl a primit 403. Firele Notary Cafe au fost citite prin API-ul public Discourse. Fiecare citat a fost căutat în textul paginii, ca la verificarea din faza 1. Fișele nu au fost modificate de verificatori. Corecțiile au fost aplicate în sesiunea principală și sunt marcate în fișe cu „[corectat la verificarea independentă, pasul 4]".

## Rezultat pe scurt

| Candidată | Corespunde | Parțial | Nu corespunde | Neverificabil | Aritmetică |
|---|---|---|---|---|---|
| 01. RSVP nuntă | 15 | 0 | 0 | 4 (3 fluxuri RSS App Store goale azi + Ubersuggest) | corectă, două mici imprecizii corectate |
| 02. Poze invitați | 13 | 0 | 0 | 7 (6 fluxuri RSS App Store goale azi + Ubersuggest) | corectă |
| 03. Retururi Shopify | 17 | 1 | 0 | 1 (Ubersuggest) | corectă |
| 04. Chargeback Shopify | 20 | 0 | 0 | 1 (Ubersuggest) | corectă |
| 05. Plata notarilor de semnări | 16 | 0 | 0 | 0 | corectă |
| 06. Detention transport | 14 | 0 | 0 | 0 | două rotunjiri corectate |
| 07. Termene proprietari | 21 | 0 | 0 | 1 (Ubersuggest) | o rotunjire corectată |
| 08. CV România | 14 | 0 | 0 | 1 (Ubersuggest) | corectă; o rotunjire corectată |
| **Total** | **130** | **1** | **0** | **15** | |

## Ce înseamnă „neverificabil" aici

- **Fluxurile RSS App Store (01 și 02).** Au răspuns cu HTTP 200, dar fără nicio recenzie, la 7 reîncercări în ~20 de minute și o încercare prin WebFetch. Citatele din recenziile App Store nu au putut fi reconfirmate independent. Asta nu arată că sunt greșite. La 02 contează mai mult: toate cele 6 nemulțumiri noi din secțiunea 2 vin din aceste fluxuri. Ambele fișe au acum o notă la secțiunile 2 și 9.
- **Ubersuggest.** Volumele vin din conector, nu dintr-o pagină publică, deci nu se pot redeschide cu curl. Au fost obținute în aceeași zi, cu sursa și locația notate.
- **Cursul BNR.** XML-ul curs.bnr.ro/nbrfxrates.xml a dat eroare la primul apel. La reîncercare a confirmat 1 USD = 4,8428 lei, publicat pe 2026-11-13. E cursul folosit în toate fișele, unde fusese citit de pe cursbnr.ro.

## Corecții aplicate în fișe

| Fișă | Secțiune | Înainte | După |
|---|---|---|---|
| 01 | 5 (tabel) | 387,37 | 387,38 (79,99 × 4,8428); numărul de cumpărători rămâne 6 |
| 01 | 4 (Google Ads) | CPC 6-13 $ (31-65 lei) | CPC 6,40-13,38 $ (31-65 lei) |
| 01, 02 | 2 și 9 | (fără notă) | notă: fluxul RSS App Store gol la reverificare |
| 03 | 0 | „Return fees aren't deducted from refunds automatically" | „Return fees aren't automatically deducted from refunds." (textul exact din pagină; sensul e același) |
| 04 | 2 (Subtlejoys) | 2026-10-22 | 2026-10-22 (editat), cum apare în pagină |
| 06 | 5 | 3.000 lei = 619,47 USD | 619,48 USD |
| 06 | 5 | 417 curse | 417,2, deci 418 curse (417 × 0,99 = 412,83 $, sub țintă) |
| 07 | 5 | 412,99 $ | 412,98 $ (numerele de clienți rămân aceleași) |
| 08 | 5 | ≈ 1.265 clicuri | ≈ 1.266 clicuri |

Corecție nefăcută, notată: la 06, în citatul Pathmark din pagină, după „detention" urmează o virgulă, nu un punct. Sensul nu se schimbă.

**Nicio corecție nu schimbă concluzia vreunei fișe.**

## Detaliu pe surse

Tabelele de mai jos sunt rapoartele verificatorilor, nemodificate.

# Verificare independentă, faza 3 pasul 4: candidatele 01-04
Data verificării: 2026-11-16. Metodă: `curl -sL` simplu (fără user-agent fals), text extras din HTML, entități și ghilimele tipografice normalizate, grep pe citatul exact. WebFetch doar unde curl a primit 403 (help.shopify.com, a doua cerere) și ca a doua încercare pe un flux RSS gol. Fișele nu au fost modificate.

Observație comună: toate fluxurile RSS App Store notate în fișe (Zola 852691916, Joy 994411720, POV 1636032890 p.1 și p.2, Scene 6758879648, PixelParty 6760188393) au întors azi HTTP 200 cu feed gol (873-875 octeți, doar metadate, fără `entry`), la 7 încercări pe parcursul a ~20 de minute, plus o încercare prin WebFetch (confirmă: „no review entries"). Paginile apps.apple.com ale Joy și POV nu conțin citatele (au alte recenzii). De aceea toate nemulțumirile din App Store sunt „neverificabil" azi; nu înseamnă că sunt greșite.

Ubersuggest (conector MCP) nu e o pagină care se poate redeschide cu curl/WebFetch: marcat „neverificabil" la toate fișele.

---

## 01. RSVP și mesaje către invitații de nuntă

| # | Sursă (link) | Ce susține | Citat/preț căutat | Rezultat | Ce apare în pagină / corecție necesară |
|---|---|---|---|---|---|
| 1 | https://apps.apple.com/us/app/id852691916 | preț SMS Zola | „Premium SMS" $59.99 / $79.99; Seating Chart $14.99 | corespunde | „Seating Chart $14.99 ... Premium SMS $59.99 ... Premium SMS $79.99" (HTTP 200) |
| 2 | https://withjoy.com/help/en/articles/8346349-sending-email-and-reminder-messages | email gratuit Joy | „Email is free." | corespunde | găsit textual |
| 3 | https://withjoy.com/help/en/articles/14480210-send-text-messages-to-your-guests-with-messaging-plus | SMS Joy plată unică | „Messaging Plus is a one-time purchase that unlocks all SMS features in Joy" | corespunde | găsit textual; nici aici, nici pe /pricing nu apare un preț |
| 3b | https://withjoy.com/pricing (sec. 1) | plan de bază 0 $ | „$0", „Email is free" | corespunde | „Joy is free to use. $ 0 /mo"; „Messaging Plus" nu apare pe pagina de prețuri (coerent cu „preț neafișat") |
| 4 | https://www.theknot.com/gs/guest-list | listă gratuită | „Our free guest list tool lets you easily manage your wedding guest list" | corespunde | găsit textual |
| 5 | https://textmywedding.com/ | preț, RSVP integrat, cifre vânzător | „One-time plans starting from $19."; „The built-in RSVP feature lets you collect and track responses"; „26,000 couples", „2.5 million texts"; 299 $ | corespunde | toate găsite; pagina mai afișează și „2,500,000+ messages sent" |
| 6 | https://textmyguests.com/pricing | preț per eveniment | „Standard $34 per event"; 59/119/229 $ | corespunde | „Standard $34 per event ... Most Popular $59 per event ... Economy $119 per event ... Deluxe" |
| 7 | https://weddingtxt.com/ | preț și import | „One-time plans from $9. Import from Zola or The Knot"; 14 $/lună | corespunde | găsit textual; „$14 Per month Unlimited Texts" |
| 8 | https://itunes.apple.com/us/rss/customerreviews/page=1/id=852691916/sortby=mostrecent/json | nemulțumire Zola 2026-11-07 | „the system would not send text messages and instead gave an error message" | neverificabil | HTTP 200, feed fără recenzii (873 octeți), 7 încercări + WebFetch |
| 9 | idem | nemulțumire Zola 2026-07-03 | „now I can’t even properly use the guest messaging feature I’ve paid for" | neverificabil | idem |
| 10 | https://itunes.apple.com/us/rss/customerreviews/page=1/id=994411720/sortby=mostrecent/json | nemulțumire Joy 2026-01-14 | „if you are really trying to do a digital wedding you want text messaging" | neverificabil | HTTP 200, feed gol; nici pagina apps.apple.com/us/app/id994411720 nu conține citatul |
| 11 | https://stripe.com/en-ro/pricing | cost card | 3,15% + 1,00 leu, +2% conversie | corespunde | „3.15% + 1.00lei for international cards + 2% if currency conversion is required" |
| 12 | https://www.twilio.com/en-us/sms/pricing/us | cost SMS, 10DLC | „$0.0083 per 160-character segment"; „subject to registration onboarding fees"; taxe operator 0,0035-0,005 $ | corespunde | găsite; taxe operator SMS outbound long code: AT&T $0.0035, T-Mobile $0.0045, Verizon $0.005, US Cellular $0.005, alții $0.0042 |
| 13 | https://www.cursbnr.ro/ | curs | „Foloseşte cursul BNR din 13.11.2026", „1 USD = 4.8428 Lei" | corespunde | găsit textual; confirmat și de https://curs.bnr.ro/nbrfxrates.xml (USD 4.8428, 2026-11-13) |
| 14 | Ubersuggest MCP | volume căutare | 12.100 / 30 / 20 | neverificabil | nu e pagină web; nerefăcut |
| s1 | https://www.zola.com/faq/how-does-zolas-premium-guest-messaging-feature-work | SMS Zola plătit | „You'll need to upgrade to a paid plan" | corespunde | „Want to send a message to your whole guest list? You'll need to upgrade to a paid plan." |
| s2 | https://developer.apple.com/support/enrollment/ | taxă App Store | „annual fee is 99 USD" | corespunde | găsit textual |
| s3 | https://hn.algolia.com/api/v1/items/48372766 și /50424013 (sec. 3) | DIY RSVP, concurent nou | „a wedding website with RSVP functionality"; withthislink.com | corespunde | 2026-06-02 și 2026-11-09, texte găsite |

Aritmetică: corectă. 2.000 / 4,8428 = 412,98 $; 22 / 13 / 7 / 6 cumpărători corecți; abonament 30 corect și tratat separat de plata unică; Stripe 15,96 lei corect; Twilio 750 × 0,0133 = 9,98 $ corect; Google Ads 77-161 clicuri corect. Două imprecizii minore: (a) 79,99 × 4,8428 = 387,38 lei (fișa: 387,37; rezultatul 6 nu se schimbă); (b) „CPC 6-13 $ (31-65 lei)": 6 $ = 29,06 lei, iar 31 lei corespunde lui 6,40 $; maximul din tabel e 13,38 $.
Rezumat: 15 corespunde, 0 parțial, 0 nu corespunde, 4 neverificabil (3 RSS + Ubersuggest)
Corecții propuse:
- Sec. 5, tabel: „387,37" → „387,38".
- Sec. 4, Google Ads: „la CPC 6-13 $ (31-65 lei)" → „la CPC 6,40-13,38 $ (31-65 lei)".
- Opțional, sec. 2 / sec. 9 pp. 8-10: adăugat „(flux RSS gol la reverificarea din 2026-11-16; citatele nu au putut fi reconfirmate)".

---

## 02. Colectarea pozelor făcute de invitați la nuntă

| # | Sursă (link) | Ce susține | Citat/preț căutat | Rezultat | Ce apare în pagină / corecție necesară |
|---|---|---|---|---|---|
| 1 | https://www.guestcam.co/pricing | preț + produs identic | „Standard is $49 and Premium is $97. No recurring fees."; tăiat $55/$110; MagicFind $45; telefon $30; „one-time fee, per event" | corespunde | toate găsite („Standard $ 55 49 one-time fee, per event", „Premium popular $ 110 97", „Dedicated Audio Guestbook Phone Number $ 30") |
| 2 | https://www.guestcam.co | fără aplicație, fără cont | „No app download, no sign-up."; „Original quality"; „unlimited uploads"; „20M+" | corespunde | toate găsite |
| 3 | https://guestpix.com/wedding-pricing/ | preț + produs identic | „NO APP NEEDED + NO GUEST REGISTRATION"; „From US$49" | corespunde | găsite; pagina mai spune „Starting price US$39–49" |
| 4 | https://kululu.com/pricing | produs identic | „No Apps Required"; „50% off ON ALL PLANS" | corespunde | găsite; prețuri în iframe JS, invizibile (coerent cu fișa) |
| 5 | https://pov.camera/pricing | preț per nivel | „Up to 10 guests Free"; 4.99/14.99/34.99/64.99/89.99; Business 49.99-249.99 | corespunde | „Up to 10 guests Free" în text; valorile în datele paginii (ex. „100",34.99) |
| 6 | https://apps.apple.com/us/app/id779463311 | preț Photo Swap | „Gold $29.99" și celelalte | corespunde | „Gold $29.99, Platinum $39.99, Gold Subscription $33.99, 3 Month Extension $12.99, Platinum Subscription $40.99" |
| 7 | https://www.wedshoots.com/us | alternativă gratuită | „¡y todo gratis!" | corespunde | găsit (pagină în spaniolă) |
| 8 | https://itunes.apple.com/us/rss/customerreviews/page=1/id=1636032890/sortby=mostrecent/json | nemulțumire POV | „Pretty misleading with the no download advertising when you have to make an account" | neverificabil | HTTP 200, feed gol (875 octeți), 7 încercări |
| 9 | idem | nemulțumire POV | „Many people had difficulty using the app due to passwords or signal" | neverificabil | idem |
| 10 | .../page=2/id=1636032890/... | nemulțumire POV | „I paid for the most expensive package so guests would be allocated 25 photos." | neverificabil | idem; pagina apps.apple.com a POV are alt text cu „25 photos", nu acest citat |
| 11 | idem p.2 | nemulțumire POV | „Don’t waste your time trying to register." | neverificabil | idem |
| 12 | .../id=6758879648/... | nemulțumire Scene | „Great app but lots of bugs" | neverificabil | idem |
| 13 | .../id=6760188393/... | nemulțumire PixelParty | „uploads frequently failed, and the site repeatedly crashed" | neverificabil | idem |
| 14 | https://hn.algolia.com/api/v1/items/46764911 | semnal încredere | „Use a login" (2026-01-26) | corespunde | răspuns „opendomain", 2026-01-26T13:06 |
| 15 | https://hn.algolia.com/api/v1/items/47605988 | concurent identic | „no app download, no account, no friction" | corespunde | găsit, 2026-04-01 |
| 16 | https://stripe.com/en-ro/pricing | cost | „3.15% + 1.00lei for international cards" | corespunde | găsit |
| 17 | https://developer.apple.com/programs/whats-included/ | regulă canal | „99 USD per membership year" | corespunde | găsit |
| 18 | https://developer.apple.com/app-store/small-business-program/ | regulă canal | „reduced commission rate of 15% on paid apps" | corespunde | găsit, inclusiv „15% on paid apps and Apple In-App Purchases" |
| 19 | https://www.cursbnr.ro/ | curs | „1 USD = 4.8428 Lei" | corespunde | găsit (și EUR 5.3498, GBP 6.4023) |
| 20 | Ubersuggest MCP | volume | 880 / 880 / 590 / 320 / 30 | neverificabil | nu e pagină web |

Aritmetică: corectă. 413/19 = 21,7 → 22; 413/29 = 14,2 → 15; 413/49 = 8,4 → 9; 29 $ = 140,44 lei; Stripe 5,42 / 8,23 lei; 15 vânzări = 81-123 lei; 5.000 lei = 1.032 $; 247 și 197 clicuri; 15/247 ≈ 6%. Doar plată unică, model tratat consecvent.
Rezumat: 13 corespunde, 0 parțial, 0 nu corespunde, 7 neverificabil (6 RSS + Ubersuggest)
Corecții propuse:
- Niciuna de conținut. Opțional, sec. 2 / sec. 9 pp. 8-13: notă „flux RSS gol la reverificarea din 2026-11-16". Atenție: toate cele 6 nemulțumiri ale fișei depind de aceste fluxuri, deci secțiunea 2 rămâne nereconfirmată independent.

---

## 03. Cererile de retur gestionate manual în magazinele Shopify mici

| # | Sursă (link) | Ce susține | Citat/preț căutat | Rezultat | Ce apare în pagină / corecție necesară |
|---|---|---|---|---|---|
| 1 | https://help.shopify.com/en/manual/fulfillment/managing-orders/returns/self-serve-returns/setup | funcție nativă | „You review and decide on every request." | corespunde | găsit |
| 2 | același link | limită nativă | „Exchanges can't be requested in self-serve returns"; „Legacy customer accounts don't display return or cancellation options." | corespunde | ambele găsite |
| 3 | https://help.shopify.com/en/manual/fulfillment/managing-orders/returns/return-rules | reguli native | „Select a preset return window, or enter a custom number of days." | corespunde | găsit |
| 3b | același link (sec. 0) | taxe neautomate | „Return fees aren't deducted from refunds automatically" | parțial | pagina spune: „Return fees aren't automatically deducted from refunds." (ordine diferită a cuvintelor; sens identic) |
| 4 | https://community.shopify.com/t/allow-customers-to-upload-photos-when-submitting-a-return-request/637828 | lipsă poze | „Currently there is no image upload field in the native return request flow." | corespunde | postarea twecoop, 2026-06-17 |
| 5 | https://apps.shopify.com/returns-center-by-aftership | preț | „Includes 20 returns/month; $0.50 per extra return."; 19 $ / 119 $; „Revenue share"; 4,7 din 1.547 | corespunde | toate găsite |
| 6 | https://apps.shopify.com/yanet-return-and-exchange | preț | „80 free requests per month, only $0.2 per extra request"; 9,99 $ / 29,99 $; „Automation Approval" | corespunde | găsite |
| 7 | https://apps.shopify.com/loopback-returns | preț, concurent | „Unlimited return requests"; 9 $; lansat 24.09.2026 | corespunde | găsite („September 24, 2026") |
| 8 | https://apps.shopify.com/opus-returns-exchanges | concurent gratuit | „Guest-order return portal with customer-requested exchanges." | corespunde | găsit; „August 14, 2026" |
| 9 | https://apps.shopify.com/categories/orders-and-shipping-returns-and-warranty-returns-and-exchanges/all | saturație | „285 apps" | corespunde | găsit |
| 10 | https://apps.shopify.com/returns-center-by-aftership/reviews?ratings%5B%5D=1&sort_by=newest | nemulțumire | „terrible UX, overly complicated setup, unintuitive design, and useless support" (2026-11-04) | corespunde | „November 4, 2026"; și „not worth it if you're a small business" (October 2, 2026, Kitty Kabana) și „Each stage they said I could not get what I wanted unless I upgraded." (Edited October 28, 2026) găsite |
| 11 | https://apps.shopify.com/loop-returns/reviews?ratings%5B%5D=2&sort_by=newest | nemulțumire | „I could not test the app, because an onboarding call is mandatory." (2026-02-02) | corespunde | „February 2, 2026 ... SAINT SKEI Cyprus"; și „It took us weeks to setup...and we still haven't correctly configured it." (December 9, 2025, HealthyFeetStore.com) găsit |
| 12 | https://community.shopify.com/t/feature-request-improve-self-serve-returns-for-merchants/644509 | nemulțumire | „Right now, it doesn’t fully solve the returns workflow" | corespunde | twecoop, 2026-07-01 |
| 13 | https://community.shopify.com/t/built-a-small-returns-app-for-stores-whose-customers-never-log-in-looking-for-honest-feedback/687215 | slăbește ipoteza | „the work doesn’t end at approval"; „guest-checkout orders end up as emails" | corespunde | ambele în același comentariu ahsandoesntcare, 2026-09-25 (firul e deschis de Tareq_Loopback) |
| 14 | https://shopify.dev/docs/apps/launch/distribution/revenue-share | regulă canal | „one-time fee of $19 USD per Partner account"; „You keep 100% of your first $1,000,000 USD..."; 15% peste; „Regulatory Operating Fee" | corespunde | găsite; tabel „First $1,000,000 USD 0% / Above $1,000,000 USD 15%" |
| 15 | același link | regulă canal | „All billing is subject to a 2.9% processing fee" | corespunde | găsit |
| 16 | https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements | regulă canal | „Apps that use off-platform billing cannot be distributed through the Shopify App store" | corespunde | găsit |
| 17 | https://www.cursbnr.ro/ | curs | „1 USD = 4.8428 Lei" | corespunde | găsit |
| s1 | Ubersuggest MCP (sec. 4) | volume | 480 / 110 / 40 / 50 | neverificabil | nu e pagină web |

Aritmetică: corectă. 413/9 = 45,9 → 46; 413/9,99 = 41,3 → 42; 413/19 = 21,7 → 22; 413/29 = 14,2 → 15; 19 $ = 92 lei. Model abonament, clienți activi, tratat corect; nu e amestecat cu plată unică.
Rezumat: 17 corespunde, 1 parțial, 0 nu corespunde, 1 neverificabil (Ubersuggest)
Corecții propuse:
- Sec. 0, tabel, rândul 4: „„Return fees aren't deducted from refunds automatically" (taxele se scad manual la rambursare)" → „„Return fees aren't automatically deducted from refunds." (taxele se scad manual la rambursare)". Marcajul poate rămâne „verificat în sursă" (acum citit și cu curl, nu doar WebFetch).

---

## 04. Dosarul de dovezi pentru chargeback în magazinele Shopify mici

| # | Sursă (link) | Ce susține | Citat/preț căutat | Rezultat | Ce apare în pagină / corecție necesară |
|---|---|---|---|---|---|
| 1 | https://curs.bnr.ro/nbrfxrates.xml | curs | `<Rate currency="USD">4.8428</Rate>`, publicat 2026-11-13 | corespunde | găsit; și EUR 5.3498, GBP 6.4023 |
| 2 | https://apps.shopify.com/chargeflow | preț | „Automation: 25% of recovered chargebacks."; „Prevent: 1,000 free then $0.10/order."; 4,5 din 439 | corespunde | găsite |
| 3 | https://apps.shopify.com/disputifier | preț | „CB Fighting: 20% of won back revenue"; „CB Alerts: from $17-$27.50/alert"; 4,6 din 140 | corespunde | găsite |
| 4 | https://apps.shopify.com/rekover | preț, lansare | „$9.99 / month"; „Launched June 30, 2026"; „Unlimited Chargebacks"; „Shopify Payments dispute evidences" | corespunde | găsite |
| 5 | https://apps.shopify.com/countercase | preț | „Standard $29 / month"; lansat 25.08.2026 | corespunde | găsite |
| 6 | https://apps.shopify.com/disputr | preț | „$5 per evidence packet generated"; 29 $ / 49 $; lansat 01.06.2026 | corespunde | găsite |
| 7 | https://apps.shopify.com/backstop | preț, lansare | „Pro $19 / month"; „Launched September 10, 2026" | corespunde | găsite |
| 8 | https://apps.shopify.com/disputes-co-pilot | preț | „Pro $9 / month"; „Shopify form filled in one click"; 5 oct. 2026 | corespunde | găsite |
| 9 | https://help.shopify.com/en/manual/payments/chargebacks/chargebacks-in-admin | alternativă gratuită | „Shopify automatically collects evidence and sends it to the credit card company"; „Include Shopify-generated insights to strengthen case (recommended)" | corespunde | ambele găsite (curl: prima cerere 403, a doua 200) |
| 10 | https://help.shopify.com/en/manual/payments/chargebacks/chargeback-process | taxa | „If you win the chargeback, then the fee is returned to you."; 15 $ SUA, 10 £ UK | corespunde | curl 403 de două ori; citit prin WebFetch: citat exact, „$15 USD", „£10 GBP" |
| 11 | https://apps.shopify.com/chargeflow/reviews?ratings%5B%5D=1&ratings%5B%5D=2&ratings%5B%5D=3&sort_by=newest | nemulțumire | „they charged me for disputes I won by myself" (2026-10-15, xLumina) | corespunde | „October 15, 2026 ... xLumina Austria" |
| 12 | același link | nemulțumire | „all the cases i won have been cases where they filled minimum evidence" (2026-09-18) | corespunde | „September 18, 2026 tldr ..." Code Breaker Labs; și „the final figure is entirely at the discretion of the service provider" (Subtlejoys, afișat „Edited October 22, 2026") și „Of all the chargebacks ... I've won 0." (September 18, 2026, Earthtones) găsite |
| 13 | https://apps.shopify.com/disputifier/reviews?ratings%5B%5D=1&ratings%5B%5D=2&ratings%5B%5D=3&sort_by=newest | nemulțumire | „Getting out of this app has been a real pain." (2026-10-28) | corespunde | „October 28, 2026"; și „It costed $317 for just two orders..." (June 17, 2026, BTendance) găsit |
| 14 | https://community.shopify.com/t/is-there-a-way-to-auto-fight-chargebacks/712425 | nemulțumire | „i’m spending hours every week on them"; „a bit nervous it will submit junk the lose cases i could’ve won" | corespunde | jgkid00, 2026-11-09; ambele găsite |
| 15 | https://community.shopify.com/t/free-browser-only-chargeback-evidence-organizer-for-shopify-merchants-optional-19-prevention-kit/675036 | slăbește ipoteza | „the merchant is not starting from zero" | corespunde | găsit; comentatorul lumine, fir din 2026-08-31 |
| 16 | https://shopify.dev/docs/apps/launch/distribution/revenue-share | regulă canal | „a one-time fee of $19 USD per Partner account" | corespunde | găsit |
| 17 | același link | regulă canal | „All billing is subject to a 2.9% processing fee and applicable sales tax." | corespunde | găsit |
| 18 | https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements | regulă canal | „Your app must use Shopify App Pricing or the Shopify Billing API"; „can reject an app at their discretion" | corespunde | ambele găsite |
| 19 | https://shopify.dev/docs/api/usage/access-scopes | regulă API | „Shopify grants these scopes to individual apps."; „Dispute or chargeback management must be a core part of what your app does" | corespunde | găsite, plus `read_shopify_payments_disputes` și `write_shopify_payments_dispute_evidences` |
| 20 | https://community.shopify.com/guidelines | regulă forum | „App recommendations are allowed only on the Ask and Offer board."; „Clearly disclose any ownership" | corespunde | găsite, plus „Recommending or promoting apps outside the Ask and Offer board" |
| s1 | Ubersuggest MCP (sec. 4) | volume | 320 / 90 / 30 / 0 | neverificabil | nu e pagină web |

Aritmetică: corectă. 2.000 / 4,8428 = 412,98 $; 9,99 $ = 48,38 lei → 42; 19 $ = 92,01 lei → 22; 29 $ = 140,44 lei → 15; procent 25%: 8.000 lei = 1.652 $, 74,49 £ × 6,4023 = 476,91 lei → 16,8 → 17 dispute; 20%: 10.000 / 476,91 = 21; plată pe dosar 5 $ = 24,21 lei → 83; 2,9% din 2.000 = 58 lei. Cele trei modele (abonament, procent, plată pe dosar) sunt tratate separat, corect.
Rezumat: 20 corespunde, 0 parțial, 0 nu corespunde, 1 neverificabil (Ubersuggest)
Corecții propuse:
- Minoră, opțională: sec. 2, rândul Subtlejoys: „2026-10-22" → „2026-10-22 (editat)" (pagina afișează „Edited October 22, 2026").

---

## Rezumat general
| Candidată | Corespunde | Parțial | Nu corespunde | Neverificabil | Aritmetică |
|---|---|---|---|---|---|
| 01 RSVP nuntă | 15 | 0 | 0 | 4 | corectă (2 imprecizii de rotunjire/interval) |
| 02 Poze invitați | 13 | 0 | 0 | 7 | corectă |
| 03 Retururi Shopify | 17 | 1 | 0 | 1 | corectă |
| 04 Chargeback Shopify | 20 | 0 | 0 | 1 | corectă |

Nicio sursă „nu corespunde". Toate prețurile și regulile de canal verificabile au fost găsite azi. Singurul punct slab: nemulțumirile din App Store (01 și 02) nu au putut fi reconfirmate, pentru că fluxurile RSS oficiale sunt goale azi; la 02, întreaga secțiune 2 depinde de ele.

# Verificare independentă, faza 3 pasul 4: candidatele 05-08

Verificat: 2026-11-16. Metodă: `curl -sL` simplu (fără user-agent fals), text extras din HTML cu entitățile decodate și ghilimelele tipografice normalizate, apoi căutare exactă a citatului. Firele Notary Cafe citite prin API-ul public Discourse (`/t/<id>.json`). Toate cele 59 de URL-uri au răspuns HTTP 200. Singura excepție temporară: https://curs.bnr.ro/nbrfxrates.xml a întors la primul apel o pagină „Error" (HTTP 200), iar la reîncercare a dat cursul corect. Paginile descărcate sunt în scratchpad/v58/.

## 05. Notarii de semnări care urmăresc plata facturilor

| # | Sursă (link) | Ce susține | Citat/preț căutat | Rezultat | Ce apare în pagină / corecție necesară |
|---|---|---|---|---|---|
| 1 | https://forum.notarycafe.com/t/quick-survey-how-do-you-track-who-owes-you-90-seconds/55458 | test anterior, răspuns rece | „Don't pay for any software when a spreadsheet works fine for me." | corespunde | postarea #6, johnsonps306, 2026-02-28. Sondajul (postarea #1) e din 2026-02-27, postarea #2 e discourse_ai_spam cu conținut gol. Găsite și „Better take a look at Notary Gadget..." (#4) și „I'd never switch." (#7, despre propria foaie de calcul) |
| 2 | https://www.vrep.org/signingpayday-survey | oferta testată | „If a $9/month app showed you exactly who owes you" | corespunde | „Question 4 of 5 If a $9/month app showed you exactly who owes you and how late they are" |
| 3 | https://forum.notarycafe.com/guidelines | regulă de canal | „Unsolicited advertisements for services or businesses is not allowed." | corespunde | text identic |
| 4 | https://www.notaryrotary.com/viewtext.asp?displaytype=forumicons | regulă de canal | „Do not advertise your own products or services without prior approval." | corespunde | text identic, secțiunea „I. Advertising" |
| 5 | https://forum.notarycafe.com/about.json | mărimea comunității | „active_users_30_days":739 | corespunde | 739; și „users_count":20219 |
| 6 | https://notaryassist.com/ | preț | „Monthly cost is $8.99, Annually cost is $95.00" | corespunde | identic, plus „Storage Only $50.00 per Year". Găsite și „how long to receive payment", „track unpaid invoices" |
| 7 | https://www.notarygadget.com/pricing | preț | „$11.95 per month billed monthly cancel anytime" | corespunde | identic. Prețul anual e într-o imagine (Graphics/Website/999.png), cum spune fișa |
| 8 | https://www.venbooks.com/pricing | preț | „Monthly $ 9 /month" | corespunde | identic; „Annual $ 100 /year" |
| 9 | https://www.capterra.com/p/10050796/NotaryNext/ | preț și funcție | „Overdue payment reminders automate follow-ups at set intervals." | corespunde | identic; „Starting price $ 15 Flat Rate, Per Month"; „Overdue invoice escalation" |
| 10 | https://www.closewise.com/pricing/ | preț | „Pro $15 /month" | corespunde | identic; Pro+ 40 $/lună |
| 11 | https://forum.notarycafe.com/t/successful-signings-still-not-paying/58403 | nemulțumire | „Did a job June 9 that was paid September 12." | corespunde | postarea #9, 2026-10-12. Și #12 („I kept putting comments on Snapdocs every day and she sent payment"), #13 („I have a list of companies that don't pay") |
| 12 | https://forum.notarycafe.com/t/a360-closeclear-non-payment/57739 | slăbește mementourile | „I've never found daily emails effective" | corespunde | postarea #6, 2026-08-17; #5 „pestering them daily is unprofessional" |
| 13 | https://forum.notarycafe.com/t/collection-referral/55168 | ce funcționează | „Try letting Title know you haven't been paid." | corespunde | postarea #8, 2026-01-28 |
| 14 | https://forum.notarycafe.com/t/coast2coast-signing-service-paymentt-issues/58475 | nemulțumire | „You have to stay on top of them until they pay you" | corespunde | postarea #2, 2026-10-14; #1 „I have yet to receive payment for any of them." |
| 15 | https://stripe.com/en-ro/pricing | cost direct | „3.15% + 1.00lei for international cards" | corespunde | „3.15% + 1.00lei for international cards + 2% if currency conversion is required" |
| 16 | https://curs.bnr.ro/nbrfxrates.xml | curs | `<Rate currency="USD">4.8428</Rate>` | corespunde | 4.8428, PublishingDate 2026-11-13 (primul apel a dat o pagină „Error", al doilea a mers) |

Aritmetică: corectă. 2.000 / 4,8428 = 412,98, deci 413 $. 413/9 = 45,9 → 46; 413/11,95 = 34,6 → 35; 413/15 = 27,5 → 28; 413/95 = 4,35 → 5 abonamente anuale noi pe lună. Plata anuală e tratată separat de abonamentul lunar, corect. Stripe la 9 $ = 43,59 lei: 3,15% = 1,37 + 1,00 = 2,37 lei (5,4%), cu conversie +0,87 lei (7,4%): corect. 46 / 739 = 6,2%: corect.

Rezumat: 16 corespunde, 0 parțial, 0 nu corespunde, 0 neverificabil

Corecții propuse: niciuna.

## 06. Dovada timpului de așteptare (detention) refuzată de brokeri

| # | Sursă (link) | Ce susține | Citat/preț căutat | Rezultat | Ce apare în pagină / corecție necesară |
|---|---|---|---|---|---|
| 1 | https://www.thetruckersreport.com/truckingindustryforum/posts/13451555/ | fir de validare / contraargument | „Before I build anything I want to know if this is actually useful to real drivers."; „Your ELD will show everything you need." | corespunde | ambele identice; răspunsul wichris datat Apr 20, 2026 |
| 2 | https://www.thetruckersreport.com/truckingindustryforum/posts/13457459/ | contraargument | „is not going to pay to you no matter what."; „The answer is not an app," | corespunde | ambele identice; chimbotano și Opendeckin, Apr 21, 2026 |
| 3 | https://www.thetruckersreport.com/truckingindustryforum/threads/whats-the-1-reason-your-detention-claims-get-denied.2529156/page-2 | sondajul pornit de un dezvoltator | „The tool I'm envisioning isn't a new billing system." | corespunde | identic; ron.oruganti, Aug 12, 2025 |
| 4 | https://www.thetruckersreport.com/truckingindustryforum/threads/detention-and-our-obligations.2543082/ | nemulțumire | „I'm getting no response from the broker or agent concerning detention." | corespunde | identic; MABYMACA, Jun 30, 2026 |
| 5 | https://www.thetruckersreport.com/truckingindustryforum/threads/pathmark-transportation-mc-number-168257.2543523/ | nemulțumire | „They then refused to pay any layover or detention." | corespunde | în pagină: „They then refused to pay any layover or detention, hiding behind a sneaky "no layover on produce" clause". Cuvintele sunt identice, doar punctul final e pus de fișă în locul virgulei. OlenaB, Jul 13, 2026 |
| 6 | https://www.thetruckersreport.com/truckingindustryforum/posts/13474722/ | nemulțumire | „TQL were masters at NOT paying detention in my experience." | corespunde | identic; FloridaRetired, May 26, 2026 |
| 7 | https://bubba.ai/problems/broker-wont-pay-detention | contraargument (vânzător) | „Most unpaid detention is unclaimed rather than refused." | corespunde | identic; „updated: 7 October 2026" (dateModified 2026-10-07) |
| 8 | https://apps.apple.com/app/id6502769929 | preț | „Per Load $0.99" / „Monthly $39.99" | corespunde | „In-App Purchases Yes Per Load $0.99 Monthly $39.99", DMRG LLC |
| 9 | https://apps.apple.com/us/app/rigright/id6761784949 | preț și funcție | „Detention Tracker" / Driver Pro „$24.99" | corespunde | „Detention Tracker - one-tap clock (liniuța lungă din pagină redată ca „-"), evidence builder and claim generator"; „Driver Pro Yearly $299.99 Driver Pro $24.99"; „Fleet Owner $69.99" |
| 10 | https://apps.apple.com/us/app/id6807165625 | preț | GetDockPay Pro „$24.99" lunar, „$239.99" anual | corespunde | „Pro ($24.99 a month or $239.99 a year)" |
| 11 | https://www.thetruckersreport.com/truckingindustryforum/help/terms | regulă de canal | „No Advertising." | corespunde | „2. No Advertising. Promoting your website or businesses will result in your account being banned." |
| 12 | https://developer.apple.com/app-store/review/guidelines/ | regulă de canal | „Don't submit apps that are indistinguishable from what's already widely available."; „background services for their intended purposes" | corespunde | ambele identice (4.3(b) și 2.5.4) |
| 13 | https://developer.apple.com/app-store/small-business-program/ | cost | „reduced commission rate of 15% on paid apps and Apple In-App Purchases" | corespunde | identic |
| 14 | https://www.truckertools.com/three-ways-to-get-detention-pay/ | alternativă gratuită | „free app for load tracking" | corespunde | „Trucker Tools free app for load tracking" |

Aritmetică: greșită în două detalii mici, concluziile nu se schimbă.
- 3.000 / 4,8428 = 619,476, deci 619,48 USD, nu 619,47 (fișa a trunchiat). 619,48 / 24,99 = 24,8 → 25, corect.
- 412,98 / 0,99 = 417,2, deci trebuie 418 curse plătite (417 × 0,99 = 412,83 $, sub țintă).
- Restul e corect: 412,98 / 24,99 = 16,5 → 17; / 39,99 = 10,3 → 11; / 29,99 = 13,8 → 14 cumpărători noi pe lună; 17 × 24,99 = 424,83 $, minus 15% = 361,11 $; 99 / 12 = 8,25 $. Plata unică (SherHaul) e tratată separat de abonament, corect.

Rezumat: 14 corespunde, 0 parțial, 0 nu corespunde, 0 neverificabil

Corecții propuse:
- Secțiunea 5, vechi: „3.000 lei = 619,47 USD/lună." → nou: „3.000 lei = 619,48 USD/lună."
- Secțiunea 5, vechi: „412,98 / 0,99 = 417 curse plătite pe lună." → nou: „412,98 / 0,99 = 417,2, deci 418 curse plătite pe lună."
- Opțional, secțiunea 2 și 9 (#5): citatul se poate nota „They then refused to pay any layover or detention," (cu virgulă, ca în pagină) sau se poate lăsa așa; nu schimbă sensul.

## 07. Termenele proprietarilor care închiriază

| # | Sursă (link) | Ce susține | Citat/preț căutat | Rezultat | Ce apare în pagină / corecție necesară |
|---|---|---|---|---|---|
| 1 | https://www.cursbnr.ro/ | curs | „1 USD = 4.8428 Lei" | corespunde | „Cursul valutar BNR comunicat în 13 noiembrie 2026 ... 1 USD = 4.8428 Lei" (confirmat și de curs.bnr.ro/nbrfxrates.xml) |
| 2 | https://www.rentredi.com/pricing | preț | „$12/month" (anual), „$29.95/month" (lunar) | corespunde | „Annual Plan $12 /month total ... Billed Annually"; „Monthly Plan $29 . 95 /month total Billed monthly"; „6-Month Plan $20 /month total". Doar formatarea diferă |
| 3 | https://rentredi.com/blog/rentredi-launches-alerts-that-help-landlords-proactively-plan-renewals-and-reduce-vacancies/ | funcție | „sends an email alert to landlords when any lease is set to expire within 90 days" | corespunde | identic |
| 4 | https://www.landlordstudio.com/pricing | preț și funcție | „Automated lease expiry reminders" (Pro 15 $/lună) | corespunde | „Pro $15.00 /mo", „Pro Plus $35.00 /mo"; rândul „Automated lease expiry reminders: Not included / Included / Included" |
| 5 | https://www.turbotenant.com/pricing/ | preț | „Starting at $12.42/month" | corespunde | identic |
| 6 | https://www.stessa.com/pricing/ | preț și funcție | „Automated reminders and late fees" | corespunde | identic |
| 7 | https://www.baselane.com/pricing | preț și funcție | „Automated rent, reminders, and late fees" | corespunde | identic |
| 8 | https://www.avail.com/pricing | preț | „Unlimited Plus $9/unit" | corespunde | „Unlimited Plus $9/unit Per Month" |
| 9 | https://apps.apple.com/us/app/epitropos/id6757116610 | preț | „Epitropos Lifetime $1.99" | corespunde | identic |
| 10 | https://apps.apple.com/us/app/id6761486538 | preț; nemulțumire | „one-time purchase of $6.99"; „I hate subscriptions" | corespunde | ambele identice (recenzia „Pod Awesome", „Sep 9", fără an) |
| 11 | https://apps.apple.com/us/app/unitguard/id6761643403 | preț, schimbare de nișă | „UnitGuard Pro Monthly $7.99", „CMEPlan: CME Renewal Tracker" | corespunde | titlul paginii: „CMEPlan: CME Renewal Tracker"; „UnitGuard Pro Annual $59.99 UnitGuard Pro Monthly $7.99" |
| 12 | https://simplenest.pages.dev/ | preț | „$99/year" | corespunde | „$99/year (less than $9/month) or $15/month" |
| 13 | https://www.biggerpockets.com/forums/80/topics/1274715-validation-request-is-automated-lease-vendor-asset-tracking-actually-useful | slăbește ipoteza | „you are essentially competing with a free spreadsheet"; „a spreadsheet + calendar reminders can approximate" | corespunde | ambele identice; dateCreated 2026-01-28 și 2026-06-12, ca în fișă |
| 14 | https://www.biggerpockets.com/forums/52/topics/1291093-california-landlords-whats-your-system-for-tracking-required-notices-and-deadlines | nemulțumire; slăbește | „missed a rent increase notice deadline by 3 days"; „a spreadsheet should be sufficient" | corespunde | ambele identice; data afișată „5mo" |
| 15 | https://www.biggerpockets.com/forums/52/topics/1271855-landlords-with-multiple-units-how-do-you-keep-routine-maintenance-from-slipping | nemulțumire | „nightmare trying to remember which HVAC got serviced when" | corespunde | identic; 2026-01-02 |
| 16 | https://www.biggerpockets.com/posts/7314030 | nemulțumire | „Spreadsheets work until the handoff breaks."; „An insurance policy or lease in a folder is only half the job" | corespunde | ambele identice; 2026-09-30 și 2026-10-20 |
| 17 | https://www.biggerpockets.com/posts/7249803 | nemulțumire; slăbește | „Sheets plus memory combo breaking down"; „I have no problems keeping track" | corespunde | ambele identice; 2026-07-26 și 2025-07-29 |
| 18 | https://www.biggerpockets.com/terms | regulă de canal | „contains advertising, promotions, or marketing, or which otherwise has a commercial purpose" | corespunde | identic, cu trimitere la forums/517-classifieds |
| 19 | https://www.biggerpockets.com/forums/517/topics/3626--read-before-posting-in-this-forum- | regulă de canal | „Only active members of the community can post here." | corespunde | identic |
| 20 | https://www.paddle.com/pricing | cost direct | „5% + 50¢" | corespunde | „5% + 50¢ per Checkout transaction" |
| 21 | https://developer.apple.com/app-store/small-business-program/ | cost direct | „reduced commission rate of 15%" | corespunde | identic |
| 22 | Ubersuggest (conector MCP), SUA 2840/en | volume de căutare | „lease expiration tracker" 0, „lease renewal reminder" 10, „landlord software" 590 (CPC 70,73 $) | neverificabil | nu e o pagină publică; nu se poate redeschide cu curl sau WebFetch, cum cere brieful |

Aritmetică: greșită la o rotunjire, rezultatele nu se schimbă.
- 2.000 / 4,8428 = 412,984, deci 412,98 $, nu 412,99 $ (fișa a rotunjit în sus).
- Restul e corect: /9 = 45,9 → 46; /15 = 27,5 → 28; 99 $/an = 8,25 $/lună, 412,98 / 8,25 = 50,06 → 51 abonați anuali, adică ~4,25 plăți anuale noi pe lună; /29 = 14,2 → 15 cumpărători noi pe lună; /6,99 = 59,1 → 60. Paddle la 9 $: 0,45 + 0,50 = 0,95 $ (10,6%), corect. Plata unică e tratată separat de abonament, corect. În secțiunea 4: 41,19 $ = 199,5 lei și 70,73 $ = 342,5 lei; 5.000 lei acoperă 14,6-25,1 clicuri, deci „15-25 de clicuri" e corect.

Rezumat: 21 corespunde, 0 parțial, 0 nu corespunde, 1 neverificabil

Corecții propuse:
- Secțiunea 5, vechi: „Ținta: 2.000 lei / 4,8428 = **412,99 $ pe lună**, brut." → nou: „Ținta: 2.000 lei / 4,8428 = **412,98 $ pe lună**, brut." Apoi peste tot în secțiunea 5: „412,99" → „412,98" (cifrele care rezultă rămân aceleași).

## 08. CV Europass sau model de CV, plătit o singură dată

| # | Sursă (link) | Ce susține | Citat/preț căutat | Rezultat | Ce apare în pagină / corecție necesară |
|---|---|---|---|---|---|
| 1 | https://www.cvmaker.ro/preturi | preț + reînnoire | „Încearcă 14 de zile pentru RON 5,99, apoi se reînnoiește automat" | corespunde | identic, după „99,99 RON pe lună" |
| 2 | https://www.cvmaker.ro/preturi | confuzie la clienți | „CVMaker.ro apare pe extrasul de cont al cardului bancar sau de credit?" | corespunde | identic |
| 3 | https://cvapp.ro/pricing | preț + reînnoire | „Dacă nu anulezi după 7 zile, vei trece automat la abonamentul lunar premium." | corespunde | identic; „€ 19,95 Lunar Încearcă 7 zile la €2,95" |
| 4 | https://cvapp.ro/pricing | plată unică existentă | „Nu mai trebuie să anulezi" lângă „€ 44,95 6 luni Plată unică" | corespunde | „€ 44,95 6 luni Plată unică" și „€ 74,95 1 an Plată unică", cu „Nu mai trebuie să anulezi" |
| 5 | https://makemycv.com/pricing | preț | „After 7 days, auto-renews for €27.95 every 4 weeks. Cancel anytime." | corespunde | identic, după „2,90€ 7-day full access"; anual „Auto-renews at 94,80€ every year" |
| 6 | https://eures.europa.eu/jobseekers/create-your-europass-cv_ro | alternativă gratuită | „Europass este gratuit pentru toată lumea" | corespunde | identic |
| 7 | https://www.undelucram.ro/creare-cv-online-simplu-romana-si-descarca-modelul-completat-cv-pdf-gratuit | alternativă gratuită | „Creare CV Online Gratis Română sau Engleză și Descarcă Model CV PDF" | corespunde | identic |
| 8 | https://www.tpu.ro/informatii-utilitare/buna-tpu-acum-o-luna-mi-am-facut-cv-pe-cvmaker-ro-si-am-uitat-sa-imi-anulez-abonamentul-cand-a-trebuit-sa-mi-se/ | nemulțumire (02.07.2024) | „Am făcut un amarat de CV și mi-au cerut ulterior 99, 99 lei abonament." | corespunde | identic; ne782UY, „2 Iulie 2024" |
| 9 | https://www.tpu.ro/afaceri-financiar/atentie-la-cvmaker-ro-acest-site-iti-face-un-cv-intitial-pentru-5-lei-iar-apoi-iti-trage-de-pe-card-100-de-lei-lunar/ | nemulțumire (07.03.2023) + contra-dovadă | „iti trage de pe card 100 de lei lunar fara sa te anunte"; „Scrie destul de clar pe site la ei care sunt costurile." | corespunde | ambele identice; dateCreated 2023-03-07 |
| 10 | https://portaldaqueixa.com/brands/cvmaker | nemulțumire altă piață (09.11.2026) | „Cobrança indevida por subscrição automática após pagamento inicial" | corespunde | „Carolina Cardoso 9 de novembro 2026 CVmaker - Cobrança indevida por subscrição automática após pagamento inicial" |
| 11 | https://www.puterea24.ro/dezvaluiri/investigatie-despre-capcanele-abonamentelor-online-si-cum-sunt-pacaliti-consumatorii-romani-226997.html | nemulțumire (26.01.2026) | „Am plătit 7 lei ca să convertesc un CV." | corespunde | identic; datePublished 2026-01-26 |
| 12 | https://www.digi24.ro/stiri/economie/capcana-abonamentelor-online-cum-poti-opri-platile-recurente-si-ce-drepturi-ai-daca-firma-continua-sa-iti-retraga-bani-de-pe-card-4029709 | context ANPC (11.11.2026) | „capcana abonamentului și obstacolele în calea anulării unui serviciu" | corespunde | identic; „Data publicării: 11.11.2026 07:00" |
| 13 | https://stripe.com/ro/pricing | cost direct | „1.5% + 1.00lei for standard European Economic Area cards" | corespunde | identic |
| 14 | https://www.cursbnr.ro/ | curs | „1 USD = 4.8428 Lei" (13.11.2026) | corespunde | identic; și „1 EURO = 5.3498 Lei" |
| 15 | Ubersuggest (MCP), România 2642, ro | volume și CPC | „cv europass" 40.500, CPC 0,815 etc. | neverificabil | nu e o pagină publică; nu se poate redeschide cu curl sau WebFetch |

Aritmetică: corectă. Conversiile EUR (5,3498) și USD (4,8428) se verifică toate: 44,95 € = 240,47 lei; 74,95 € = 400,97; 19,95 € = 106,73; 2,95 € = 15,78; 2,90 € = 15,51; 27,95 € = 149,53; 94,80 € = 507,16; CPC 0,815 $ = 3,95 lei, 1,86 = 9,01, 1,48 = 7,17, 2,51 = 12,16, 0,87 = 4,21. Tabelul: 2.000/19 → 106, /29 → 69, /49 → 41; comision Stripe 1,29 / 1,44 / 1,74 lei; net 17,72 / 27,57 / 47,27 lei (rotunjiri de 0,01 la 19 și 29 lei, acceptabile). Pragurile: 3,95/27,57 = 14,3%; 4,21/27,57 = 15,3%; 9,01/27,57 = 32,7%; 3,95/47,27 = 8,4%; 9,01/47,27 = 19,1%. 5.000/3,95 = 1.266 clicuri (fișa: 1.265, trunchiat), 5.000/9,01 = 555; 69/1.265 = 5,5%. Modelul e plată unică, tratat corect drept cumpărători noi în fiecare lună. Nota: CPC-urile Ubersuggest sunt tratate ca USD, marcat „dedus" în fișă.

Rezumat: 14 corespunde, 0 parțial, 0 nu corespunde, 1 neverificabil

Corecții propuse: niciuna obligatorie. Opțional, secțiunea 5: „5.000 lei la 3,95 lei/clic ≈ 1.265 clicuri" → „≈ 1.266 clicuri" (5.000 / 3,95 = 1.265,8).

## Observație generală
În fișele 06 și 08, antetul spune că XML-ul BNR „a întors o pagină Error / HTML". Azi, la https://curs.bnr.ro/nbrfxrates.xml, primul apel a dat aceeași pagină „Error", iar o reîncercare a dat cursul 4.8428 (PublishingDate 2026-11-13). Cursul folosit în toate cele 4 fișe e deci confirmat de sursa oficială.
