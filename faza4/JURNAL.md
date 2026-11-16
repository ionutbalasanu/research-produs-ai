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
