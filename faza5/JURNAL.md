# Faza 5: jurnal de decizii

Data: 2026-11-16. Ramura de lucru `claude/loving-ptolemy-i15ysg` a pornit din `origin/claude/elegant-ramanujan-p46d2r`.

## Surse și acces

1. **EUR-Lex răspunde cu provocare WAF** (HTTP 202, `x-amzn-waf-action: challenge`). Nu am ocolit-o cu browser. Am citit textele prin **Cellar**, serviciul oficial al Oficiului pentru Publicații al UE (`http://publications.europa.eu/resource/celex/<CELEX>`, cu `Accept: application/xhtml+xml`), care servește același text publicat în Jurnalul Oficial. Scriptul e `faza5/scripts/cellar.sh`. Fiecare citare dă ambele linkuri.
2. **gesetze-im-internet.de** închide conexiunea (reset). Notat, neocolit. Pentru Germania se folosește recht.bund.de (Bundesgesetzblatt).
3. **legifrance.gouv.fr** răspunde 403. Notat, neocolit.
4. **plugins.trac.wordpress.org/log** a dat 429 o dată. Datele versiunilor Germanized au fost luate din antetul `last-modified` al fișierului readme din fiecare etichetă SVN. Asta e data ultimei modificări a etichetei, nu neapărat a publicării, deci e marcată „dedus".

## Pasul 1 (precedente)

1. **Selecția aplicațiilor Shopify** fără căutarea din magazin (interzisă în robots.txt, ca în faza 4): handle-uri din sitemap + numele aplicațiilor din crawlul fazei 4. 457 de pagini.
2. **Grupul unei aplicații se dă după titlu.** Aplicația `gpsr` (GCM) are azi în titlu și „GARAN", dar a fost lansată în 2024 ca aplicație GPSR, deci am pus-o la GPSR.
3. **Recenziile** au fost descărcate din nou pentru toate cele 58 de aplicații (nu am refolosit fișierele fazei 4), ca toate seriile să aibă aceeași dată. Doar procentul de țări (65,2% Germania) vine din fișierele fazei 4, pentru că doar acolo e salvată țara.
4. **„Câștigător"** = aplicația cu cele mai multe recenzii din grup. La EAA câștigătorul e o firmă mare (Avada), deci am dat și nou-veniții mici.
5. **WordPress: seria de descărcări are maximum 730 de zile**, deci începe la 17.11.2024. La GPSR lipsesc lunile dinainte de termen. Am notat.
6. **Faza 4 spunea 2.601 recenzii în iunie 2026 pentru 7 aplicații.** Aici sunt 2.788 pentru 25 de aplicații. Nu e o contradicție: grupul e mai larg.
