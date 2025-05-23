### 1. Manifestide genereerimine
- Koguda vajalikud andmed komponentide, versioonide ja konfiguratsioonide kohta.
- Koostada uuenduste manifestid struktureeritud formaadis (JSON/YAML).
- Rakendada versioonihaldus manifestidele.

### 2. Manifestide valideerimine
- Rakendada skeemipõhine valideerimine (nt SCHEMA-001).
- Tagada keelatud väljade puudumine (nt log_content, user_id).
- Logida vigased kirjed ja visata need tagasi.

### 3. Manifestide salvestamine ja haldamine
- Talletada valideeritud manifestid turvalises registris või andmebaasis.
- Tagada manifestide ajalugu ja versioonide jälgitavus.
- NEED 2 TASKI OLKS CENTRAL CENTOP ALL TEOSTATAVAD, EHK REGISTER JA HISTORY/VERSION SÄILITATAKSE CENTRAL CENTOPS ALL

### 4. API loomine manifestide jagamiseks
- Arendada turvaline API, mis eksponeerib manifestide andmeid.
- Tagada API kaudu struktureeritud ja päringuvõimeline JSON-väljund.
- Toetada päringuid nagu `metrics_by_component`, `error_rate_over_time`, `uptime_by_environment`.

### 5. Integratsioon GitHub Actionsiga
- Integratsioon oleks Github poolne, ehk et ndpoint CENTRAL CENTOPSIS mis on ootel, sinna poole workflow pushib peale image ehitamise workflowd manifeti

### 6. Kliendiagentide informeerimine
- Tagada, et kliendiagent saab API kaudu vajaliku manifesti info.
- Toetada manifesti rakendamise ja uuenduste algatamise mehhanisme kliendikeskkonnas.
