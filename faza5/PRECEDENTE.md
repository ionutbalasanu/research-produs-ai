# Faza 5, pasul 1: precedente (patru valuri create de un termen legal)

Data citirii pentru toate sursele: 2026-11-16, dacă nu scrie altfel.

## Pe scurt

| Val | Termen (verificat în sursă) | Vârf lunar Shopify (recenzii, toate aplicațiile grupului) | Câștigătorul Shopify, zile față de termen | Recenzii după termen la cei listați după termen |
|---|---|---|---|---|
| GPSR | 13.12.2024 | 9 (decembrie 2024) | GCM / gpsr, −87 | 4 recenzii la 55 de aplicații |
| Accesibilitate (EAA) | 28.06.2025 | 42 (iunie 2025) | Avada Accessibility, −171 (firmă mare) | 14 recenzii la 76 de aplicații |
| Buton de retragere | 19.06.2026 | 2.788 (iunie 2026) | eu-widerrufsbutton, −161 | 68 recenzii la 75 de aplicații |
| Etichetă de garanție (GARAN) | 27.09.2026 | 147 (septembrie 2026) | eu-warranty-garan-label, −53 | 18 recenzii la 26 de aplicații (doar 7 săptămâni de la termen) |

**Concluzia pasului (dedus din tabelele de mai jos):**
1. **Doar unul din patru valuri a fost mare.** Butonul de retragere a adus de ~19 ori mai multe recenzii în luna termenului decât eticheta de garanție și de ~66 de ori mai multe decât accesibilitatea. GPSR aproape nu a existat ca val de aplicații pe Shopify. Ipoteza din faza 4 („un termen legal = un val") e adevărată doar pentru un tip de obligație: **un element funcțional nou (buton, formular, e-mailuri, legătura cu comanda), cerut tuturor magazinelor, pe care tema nu îl are și care nu se face de mână cu un text.** GPSR (date în descrierea produsului sau metafield, cum spune chiar răspunsul de pe forumul Shopify), eticheta de garanție (o imagine și un text) și accesibilitatea (overlay-uri existente de ani de zile, plus scutirea microîntreprinderilor) nu au avut forma asta. **dedus**
2. **Cine se listează după termen nu prinde nimic.** La toate cele patru valuri, aplicațiile listate după termen au împreună sub 70 de recenzii. La butonul de retragere: 44 de aplicații listate înainte au azi 3.696 de recenzii; 75 listate după au 68. **verificat în sursă** (numărătoarea), **dedus** (interpretarea)
3. **Cu câte luni înainte:** câștigătorii mici s-au listat cu **1,5-5,5 luni** înainte (−32 până la −171 de zile). Liderul valului mare s-a listat cu 5,3 luni înainte și a luat 70% din recenziile lunii termenului (1.947 din 2.788). Aplicațiile listate cu 2-6 săptămâni înainte au prins totuși 50-330 de recenzii. **Regula de lucru: listat cel târziu cu 3 luni înainte de termen, ideal 5-6, ca să ai recenziile de început și poziția în căutare când vine luna termenului.** **dedus**
4. **Valul se stinge în 1-2 luni.** La butonul de retragere: 2.788 în iunie, 176 în iulie, 67 în octombrie 2026 (o patruzecime din vârf). **verificat în sursă**
5. **Germania a fost motorul.** 65,2% din cele 3.451 de recenzii salvate în faza 4 pentru 7 aplicații de retragere și garanție vin din magazine germane; urmează Austria 5,2% și Franța 4,5%. **verificat în sursă** (`faza4/date/shopify/recenzii/*.json`, câmpul de țară)
6. **Platformele reacționează la termen, nu înainte.** Shopify a scos anularea prin „self-serve returns" pe 18.06.2026, cu o zi înainte de termen. WooCommerce Germanized (incumbentul german, 70.000 de instalări) a scos GPSR cu 78 de zile înainte, butonul cu 85 de zile înainte și eticheta GARAN cu 31 de zile înainte. **verificat în sursă**

## Metodă

- **Datele legale** au fost citite în textul oficial, prin serviciul Cellar al Oficiului pentru Publicații (EUR-Lex dă provocare WAF; vezi JURNAL.md). Fișierele sunt în `faza5/date/legal/`.
- **Shopify:** am luat toate aplicațiile din sitemap (30.532) al căror handle conține cuvinte-cheie ale celor patru obligații, plus aplicațiile lansate după 16.11.2024 din crawlul fazei 4 al căror nume sau subtitlu le conține. Rezultat: 457 de pagini descărcate (`faza5/date/shopify/app/`, analiza în `candidati.json`). Am încadrat fiecare aplicație într-un grup după titlu și am scos aplicațiile de alt tip (insigne de încredere, garanții extinse vândute, protecția expedierii, texte alternative). Pentru cele 58 de aplicații din grupuri cu cel puțin 5 recenzii am descărcat toate recenziile și le-am numărat pe luni (`faza5/date/shopify/recenzii/`, rezultatul în `valuri_shopify.json`). Scripturile sunt în `faza5/scripts/`.
- **WordPress.org:** căutare prin API după 13 termeni (1.564 de pluginuri, `faza5/date/wp/cautare_api.json`), apoi descărcările zilnice din `stats/plugin/1.0/downloads.php` (`faza5/date/wp/descarcari/`, analiza în `valuri_wp.json`).
- **„Autor mic":** regulile din faza 4. Shopify: dezvoltator cu cel mult 3 aplicații, fără firmă mare (numărate pe paginile `apps.shopify.com/partners/<cont>`, `faza5/date/shopify/partner/`). WordPress: autor cu cel mult 5 pluginuri, fără firmă mare.

**Limite:**
- Recenziile nu sunt vânzări. Sunt cel mai apropiat semn public (faza 4).
- Aplicațiile scoase din magazin nu mai apar în sitemap, deci valurile pot fi subestimate (supraviețuitori). **necunoscut** cât.
- Căutarea după handle ratează aplicațiile mai vechi de noiembrie 2024 cu handle fără cuvânt-cheie. La aplicațiile mai noi, crawlul fazei 4 acoperă și numele.
- La WordPress, „descărcări" include actualizările automate ale instalărilor existente. La pluginurile vechi (Germanized, Ally, UserWay), cifrele urmăresc lansările de versiuni, nu clienții noi. Seria API se oprește la 730 de zile, deci începe la 17.11.2024. Pentru GPSR lipsesc lunile dinainte de termen.
- Noiembrie 2026 e lună parțială (până pe 15-16).

---

## 1. GPSR: Regulamentul (UE) 2023/988

**Termenul:** art. 52: „It shall apply from 13 December 2024." Regulament, deci direct aplicabil. Sursa: http://publications.europa.eu/resource/celex/32023R0988 (EUR-Lex: https://eur-lex.europa.eu/eli/reg/2023/988/oj), `faza5/date/legal/32023R0988.html`. **verificat în sursă**

### Shopify
- 56 de aplicații în grup. 1 listată înainte de termen, 55 după (majoritatea în 2026). **verificat în sursă**
- **Câștigătorul:** GCM | GPSR Compliance (https://apps.shopify.com/gpsr), 401layers UG, 2 aplicații (aceeași firmă care va câștiga valul butonului de retragere), lansat **17.09.2024 = −87 de zile**. Azi are 29 de recenzii, rating 4,8. Prețuri: gratuit; 15 $/lună sau 149 $/an; 29 $/lună sau 299 $/an. **verificat în sursă**
- **Recenzii pe luni (toate aplicațiile grupului = doar GCM):**

| 2024-06 | 07 | 08 | 09 | 10 | 11 | **12** | 2025-01 | 02 | 03 | 04 | 05 | 06 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 3 | 3 | **9** | 7 | 0 | 0 | 1 | 1 | 2 |

- **Ultimele trei luni (aug.-oct. 2026):** 0 recenzii pentru GCM. Cele 55 de aplicații GPSR listate după termen au împreună 4 recenzii. **verificat în sursă**
- **Reacția Shopify:** nicio intrare GPSR în changelog-ul pentru comercianți (1.660 de intrări din 2018 până azi, `faza5/date/platforma/changelog_shopify_feed.xml`). Pe forumul Shopify, la întrebarea din 31.01.2025, singurul răspuns spune: „You can provide any information required under the GPSR by adding to your product descriptions or adding a metafield" (https://community.shopify.com/t/shopify-eu-general-product-safety-regulations-gpsr-any-updates/391307). Pagina nu marchează autorul ca angajat Shopify. **doar fragment**

### WordPress.org
- **gpsr-for-woocommerce** (WP Desk, 25 de pluginuri, deci nu e autor mic), adăugat **13.12.2024 = ziua termenului**, 300 de instalări. Descărcări: dec. 2024 500, ian. 472, feb. 196, mar. 374, apr. 235, mai 157, iun. 310. Ultimele trei luni: 564 în total. **verificat în sursă**
- **gpsr-ce-ukca-for-woocommerce** (Euverify), adăugat 24.01.2025 (+42 de zile), 20 de instalări. **verificat în sursă**
- **Reacția incumbentului:** WooCommerce Germanized 3.18.0, „New: Compliance with new GPSR regulation". Fișierul readme al etichetei 3.18.0 e modificat ultima dată pe 26.09.2024 (antetul `last-modified` din SVN), adică **−78 de zile**. Sursa: https://plugins.trac.wordpress.org/browser/woocommerce-germanized/trunk/readme.txt și https://plugins.svn.wordpress.org/woocommerce-germanized/tags/3.18.0/readme.txt. **verificat în sursă** (data = data ultimei modificări a fișierului din etichetă, deci **dedus** ca dată a lansării)
- **WooCommerce nativ:** nu are câmpuri GPSR. Există o cerere de funcție deschisă pe 10.10.2026, cu 1 vot (https://woocommerce.com/feature-request/native-eu-gpsr-product-safety-and-manufacturer-information/). **verificat în sursă**

**Valul GPSR:** practic inexistent pe Shopify (vârf 9 recenzii pe lună). **verificat în sursă**

---

## 2. Actul european privind accesibilitatea: Directiva (UE) 2019/882

**Termenul:** art. 31 alin. (2): „They shall apply those measures from 28 June 2025." Art. 2 alin. (2): directiva se aplică serviciilor prestate consumatorilor „after 28 June 2025". Sursa: http://publications.europa.eu/resource/celex/32019L0882, `faza5/date/legal/32019L0882.html`. **verificat în sursă**

### Shopify
- 103 aplicații în grup: 27 listate înainte de termen, 76 după. **verificat în sursă**
- **Câștigătorul:** Avada Accessibility ADA EAA (https://apps.shopify.com/sea-accessibility-ada-wcag), contul „TrustTerm by Avada", lansat **08.01.2025 = −171 de zile**, 331 de recenzii. Prețuri: gratuit; 9, 14 și 19 $/lună. **Avada e o firmă mare** (sitemapul are 11 aplicații cu prefixul „avada-"), **deci nu e autor mic**. **verificat în sursă** (prețuri, dată), **dedus** (firmă mare)
- **Ceilalți nou-veniți:** accessibilityway (−67 de zile, 48 de recenzii, 6 aplicații, de la 39 $/lună), accessify-web-accessibility (−1 zi, 45 de recenzii, 2 aplicații, 8 și 13 $/lună). Recenziile lor au venit mai ales în 2026, nu în jurul termenului. **verificat în sursă**
- **Recenzii pe luni (toate aplicațiile grupului cu cel puțin 5 recenzii):**

| 2024-12 | 2025-01 | 02 | 03 | 04 | 05 | **06** | 07 | 08 | 09 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | 8 | 5 | 3 | 13 | 13 | **42** | 27 | 17 | 21 | 27 | 12 | 20 |

Din care Avada: 0, 1, 4, 1, 8, 7, **32**, 17, 14, 16, 22, 4, 15.

- **Ultimele trei luni (aug.-oct. 2026):** 128 de recenzii în grup (Avada 33). Nu se stinge, dar nici nu a fost un val. **verificat în sursă**
- **Reacția Shopify:** nicio intrare despre accesibilitate sau EAA în changelog-ul pentru comercianți. **verificat în sursă** (absența în feed). Pagina de ajutor Shopify despre EAA: **necunoscut** (căutarea nu a găsit-o; sursele găsite sunt bloguri de vânzători).

### WordPress.org
- **Câștigătorul mic:** Accessibility Widget by OneTap (https://wordpress.org/plugins/accessibility-onetap/), autor cu 1 plugin, adăugat **12.11.2024 = −228 de zile**, azi **60.000 de instalări**. Pro: 129 $/an pentru un site, 169 $/an pentru 3 site-uri (preț de listă, cu reducere de Black Friday 59 $ și 99 $, https://wponetap.com/pricing/). **verificat în sursă**
- Descărcări OneTap pe luni (2024-12 până în 2025-12): 142, 230, 543, 1.030, 2.346, 3.595, **6.586**, 11.193, 4.850, 10.216, 12.346, 30.131, 18.299. Ultimele trei luni: 56.145. **Creșterea continuă după termen, deci nu e val, e piață.** **verificat în sursă** (cifre), **dedus** (interpretare)
- Pluginurile vechi (Ally/Elementor 500.000, UserWay 80.000, WP Accessibility 60.000) au salturi legate de versiuni noi, nu de termen. **dedus**

**Valul EAA:** mic pe Shopify (vârf 42 de recenzii), piață în creștere continuă pe WordPress. **verificat în sursă**

---

## 3. Butonul de retragere: Directiva (UE) 2023/2673

**Termenul:** art. 2 alin. (1): „Member States shall adopt and publish by 19 December 2025 … They shall apply those measures from 19 June 2026." Sursa: http://publications.europa.eu/resource/celex/32023L2673, `faza5/date/legal/32023L2673.html`. **verificat în sursă**

### Shopify
- 119 aplicații în grup: 44 listate înainte de termen (38 în ultimele 90 de zile), 75 după. Cele listate înainte au azi 3.696 de recenzii, cele listate după 68. **verificat în sursă**
- **Câștigătorii:**

| Aplicație | Dezvoltator (aplicații) | Lansată | Zile față de termen | Recenzii | Preț |
|---|---|---|---|---|---|
| eu-widerrufsbutton | 401layers UG (2) | 09.01.2026 | −161 | 2.324 | gratuit (mod de evaluare); 9,99 $/lună sau 99,99 $/an; 29,99 $/lună |
| eu-withdrawal-form (Revoq) | BuschBytes (2) | 11.03.2026 | −100 | 582 | gratuit; 9 $/lună sau 90 $/an; 25 $/lună |
| eu-widerruf-pro | ECOMBEAT (3) | 07.05.2026 | −43 | 330 | gratuit; 11,99 $ și 17,99 $/lună (planurile plătite vând acum verificarea adresei) |
| wideruf-button | Anviara LLC (1) | 06.05.2026 | −44 | 108 | gratuit; 7,99 $/lună |
| eu-withdrawal-button-form | Nayvo (4) | 03.06.2026 | −16 | 76 | gratuit; 7,99 $/lună sau 80 $/an; 22 $/lună |

Sursa: paginile aplicațiilor și ale partenerilor. **verificat în sursă**. Toți sunt autori mici, cu excepția Nayvo (4 aplicații, peste prag cu una).

- **Recenzii pe luni (25 de aplicații cu cel puțin 5 recenzii):**

| 2025-12 | 2026-01 | 02 | 03 | 04 | 05 | **06** | 07 | 08 | 09 | 10 | 11 (parțial) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 6 | 13 | 30 | 37 | 324 | **2.788** | 176 | 137 | 104 | 67 | 34 |

Din care eu-widerrufsbutton: 0, 1, 12, 14, 14, 195, **1.947**, 52, 36, 27, 18, 8.

- **Ultimele trei luni (aug.-oct. 2026):** 308 recenzii în grup, adică 11% din luna termenului. Liderul: 81. **verificat în sursă**
- **Reacția Shopify** (changelog pentru comercianți, `faza5/date/platforma/cl_*.html`): **verificat în sursă**
  - 18.06.2026: „Self-serve returns now support cancellations … This enables merchants selling in the EU to offer a withdrawal policy" (−1 zi).
  - 16.07.2026: Managed Markets acceptă cereri de anulare și retur în UE (+27 de zile).
  - 10.11.2026: regulile de retur și anulare se pot seta pe fiecare piață; variabile Liquid noi pentru ora cererii în notificări (+144 de zile).
  - Dacă funcția nativă acoperă cerința legală: **necunoscut**. Recenziile noi din august-octombrie arată că aplicațiile se instalează în continuare. **dedus**

### WordPress.org
| Plugin | Autor (pluginuri) | Adăugat | Zile | Instalări | Descărcări aug.-oct. 2026 |
|---|---|---|---|---|---|
| eu-order-withdrawal-button-for-woocommerce | vendidero (7, autorul Germanized) | 26.03.2026 | −85 | 6.000 | 25.272 |
| eu-withdrawal-compliance | Fernando Tellado (23) | 15.05.2026 | −35 | 2.000 | 12.083 |
| wt-eu-withdrawal-button | WebToffee (22) | 11.06.2026 | −8 | 1.000 | 5.826 |
| easy-return-eu-withdrawal-button-for-woocommerce | EasyReturn | 26.05.2026 | −24 | 500 | 2.409 |
| eu-withdrawal-button-for-woocommerce | riinagency | 24.04.2026 | −56 | 500 | 764 |

- Descărcările liderului pe luni (martie-noiembrie 2026): 161, 550, 1.577, **10.028**, 5.622, 9.434, 6.325, 9.513, 4.906. **verificat în sursă**
- Niciun câștigător WordPress nu e autor mic (faza 4 a ajuns la aceeași concluzie). **verificat în sursă**
- **Reacția incumbentului:** Germanized 4.0.0, „New: Withdrawal button in compliance with EU directive 2023/2673", eticheta 4.0.0 modificată pe 26.03.2026, adică **−85 de zile**, aceeași zi cu pluginul separat al aceluiași autor. **verificat în sursă**, data **dedusă** din antetul SVN.
- **WooCommerce nativ:** căutarea „withdrawal" pe blogul pentru dezvoltatori WooCommerce nu dă niciun articol (`faza5/date/platforma/woo_dev_s_withdrawal.html`). **verificat în sursă**

**Valul butonului:** singurul val mare. **verificat în sursă**

---

## 4. Eticheta de garanție: Directiva (UE) 2024/825

**Termenul:** art. 4 alin. (1): „By 27 March 2026, Member States shall adopt and publish … They shall apply those measures from 27 September 2026." Art. 22a nou din Directiva 2011/83/UE cere ca notificarea armonizată și eticheta armonizată să fie stabilite prin acte de punere în aplicare „By 27 September 2025". Considerentul 28: eticheta se plasează „directly next to the picture of the good in the case of online sale", iar notificarea poate fi „placed as a general reminder on the website". Sursa: http://publications.europa.eu/resource/celex/32024L0825, `faza5/date/legal/32024L0825.html`. **verificat în sursă**. Numărul regulamentului de punere în aplicare: **necunoscut** (nu l-am citit; nu schimbă data de aplicare).

### Shopify
- 77 de aplicații în grup: 51 listate înainte (34 în ultimele 90 de zile), 26 după. **verificat în sursă**. Grupul include și câteva aplicații vechi de garanții, ale căror recenzii nu intră în valul GARAN.
- **Câștigătorii:**

| Aplicație | Dezvoltator (aplicații) | Lansată | Zile | Recenzii | Preț |
|---|---|---|---|---|---|
| eu-warranty-garan-label | Nico Münster et al. GbR (2) | 05.08.2026 | −53 | 50 | gratuit până la 15 produse; 4,99 $/lună sau 49,90 $/an |
| eu-guarantee-warranty-label | Consentico (3) | 26.08.2026 | −32 | 49 | gratuit; 4,99 $/lună; 9,99 $/lună |
| eu-gewaehrleistungslabel | TG-AI Apps / timmgard GmbH (4) | 24.06.2026 | −95 | 38 | gratuit până la 20 de produse; 4,99 $ și 9,99 $/lună |
| eu-gewahrleistungslabel-garan | Appsentials (7) | 22.07.2026 | −67 | 18 | **necitit** |

**verificat în sursă**

- **Recenzii pe luni:**

| 2026-03 | 04 | 05 | 06 | 07 | 08 | **09** | 10 | 11 (parțial) |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 5 | 4 | **147** | 48 | 9 |

Lunile de după noiembrie 2026 nu există încă.

- **Ultimele trei luni:** coincid cu valul (199 de recenzii în aug.-oct.). În noiembrie (parțial): 9. **verificat în sursă**
- **Reacția Shopify:** nicio intrare despre etichetă sau notificarea de garanție în changelog. **verificat în sursă** (absența)

### WordPress.org
- garanlabs-eu-guarantee-notice-durability-labels (GaranLabs, 1 plugin), adăugat 28.08.2026 (−30), 200 de instalări; descărcări august-noiembrie: 69, 603, 746, 409. **verificat în sursă**
- arthursmith-guarantee-notice-garan-label (−42, 100 de instalări), eu-warranty-ready (−44, 50). **verificat în sursă**
- **Reacția incumbentului:** Germanized 4.1.0, „New: EU legal guarantee, commercial guarantee labels", eticheta modificată pe 27.08.2026, adică **−31 de zile**. **verificat în sursă**, data **dedusă** din antetul SVN.

**Valul etichetei:** mic (vârf 147 de recenzii pe lună), cu prețuri de 4,99 $/lună. **verificat în sursă**

---

## Ce înseamnă pentru calendar (dedus)

1. **Un termen legal nu e suficient.** Trebuie să ceară un element funcțional pe care tema nu îl are și pe care comerciantul nu îl poate face de mână. Altfel valul rămâne sub 150 de recenzii pe lună în tot magazinul Shopify, adică puțini clienți împărțiți la zeci de aplicații.
2. **Trebuie să atingă masiv magazinele din Germania.** Două treimi din valul butonului au venit de acolo.
3. **Fereastra de listare:** cel târziu cu 3 luni înainte, ideal cu 5-6. Construcția trebuie deci să înceapă cu cel puțin 5-8 luni înainte de termen (efortul estimat în faza 4 pentru butonul de retragere: 6-8 săptămâni, plus revizuirea Shopify, cu durată necunoscută).
4. **Prețul de piață al acestor aplicații:** plan gratuit + 5-12 $/lună. Doar GPSR (15-29 $) și accesibilitatea (9-39 $) au urcat mai sus.
5. **După val rămâne 3-11% din ritmul lunii termenului** (butonul: 67 în octombrie față de 2.788 în iunie). Venitul rămas vine din magazinele care nu dezinstalează.
6. **Platforma răspunde în jurul termenului**, nu cu luni înainte. La Shopify, răspunsul nativ la butonul de retragere a venit cu o zi înainte și nu a oprit instalările. La WooCommerce, incumbentul Germanized acoperă fiecare obligație germană cu 1-3 luni înainte, ceea ce închide WordPress pentru un nou-venit pe piața germană.
