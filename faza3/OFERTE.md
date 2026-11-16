# Faza 3, pasul 5: oferte

Data: 2026-11-16. Sursa: cele 8 fișe din faza3/candidate/, după corecțiile din VERIFICARE.md. Curs: 1 USD = 4,8428 lei (BNR, publicat pe 2026-11-13, confirmat la verificare). Pragurile de mai jos sunt propuneri argumentate; le decide proprietarul.

## Concluzie

**Rămân 2 oferte, nu 3.** La celelalte 6 candidate, verificarea pe web a găsit fie o piedică demonstrată, fie un risc pe care un test de cel mult 14 zile și 1.000 lei nu îl poate măsura, pentru că nu ajunge la expunerea minimă (tabelul de la final).

Ordinea:
1. **CV fără abonament, România.**
2. **Galerie QR pentru pozele invitaților la nuntă, SUA.**

**Motivul ordinii.** Oferta 1 are expunerea cea mai ieftină: 1.000 lei cumpără ~250 de clicuri la 3,95 lei/clic, față de ~40-49 la oferta 2. Are și pragul de rentabilitate al reclamei mai mic: 14,3% din clicuri, față de 15,3-19,2%. Nu are riscul unui eșec irecuperabil în ziua evenimentului și se poate construi în 2-3 săptămâni (dedus). Oferta 2 are dovada mai tare că oamenii plătesc în categorie: prețuri per eveniment verificate azi la patru concurenți și 15.677 de evaluări la POV. Dar produsul e identic cu cel al concurenților, iar testul ar cădea în luna cea mai slabă a sezonului.

Ambele oferte au o slăbiciune comună: ipoteza de schimbare se sprijină pe un singur argument. La oferta 1 argumentul e „plată unică", la oferta 2 e „preț mai mic". Niciuna nu are o nemulțumire recentă, din piața ei, care să ceară explicit produsul propus. Cumpărarea efectivă se află doar din test.

---

## Oferta 1: CV fără abonament (România, română)

