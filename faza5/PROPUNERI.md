# Faza 5, pasul 5: propuneri

Data: 2026-11-16.

## Verdict

**Nicio propunere.** Dintre cele 3 obligații din calendar (CALENDAR.md), niciuna nu are forma care a produs un val în precedente. Două se mai pot prinde ca timp (CRA, CLP), dar ambele sunt afișări de date pe produs, ca GPSR și eticheta de garanție, care au dat cele mai mici valuri. A treia (tutunul în UK) e peste 6 săptămâni.

### Testul folosit, din PRECEDENTE.md

O obligație merită o aplicație construită din timp dacă trece toate patru:

| Test | De unde vine | Butonul de retragere (singurul val mare) |
|---|---|---|
| T1. Cere un **element funcțional** (buton, formular, e-mailuri, legătură cu comanda), nu doar un text sau o imagine pe produs | GPSR (date pe produs): vârf 9 recenzii pe lună; GARAN (imagine + text): 147; butonul: 2.792 | da |
| T2. Atinge **aproape toate magazinele** care vând consumatorilor din UE, cu greutate mare în Germania | 65% din recenziile valului 2026 vin din Germania | da |
| T3. Platforma **nu îl rezolvă nativ** înainte de termen | Shopify a răspuns cu o zi înainte, Germanized cu 1-3 luni înainte | parțial (Shopify) |
| T4. Se poate **lista cu cel puțin 3 luni înainte**, pornind construcția în decembrie 2026 | câștigătorii mici: 1-5,3 luni înainte; cei de după termen: cel mult 71 de recenzii pe val | da (a fost) |

