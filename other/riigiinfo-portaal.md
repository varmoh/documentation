# Riigiinfo portaal - arhitektuuriline kirjeldus
Selle dokumendi eesmärk on anda täielik arhitektuuriline ülevaade, kuidas ehitada avatud lähtekoodiga lihtne, LLM-põhine, Eesti riigiinfo portaal.

---

## 1. Ülevaade

Süsteem koosneb kahest suuremast komponendist:

1. **Scraper Pipeline** - kogub ja struktureerib riigiinfo
2. **Backend API** - vastab kasutajale LLM-i abil
3. **Frontend** - kasutajaliides päringute esitamiseks

```
                  ┌────────────────────┐
                  │      Scraper        │
                  │  (ETL + puhastus)   │
                  └─────────┬───────────┘
                            │
     HTML / PDF / JSON      │     Cron job 1x päevas/nädalas
────────────────────────────┼───────────────────────────────────
                            ▼
                  ┌────────────────────┐
                  │   Data Storage      │
                  │ SQLite + Faiss index│
                  │   (dokumendid+vektorid)
                  └─────────┬───────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │      Backend        │
                  │  FastAPI / Node.js  │
                  └─────────┬───────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │      LLM API        │
                  │ (Groq, Gemini, HF)  │
                  └─────────┬───────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │      Frontend       │
                  │  (React / SPA / UI) │
                  └─────────────────────┘
```

---

## 2. Scraper Pipeline

### Funktsioonid

* Laeb alla avalikud HTML-lehed, PDF-dokumendid ja API-d (PPA, MTA, SKA, Riigi Teataja)
* Puhastab HTML ja PDF dokumendid (eemaldab menüüd, reklaamid, jalused)
* Chunkib dokumendid 300-500 sõna lõikudeks
* Lisab meta-info (URL, kategooria, timestamp)
* Loob embeddingud Faiss / Chroma / LanceDB jaoks
* Salvestab lõplikud chunkid SQLite andmebaasi ja embedding indeksi

### Scraperi töötsükkel

* Jookseb eraldi cron-jobina või GitHub Actions workflow’na
* Värskendab ainult muudetud või uued dokumendid
* Backend ei tee scrapingut päringu ajal

---

## 3. Data Storage

* **SQLite**: dokumentide metadata ja tekst (failipõhine, serverivaba)

  ```
  documents
  ---------
  id (pk)
  category
  source_url
  title
  content_text
  updated_at
  ```
* **Faiss / Chroma / LanceDB**: embeddingute indeks, mis viitab SQLite id-dele
* Kiire otsing (1–5 ms) ja täiesti lokaalne

---

## 4. Backend API

### Funktsioonid

1. Võtab kasutaja päringu
2. Loob embeddingu küsimusest
3. Otsib Faiss indeksist 3–8 kõige relevantsemat chunk’i
4. Koostab prompti LLM-ile
5. Saadab päringu LLM API-le (Groq / Gemini / HF / kohalik mudel)
6. Vormindab vastuse frontendi jaoks:

   * tekst
   * ametlik allikas / URL
   * kontaktid
   * hoiatus „Ei ole õiguslik nõu“

### Tehnoloogia

* Python: FastAPI või Flask
* Node.js alternatiiv: Express / Fastify
* SQLite + Faiss / Chroma integratsioon

---

## 5. Frontend

* React / Vue / Next.js või statiline HTML + JS
* Küsimuse lahter + vastuse ala
* Võib olla chatbot stiilis või lihtne otsing
* Kõik päringud lähevad backendile → backend teeb otsingu ja LLM API päringu

---

## 6. Arhitektuuri eelised

* **Kiirus**: Faiss + SQLite otsing <5ms, LLM vastab 150–300ms
* **Tasuta**: kõik komponendid tasuta (Python, SQLite, Faiss, LLM Free Tier)
* **Hallutsinatsioonivaba**: LLM selgitab ainult scraperi poolt kogutud dokumente
* **Stabiilne**: ei sõltu kodulehtede uptime’ist
* **Lihtne laiendada**: uued kategooriad lisatakse scraperisse → update andmebaasis

---

## 7. Kokkuvõte

* **Scraper**: kogub ja struktureerib infot, käib offline
* **Data storage**: SQLite + Faiss / Chroma indekseerib dokumendid ja embeddingud
* **Backend**: FastAPI / Node.js, otsib dokumente, küsib LLM-i, tagastab kasutajale
* **Frontend**: React / SPA, kasutajaliides päringute esitamiseks
* **LLM API**: tasuta tierid või kohalik mudel
* **Kõik tasuta ja kerge infrastruktuuriga**

---

# 🟦 Soovitused

* Hoia scraper eraldi protsessina, mitte backendis
* Hoia andmebaas ja embeddingud lokaalselt või väikese serveri Free Tieris
* Uuenda scraper kord päevas/nädalas
* Kasuta LLM-i ainult dokumentide selgitamiseks, mitte otseseks seaduslikuks nõuks
