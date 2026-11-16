# Faza 4, pasul 1: WordPress.org, măsurare

Data: 2026-11-16. Fereastra: pluginuri cu `added` ≥ 2024-11-16 (24 de luni). Curs BNR din 13.11.2026 (faza4/date/bnr_nbrfxrates.xml): 1 USD = 4,8428 lei, 1 EUR = 5,3498 lei.

## Ce s-a descărcat

- API: `https://api.wordpress.org/plugins/info/1.2/?action=query_plugins&request[browse]=new&request[per_page]=250&request[page]=N`, paginile 1-111. Pagina 111 coboară la 2024-10-27, deci pragul 2024-11-16 e acoperit. Răspunsurile brute sunt în `faza4/date/wp/new_p001.json.gz` … `new_p111.json.gz`. Am cerut API-ului să omită câmpurile `description`, `icons` și `download_link`, ca arhiva să rămână mică (4,9 MB). Toate celelalte câmpuri sunt cele brute. **verificat în sursă**
- **Rezultat: 27.519 pluginuri lansate în perioadă, dintre care 268 au `active_installs` ≥ 1.000 (0,97%).** Lista celor 268 cu slug, added, active_installs, rating, num_ratings, tags, last_updated și autor e în `faza4/date/wp/castigatori_1000.tsv`. **verificat în sursă**
- Numărul de pluginuri al fiecărui autor vine din `request[author]=<utilizator>` (răspunsuri în `faza4/date/wp/autori/`). Filtrul API-ului întoarce și pluginurile la care utilizatorul e doar contributor, deci cifra e o limită superioară. **dedus**
- Pentru pluginurile autorilor mici: `plugin_information` cu secțiunile (`faza4/date/wp/pluginuri/`), paginile de preț (`faza4/date/wp/preturi/`) și curbele de descărcări (`faza4/date/wp/descarcari/`).

## Limite de măsură, spuse de la început

1. **`active_installs` e rotunjit în trepte** (1.000, 2.000 … 10.000, 20.000). Un plugin cu 1.000 poate avea între 1.000 și 1.999 instalări. **verificat în sursă** (valorile din API sunt doar trepte)
2. **Instalările nu înseamnă clienți plătitori.** WordPress.org nu publică vânzări. Faptul că există o versiune plătită și prețul ei se văd. Câți o cumpără nu se vede. Ăsta e cel mai mare gol al pasului: în WordPress, „a prins clienți plătitori" rămâne **necunoscut** pentru fiecare plugin.
3. **Pluginurile închise sau retrase nu apar în API.** Numitorul conține doar supraviețuitorii, deci rata de reușită e supraestimată. **dedus**
4. **Grupările sunt făcute după problema rezolvată, prin expresii de căutare** aplicate pe slug, nume, etichete și descrierea scurtă. Aceeași expresie dă și numitorul, și numărătorul. Un plugin poate cădea în două grupuri. Expresiile sunt în `faza4/date/wp/grupuri_expresii.txt`. Numărătoarea e reproductibilă, dar granițele grupurilor sunt o alegere a mea. **dedus**
5. **Descărcările conțin zgomot.** Exemple: `designsetgo` are 313.212 descărcări în 730 de zile și 8.000 de instalări; `bolt-cta-button` are 7.429 descărcări în primele 30 de zile, apoi aproape nimic. Folosesc descărcările doar ca formă a curbei, nu ca număr de clienți. **verificat în sursă** (cifrele), **dedus** (interpretarea)

## Criteriul „autor mic"

Cel mult 5 pluginuri pe WordPress.org **și** fără o firmă mare în spate. Am scos din „mici": găzduiri (SiteGround, Hostinger, Cloudways, MilesWeb, JetHost, RunCloud, aaPanel), procesatori de plăți și curieri (pluginul oficial al unui serviciu), firme cu portofolii mari (Brainstorm Force, Softaculous, Syed Balkhi/Awesome Motive, Elementor, WPDeveloper, Themeisle, WP Royal, WPManageNinja, miniOrange, Acowebs) și conectorii oficiali ai unor SaaS (rankingCoach, Jotform, ProvenExpert, Ubersuggest). Ultimii sunt notați separat, în grupul WP-L. **dedus** (încadrarea firmelor e judecata mea, pe baza numelui și a site-ului)

## Grupuri cu cel puțin 3 nou-veniți mici peste prag

| ID | Problema | Lansate (numitor) | ≥1.000 instalări (toți) | Autori mici ≥1.000 | Rata autorilor mici |
|---|---|---|---|---|---|
| WP-A | Conectare agenți AI (MCP) la site | 248 | 15 | 5 | 2.0% |
| WP-B | Vizibilitate în căutarea AI (llms.txt, roboți AI) | 780 | 8 | 3 | 0.4% |
| WP-C | Blocarea roboților, țărilor și IP-urilor | 125 | 5 | 4 | 3.2% |
| WP-D | Butoane flotante de contact (WhatsApp, Telegram, apel) | 791 | 7 | 4 | 0.5% |
| WP-E | Gestionarea bibliotecii media (import, export, curățare) | 630 | 8 | 5 | 0.8% |
| WP-F | Banner de consimțământ cookie | 610 | 14 | 3 | 0.5% |
| WP-G | Widgeturi și extensii Elementor | 1094 | 24 | 7 | 0.6% |
| WP-H | Extensii pentru editorul de blocuri (Gutenberg) | 2473 | 36 | 9 | 0.4% |
| WP-I | Utilitare de administrare (notificări, heartbeat, setări PHP) | 80 | 5 | 3 | 3.8% |

Grupuri verificate care **nu** ajung la 3 autori mici (rămân în afara pasului 3):