| Obligație | T1 funcțional | T2 toate magazinele | T3 fără răspuns nativ | T4 timp | Rezultat |
|---|---|---|---|---|---|
| C1. CRA, perioada de suport (11.12.2027) | **nu** (o dată pe produs) | **nu** (doar produse cu elemente digitale, obligația e a producătorului) | **nu** (câmpul nativ Shopify „disclosures", 17.06.2026) | da | respinsă |
| C2. CLP, elementele etichetei în oferta la distanță (1.1.2028, condiționat) | **parțial** (pictograme și fraze H/P în toate limbile, generate din coduri) | **nu** (doar vânzătorii de produse periculoase) | parțial (disclosures fără pictograme și fraze traduse; liderul GPSR le are deja) | da, dar data poate cădea | respinsă |
| C3. UK, tutun (1.1.2027) | parțial (poarta de vârstă cu prag fix) | **nu** (nișă) | necunoscut | **nu** (6 săptămâni) | respinsă |

Toate evaluările de mai sus sunt **dedus** din cifrele din PRECEDENTE.md și din textele citate în CALENDAR.md.

---

## De ce nu C2 (cea mai apropiată)

C2 e singura cu o parte tehnică reală. Aplicația ar putea primi codurile H și P de pe fișa cu date de securitate și ar afișa pictogramele și frazele oficiale în toate cele 24 de limbi, pe produs, în coș și în e-mail. Comerciantul nu face asta ușor de mână. Motivele pentru care nu o propun:

1. **Data poate dispărea.** Omnibus VI e votat de Parlament (22.10.2026) și așteaptă Consiliul. Rezumatul oficial păstrează obligația, dar o restrânge la vânzările către publicul larg. Sursele secundare spun că data se mută la 1.1.2030. Pagina Consiliului și textul adoptat nu au putut fi citite (403 și refuz de permisiune). **doar fragment / necunoscut**. Dacă data se mută, o construcție începută în decembrie 2026 așteaptă trei ani.
2. **Precedentul cel mai apropiat e GPSR.** Tot date pe produs, tot în toate limbile, tot pentru UE. Liderul GPSR pe Shopify are 29 de recenzii în doi ani. Cele 55 de aplicații GPSR listate după termen au împreună 4. **verificat în sursă**. C2 atinge mai puține magazine decât GPSR.
3. **Concurenții deja listați nu au clienți, dar cel mai periculos e deja acolo.** Trei aplicații CLP din iulie-august 2026 au 0-1 recenzii; ele s-au lansat pentru vechea dată și au rămas fără val. În plus, GCM / gpsr de la 401layers (liderul GPSR și firma care a luat 70% din valul butonului) oferă deja frazele GHS în planul de 15 $/lună. Dacă vine un val CLP, 401layers pornește cu baza de clienți GPSR. **verificat în sursă**
4. **Prețul de piață ar fi mic.** Aplicațiile CLP existente cer 9,99 $/lună (gpsr-clp-hazard-labels) și 19-79 $/lună (CLPLens), fără clienți vizibili. Câștigătorii GPSR cer 15-29 $/lună, dar cu foarte puțini clienți. **verificat în sursă**
5. **Criteriul (5) e la limită.** Dacă fișa furnizorului lipsește, magazinul ar cere aplicației să „spună ce pictograme pune". Asta e clasificare, adică exact ce aplicația nu trebuie să facă. **dedus**

## De ce nu C1

- Obligația e a producătorului și se aplică doar produselor cu elemente digitale introduse pe piață după 11.12.2027. Magazinele care revând electronice doar verifică. **verificat în sursă**
- Afișarea e o singură dată (lună și an). Câmpul nativ Shopify „disclosures" (17.06.2026) o acoperă gratuit pe temele compatibile. **verificat în sursă** (funcția), **dedus** (acoperirea)
- Nicio aplicație nu afișează explicit perioada de suport. Cele trei aplicații Shopify care ating CRA au 0 recenzii, iar pluginurile CRA de pe WordPress sunt pentru dezvoltatori de software. **verificat în sursă**. Lipsa concurenței aici înseamnă lipsa cererii, după precedentul GARAN (o etichetă simplă, preț de 4,99 $/lună, vârf 147 de recenzii). **dedus**

## De ce nu C3

Termenul e la 1.1.2027. Precedentele cer listarea cu cel puțin 3 luni înainte, iar construcția ar începe abia în decembrie 2026. Nișă: doar vânzătorii online de tutun din UK. **dedus**

---

## Ce ar schimba verdictul și când se reverifică

| Semnal | Unde se citește | Când | Ce ar însemna |
|---|---|---|---|
| UK: regulamentul pentru abonamente aprobat ca SI și un regulament de commencement pentru DMCCA s.254 | legislation.gov.uk | lunar, de acum | primul candidat funcțional (ieșire online, notificări de reamintire), ca butonul de retragere; dar termenul anunțat e ianuarie 2027, deci prea aproape pentru o aplicație nouă, iar pe Shopify fluxul îl țin aplicațiile de abonamente |
| Omnibus VI publicat în JO | Cellar / JO | lunar | dacă păstrează 1.1.2028, C2 se reevaluează; dacă mută la 2030, C2 iese |
| Germania: avertismente (Abmahnungen) pentru CLP în magazine online | surse de executare din Germania | după publicarea Omnibus VI | ar schimba T2 pentru piața germană |
| Detergenți, Regulamentul (UE) 2026/405, art. 20 (afișare la vânzarea la distanță) | adoptat, se aplică din 23.09.2029 | se reevaluează în 2028 | în afara ferestrei de acum; listare țintă primăvara 2029 |
| Digital Fairness Act | propunere din 11.11.2026 | la adoptare | dark patterns, rezilierea abonamentelor; se va aplica după 2028 |

## Ce nu s-a schimbat față de faza 4

Propunerile din faza 4 nu au fost redeschise (regula fazei). PRECEDENTE.md confirmă un singur lucru folositor pentru propunerea 1 din faza 4 (butonul de retragere): aplicațiile listate după termen au primit 71 de recenzii, la 81 de aplicații. **verificat în sursă**
