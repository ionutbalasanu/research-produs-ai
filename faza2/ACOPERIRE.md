# Faza 2: acoperire

Data: 2026-11-15. Uneltele și probele sunt descrise în UNELTE.md.

## Pe familii

- **Sugestii strânse:** sugestiile unice de completare automată Google (hl=ro, gl=ro) pentru expresiile de bază + „ a”…„ z”.
- **Păstrate:** căutările cu intenție „rezolv acum”, după eliminările din sarcină.
- **Cu volum:** volum găsit în Ubersuggest prin `match_keywords` (toate expresiile de bază). La lista unită se adaugă 137 de volume din `keyword_overview`, care nu apar în coloana de pe familii.
- **În primele 120:** câte căutări din CAUTARI.md aparțin familiei. O căutare poate aparține mai multor familii.

| Familie | Expresii de bază | Sugestii strânse | Păstrate | Cu volum | În primele 120 | Blocat la pasul 1 | Expresii fără date în Ubersuggest |
|---|---|---|---|---|---|---|---|
| 01 calculator și simulare | 23 | 2.932 | 2.172 | 321 | 43 | nimic (0/621 interogări) | calculator ipoteca; calculator cass (fără volum propriu) |
| 02 model, formular, cerere | 22 | 2.977 | 2.900 | 341 | 11 | nimic (0/594) | formular tipizat |
| 03 generator | 25 | 2.617 | 817 | 113 | 12 | nimic (0/675) | generator eticheta, generator diploma, generator invitatie |
| 04 verificare și validare | 25 | 2.452 | 2.032 | 169 | 18 | nimic (0/675) | validare iban, verificare carte identitate, verificare cod bare |
| 05 convertor și transformare | 22 | 1.842 | 771 | 79 | 8 | nimic (0/594) | transformare grade, convertor text, convertor diacritice, convertor heic |
| 06 mașină și drum | 22 | 2.627 | 1.291 | 112 | 21 | nimic (0/594) | valoare masina |
| 07 casă, chirie, utilități, bloc | 25 | 1.483 | 559 | 52 | 4 | nimic (0/675) | calcul suprafata, calculator intretinere |
| 08 școală și examene | 25 | 3.064 | 679 | 57 | 5 | nimic (0/675) | test cunostinte, punctaj admitere, convertor note |
| 09 muncă | 24 | 3.076 | 1.851 | 228 | 27 | nimic (0/648) | model scrisoare intentie, scrisoare recomandare |
| 10 evenimente și familie | 24 | 1.364 | 361 | 32 | 0 | nimic (0/648) | plan nunta, plan botez, plan mese, buget botez, calculator petrecere, calculator nunta |
| 11 PFA și firme mici | 24 | 1.609 | 1.104 | 121 | 1 | nimic (0/648) | generator etichete, calculator adaos, calculator manopera |
| 12 timp liber | 25 | 1.128 | 497 | 39 | 4 | nimic (0/675) | calculator semanat, varsta caine, calculator pace, marime schiuri și alte 10 expresii |
| **Total, după scoaterea dublurilor între familii** | | | **12.813** | **1.491** | **120** | | |

## Ce nu s-a putut face sau s-a făcut doar parțial

### 1. Volume
- **Acoperire.** 11.322 din 12.813 căutări păstrate (88%) au rămas „volum necunoscut”. Ubersuggest întoarce între 0 și ~170 de variante pe expresie, iar potrivirea s-a făcut doar pe text exact. Nu s-a estimat niciun volum.
- **Limita zilnică.** `keyword_overview` a fost folosit pe 138 de căutări scurte fără volum, până la limita zilnică de 150 de rapoarte. Două căutări din listă au rămas neinterogate: „cerere concediu invatamant” și „cerere tip alocatie”.
- **Keyword Planner** (Adspirer) a fost folosit o singură dată, ca probă de comparație, din cauza limitei de 15 apeluri pe lună.
- **Perioada datelor.** Ultima lună din istoric diferă de la o căutare la alta: de obicei 2026-10, uneori mai veche. Pentru volumele din `match_keywords` nu există istoric lunar. Riscul „sezonier” s-a putut nota doar după textul căutării, nu după date.

### 2. Rezultatele de azi (pasul 3)
- **Sursa listei.** Lista primelor 10 rezultate vine din `serp_analysis` (Ubersuggest), nu direct din Google: pagina de rezultate Google nu se poate citi fără ocolirea protecțiilor, iar DuckDuckGo HTML a răspuns cu verificare anti-bot.
- **Date de colectare diferite.** Între 2026-08-27 și 2026-11-15. Data e trecută la fiecare rând.
- **Liste cu goluri.** Multe colectări au goluri în pozițiile 1-10. Numărul de rezultate organice pe care s-a sprijinit verdictul e trecut la fiecare rând. Două cazuri limită:
  - „calcul consum”: `serp_analysis` nu a întors nimic, deci nu are verdict.
  - „verificare cnp”: nu are niciun rezultat organic în pozițiile 1-10.