| ID | Problema | Lansate | ≥1.000 (toți) | Autori mici ≥1.000 |
|---|---|---|---|---|
| WP-J | Widgeturi de recenzii (Google, Trustpilot) | 225 | 6 | 2 |
| WP-K | Teste A/B și hărți de căldură | 92 | 3 | 2 |
| WP-L | Conectori ai unor SaaS de articole SEO generate cu AI (soro-seo, getautoseo, textbulker, grandranker, outrank, koala-ai, babylovegrowth) | nenumărat separat | 7 | 0 mici în sensul de mai sus | n/a |

Pentru context, pe tot setul rata e 268 / 27.519 = 0,97%. Numărul de autori mici din tot setul nu l-am numărat.

WP-L nu e buzunar al canalului WordPress.org. Produsul e un SaaS vândut pe site-ul propriu, iar pluginul doar îl conectează. Instalările lui arată clienții SaaS-ului, nu faptul că magazinul aduce clienți. Îl notez în ANEXA.md. **dedus**

## Autorii mici: versiune plătită și preț

Prețurile au fost citite pe 2026-11-16 de pe paginile salvate în `faza4/date/wp/preturi/`. Fără altă mențiune, starea e **verificat în sursă**.

| Grup | Plugin (instalări) | Pluginuri autor | Versiune plătită | Preț | Sursa prețului |
|---|---|---|---|---|---|
| WP-A | royal-mcp (10.000) | 5 | da, în pachetul „Royally" | de la 9 $/lună (3 site-uri) | https://royalplugins.com/support/royal-mcp/ |
| WP-A | enable-abilities-for-mcp (6.000) | 1 | nu se vede; doar donații (ko-fi) | — | readme pe WP.org |
| WP-A | wsp-mcp-ai-agents-connector (3.000) | 1 | nu se vede („Free MCP plugin") | — | readme pe WP.org |
| WP-A | cowboy-mcp (2.000) | 1 | nu („no Pro tier, no credits") | — | readme pe WP.org |
| WP-A | diviops-agent (1.000) | 1 | da | Pro de la 29 €/an (prețul de fondator; regulat 49 €/an) | https://diviops.com/ |
| WP-B | llms-txt-generator (1.000) | 1 | da (aeomatic) | 49 $/an (1 site), 99 $ (3), 179 $ (20) | https://aeomatic.com |
| WP-B | lovedbyai-seo-for-llms-and-ai-search (1.000) | 1 | da, SaaS | 29 $/lună anual (Pro), 59 $/lună (Business) | https://lovedby.ai |
| WP-B | llm-bot-tracker-by-hueston (1.000) | 1 | nu („100% Free Forever") | — | readme pe WP.org |
| WP-C | botblocker-security (3.000) | 2 | probabil („Honest free version", pagina /pricing/ există) | **necunoscut**: pagina de preț a răspuns 400 | https://botblocker.top/pricing/ (blocat) |
| WP-C | advanced-ip-blocker (3.000) | 1 | nu se vede; donații prin Stripe | — | readme; site-ul advaipbl.com a răspuns 403 |
| WP-C | country-access-blocker (1.000) | 2 | nu se vede | — | readme pe WP.org |
| WP-C | geo-blocker (1.000) | 2 | nu pentru acest plugin (trimite la alt plugin, Fortress Login Pro) | — | readme pe WP.org |
| WP-D | animated-floating-chat-button (4.000) | 1 | nu se vede | — | readme |
| WP-D | bolt-cta-button (2.000) | 2 | nu („Every feature is free. Forever.") | — | readme |
| WP-D | dibrother-floating-buttons (1.000) | 3 | nu se vede | — | readme |
| WP-D | floating-contact-button-for-max-and-telegram (1.000) | 1 | da, „PRO" menționat | **necunoscut** (pagina autorului nu arată preț) | cryptolamer.ru |
| WP-E | smart-auto-upload-images (5.000) | 4 | nu se vede | — | readme |
| WP-E | add-from-server-reloaded (4.000) | 4 | da | 59 $/an (1 site), 79 $/an (3 site-uri) | https://elearningevolve.com/products/add-from-server-pro/ |
| WP-E | export-media-as-zip (3.000) | 4 | da („Premium") | **necunoscut** (nu am găsit pagina de preț) | readme |
| WP-E | media-sweep (1.000) | 4 | nu se vede | — | readme |
| WP-E | calliope-media-import-export (1.000) | 5 | da („Pro add-on") | **necunoscut** | readme |
| WP-F | faz-cookie-manager (3.000) | 1 | nu („no premium plan needed") | — | readme |
| WP-F | kansleri-cookie-consent (1.000) | 1 | nu („no pro version, and no upsells") | — | readme |
| WP-F | fz-152-rf (1.000) | autor negăsit prin API | da | 1.990 ₽ pe site, cu un an de actualizări (≈117 lei la 0,0589 lei/₽) | https://fz152rf.ru/ |
| WP-G | pdf-smart-viewer-for-elementor (1.000) | 1 | nu se vede; pagina autorului dă 404 | — | deknows.com |
| WP-G | popup-for-elementor (1.000) | 1 | da („Optional Pro Version") | **necunoscut**: conexiunea a fost resetată | popupforelementor.com (blocat) |
| WP-G | dynamic-elementor-acf-repeater (1.000) | 2 | da (Freemius) | **necunoscut** (pagina de plată Freemius nu e statică) | readme |
| WP-G | aitoel-html-importer (1.000) | 4 | da, SaaS cu cotă de conversii | Solo 47 $/an (30 conversii/lună) | https://aitoelementor.com |
| WP-G | mox-icons-pack-for-elementor (1.000) | 1 | nu se vede | — | readme |
| WP-G | custom-iframe (4.000) | 2 | da | 19 $ o dată (redus de la 49 $), Studio 39 $ (5 site-uri) | https://customiframe.com/pricing/ |
| WP-G | better-post-filter-widgets-for-elementor (4.000) | 2 | nu se vede („The only free…") | — | readme |
| WP-H | designsetgo (8.000) | 2 | nu se vede | — | designsetgoblocks.com |
| WP-H | ollie-menu-designer (6.000) | 2 | indirect (Ollie Pro, temă) | nu l-am citit | readme |
| WP-H | gutentools (4.000) | 1 | nu se vede | — | readme |
| WP-H | justify-for-paragraph-block (3.000) | 3 | nu | — | readme |
| WP-H | frontedit-live-block-editor (1.000) | 1 | da | 59,90 $/an (1 site), 179,90 $/an (5), 299,90 $/an (nelimitat) | https://maintainwp.com/products/frontedit/ |
| WP-H | blockenberg (1.000) | 1 | da | 6 $ o singură dată | https://blockenberg.com/ |
| WP-H | faqly-ultimate-faq (1.000) | 1 | da | 15 $ (redus de la 20 $) | seothemesexpert.com |
| WP-H | makeiteasy-slider (1.000) | 5 | nu se vede | — | readme |
| WP-H | noted (1.000) | 2 | nu se vede | — | readme |
| WP-I | unnotifier (1.000) | 5 | nu se vede pe pagina citită | — | wp-aifactory.com |
| WP-I | easy-php-settings (1.000) | 4 | da („Easy PHP Settings Pro") | **necunoscut** | plugin.codereyes.com (fără preț în pagină) |
| WP-I | heartbeat-controller (1.000) | 2 | nu (buymeacoffee) | — | readme |
| WP-J | gr-widget (1.000) | 1 | da | 4,75 $/lună anual (57 $/an), 5,99 $/lună lunar | https://grwidget.com/pricing |
| WP-J | gutensuite-reviewkit (1.000) | 2 | da | 9,99 $/an (1 site), 39,99 $/an (5), 79,99 $/an (nelimitat) | https://reviewkit.gutensuite.net/pricing |
| WP-K | opti-behavior (2.000) | 1 | da | 89 €/an (1 site), 179 €/an (5) | https://optiuser.com/opti-behavior/pricing/ |
| WP-K | convertpro (10.000) | 4 | nu se vede | — | readme |

## Ce arată pasul 1 (dedus)

- În **toate** grupurile, cei mai mulți nou-veniți mici care au trecut de 1.000 de instalări **nu au versiune plătită vizibilă** sau au una ieftină (6-60 $ o dată sau pe an). Prag de 1.000 instalări + autor mic + versiune plătită cu preț citit: WP-A 2, WP-B 2, WP-C 0, WP-D 0, WP-E 1, WP-F 1, WP-G 2, WP-H 3, WP-I 0, WP-J 2, WP-K 1.
- Niciun grup nu are 3 nou-veniți mici care să aibă **și** versiune plătită cu preț citit **și** să rezolve aceeași problemă, cu excepția WP-H. Acolo însă cele 3 rezolvă probleme diferite (editare din front-end, șabloane, FAQ).
- Pragul de 1.000 de instalări funcționează ca filtru de **atenție**, nu de **plată**. Schimbarea pragului e discutată la pasul 3.

## Anexă: toate pluginurile cu ≥1.000 instalări din fiecare grup (din API, 2026-11-16)

### WP-A. Conectare agenți AI (MCP) la site

Lansate în perioadă (numitor, după expresia de căutare): **248**. Cu ≥1.000 instalări active: **15**. Dintre ele, autori mici: **5** (rată de reușită a autorilor mici: 2.0%).

| slug | added | instalări | rating | nr. evaluări | autor | pluginuri ale autorului pe WP.org | last_updated | tags |
|---|---|---|---|---|---|---|---|---|
| mcp-adapter | 2026-10-02 | 70000 | 100 | 1 | WordPress.org | 57 | 2026-10-16 | abilities-api, ai, mcp, model-context-protocol |
| diviops-agent | 2026-08-20 | 1000 | 0 | 0 | diviops | 1 | 2026-11-04 | ai, divi, mcp, rest-api, site-builder |
| ylabs-ai-assistant-connector | 2026-07-23 | 1000 | 0 | 0 | YLabs | 2 | 2026-09-09 | ai, chatgpt, claude, mcp, seo |
| wsp-mcp-ai-agents-connector | 2026-07-13 | 3000 | 100 | 9 | Bilal Naseer | 1 | 2026-11-11 | ai, ai-agent, chatgpt, claude, mcp |
| cowboy-mcp | 2026-07-03 | 2000 | 100 | 7 | februality | 1 | 2026-11-14 | ai-agent, claude, mcp, mcp-server, model-context-protocol |
| miniorange-secure-mcp-server | 2026-06-04 | 10000 | 100 | 10 | miniOrange | 25 | 2026-11-13 | chatgpt, claude, mcp, mcp-server, wordpress-mcp |
| xspeed | 2026-05-27 | 10000 | 100 | 28 | WPDeveloper | 39 | 2026-11-12 | cache, mcp, optimization, page-speed, performance |
| vibe-ai | 2026-04-20 | 100000 | 98 | 216 | SeedProd | 9 | 2026-11-11 | ai-assistant, chatgpt, claude, mcp, mcp-server |
| easy-mcp-ai | 2026-03-25 | 40000 | 98 | 17 | Themeisle | 35 | 2026-11-10 | chatgpt, claude, connector, mcp, wordpress-mcp |
| enable-abilities-for-mcp | 2026-03-24 | 6000 | 100 | 17 | Fabio Montenegro | 1 | 2026-11-13 | ai, content-management, mcp, rest-api, woocommerce |
| ylabs-connector-for-wpwriter | 2026-02-15 | 5000 | 100 | 1 | YLabs | 2 | 2026-10-20 | ai-assistant, chatgpt, claude, connector, mcp |
| royal-mcp | 2026-01-14 | 10000 | 100 | 7 | Royal Plugins | 5 | 2026-11-11 | ai, chatgpt, claude, elementor, mcp |
| ai | 2025-12-02 | 60000 | 84 | 10 | WordPress.org | 57 | 2026-10-30 | abilities, ai, artificial-intelligence, experiments, mcp |
| angie | 2025-09-17 | 100000 | 66 | 20 | Elementor | 14 | 2026-10-06 | agent, ai, assistant, elementor, mcp |
| thinkrank | 2025-08-10 | 20000 | 98 | 38 | WPDeveloper | 39 | 2026-11-15 | ai-seo, google-search-console, schema, seo, xml-sitemap |

### WP-B. Vizibilitate în căutarea AI (llms.txt, roboți AI)

Lansate în perioadă (numitor, după expresia de căutare): **780**. Cu ≥1.000 instalări active: **8**. Dintre ele, autori mici: **3** (rată de reușită a autorilor mici: 0.4%).

| slug | added | instalări | rating | nr. evaluări | autor | pluginuri ale autorului pe WP.org | last_updated | tags |
|---|---|---|---|---|---|---|---|---|
| lovedbyai-seo-for-llms-and-ai-search | 2026-01-13 | 1000 | 88 | 5 | LovedByAI | 1 | 2026-11-15 | aeo, agentic-commerce, ai-seo, generative-engine-optimization, geo |
| vigia | 2026-01-02 | 2000 | 100 | 19 | Fernando Tellado | 23 | 2026-11-09 | ai, analytics, claude, gpt, llms |
| llm-bot-tracker-by-hueston | 2025-09-09 | 1000 | 60 | 2 | Hueston | 1 | 2025-09-24 | ai-bot-tracker, ai-seo, chatgpt-detector, claude-bot, perplexity-crawler |
| llms-full-txt-generator | 2025-03-14 | 4000 | 100 | 7 | visibility.so | 2 | 2026-11-09 | ai, generator, llms, seo, txt |
| check-for-broken-links | 2025-02-06 | 2000 | 80 | 6 | Norse Digital Group LLC | 3 | 2026-11-10 | ai-visibility, broken-link-checker, internal-link, rank-tracker, uptime-monitor |
| llms-txt-generator | 2025-01-11 | 1000 | 70 | 2 | Pedro Ladeira | 1 | 2025-02-14 | ai, artificial-intelligence, chatgpt, content-optimization, seo |
| website-llms-txt | 2025-01-04 | 50000 | 94 | 12 | Ryan Howard | 6 | 2026-10-04 | ai, llm, rankmath, seo, yoast |
| xagio-seo | 2024-12-09 | 10000 | 98 | 51 | Xagio SEO | 1 | 2026-11-13 | aeo, ai-seo, rank-tracker, schema, seo |

### WP-C. Blocarea roboților, țărilor și IP-urilor

Lansate în perioadă (numitor, după expresia de căutare): **125**. Cu ≥1.000 instalări active: **5**. Dintre ele, autori mici: **4** (rată de reușită a autorilor mici: 3.2%).

| slug | added | instalări | rating | nr. evaluări | autor | pluginuri ale autorului pe WP.org | last_updated | tags |
|---|---|---|---|---|---|---|---|---|
| atomic-edge-security | 2026-01-29 | 1000 | 100 | 5 | shift8 | 15 | 2026-10-02 | 2fa, firewall, malware, scanner, security |
| botblocker-security | 2025-11-02 | 3000 | 98 | 14 | Yevhen Leonidov | 2 | 2026-11-09 | anti-spam, brute-force, captcha, firewall, security |
| country-access-blocker | 2025-09-19 | 1000 | 100 | 3 | Valeri Kluger | 2 | 2026-01-24 | block-country, block-ip, country-blocker, geo-blocking, ip-blocker |
| advanced-ip-blocker | 2025-06-26 | 3000 | 98 | 28 | IniLerm | 1 | 2026-11-15 | 2fa, firewall, geoblocking, security, waf |
| geo-blocker | 2025-05-18 | 1000 | 100 | 1 | Mohamed Shili | 2 | 2025-05-18 | access-control, country-restriction, geo-blocking, geolocation, ip-blocker |

### WP-D. Butoane flotante de contact (WhatsApp, Telegram, apel)

Lansate în perioadă (numitor, după expresia de căutare): **791**. Cu ≥1.000 instalări active: **7**. Dintre ele, autori mici: **4** (rată de reușită a autorilor mici: 0.5%).

| slug | added | instalări | rating | nr. evaluări | autor | pluginuri ale autorului pe WP.org | last_updated | tags |
|---|---|---|---|---|---|---|---|---|
| bolt-cta-button | 2026-04-23 | 2000 | 100 | 4 | ismeteroglu | 2 | 2026-05-29 | click-to-call, contact-button, floating-button, sticky-bar, whatsapp |
| shore-booking-widget | 2025-11-21 | 3000 | 0 | 0 | shoregmbh | 1 | 2026-03-16 | appointments, booking, scheduling, shore, widgets |
| siteleads | 2025-11-06 | 10000 | 100 | 2 | Extend Themes | 10 | 2026-08-21 | ai-chatbot, chat-button, contact-widget, lead-generation, whatsapp |
| smashballoon-wpchat-livechat-customer-support | 2025-10-10 | 7000 | 90 | 2 | Syed Balkhi | 80 | 2026-11-12 | chat-button, chat-widget, click-to-chat, customer-support, whatsapp |
| dibrother-floating-buttons | 2025-09-02 | 1000 | 100 | 2 | Di Brother | 3 | 2025-09-06 | call-now, contact-button, floating-buttons, messenger, zalo |
| floating-contact-button-for-max-and-telegram | 2025-08-16 | 1000 | 100 | 7 | Alexander Alekseenko | 1 | 2026-11-02 | contact-button, facebook-messenger, floating-button, telegram, whatsapp |
| animated-floating-chat-button | 2025-02-16 | 4000 | 100 | 6 | HABIBUR (Adnan Habib) | 1 | 2026-10-17 | click-to-chat, live-chat, whatsapp, whatsapp-chat-button, woocommerce-whatsapp |

### WP-E. Gestionarea bibliotecii media (import, export, curățare)

Lansate în perioadă (numitor, după expresia de căutare): **630**. Cu ≥1.000 instalări active: **8**. Dintre ele, autori mici: **5** (rată de reușită a autorilor mici: 0.8%).

| slug | added | instalări | rating | nr. evaluări | autor | pluginuri ale autorului pe WP.org | last_updated | tags |
|---|---|---|---|---|---|---|---|---|
| add-from-server-reloaded | 2025-12-10 | 4000 | 100 | 4 | Adeel | 4 | 2026-10-14 | ftp, import, large-files, upload, upload-limit |
| export-media-as-zip | 2025-11-04 | 3000 | 74 | 3 | Huzoor Bux | 4 | 2026-10-09 | backup, download-images, export, media, zip |
| maxlimits-increase-maximum-limits | 2025-10-28 | 2000 | 100 | 2 | Dominopress | 26 | 2026-04-10 | execution-time, max-upload-size, max_input_vars, memory-limit, php-limits |
| media-sweep | 2025-10-27 | 1000 | 76 | 11 | WPCreatix | 4 | 2026-11-15 | cleanup, files, images, library, media |
| calliope-media-import-export | 2025-10-07 | 1000 | 74 | 3 | Maira Foresto | 5 | 2026-09-24 | csv-export, csv-import, media-export, media-import, media-library |
| post-export-import-with-media | 2025-09-20 | 1000 | 90 | 8 | wpazleen | 8 | 2026-10-28 | export-media, import, migration, page-export, post-export |
| smart-auto-upload-images | 2025-08-03 | 5000 | 86 | 6 | Burhan Nasir | 4 | 2026-10-26 | auto-upload, external-images, import-images, media-library, seo |
| url-image-importer | 2025-02-13 | 1000 | 100 | 2 | Infinite Uploads | 4 | 2026-09-29 | csv-import, image-import, images, media-library, upload |

### WP-F. Banner de consimțământ cookie

Lansate în perioadă (numitor, după expresia de căutare): **610**. Cu ≥1.000 instalări active: **14**. Dintre ele, autori mici: **3** (rată de reușită a autorilor mici: 0.5%).

| slug | added | instalări | rating | nr. evaluări | autor | pluginuri ale autorului pe WP.org | last_updated | tags |
|---|---|---|---|---|---|---|---|---|
| cookieray | 2026-05-23 | 1000 | 100 | 1 | DevItems | 29 | 2026-10-14 | ccpa, cookie-banner, cookie-consent, gdpr, privacy |
| cookiez | 2026-05-18 | 50000 | 88 | 5 | Elementor | 14 | 2026-09-30 | ccpa, compliance, cookie-consent, gdpr |
| eu-withdrawal-compliance | 2026-05-15 | 2000 | 100 | 17 | Fernando Tellado | 23 | 2026-10-29 | consumer-rights, garan, legal-guarantee, withdrawal, woocommerce |
| faz-cookie-manager | 2026-04-30 | 3000 | 100 | 30 | fabiodalez | 1 | 2026-11-11 | ccpa, consent, cookie, gdpr, privacy |
| surecookie | 2026-03-23 | 80000 | 98 | 26 | Brainstorm Force | 31 | 2026-11-09 | ccpa, consent-logs, cookie-banner, cookie-consent, cookie-policy |
| kansleri-cookie-consent | 2026-03-19 | 1000 | 100 | 7 | tapiokansleri | 1 | 2026-11-02 | cookie-banner, cookie-consent, gdpr, google-consent-mode, privacy |
| legalblink-for-aruba | 2026-01-23 | 10000 | 0 | 0 | LegalBlink | 2 | 2026-06-19 | compliance, cookie, gdpr, policy, privacy |
| fz-152-rf | 2025-12-06 | 1000 | 100 | 5 | Kotik | 0 | 2026-10-30 | 152-%d1%84%d0%b7, cookie, %d0%bf%d0%b5%d1%80%d1%81%d0%be%d0%bd%d0%b0%d0%bb%d1%8c%d0%bd%d1%8b%d0%b5-%d0%b4%d0%b0%d0%bd%d0%bd%d1%8b%d0%b5, %d1%81%d0%be%d0%b3%d0%bb%d0%b0%d1%81%d0%b8%d0%b5, woocommerce |
| privacy-policy-usercentrics | 2025-11-19 | 1000 | 0 | 0 | cookiebot | 2 | 2026-02-27 | ccpa, compliance, gdpr, privacy, privacy-policy |
| getterms-cookie-consent-policies | 2025-11-19 | 1000 | 100 | 1 | getterms | 1 | 2026-10-07 | compliance, cookie-consent, gdpr, privacy, terms-of-service |
| atr-cookie-notice | 2025-09-14 | 1000 | 100 | 13 | yehudaT | 6 | 2026-11-07 | amendment-13, consent, cookies, israeli-law, privacy |
| cookieadmin | 2025-07-15 | 400000 | 100 | 3 | Softaculous | 14 | 2026-10-12 | banner, consent, cookie, gdpr, notice |
| mate-recently-viewed-products | 2025-06-01 | 1000 | 100 | 2 | Alfonso Catrón | 1 | 2025-06-14 | block, cache, products, recently-viewed, woocommerce |
| wpconsent-cookies-banner-privacy-suite | 2024-12-20 | 200000 | 98 | 88 | Syed Balkhi | 80 | 2026-11-12 | ccpa, cookie-banner, cookie-consent, cookie-notice, gdpr |

### WP-G. Widgeturi și extensii Elementor

Lansate în perioadă (numitor, după expresia de căutare): **1094**. Cu ≥1.000 instalări active: **24**. Dintre ele, autori mici: **7** (rată de reușită a autorilor mici: 0.6%).

| slug | added | instalări | rating | nr. evaluări | autor | pluginuri ale autorului pe WP.org | last_updated | tags |
|---|---|---|---|---|---|---|---|---|
| aitoel-html-importer | 2026-06-04 | 1000 | 100 | 3 | georget777 | 4 | 2026-10-23 | ai, elementor, html-import, import, page-builder |
| miniorange-secure-mcp-server | 2026-06-04 | 10000 | 100 | 10 | miniOrange | 25 | 2026-11-13 | chatgpt, claude, mcp, mcp-server, wordpress-mcp |
| mox-icons-pack-for-elementor | 2026-05-25 | 1000 | 100 | 2 | moxtheme | 1 | 2026-10-07 | elementor, icon-pack, icons, svg-icons, web-design |
| rs-template-builder | 2026-04-28 | 2000 | 0 | 0 | RSTheme | 12 | 2026-10-01 | elementor, footer-builder, header-builder, mega-menu, popup |
| manage | 2026-03-08 | 100000 | 40 | 1 | Elementor | 14 | 2026-11-01 | bulk, elementor, monitoring, performance, updates |
| royal-mcp | 2026-01-14 | 10000 | 100 | 7 | Royal Plugins | 5 | 2026-11-11 | ai, chatgpt, claude, elementor, mcp |
| ultimate-data-table-addon-for-elementor | 2026-01-07 | 1000 | 0 | 0 | RSTheme | 12 | 2026-09-30 | data-table, data-tables, elementor, responsive-table, table-addon |
| news-photocard-pro | 2025-11-02 | 1000 | 0 | 0 | Rasedul Haque Rumi | 9 | 2025-11-02 | design, elementor, news, social-media, template |
| marqueeall | 2025-09-30 | 1000 | 0 | 0 | Aman Brar | 6 | 2026-08-24 | elementor, image-marquee, marquee, news-ticker, ticker |
| header-footer-builder-for-elementor | 2025-09-27 | 30000 | 100 | 5 | Turbo Addons | 7 | 2026-10-17 | elementor-footer, elementor-header, elementor-templates, header-footer-builder, mega-menu |
| angie | 2025-09-17 | 100000 | 66 | 20 | Elementor | 14 | 2026-10-06 | agent, ai, assistant, elementor, mcp |
| pdf-smart-viewer-for-elementor | 2025-07-17 | 1000 | 60 | 2 | DeKnows | 1 | 2025-09-20 | elementor, pdf, responsive, viewer, zoom |
| loop-grid-extender-for-elementor-pro | 2025-06-26 | 1000 | 100 | 9 | Cool Plugins | 38 | 2026-10-22 | acf-repeater-fields, dropdown-filter, elementor, loop-grid, taxonomy-filter |
| language-switcher-for-divi-polylang | 2025-05-26 | 1000 | 100 | 2 | Cool Plugins | 38 | 2026-11-13 | divi, elementor, language-switcher, multilingual, polylang |
| popup-for-elementor | 2025-05-25 | 1000 | 20 | 1 | Veelo | 1 | 2026-06-06 | elementor, modal, popup, wordpress-popup |
| classified-listing-toolkits | 2025-05-08 | 4000 | 0 | 0 | RadiusTheme | 15 | 2026-10-18 | classified-listing, divi, elementor, listing-plugin, wordpress-builder-support |
| dynamic-elementor-acf-repeater | 2025-04-04 | 1000 | 100 | 4 | wpluna | 2 | 2026-09-02 | acf-repeater, dynamic-tags, elementor, loop-grid, repeater-fields |
| custom-iframe | 2025-02-26 | 4000 | 100 | 5 | Coderz Studio | 2 | 2026-06-15 | 3d-flip-book, elementor, embed-pdf, embed-youtube, iframe |
| inspiro-starter-sites | 2025-02-11 | 10000 | 100 | 1 | WPZOOM | 20 | 2026-11-14 | demo-importer, elementor, gutenberg, starter-sites, templates |
| advanced-marquee-effect | 2025-02-08 | 2000 | 94 | 6 | mdashikul | 7 | 2026-08-01 | elementor-marquee, icon-box-marquee, logo-slider, marquee-text, news-ticker |
| better-post-filter-widgets-for-elementor | 2025-02-06 | 4000 | 100 | 18 | WP Smart Widgets | 2 | 2026-10-25 | ajax-filter, elementor, post-filter, product-filter, woocommerce |
| element-camp | 2025-01-13 | 1000 | 100 | 1 | wpdive | 6 | 2026-04-22 | addons, elementor, widget |
| hello-plus | 2024-12-05 | 70000 | 60 | 1 | Elementor | 14 | 2026-05-19 | elementor, hello-plus, hello-themes, themes, widgets |
| if-so-conditional-elementor-elements | 2024-12-02 | 1000 | 100 | 1 | If-So Dynamic Content | 3 | 2026-09-02 | conditional, dynamic-content, elementor, geotargeting, location |

### WP-H. Extensii pentru editorul de blocuri (Gutenberg)

Lansate în perioadă (numitor, după expresia de căutare): **2473**. Cu ≥1.000 instalări active: **36**. Dintre ele, autori mici: **9** (rată de reușită a autorilor mici: 0.4%).

| slug | added | instalări | rating | nr. evaluări | autor | pluginuri ale autorului pe WP.org | last_updated | tags |
|---|---|---|---|---|---|---|---|---|
| scrumptious | 2026-09-28 | 1000 | 100 | 1 | natebald | 1 | 2026-11-04 | cooking, food-blog, recipe, recipe-card, schema |
| cosmo-block-edit-mode-for-acf | 2026-08-29 | 1000 | 0 | 0 | Bakhodir Sh | 2 | 2026-11-12 | block-editor, blocks, custom-fields, editor, inline-editing |
| frontedit-live-block-editor | 2026-07-20 | 1000 | 100 | 2 | Pierce | 1 | 2026-09-25 | block-editor, front-end-editing, frontend-editor, gutenberg, inline-editor |
| gr-widget | 2026-07-11 | 1000 | 0 | 0 | GR Widget | 1 | 2026-11-15 | business-reviews, google-reviews, google-reviews-embed, google-reviews-widget, testimonials |
| spectra-blocks | 2026-07-08 | 70000 | 92 | 54 | Brainstorm Force | 31 | 2026-11-11 | ai-website-builder, block-editor, gutenberg-blocks, page-builder, website-builder |
| erecht24 | 2026-07-08 | 50000 | 100 | 1 | erecht24 | 1 | 2026-10-12 | gutenberg, imprint, legal, privacy, shortcode |
| zip-ai | 2026-07-02 | 2000 | 100 | 2 | Brainstorm Force | 31 | 2026-11-12 | ai-agent, ai-website-builder, gutenberg, website-builder, wordpress-ai |
| cookiez | 2026-05-18 | 50000 | 88 | 5 | Elementor | 14 | 2026-09-30 | ccpa, compliance, cookie-consent, gdpr |
| blockenberg | 2026-01-16 | 1000 | 92 | 5 | blockenberg | 1 | 2026-11-09 | blocks, custom-blocks, editor, gutenberg, page-builder |
| iconvert-email-marketer | 2025-12-19 | 1000 | 0 | 0 | iConvert | 3 | 2026-09-17 | email, gmail, newsletter, sendgrid, smtp |
| load-combined-core-block-assets | 2025-12-08 | 1000 | 100 | 6 | Weston Ruter | 31 | 2026-09-18 | performance |
| designsetgo | 2025-11-14 | 8000 | 100 | 3 | Justin Nealey | 2 | 2026-10-23 | animations, blocks, form-builder, gutenberg, query-loop |
| botblocker-security | 2025-11-02 | 3000 | 98 | 14 | Yevhen Leonidov | 2 | 2026-11-09 | anti-spam, brute-force, captcha, firewall, security |
| better-block-editor | 2025-10-29 | 6000 | 100 | 11 | Dream Theme | 1 | 2026-11-11 | animation, block-editor, page-builder, responsive, templates |
| country-access-blocker | 2025-09-19 | 1000 | 100 | 3 | Valeri Kluger | 2 | 2026-01-24 | block-country, block-ip, country-blocker, geo-blocking, ip-blocker |
| persian-calendar | 2025-09-16 | 3000 | 100 | 8 | Mohammadreza Ahm | 10 | 2026-11-12 | calendar, gutenberg, jalali, shamsi, %d8%b4%d9%85%d8%b3%db%8c |
| ollie-menu-designer | 2025-09-12 | 6000 | 100 | 8 | Mike McAlister | 2 | 2026-09-03 | block, dropdown-menu, mega-menu, mobile-menu, navigation |
| galleryberg-gallery-block | 2025-07-27 | 2000 | 100 | 9 | Imtiaz Rayhan | 11 | 2026-10-19 | block, gallery, gutenberg, images, lightbox |
| mailerpress | 2025-07-23 | 1000 | 100 | 17 | MailerPress Team | 2 | 2026-10-26 | email-automation, email-marketing, newsletter, subscribers, woocommerce-emails |
| phone-validator-with-flags-for-woocommerce | 2025-07-12 | 1000 | 100 | 9 | Mokhtar Bensaid | 5 | 2026-05-25 | checkout, country-flags, phone-field, phone-validation, woocommerce |
| advanced-ip-blocker | 2025-06-26 | 3000 | 98 | 28 | IniLerm | 1 | 2026-11-15 | 2fa, firewall, geoblocking, security, waf |
| mate-recently-viewed-products | 2025-06-01 | 1000 | 100 | 2 | Alfonso Catrón | 1 | 2025-06-14 | block, cache, products, recently-viewed, woocommerce |
| sliderberg | 2025-05-29 | 2000 | 100 | 7 | Imtiaz Rayhan | 11 | 2026-11-08 | block, carousel, gutenberg, slider, text-slider |
| language-switcher-for-divi-polylang | 2025-05-26 | 1000 | 100 | 2 | Cool Plugins | 38 | 2026-11-13 | divi, elementor, language-switcher, multilingual, polylang |
| geo-blocker | 2025-05-18 | 1000 | 100 | 1 | Mohamed Shili | 2 | 2025-05-18 | access-control, country-restriction, geo-blocking, geolocation, ip-blocker |
| easy-tabs-block | 2025-04-24 | 1000 | 100 | 5 | Easy Tabs Block | 2 | 2026-10-21 | accordion, responsive-tabs, tab, tabs, wordpress-tabs |
| gslider-blocks | 2025-04-23 | 1000 | 100 | 7 | Noruzzaman | 2 | 2026-11-09 | carousel, gutenberg, logo-carousel, slider, slideshow |
| faqly-ultimate-faq | 2025-04-15 | 1000 | 76 | 5 | drakearthur | 1 | 2026-11-13 | accordion, faq, faq-block, faq-shortcode, faqs |
| table-of-content-block | 2025-03-23 | 3000 | 100 | 4 | bPlugins | 106 | 2026-11-12 | best-table-of-contents, block, sitemap, table-of-content-block, table-of-contents |
| custom-iframe | 2025-02-26 | 4000 | 100 | 5 | Coderz Studio | 2 | 2026-06-15 | 3d-flip-book, elementor, embed-pdf, embed-youtube, iframe |
| inspiro-starter-sites | 2025-02-11 | 10000 | 100 | 1 | WPZOOM | 20 | 2026-11-14 | demo-importer, elementor, gutenberg, starter-sites, templates |
| justify-for-paragraph-block | 2025-01-10 | 3000 | 100 | 3 | NickDigitalProjects | 3 | 2026-07-27 | block-editor, justify, paragraph, text-alignment, typography |
| makeiteasy-slider | 2025-01-02 | 1000 | 100 | 3 | Lovro Hrust | 5 | 2026-09-26 | block, carousel, slider, swiper |
| gutentools | 2024-12-31 | 4000 | 100 | 4 | Gutentools | 1 | 2026-09-14 | block-editor, gutenberg, gutenberg-templates |
| cp-blocks-for-acf | 2024-11-24 | 1000 | 100 | 3 | Tekod lab. | 6 | 2026-11-08 | acf, copy, flexible, layout, paste |
| noted | 2024-11-22 | 1000 | 100 | 15 | Kyle Van Deusen | 2 | 2026-10-14 | admin, dashboard, markdown, notes, productivity |

### WP-I. Utilitare de administrare (notificări, heartbeat, setări PHP)

Lansate în perioadă (numitor, după expresia de căutare): **80**. Cu ≥1.000 instalări active: **5**. Dintre ele, autori mici: **3** (rată de reușită a autorilor mici: 3.8%).

| slug | added | instalări | rating | nr. evaluări | autor | pluginuri ale autorului pe WP.org | last_updated | tags |
|---|---|---|---|---|---|---|---|---|
| desktop-mode | 2026-05-07 | 1000 | 100 | 23 | WordPress.org | 57 | 2026-11-13 | admin-dashboard, custom-dashboard, dashboard-notes, notes, sticky-notes |
| maxlimits-increase-maximum-limits | 2025-10-28 | 2000 | 100 | 2 | Dominopress | 26 | 2026-04-10 | execution-time, max-upload-size, max_input_vars, memory-limit, php-limits |
| unnotifier | 2025-10-01 | 1000 | 100 | 4 | Alexander Kovalev | 5 | 2026-08-27 | dashboard-cleanup, disable-admin-notices, disable-notices, hide-notifications, notice-control |
| easy-php-settings | 2025-08-12 | 1000 | 100 | 7 | shahadul878 | 4 | 2026-11-06 | debug, ini, performance, php-settings, wp-config |
| heartbeat-controller | 2025-07-28 | 1000 | 0 | 0 | Abdur Rahman | 2 | 2025-07-28 | admin-ajax-php, autosave, heartbeat, heartbeat-api, performance |

### WP-J. Widgeturi de recenzii (Google, Trustpilot)

Lansate în perioadă (numitor, după expresia de căutare): **225**. Cu ≥1.000 instalări active: **6**. Dintre ele, autori mici: **2** (rată de reușită a autorilor mici: 0.9%).

| slug | added | instalări | rating | nr. evaluări | autor | pluginuri ale autorului pe WP.org | last_updated | tags |
|---|---|---|---|---|---|---|---|---|
| gr-widget | 2026-07-11 | 1000 | 0 | 0 | GR Widget | 1 | 2026-11-15 | business-reviews, google-reviews, google-reviews-embed, google-reviews-widget, testimonials |
| marqueeall | 2025-09-30 | 1000 | 0 | 0 | Aman Brar | 6 | 2026-08-24 | elementor, image-marquee, marquee, news-ticker, ticker |
| gutensuite-reviewkit | 2025-09-06 | 1000 | 100 | 2 | GutenSuite | 2 | 2026-11-16 | reviews, social-proof, testimonials, trust-badges, trustpilot |
| creta-testimonial-showcase | 2025-07-26 | 3000 | 20 | 2 | Creta Themes | 1 | 2026-11-10 | feedback, reviews, testimonials, wordpress-plugin |
| gslider-blocks | 2025-04-23 | 1000 | 100 | 7 | Noruzzaman | 2 | 2026-11-09 | carousel, gutenberg, logo-carousel, slider, slideshow |
| advanced-marquee-effect | 2025-02-08 | 2000 | 94 | 6 | mdashikul | 7 | 2026-08-01 | elementor-marquee, icon-box-marquee, logo-slider, marquee-text, news-ticker |

### WP-K. Teste A/B și hărți de căldură

Lansate în perioadă (numitor, după expresia de căutare): **92**. Cu ≥1.000 instalări active: **3**. Dintre ele, autori mici: **2** (rată de reușită a autorilor mici: 2.2%).

| slug | added | instalări | rating | nr. evaluări | autor | pluginuri ale autorului pe WP.org | last_updated | tags |
|---|---|---|---|---|---|---|---|---|
| opti-behavior | 2025-11-19 | 2000 | 100 | 6 | OptiUser | 1 | 2026-11-16 | behavior-analytics, click-tracking, conversion-optimization, heatmap, woocommerce-analytics |
| sigmize | 2025-10-31 | 6000 | 74 | 3 | Brainstorm Force | 31 | 2026-11-16 | ab-testing, conversion-optimization, heatmaps, split-testing, woocommerce |
| convertpro | 2025-03-30 | 10000 | 100 | 1 | WP Grids | 4 | 2026-10-06 | ab-testing, ab-test, conversion-rate, landing-page, split-testing |
