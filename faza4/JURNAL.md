# Faza 4: jurnal de decizii

Data: 2026-11-16. Ramura de lucru a pornit din `origin/claude/inspiring-heisenberg-egdczr`.

## Pasul 1 (WordPress.org)

1. **Arhiva brută fără descrieri.** Am cerut API-ului să omită `description`, `icons` și `download_link`. Cu ele, 111 pagini ar fi avut ~170 MB. Câmpurile cerute în sarcină sunt toate păstrate.
2. **Oprirea paginării.** Pagina 111 coboară la 2024-10-27. Am păstrat doar `added` ≥ 2024-11-16.
3. **Gruparea după problemă.** Am făcut-o cu expresii de căutare pe slug, nume, etichete și descrierea scurtă. Aceeași expresie dă numitorul și numărătorul. Prima clasificare automată, exclusivă (un plugin într-un singur grup), a pus greșit multe pluginuri: geo-blocarea a ajuns la „vizibilitate AI" din cauza cuvântului „geo", iar butonul de retragere UE la „cookie". Am trecut la grupuri neexclusive, definite pe problemă, și am verificat de mână fiecare plugin de peste 1.000 de instalări din grupurile reținute.
4. **„Autor mic".** Am numărat pluginurile autorului prin `request[author]`. Firmele mari, găzduirile, procesatorii de plăți și conectorii oficiali ai unor SaaS au fost scoși prin judecata mea. Lista e în PAS1_WORDPRESS.md.
5. **Conectorii SaaS de articole AI (WP-L)** nu sunt tratați ca buzunar al canalului WordPress.org, pentru că produsul se vinde în afara magazinului.
6. **Pagini blocate, neocolite:** botblocker.top/pricing (400), advaipbl.com (403), popupforelementor.com (conexiune resetată), deknows.com (404).

## Pasul 2 (Shopify App Store)

1. **Ce există, verificat înainte de folosire:** robots.txt (permite /categories și paginile aplicațiilor; interzice `*q=*`, adică nu am folosit căutarea), sitemap.xml cu 30.532 de aplicații în engleză (fără dată de lansare), 161 de adrese de categorie. Dintre ele, 122 sunt categorii-frunză cu listă completă la `/categories/<slug>/all?sort_by=newest`. Celelalte 39 răspund 404 la `/all`, pentru că sunt doar părinți.
2. **Sortarea „newest" urmează data „Launched" de pe pagina aplicației.** Am verificat pe 6 aplicații din aceeași categorie: datele scad monoton. Pe asta se sprijină oprirea paginării.
3. **Oprirea în fiecare categorie.** Am deschis pagina ultimei aplicații de pe fiecare pagină de listă. Când data ei a coborât sub 2024-11-16, am găsit granița în pagina respectivă prin căutare binară, deschizând paginile aplicațiilor.
4. **Ritm.** 4 procese în paralel, câte o cerere la ~0,7 s fiecare, cu reîncercare la eroare.
5. **Rezultatul crawlerului:** 20.755 de aplicații unice lansate în fereastră. 451 au cel puțin 20 de recenzii, iar 182 trec toate pragurile. Am verificat granița la două categorii și am deschis aleator 3 aplicații dintr-o categorie: toate erau corecte.
6. **„Plan plătit"** = un preț > 0 în secțiunea de prețuri a paginii aplicației sau „$" în eticheta de preț. „Free" fără alt plan înseamnă gratuit.

## Pasul 3 (buzunare)

1. **Buzunarele sunt pe problemă, nu pe categoria Shopify.** Numitorul e numărul de aplicații lansate în fereastră al căror nume și subtitlu se potrivesc cu o expresie. Membrii au fost aleși de mână dintre cele 182, după ce am citit numele și prețurile. Firmele mari (Judge.me, Trustpilot, Chatbase, Shogun, GoKwik, Clickpost) au fost scoase.
2. **Expresiile s-au rafinat de două ori.** B6 prindea „ChatGPT" prin cuvântul „chat", iar B7 prindea orice „bot". La B3 și B6, câte un membru nu se potrivea cu expresia și a fost adăugat la numitor.
3. **La WordPress am adăugat o condiție:** cel puțin 2 nou-veniți mici cu preț citit. Pragul de 1.000 de instalări singur nu spune nimic despre plată.
4. **Curbele de 90 de zile la Shopify sunt numărate din recenzii.** Am descărcat toate recenziile celor 59 de nou-veniți (10 pe pagină, sortare implicită, fără sortare după dată în magazin) și le-am numărat după data lor.
5. **Clasamentul** e după numărul de nou-veniți plătiți, mediana recenziilor la 90 de zile și ritmul din august-octombrie 2026. E o judecată, nu un scor.
6. **Accesibilitatea și protecția expedierii** au fost eliminate prin criteriul (d), înainte de clasament.

## Pasul 4 (slăbiciuni)

1. La lideri am folosit filtrul de rating al magazinului (`ratings[]=1,2,3`), primele 6 pagini. Am verificat că filtrul întoarce doar 1-3 stele.
2. Shopify nu are forum public de suport pe aplicație. „Fire nerezolvate" s-au citit doar pe WordPress.org.
3. Fiecare citat a fost verificat automat față de textul recenziei salvate. Două citate au fost corectate: unul trunchiat și unul tradus în loc de original.

## Pasul 6 (propuneri)

1. **Am păstrat 3 propuneri, cu a treia marcată „slabă".** Ea e susținută doar de legătura cu faza 1 (09-P4) și de plângerile la lider, nu de curbe.
2. **B2 (vizibilitate AI) nu a intrat**, deși are mai mulți nou-veniți decât B8. Funcția de bază se face de mână, iar 700 de lansări arată clonare.
3. **Regulile platformei au fost citite pe shopify.dev și pe developer.wordpress.org**, pentru criteriile (b) și (c) și pentru secțiunea „regulile platformei". Nu am citit acolo nimic altceva.
4. **Prețurile propuse și pragurile de oprire** sunt judecata mea și sunt marcate „dedus".