> Pentru oamenii din România care își fac un CV pentru o aplicare (căutări „cv europass", „model cv", „cv online gratis pdf"), un CV în format Europass sau într-unul din 3-5 modele simple, descărcat ca PDF și Word, la **29 lei plată unică, fără reînnoire**. Azi folosește Europass sau undelucram.ro (gratuite), cvmaker.ro (5,99 RON pentru 14 zile, apoi 99,99 RON/lună, cu reînnoire automată) sau cvapp.ro (2,95 € pentru 7 zile, apoi 19,95 €/lună; sau 44,95 € pentru 6 luni). Ipoteza de schimbare este că o parte din cei care nu vor un abonament și au nevoie de un aspect mai bun decât Europass plătesc o sumă mică, o singură dată, unui site care spune clar „fără abonament". Bariera principală este încrederea: un site nou care cere cardul pentru un CV seamănă cu site-urile de care oamenii s-au plâns. Vine și alternativa gratuită oficială, care e prima la căutarea cea mai mare.

Dovezi (din faza3/candidate/08-cv-romania.md, verificate în sursă la pasul 4):
- Prețurile și condițiile de reînnoire de mai sus au fost văzute azi pe paginile lor.
- Nemulțumirea față de proba care devine abonament: 8 autori pe TPU.ro, între 2022 și 2024. Actualitatea nu e verificată, pentru că nu am găsit nicio plângere verificată din România în ultimele 12 luni. Tot pe TPU, alți utilizatori spun că prețul era scris clar pe site.
- Volume (Ubersuggest, România, 2026-11-16): „cv europass" 40.500/lună, CPC 3,95 lei; „model cv" 9.900, CPC 7,17 lei; „cv online gratis pdf" 590, CPC 4,21 lei. Concurența la reclame e mare (65-80 din 100).

### Aritmetica (din fișă, verificată)
- Plată unică, deci contează cumpărătorii noi în fiecare lună: 2.000 lei / 29 lei = **69 de cumpărători noi pe lună**.
- Net pe vânzare, după Stripe (1,5% + 1 leu): 27,57 lei.
- Pragul la care reclama se plătește singură e conversia clic → cumpărare = CPC / net: **14,3%** la „cv europass" și 32,7% la „cv online".
- Atenție: chiar la 14,3%, 69 de vânzări cer ~483 de clicuri și ~1.900 lei de reclame pe lună. Ținta de 2.000 lei încasări brute s-ar atinge, dar aproape tot venitul net ar merge pe reclame. Un profit ar veni doar dintr-o conversie peste prag sau din trafic neplătit (SEO), pe care testul nu îl măsoară. Asta e și obiecția mea la ipoteza „ținta = încasări brute": cu reclame plătite, încasarea brută poate fi atinsă cu profit zero.

### Planul de test (cel mult 14 zile, cel mult 1.000 lei)
- **Ce trebuie construit înainte:** produsul restrâns din fișă. Generatorul cu 3-5 șabloane, previzualizare cu filigran, plată unică prin Stripe Checkout fără reînnoire, descărcare PDF și Word, plus pagina de vânzare. Estimare: 2-3 săptămâni (dedus). Nu recomand o pagină fără produs, cu buton de plată fals: cumpărătorul plătește și descarcă pe loc, iar o „ușă falsă" ar măsura doar clicul, nu plata.
- **Canalul:** Google Ads, rețeaua de căutare, România, limba română. Cuvinte: „cv europass", „model cv", „cv online gratis pdf", potrivire exactă sau de expresie. Prețul de 29 lei apare în anunț, ca să nu se plătească clicuri de la cei care vor gratuit.
- **Expunerea minimă, stabilită dinainte: 200 de clicuri** din aceste căutări (~790-840 lei la CPC 3,95-4,21 lei). Argument: la pragul de 14,3% sunt de așteptat ~29 de cumpărări, iar la 5% ~10. La 200 de clicuri cele două situații se deosebesc clar. Sub 200 de clicuri nu se poate distinge.
- **Cele trei rezultate posibile:**
  - **Continuăm:** cel puțin **29 de cumpărări la 200 de clicuri** (≥ 14,3%). Reclama se plătește singură, iar ținta de 69 de cumpărători pe lună devine o problemă de buget de reclamă, nu de ofertă.
  - **Oprim sau schimbăm oferta:** **sub 29 de cumpărări la 200 de clicuri**. Schimbarea propusă, o singură dată, e prețul de 49 lei, unde pragul scade la 8,4% (din fișă). Între 17 și 28 de cumpărări (8,5-14%), schimbarea are sens. Sub 17 cumpărări, recomand oprirea.
  - **Neconcludent:** sub 200 de clicuri în 14 zile, de exemplu din cauza aprobării anunțurilor, a unui CPC mult peste 4,21 lei sau a unui volum real mai mic decât cel din Ubersuggest. Urmează o singură repetare pe alt canal: Meta Ads (Facebook și Instagram) cu public din România, la costul pe clic de acolo, care e necunoscut. Apoi decizia.
- **Ce măsoară testul:** **oferta**, adică dacă oamenii care au căutat un CV plătesc 29 lei odată ce văd prețul și previzualizarea. Separat, ca informație, nu ca prag de decizie: costul real pe clic și rata de clic arată accesul la public. Testul **nu** măsoară valoarea produsului. Aceea s-ar vedea abia după vânzare, din rambursări și reclamații.

---

## Oferta 2: galerie QR pentru pozele invitaților (SUA, engleză)

> Pentru gazdele de nuntă din SUA (căutări „wedding photo sharing app", „wedding photo app", „qr code wedding photos"), o galerie în care invitații încarcă pozele și videoclipurile scanând un cod QR, fără aplicație și fără cont, la calitate originală, cu descărcarea întregului album, la **29 $ plată unică pe eveniment**. Azi folosește POV (gratuit până la 10 invitați, apoi 4,99-89,99 $ pe eveniment), GuestCam (49 $ / 97 $), Guestpix (de la 49 $) sau Wedding Photo Swap (29,99 $ / 39,99 $). Ipoteza de schimbare este prețul mai mic pentru același rezultat ca la GuestCam sau Guestpix, plus lipsa contului și a limitei de poze, de care se plâng recenziile POV. Bariera principală este încrederea: o nuntă nu se repetă, iar concurenții au mii de evenimente și recenzii (POV: 15.677 de evaluări în App Store).

Dovezi (din faza3/candidate/02-poze-invitati-nunta.md):
- Prețurile de mai sus au fost verificate în sursă la pasul 4.
- 6 nemulțumiri noi din ultimele 12 luni, din fluxul App Store: cont obligatoriu, limită de poze, încărcări eșuate. Ele nu au putut fi reconfirmate la pasul 4, pentru că fluxul a răspuns gol azi.
- Aceleași date slăbesc ipoteza: la POV, 89 din 100 de recenzii din ultimele 12 luni au 5 stele, iar produsul nostru restrâns există deja, identic, la GuestCam, Guestpix și Kululu.

### Aritmetica (din fișă, verificată)
- Plată unică pe eveniment, deci contează cumpărătorii noi în fiecare lună: 413 $ / 29 $ = **15 cumpărători noi pe lună** (la 49 $: 9).
- Net pe vânzare la 29 $ (140,44 lei), după Stripe cu conversie valutară (3,15% + 1 leu + 2%): ~132,2 lei. Costul de stocare pentru fișierele la calitate originală e necunoscut.
- Pragul la care reclama se plătește singură (calculul meu, pe cifrele din fișă) e CPC / net: „wedding photo sharing app" 4,17 $ = 20,19 lei, deci **15,3%**; „qr code wedding photos" 5,25 $ = 25,42 lei, deci **19,2%**.
- Sezonalitate: „wedding photo app" are 480 de căutări în decembrie și 1.300 în mai (Ubersuggest).

### Planul de test (cel mult 14 zile, cel mult 1.000 lei)
- **Ce trebuie construit înainte:** produsul restrâns din fișă: crearea evenimentului și plata, codul QR, pagina de încărcare din browser cu reîncercare la semnal slab, galeria și descărcarea zip. Estimare: 3-4 săptămâni (dedus). Partea critică e fiabilitatea încărcării pe rețele mobile proaste. Nu se poate vinde înainte de a o avea.
- **Canalul:** Google Ads, căutare, SUA, pe cele trei căutări de mai sus. Cu 1.000 lei (~206 $) ies **~39-49 de clicuri**.
- **Expunerea minimă, stabilită dinainte: 40 de clicuri.** Argument: la pragul de ~15% sunt de așteptat ~6 cumpărări. Dacă rata reală ar fi 15%, probabilitatea de a avea cel mult o cumpărare la 40 de clicuri e de aproximativ 1-2% (calcul binomial, dedus). La 40 de clicuri, rezultatul „aproape nimeni" se distinge deci de pragul de rentabilitate. Mai fin nu se poate distinge cu acest buget.
- **Cele trei rezultate posibile:**
  - **Continuăm:** cel puțin **6 cumpărări la 40 de clicuri** (≥ 15%).
  - **Oprim sau schimbăm oferta:** **sub 6 cumpărări la 40 de clicuri**. Cu 2-5 cumpărări, schimbarea propusă o singură dată e prețul de 49 $ (la nivelul GuestCam), unde pragul scade la ~9% (calcul pe aceeași formulă, dedus). Cu 0-1 cumpărări, recomand oprirea.
  - **Neconcludent:** sub 40 de clicuri în 14 zile. E un risc real în decembrie, la minimul sezonului. Urmează o singură repetare pe alt canal: Pinterest Ads sau Meta Ads în SUA, la costuri pe clic necunoscute, de preferat în martie-mai, când căutările cresc. Apoi decizia.
- **Ce măsoară testul:** **oferta**, adică dacă o gazdă care caută exact acest produs alege un furnizor nou, mai ieftin, după ce vede prețul și demonstrația. Nu măsoară valoarea produsului. Aceea se vede abia după nuntă, din încărcările reușite, rambursări și recenzii. Accesul la public, adică CPC-ul real și rata de clic, se notează separat.

---

## Buget

Cele două teste costă cel mult 2 × 1.000 lei. Dacă ambele ies neconcludente și se repetă o dată, se ajunge la cel mult 4.000 lei, în limita bugetului total de 5.000 lei. Costul construirii nu e inclus: e timpul proprietarului, 2-3 săptămâni la oferta 1 și 3-4 la oferta 2 (dedus), plus abonamentele de găzduire și stocare, necunoscute.

## Cele 6 candidate care nu au devenit oferte

| Candidată | Ce a lipsit | Tipul lipsei |
|---|---|---|
| 01. RSVP și SMS pentru nuntă (SUA) | Partea plătită (SMS) are 20-30 de căutări pe lună. RSVP-ul e gratuit la Zola, The Knot și Joy. Același pachet se vinde deja la 9-19 $ (WeddingTXT, Text My Wedding). La CPC-ul căutărilor de RSVP (6,40-13,38 $), 1.000 lei înseamnă 15-32 de clicuri, din căutări cu intenție de gratuit. | **Risc testabil, dar fără canal**: testul nu poate atinge o expunere minimă relevantă în 14 zile și 1.000 lei. Lipsește un canal în care cumpărătorii părții plătite să poată fi găsiți. |
| 03. Retururi Shopify | Shopify oferă gratuit portalul de retur. Golul rămas (cerere fără cont, poze) e acoperit de Loopback (9 $/lună) și Opus (gratuit), lansate în august-septembrie 2026. Căutările: „shopify returns" 480/lună, „shopify returns app" 110/lună. | **Risc testabil, cu dovezi contrare verificate.** Cumpărarea nu e exclusă, dar alternativa gratuită nativă și clonele sunt fapte verificate. Un test pe Shopify App Store nu încape în 14 zile, pentru că listarea cere aprobare. |
| 04. Chargeback Shopify | Shopify strânge și trimite dovezile gratuit. Cel puțin 12 aplicații lansate în 2026 au 0-5 recenzii. Scrierea dovezilor prin API cere aprobarea Shopify. „shopify chargeback app" are 30 de căutări pe lună. | **Piedică demonstrată pentru produsul complet** (aprobarea API, verificată în sursă) și **risc testabil** pentru varianta cu PDF descărcat. |
| 05. Plata notarilor de semnări | Exact această ofertă (aplicație de 9 $/lună pentru plătitorii întârziați, „SigningPayday") a fost testată public pe Notary Cafe în februarie 2026, cu răspunsuri reci. Funcția există deja în NotaryAssist, NotaryGadget și VenBooks. Forumul interzice reclama nesolicitată, iar „notary invoice software" are volum 0. | **Piedică demonstrată**: testul publicului a fost deja făcut de altcineva și nu există canal permis. |
| 06. Detention transport | Sursele spun că brokerul plătește sau nu după rate con și după bunăvoință, nu după calitatea dovezii. Dovada există deja gratuit (ELD, aplicațiile brokerilor). Două dintre firele din faza 1 erau ale unor dezvoltatori care își testau aplicația. Forumul interzice reclama, iar căutările au volum 0. | **Piedică demonstrată**: cauza pierderii nu e cea pe care o rezolvă produsul. |
| 07. Termene proprietari | Proprietarii din segment spun că le ajunge o foaie de calcul („a spreadsheet should be sufficient"). Suitele de 12-15 $/lună includ deja alertele de contract. Aplicațiile dedicate se vând la 1,99-6,99 $ o singură dată. Căutările au volum aproape zero, iar CPC-ul general e de 41-71 $. BiggerPockets permite promovarea doar la Classifieds, după 10 postări. | **Risc testabil, cu dovezi contrare verificate și fără canal.** Testul nu poate atinge o expunere minimă în 14 zile și 1.000 lei. |

## Ce nu s-a putut verifica

- Rata reală clic → cumpărare la oricare ofertă: se află doar din test.
- Costul pe clic pe Meta Ads și Pinterest Ads (canalele de repetare): necunoscut.
- Costul de stocare pentru oferta 2 și TVA-ul pentru oferta 1: necunoscute.
- Nemulțumirile din App Store la candidatele 01 și 02: nu au putut fi reconfirmate independent, pentru că fluxul RSS a răspuns gol la pasul 4.
- Regulile grupurilor românești de Facebook și ale TPU.ro (posibile canale pentru oferta 1): nu au fost citite. Sunt în spatele autentificării sau nu au fost găsite.