- **Pozițiile peste 10 la loturile 01, 02, 03 și 05.** Când lista avea goluri, aceste loturi au trecut în tabele și rezultate de pe pozițiile 11-54: 62 de rânduri în total, mai ales aplicații Google Play netestate, documente și articole. Lotul 04 și loturile 06-10 s-au limitat strict la pozițiile 1-10.
  - Am verificat dacă vreun verdict depinde de aceste rânduri. Doar trei au instrumente funcționale: finance.imobiliare.ro (poz. 12, „calculator credit”), jobinfo.ro (poz. 13, „calculator salariu minim 2025”) și calculator-salarii.ro (poz. 12, „calculator salariu”). Toate trei sunt la căutări cu verdict PUTERNICE, care se sprijină pe primele 5 poziții.
  - Niciun verdict SLABE sau MEDII nu depinde de un rezultat de după poziția 10.
  - Numărul de rezultate trecut în CAUTARI.md („pe N rezultate din poz. 1-10”) numără doar pozițiile 1-10.
- **Testarea instrumentelor.**
  - Nu s-au introdus date personale reale (numere de înmatriculare, CNP-uri).
  - Verificatoarele de rovinietă au fost testate doar cu numărul-exemplu afișat de site-uri sau deloc.
  - Convertoarele de pe YouTube nu au fost testate.
- **Pauză tehnică.** Lucrul a fost întrerupt de limita de utilizare a contului (5 ore) și reluat după resetare. Nicio căutare nu a rămas nelucrată.

### 3. Eliminate la pasul 1, dar cu volum
64 de căutări eliminate la pasul 1 au volum de cel puțin 1.000 în Ubersuggest. Exemple:
- subiecte de bacalaureat de descărcat;
- plata taxei de pod prin SMS;
- verificarea facturii la un furnizor numit;
- „invitatii nunta” (14.800);
- „registru de casa” (1.300).

Nu au fost reintroduse. Lista completă e în `date/eliminate-la-pasul1-cu-volum.tsv`.

## Surse blocate la pasul 3 (pe loturi)

La pasul 1 nu s-a blocat nimic: Google a răspuns la toate cele 7.722 de interogări de completare automată.

La pasul 3 s-au notat și site-urile care au dat erori de conexiune, separat de blocajele anti-bot:

| Lot | Blocate (403, 429, captcha, anti-bot) | Nu s-au deschis (conexiune, TLS, 5xx) |
|---|---|---|
| 01 | ejobs.ro, canva.com, 8ore.ro, calculator-casa.raiffeisen.ro, bancatransilvania.ro, britannica.com | |
| 02 | shutterstock.com, harunpehlivan.arsigo.com, bancatransilvania.ro, raiffeisen.ro, unicredit.ro, cec.ro, ghiseul.ro, bpr.politiaromana.ro | mfinante.ro, finzoom.ro |
| 03 | time.is, universuljuridic.ro; asigurari.ro, calculatoare-salarizare.ro și contabilitatepebune.ro au cerut verificare anti-bot în browser, dar au mers prin curl | vehio.ro, oralocala.timein.org, mfinante.gov.ro, cnadnr.ro |
| 04 | aida.info.ro, portalcontabilitate.ro, trendyol.com, youtube.com, medium.com | erovinieta.ro/vgncheck (503), cnadnr.ro (502), anp.gov.ro |
| 05 | studocu.com, fliphtml5.com, ecomunicate.ro, facebook.com (cere logare), reddit.com (fără conținut) | facile.it, cvultau.ro, cjpolt.ro, hdsatelit.com |
| 06 | bancatransilvania.ro, raiffeisen.ro, cec.ro, capital.ro, portal.just.ro, impozitauto.ro, pdfcoffee.com, ejobs.ro; portalcontabilitate.ro a cerut verificare în browser, dar a mers prin curl | finzoom.ro, cronicavj.ro, calculatorvenituri.sdworx.ro, cas.cnas.ro, for.casbt.ro, politiaromana.ro (TLS) |
| 07 | youtube.com, rrf.ro, my.cnpp.ro (firewall), international-iq-test.com, distanta.com, reddit.com | anp.gov.ro, finzoom.ro, creatorsai.me (TLS) |
| 08 | youtube.com, assicurazioni.segugio.it, fontspace.com, capitalizemytitle.com, calculator-casa.raiffeisen.ro, bancatransilvania.ro, unicredit.ro, cec.ro | cnadnr.ro, bucuresti.cnadnr.ro, prefecturasibiu.ro, sb.politiaromana.ro (TLS) |
| 09 | evz.ro, upriserz.ro, impozitauto.ro, serviciielectronice.brasovcity.ro, autoklass.ro, youtube.com, social2.ro, termene.ro (9 URL-uri), liveutmb.sharepoint.com; portalcodulfiscal.ro a cerut verificare în browser, dar a mers prin curl | |
| 10 | ytmp3.rent, ro.linkedin.com, cnpp.ro, cnas.gov.md, listafirme.ro, studocu.com, btleasing.ro, raiffeisen-leasing.ro, unicreditleasing.ro | finzoom.ro, mfinante.gov.ro, dprp.gov.ro, afm.ro, economie.gov.ro |

## Verificarea a 30 de rânduri alese la întâmplare

(în lucru)
