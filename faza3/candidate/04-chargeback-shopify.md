# 04. Dosarul de dovezi pentru chargeback în magazinele Shopify mici
Piață: magazine Shopify mici (surse UK, SUA și alți comercianți Shopify de limbă engleză) | Limbă: engleză | Verificat: 2026-11-16 | Verdict la pasul 1: INTRĂ (09-P1) | Curs folosit: 1 USD = 4,8428 lei; 1 GBP = 6,4023 lei; 1 EUR = 5,3498 lei (BNR, https://curs.bnr.ro/nbrfxrates.xml, curs publicat 2026-11-13, ultimul disponibil la 2026-11-16; www.bnr.ro/nbrfxrates.xml a dat 404 azi)

Pe scurt: problema există, dar nișa s-a umplut în 2026. Am deschis 12 aplicații Shopify pentru dispute lansate între mai și octombrie 2026, aproape toate cu 0 recenzii și cu prețuri de 9-39 $/lună. În plus, Shopify strânge singur dovezile și scrie o apărare cu AI în formularul de răspuns.

## 0. Întrebarea decisivă (doar pentru candidatele din „de clarificat")
Nu se aplică: candidata a intrat direct (SELECTIE.md, rândul 04). Întrebările cerute de sesiunea principală au răspuns în secțiunile 1, 4 și 5:
- Modelul de preț: la liderii vechi e procent din suma recuperată (Chargeflow 25%, Disputifier 20%). Aplicațiile noi au trecut aproape toate pe abonament fix (9,99-39 $/lună) sau plată pe dosar (5 $). **verificat în sursă** (sec. 1).
- API: o aplicație publică poate citi disputele (`read_shopify_payments_disputes`, fără aprobare). Pentru a scrie dovezi (`write_shopify_payments_dispute_evidences`) e nevoie de aprobare de la Shopify, acordată doar aplicațiilor publice la care disputele sunt „core part”. **verificat în sursă** (sec. 4).

## 1. Alternative actuale și prețuri

| Alternativă | Ce face | Preț văzut azi | Link | Data | Marcaj |
|---|---|---|---|---|---|
| Shopify Payments (formular de răspuns inclus) | Shopify strânge automat dovezi și le trimite la termen; adaugă implicit o apărare scrisă cu AI („Include Shopify-generated insights to strengthen case (recommended)”) | inclus; costul funcției AI nu e menționat pe pagină. Taxa de chargeback: 15 $ (SUA), 10 £ (UK), returnată dacă negustorul câștigă | https://help.shopify.com/en/manual/payments/chargebacks/chargebacks-in-admin ; https://help.shopify.com/en/manual/payments/chargebacks/chargeback-process | 2026-11-16 | verificat în sursă (citit prin WebFetch; curl a primit 403 la a doua cerere) |
| Chargeflow (4,5 din 439 recenzii) | Prevenire, alerte, răspuns automat la dispute, construit cu AI | „Automation: 25% of recovered chargebacks. Prevent: 1,000 free then $0.10/order.” | https://apps.shopify.com/chargeflow | 2026-11-16 | verificat în sursă |
| Disputifier (4,6 din 140 recenzii) | Răspuns automat la dispute, alerte | „CB Fighting: 20% of won back revenue”; „CB Alerts: from $17-$27.50/alert” | https://apps.shopify.com/disputifier | 2026-11-16 | verificat în sursă |
| Rekover.ai (5,0 din 5 recenzii; lansată 30 iunie 2026) | AI construiește și trimite dovezile | 9,99 $/lună, „Unlimited Chargebacks” | https://apps.shopify.com/rekover | 2026-11-16 | verificat în sursă |
| Evidkit (handle countercase; 0 recenzii; lansată 25 aug. 2026) | Dovezi redactate cu AI, nimic trimis fără aprobare | 29 $/lună | https://apps.shopify.com/countercase | 2026-11-16 | verificat în sursă |
| Disputr (0 recenzii; lansată 1 iunie 2026) | Pachet PDF de dovezi gata de trimis | 5 $ per pachet, fără abonament; 29 $/lună (20 pachete); 49 $/lună (100 pachete) | https://apps.shopify.com/disputr | 2026-11-16 | verificat în sursă |
| Chargeback Gurus | Firmă de gestionare a disputelor pentru industrii mari (ticketing, hoteluri, închirieri auto) | preț neafișat (chargebackgurus.com/pricing = 404; nu există pe Shopify App Store la apps.shopify.com/chargeback-gurus) | https://www.chargebackgurus.com/pricing | 2026-11-16 | verificat în sursă (lipsa prețului); nu e alternativă reală pentru un magazin mic (dedus) |

Alte aplicații din aceeași nișă, toate deschise azi (2026-11-16), cu preț și dată de lansare de pe pagina lor (**verificat în sursă**):

| Aplicație | Preț | Lansată | Recenzii |
|---|---|---|---|
| DisputeDesk (apps.shopify.com/disputedesk) | gratuit 5 pachete; 29 $/lună (20 pachete); 129 $/lună | 27 mai 2026 | 1 |
| Chargeback Copilot (apps.shopify.com/chargeback-copilot) | gratuit 3 PDF/lună; 19 / 39 / 99 $/lună | 11 mai 2026 | 0 |
| Chargeback Dispute: Recovery (apps.shopify.com/chargeback-dispute) | 19 $/lună + 10% din disputele câștigate; 39 $; 99 $ | 17 iunie 2026 | 0 |
| ChargebackWiz (apps.shopify.com/chargebackwiz) | 18% din fiecare chargeback recuperat | 3 iulie 2026 | 1 |
| DisputePack (apps.shopify.com/disputepack) | gratuit 2 dispute/lună; 39 / 79 / 149 $/lună | 21 aug. 2026 | 0 |
| Chargeback Trail (apps.shopify.com/chargeback-trail) | 99 / 199 / 299 $/lună | 25 aug. 2026 | 0 |
| Backstop (apps.shopify.com/backstop) | gratuit (urmărire termene); Pro 19 $/lună (PDF dovezi) | 10 sept. 2026 | 0 |
| Disputewatch (apps.shopify.com/disputes-co-pilot) | gratuit; Pro 9 $/lună („Shopify form filled in one click”) | 5 oct. 2026 | 0 |
| Do The Proof (apps.shopify.com/dotheproof) | gratuit (doar ciorne); Growth: 19 $ per dispută câștigată + 15% | 8 oct. 2026 | 0 |

Pe forumul Shopify apar și alți constructori cu produse identice în 2026: RebuttalKit (675036), WinPacket (709243), Chargeback Assist la 49 $/dispută (679329), SignalCards Evidence (665535), Chargeam (659719), DisputeKit (681537), CaseSignal (588268), Parry (712425). **verificat în sursă** (firele deschise azi; paginile produselor lor nu le-am deschis).

Concluzie la secțiunea 1 (**dedus**): modelul „procent din suma recuperată” rămâne la liderii cu recenzii. Noii intrați concurează pe abonament ieftin, de la 9 $/lună, sau gratuit. Prețul de referință pentru o aplicație nouă e deci 9-29 $/lună.

## 2. Nemulțumiri

Doar surse noi față de faza 1 (M-Shape Beauty, 631249 și 646203 nu sunt repetate).

| Sursă (link) | Data | Față de | Citat ≤15 cuvinte | Actualitate | Marcaj | Piață |
|---|---|---|---|---|---|---|
| https://apps.shopify.com/chargeflow/reviews?ratings%5B%5D=1&ratings%5B%5D=2&ratings%5B%5D=3&sort_by=newest (Subtlejoys, UK) | 2026-10-22 | Chargeflow (taxe Prevent) | „the final figure is entirely at the discretion of the service provider” | ultimele 12 luni | verificat în sursă | Shopify UK |
| același link (xLumina, Austria) | 2026-10-15 | Chargeflow | „they charged me for disputes I won by myself” | ultimele 12 luni | verificat în sursă | Shopify, Austria (altă țară, aceeași platformă) |
| același link (Code Breaker Labs, Australia) | 2026-09-18 | Chargeflow (calitatea dovezilor) | „all the cases i won have been cases where they filled minimum evidence” | ultimele 12 luni | verificat în sursă | Shopify, Australia, engleză |
| același link (Earthtones, Canada) | 2026-09-18 | Chargeflow | „Of all the chargebacks that have been disputed by Chargeflow I’ve won 0.” | ultimele 12 luni | verificat în sursă | Shopify, Canada, engleză |
| https://apps.shopify.com/disputifier/reviews?ratings%5B%5D=1&ratings%5B%5D=2&ratings%5B%5D=3&sort_by=newest (HugCloud, SUA) | 2026-10-28 | Disputifier (ieșire, facturi) | „Getting out of this app has been a real pain.” | ultimele 12 luni | verificat în sursă | Shopify SUA |
| același link (BTendance, Canada) | 2026-06-17 | Disputifier (cost alerte) | „It costed $317 for just two orders in the name of chargeback prevention.” | ultimele 12 luni | verificat în sursă | Shopify, Canada |
| https://community.shopify.com/t/is-there-a-way-to-auto-fight-chargebacks/712425 (jgkid00) | 2026-11-09 | proces manual | „i’m spending hours every week on them, for pulling tracking, screenshots, policy pages” | ultimele 12 luni | verificat în sursă | Shopify (țară nedeclarată) |
| același fir (jgkid00), teamă de aplicațiile AI | 2026-11-09 | aplicații AI automate | „a bit nervous it will submit junk the lose cases i could’ve won” | ultimele 12 luni | verificat în sursă | Shopify |
| https://community.shopify.com/t/shopify-merchants-are-being-penalised-for-chargeback-evidence-we-literally-cannot-provide-on-any-other-plan-other-than-plus/622590 (Sau2610) | 2026-05-14 | Shopify (dovada acceptării termenilor) | „lost several chargebacks where the issuing bank explicitly stated that we failed to provide” | ultimele 12 luni | verificat în sursă | Shopify (țară nedeclarată) |
| https://community.shopify.com/t/chargeback-lost-despite-evidence-submitted/695184 (shopfy-2020) | 2026-10-09 | Shopify Payments (dovezi automate) | „The bank’s chargeback reply was that there was no proof that the order was delivered” | ultimele 12 luni | verificat în sursă | Shopify (țară nedeclarată) |

Total: 10 nemulțumiri noi din ultimele 12 luni, din 9 surse independente (6 recenzii pe Shopify App Store, 3 fire de forum). Observație (**dedus**): plângerile față de Chargeflow și Disputifier sunt mai ales despre facturare și rata de câștig, nu despre lipsa unui dosar. Firul 695184 arată că și un dosar complet poate pierde.

## 3. Ipoteza de schimbare
Ipoteza: un proprietar de magazin Shopify mic, care pierde ore cu fiecare dispută sau nu are încredere în aplicațiile cu procent, ar plăti un abonament mic pentru un dosar de dovezi generat din comanda Shopify, pe care îl revizuiește înainte de trimitere.

### Ce o susține
- Timpul pierdut manual: „hours every week” (712425, 2026-11-09). **verificat în sursă**
- Neîncredere în AI care trimite singur: același fir; primul răspuns recomandă revizuire înainte de trimitere. **verificat în sursă**
- Nemulțumiri de facturare la modelul cu procent sau alerte (Chargeflow, Disputifier, sec. 2). **verificat în sursă**
- Un comentator pe forum (Maximus3, 679329, 2026-09-09) spune că plata pe dispută „don’t make much sense”, dar asta slăbește doar modelul pe dispută, nu abonamentul. **verificat în sursă**

### Ce o slăbește
- Shopify face deja gratuit o parte mare: „Shopify automatically collects evidence and sends it to the credit card company” (chargebacks-in-admin, 2026-11-16) și adaugă implicit o apărare scrisă cu AI. **verificat în sursă**
- Pe forum, un comentator i-a spus unui constructor că negustorul „is not starting from zero” (lumine, 675036, 2026-08-31). **verificat în sursă**
- Cel puțin 12 aplicații noi pe același job, lansate în 2026, cu 0-5 recenzii (sec. 1) și cel puțin 8 constructori care cer piloți pe forum. Nicio aplicație nouă nu are tracțiune vizibilă în recenzii. **verificat în sursă** (numărul de recenzii); tracțiunea în instalări: **necunoscut**.
- Un constructor (SignalCards, 651370, 2026-09-07) refuză să spună public cifrele de plată după pilot. Lipsa de semnale publice de cerere plătită. **verificat în sursă** (lipsa cifrelor), interpretare **dedusă**.
- Volum de căutare mic (sec. 4). **verificat în sursă**

### Bariere de schimbare
- Aprobarea Shopify pentru scope-urile de scriere a dovezilor: fără ea, aplicația doar generează PDF de încărcat manual. **verificat în sursă**
- Încredere: o aplicație nouă cere acces la comenzi, clienți și dispute; fără recenzii. **dedus**
- Gratuitul nativ Shopify e deja în fluxul negustorului. **dedus**
- Disputele vin rar la un magazin mic (frecvență **necunoscută**); un abonament lunar pentru un eveniment rar e greu de justificat. **dedus**

### Cumpărarea efectivă: se află doar din test.

## 4. Calea către cumpărători

### Căutări (Ubersuggest, SUA, locId 2840, limba en, 2026-11-16; contor `reports` la start: 0 din 150; 2 apeluri folosite)
| Cuvânt cheie | Volum lunar | CPC |
|---|---|---|
| shopify chargeback | 320 | 21,55 $ |
| shopify chargeback protection | 90 | 43,62 $ |
| shopify chargeback app | 30 | 30,13 $ |
| shopify chargeback fee | 30 | 0 |
| shopify chargeback evidence | 0 | 0 |
| best shopify chargeback app | 0 | 0 |
| chargeback evidence | 10 | 0 |

Sursa: Ubersuggest `match_keywords` „shopify chargeback” și `keyword_overview` „chargeback evidence”, 2026-11-16 (seria lunară din răspuns se oprește la 2025-11). **verificat în sursă**. Concluzie: căutările de cumpărare („app”, „evidence”) au 0-30 pe lună în SUA; CPC-ul de 30-44 $ face reclama pe căutare scumpă față de un abonament de 9-29 $/lună. **dedus**

### Shopify App Store: reguli citite azi
- Taxă de înregistrare partener: „a one-time fee of $19 USD per Partner account” (= 92 lei). **verificat în sursă**, https://shopify.dev/docs/apps/launch/distribution/revenue-share
- Comision Shopify: „You keep 100% of your first $1,000,000 USD in lifetime gross app revenue”. **verificat în sursă**, același link
- Taxă de procesare: „All billing is subject to a 2.9% processing fee and applicable sales tax.” **verificat în sursă**, același link
- Facturarea trebuie să treacă prin Shopify: „Your app must use Shopify App Pricing or the Shopify Billing API for all app charges” (1.2). **verificat în sursă**, https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements
- Recenzie de către echipa Shopify, care „can reject an app at their discretion”; durata nu e afișată pe pagina citită. **verificat în sursă** / durata: **necunoscut**

### API pentru dispute (shopify.dev, 2026-11-16)
- Citire: obiectul `ShopifyPaymentsDispute` cere `read_shopify_payments_disputes`, care nu e marcat „Shopify approval required”; are `evidenceDueBy`, `reasonDetails`, `status`. **verificat în sursă**, https://shopify.dev/docs/api/admin-graphql/latest/objects/ShopifyPaymentsDispute și https://shopify.dev/docs/api/usage/access-scopes
- Scriere: mutația `disputeEvidenceUpdate` „Updates the evidence package for a Shopify Payments dispute”, cere `write_shopify_payments_dispute_evidences`. **verificat în sursă**, https://shopify.dev/docs/api/admin-graphql/latest/mutations/disputeEvidenceUpdate
- Câmpul `submitEvidence` din input e marcat „deprecated”. Dacă o aplicație mai poate trimite efectiv răspunsul sau doar completează formularul: **necunoscut** din paginile citite. https://shopify.dev/docs/api/admin-graphql/latest/input-objects/ShopifyPaymentsDisputeEvidenceUpdateInput
- Scope-urile de dovezi sunt restricționate: „Shopify grants these scopes to individual apps.” Condiții: distribuție publică și „Dispute or chargeback management must be a core part of what your app does.” Cererea se face prin Shopify Support. **verificat în sursă**, https://shopify.dev/docs/api/usage/access-scopes
- Mai multe aplicații noi (Rekover, DisputeDesk, Do The Proof, Disputewatch) afișează în lista de date accesate „Shopify Payments dispute evidences”, deci aprobarea a fost obținută de aplicații mici noi. **verificat în sursă** (lista de acces); că aprobarea e ușor de obținut: **dedus**.
- Implicit, aplicația vede doar comenzile din ultimele 60 de zile; `read_all_orders` cere aprobare pentru aplicații din organizații Partner. **verificat în sursă** (access-scopes). Disputele pot veni pe comenzi mai vechi: impact **dedus**.

### Forumul community.shopify.com: reguli citite azi
- „App recommendations are allowed only on the Ask and Offer board.” Interzis: „Recommending or promoting apps outside the Ask and Offer board”, chiar și când membrul cere explicit recomandări. Cerință: „Clearly disclose any ownership”. Mesajele private promoționale nesolicitate sunt interzise. **verificat în sursă**, https://community.shopify.com/guidelines, 2026-11-16
- Practic: pe firele de chargeback, postările promoționale apar deja des, iar unele sunt marcate „flagged by the community” (695184). **verificat în sursă**

## 5. Drumul până la 2.000 lei/lună (încasări brute)
Țintă: 2.000 lei / 4,8428 = 412,98 $ pe lună.

**Abonament (clienți ACTIVI plătitori, în fiecare lună):**
- la 9,99 $/lună (Rekover): 2.000 / 48,38 lei = 41,3, deci **42 clienți activi**
- la 19 $/lună (Backstop Pro, Chargeback Copilot Starter): 2.000 / 92,01 lei = 21,7, deci **22 clienți activi**
- la 29 $/lună (Evidkit, DisputeDesk, Disputr): 2.000 / 140,44 lei = 14,2, deci **15 clienți activi**

**Procent din suma recuperată (venit variabil, depinde de disputele câștigate de toți clienții într-o lună):**
- la 25% (Chargeflow): trebuie recuperați 8.000 lei/lună (1.652 $). Cu valoarea unei dispute ca în exemplul din faza 1 (74,49 £ = 476,91 lei), sunt **17 dispute câștigate pe lună**, adunate de la toți clienții.
- la 20% (Disputifier): 10.000 lei recuperați, deci **21 dispute câștigate pe lună** la aceeași valoare.
- Câte dispute are un magazin mic pe lună și rata de câștig: **necunoscut**. Acest model nu e echivalent cu abonamentul: venitul fluctuează și apare cu întârziere (decizia băncii vine după săptămâni; durata: **necunoscut** din sursele citite).

**Plată pe dosar (cumpărători sau dosare NOI în fiecare lună):** la 5 $/pachet (Disputr), 2.000 / 24,21 lei = 82,6, deci **83 dosare plătite pe lună**.

**Costuri directe cunoscute:**
- 19 $ o singură dată pentru contul de partener = 92 lei (shopify.dev revenue-share). **verificat în sursă**
- comision Shopify 0% sub 1.000.000 $ cumulat. **verificat în sursă**
- 2,9% taxă de procesare pe facturare = 58 lei la 2.000 lei. **verificat în sursă**
- găzduire, generare PDF, costul modelului AI pe dosar: **necunoscut**.
- reclamă: CPC 21-44 $ pe căutările relevante (Ubersuggest, sec. 4); rata de conversie: **necunoscut**.

## 6. Produsul restrâns
### Ce face (max 5 rânduri)
1. Aplicație Shopify publică: citește disputele Shopify Payments și termenul (`evidenceDueBy`).
2. Pentru fiecare dispută, adună din comandă: tracking și livrare, adresa, mesaje, politicile magazinului, potrivite pe codul de motiv.
3. Arată ce lipsește față de ce Shopify trimite deja automat (nu repetă ce face nativ).
4. Generează PDF-ul și textul de răspuns; negustorul revizuiește și încarcă (sau, cu aprobarea scope-ului, completează formularul).
5. Alerte de termen pe e-mail.

### Efort de construire (dedus)
3-4 săptămâni pentru un om cu unelte AI: șablon de aplicație Shopify, OAuth, Billing API, webhook-uri de dispute, generare PDF, o pagină de listare. Plus timp de recenzie Shopify și de aprobare a scope-urilor: **necunoscut**. Aplicațiile din sec. 1 arată că versiuni similare au fost lansate de echipe mici, deci construirea e fezabilă (**dedus**).

### Efort de operare lunar (dedus)
Suport pentru negustori cu bani blocați (presiune mare), actualizarea șabloanelor pe coduri de motiv Visa/Mastercard, răspuns la recenzii, monitorizarea erorilor PDF. Estimare: câteva ore pe săptămână (**dedus**).

### Ce se poate strica lunar
- Shopify extinde formularul nativ și apărarea AI (deja refăcut în decembrie 2025, conform faza 1), ceea ce reduce valoarea aplicației. **dedus**
- Schimbări în API (de ex. `submitEvidence` deja „deprecated”). **verificat în sursă** (statutul), impact **dedus**
- Retragerea sau refuzul aprobării pentru scope-urile restricționate. **dedus**
- Recenzii negative când negustorul pierde o dispută, chiar cu dosar complet (cf. 695184). **dedus**

## 7. Presupunerea care omoară ideea
Că cel puțin 15-22 de magazine Shopify mici vor plăti lunar 19-29 $ unei aplicații noi, fără recenzii, aleasă dintre peste 12 aplicații echivalente lansate în 2026, pentru un dosar pe care Shopify îl strânge și îl trimite deja gratuit. Dacă negustorii mici rămân pe formularul nativ (sau aleg varianta gratuită a celorlalte aplicații), ideea nu ajunge la 2.000 lei/lună.

## 8. Surse blocate
- reddit.com (r/shopify, căutare „chargeback app”): HTTP 200, dar pagina conține doar titlul „Reddit”. 2026-11-16.
- g2.com (Chargeflow reviews): HTTP 403. 2026-11-16.
- trustpilot.com (chargeflow.io): HTTP 403. 2026-11-16.
- capterra.com: linkul încercat a dat 404 (nu e blocare, dar nu am găsit pagina). 2026-11-16.
- help.shopify.com: prima cerere curl HTTP 200; următoarele HTTP 403 („Verifying your connection...”). Paginile chargebacks-in-admin și chargeback-process au fost citite prin WebFetch, fără ocolire.
- apps.shopify.com/search?q=chargeback: „We are having trouble loading your results” (rezultatele se încarcă prin JavaScript). Aplicațiile au fost găsite prin WebSearch și deschise apoi direct.
- www.bnr.ro/nbrfxrates.xml: 404; am folosit curs.bnr.ro (domeniul oficial BNR).

## 9. Lista surselor decisive pentru verificarea independentă
1. https://curs.bnr.ro/nbrfxrates.xml, 2026-11-16, curs: „<Rate currency="USD">4.8428</Rate>” (publicat 2026-11-13)
2. https://apps.shopify.com/chargeflow, 2026-11-16, preț: „Automation: 25% of recovered chargebacks.”
3. https://apps.shopify.com/disputifier, 2026-11-16, preț: „CB Fighting: 20% of won back revenue”
4. https://apps.shopify.com/rekover, 2026-11-16, preț: „$9.99 / month” și „Launched June 30, 2026”
5. https://apps.shopify.com/countercase, 2026-11-16, preț: „Standard $29 / month”
6. https://apps.shopify.com/disputr, 2026-11-16, preț: „$5 per evidence packet generated”
7. https://apps.shopify.com/backstop, 2026-11-16, preț: „Pro $19 / month” și „Launched September 10, 2026”
8. https://apps.shopify.com/disputes-co-pilot, 2026-11-16, preț: „Pro $9 / month” și „Shopify form filled in one click”
9. https://help.shopify.com/en/manual/payments/chargebacks/chargebacks-in-admin, 2026-11-16, alternativă gratuită: „Shopify automatically collects evidence and sends it to the credit card company”
10. https://help.shopify.com/en/manual/payments/chargebacks/chargeback-process, 2026-11-16, taxa: „If you win the chargeback, then the fee is returned to you.”
11. https://apps.shopify.com/chargeflow/reviews?ratings%5B%5D=1&ratings%5B%5D=2&ratings%5B%5D=3&sort_by=newest, 2026-11-16, nemulțumire: „they charged me for disputes I won by myself”
12. același link, 2026-11-16, nemulțumire: „all the cases i won have been cases where they filled minimum evidence”
13. https://apps.shopify.com/disputifier/reviews?ratings%5B%5D=1&ratings%5B%5D=2&ratings%5B%5D=3&sort_by=newest, 2026-11-16, nemulțumire: „Getting out of this app has been a real pain.”
14. https://community.shopify.com/t/is-there-a-way-to-auto-fight-chargebacks/712425, 2026-11-16, nemulțumire față de procesul manual: „i’m spending hours every week on them”
15. https://community.shopify.com/t/free-browser-only-chargeback-evidence-organizer-for-shopify-merchants-optional-19-prevention-kit/675036, 2026-11-16, slăbește ipoteza: „the merchant is not starting from zero”
16. https://shopify.dev/docs/apps/launch/distribution/revenue-share, 2026-11-16, regulă de canal: „a one-time fee of $19 USD per Partner account”
17. același link, 2026-11-16, regulă de canal: „All billing is subject to a 2.9% processing fee and applicable sales tax.”
18. https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements, 2026-11-16, regulă de canal: „Your app must use Shopify App Pricing or the Shopify Billing API”
19. https://shopify.dev/docs/api/usage/access-scopes, 2026-11-16, regulă API: „Shopify grants these scopes to individual apps.”
20. https://community.shopify.com/guidelines, 2026-11-16, regulă de forum: „App recommendations are allowed only on the Ask and Offer board.”
