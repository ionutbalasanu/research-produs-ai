# Faza 2: unelte pentru volum de căutare

Verificat la 2026-11-15 de sesiunea principală.

## 1. Ubersuggest (conector MCP): unealta principală

- **Stare:** autentificat, plan „tier1”.
- **Limite:** 150 de rapoarte pe zi, iar fiecare apel la `keyword_overview` sau `match_keywords` consumă unul.
- **Locație:** România are `locId` 2642, limba `ro`.
- **Probă 1:** `keyword_overview("calculator salariu net", ro, 2642)`.
  - Volum lunar: **90.500**.
  - Istoric lunar disponibil din 2025-01 până în **2026-01**, adică ultima lună cu date e ianuarie 2026, nu luna curentă.
  - Exemple din istoric: 135.000 în 2025-01, 74.000 în 2025-12, 90.500 în 2026-01.
- **Probă 2:** `match_keywords(["model cerere"], ro, 2642)`.
  - Într-un singur apel întoarce volumul expresiei de bază (2.900) și ~90 de variante cu volum, din 233 găsite, cu paginare.
  - Exemple: „model cerere demisie simpla” 1.900, „model cerere concediu” 1.300, „model cerere radiere auto primarie” 720.
- **Folosire:** volumele din faza 2 vin din `match_keywords` pe expresiile de bază, cu potrivire exactă a textului. Pentru căutările rămase fără volum se folosește `keyword_overview`, câte una, în limita rapoartelor zilnice.

## 2. Google Ads Keyword Planner prin Adspirer (conector MCP): verificare încrucișată

- **Stare:** cont Google Ads conectat (3764143097), unealta `research_keywords`.
- **Limite:** 15 apeluri pe lună pentru întregul conector. La 2026-11-15 erau folosite 4 înainte de probă; după probă mai rămân aproximativ 10.
- **Probă:** expresii de pornire „calculator salariu net”, „model cerere demisie”, „verificare cui”, „calculator rata credit”, „generator factura”; România, limba română.
  - „calculator salariu net”: **90.500** pe lună, aceeași cifră ca în Ubersuggest.
  - „model cerere demisie fara preaviz”: 1.300 (Ubersuggest: 1.600).
  - „verificare cui anaf”: 5.400.
- **Observație:** Keyword Planner grupează variantele apropiate și le dă același volum. De exemplu, „calc salariu net”, „calculatie salariu net” și „calculatorsalariu net” primesc toate 90.500. Cifrele lui nu se adună între variante.
- **Folosire:** doar pentru verificare încrucișată pe câteva rânduri, din cauza limitei lunare.

## 3. Sugestii de completare automată (pasul 1)

- **Google:** `suggestqueries.google.com/complete/search?client=firefox&hl=ro&gl=ro&q=...` funcționează prin curl simplu (HTTP 200, JSON). Probă: „calculator salariu n” a întors 10 sugestii, de exemplu „calculator salariu net 2026”, „calculator salariu net cu bonuri de masa”.
- **DuckDuckGo:** `duckduckgo.com/ac/?q=...&kl=ro-ro` funcționează (HTTP 200). Rezervă pentru cazul în care Google blochează.
- **Bing:** `api.bing.com/osjson.aspx` a întors HTTP 204, fără conținut. Nu poate fi folosit.

## 4. Pasul 3 (rezultatele de azi)

- Nu există acces direct la pagina de rezultate Google: `google.com/search` nu se folosește prin curl, ar însemna ocolirea protecțiilor anti-bot.
- **Sursa listei de rezultate:** `serp_analysis` din Ubersuggest dă primele URL-uri din ultima colectare, cu data colectării. Reîmprospătarea costă 2 credite din 250 pe lună și nu se folosește fără acordul utilizatorului.
- **Citirea paginilor:** fiecare pagină din listă se deschide și se citește cu curl simplu.
- **Ce se notează:** data colectării SERP pentru fiecare căutare.
