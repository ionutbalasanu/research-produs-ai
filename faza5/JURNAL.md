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

## Push

1. Primul push a fost respins de scanarea de secrete GitHub: pagina legislation.gov.uk a SI 2024/1332 conține șiruri care seamănă cu chei Mailgun (fals pozitiv, cod de analiză al site-ului). Am păstrat textul paginii ca `.txt` (cu șirurile înlocuite) și am scos HTML-ul din git (`.gitignore`).

## Pasul 2 (calendar)

1. Căutarea a fost împărțită la doi agenți: acte UE și acte naționale (UK, DE, FR, IT, ES, NL, PL, RO). Datele celor două obligații UE reținute (CRA, CLP) le-am recitit eu în text.
2. **CLP e reținut condiționat.** Data de 1.1.2028 e în vigoare azi, în textul publicat. Omnibus VI, votat de Parlament, poate să o schimbe. Regula din sarcină cere data citită în sursa oficială, iar asta e data în vigoare.
3. **Descărcarea textului adoptat de PE (T10-0362/2026) a fost refuzată de sistemul de permisiuni al sesiunii.** Nu am ocolit; am folosit Legislative Observatory prin WebFetch.
4. **Tutunul UK** a fost verificat de agent în textul legii și în SI 2026/996. Nu l-am recitit, pentru că nu ajunge la propuneri (termen prea aproape).
5. **Abonamentele UK** stau la „de urmărit": regulamentul e proiect și s.254 nu are regulament de commencement.

## Pasul 4 (verificare)

1. Verificarea independentă (VERIFICARE.md) a confirmat toate datele legale, totalurile lunare și datele Germanized. A găsit o eroare în `valuri.py`: excluderea „RMA" fără majuscule scotea aplicații ca widerruf-app („Germany", „confirmation"), iar „claims" scotea o aplicație GARAN.
2. **Corecția mea diferă puțin de numărătoarea verificatorului.** Am făcut „RMA" cuvânt întreg cu majuscule, am scos „claims" și „alt text" (păstrat doar ca excludere când titlul nu conține „accessib") și am adăugat „extended warrant", „warranty upsell", „warranty management", ca să nu intre garanțiile extinse vândute în grupul GARAN. Rezultat: retragere 127 de aplicații (verificatorul: 126), EAA 123 (105), GPSR 60 (58), garanție 77 (78). Totalurile lunare ale butonului ies identic (2.792 în iunie, 72 în octombrie). Diferențele sunt doar în aplicații fără recenzii.
3. Toate corecțiile din lista verificatorului au fost aplicate în PRECEDENTE.md, CALENDAR.md și PROPUNERI.md. Niciuna nu schimbă concluzia pașilor 1 și 5.

## Pasul 5 (propuneri)

1. **Nicio propunere.** Am construit din precedente un test cu patru condiții (element funcțional, toate magazinele, fără răspuns nativ, timp de listare). Nicio obligație din calendar nu le trece. Testul e judecata mea, sprijinită pe cifrele din PRECEDENTE.md.
2. C2 (CLP) a fost cea mai apropiată. Am respins-o pentru data nesigură, precedentul GPSR și prezența liderului 401layers.
