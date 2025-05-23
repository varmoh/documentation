telemeetria service

**Minu enda jaoks:**  
Telemetria, ehk lahendus kus süsteem jälgib iseennast ja eavitab kuidas läheb.
Mida jälgitakse ?
Kas CentOpsi enda agent töötab?

Kas update-runner jookseb õigesti?

Kui mitu uuendust on tehtud ja mitu neist ebaõnnestus?

Kas CentOpsi telemeetria teenus saab andmeid?

Kui kaua võtab CentOpsi enda API vastamine?

**Kireldus**
CentOps peab pakkuma standardiseeritud, valideeritavat ja turvalist telemeetrialahendust oma komponentide töökindluse ja oleku jälgimiseks. 
Lahendus peab vastama SCHEMA-001 määratud skeemile ning toetama andmete kogumist, valideerimist ja edasiandmist visualiseerimise või alerting-süsteemidele.

**Tegevused:**  
- Rakenda telemeetriapunktid ja andmete kogumine  
- CentOps ADR VIS-001
- Tagada andmete turvalisus ja kättesaadavus

**Valmisoleku kriteeriumid:**  
- **Telemeetriaskeem (schema) on rakendatud kõikides CentOpsi komponentides:**
  - Igal komponendil peab olema `/metrics` või muu määratud endpoint.
  - Skeem sisaldab vähemalt järgmisi välju:
    - `environment_id`, `component`, `metric_type`, `value`, `timestamp`
  - Puuduvad keelatud väljad:
    - `log_content`, `user_id`, `trace_payloads`

- **Kõik telemeetriasisendid valideeritakse skeemi vastu enne töötlemist:**
  - Vigased kirjed logitakse ja visatakse tagasi.
  - Versioonihaldus (`input_schema_version`) peab olema toetatud.

- **Telemeetriaväljundid eksporditakse turvalise API kaudu:**
  - API peab pakkuma struktureeritud JSON-põhist väljundit.
  - API peab toetama vähemalt järgmisi päringuid:
    - `metrics_by_component`
    - `error_rate_over_time`
    - `uptime_by_environment`

- **Telemeetrialahendus ei kogu ega ekspordi klientide tundlikku teavet:**
  - Kontrollmehhanismid tagavad, et tundlikud väljad ei satu ekslikult väljundisse.
  - Kõik andmed on anonüümsed ja metaandmepõhised.

- **Telemeetria on integreeritud Prometheus/Grafana tööriistadega:**
  - Andmed on nähtavad ja päringuvalmid standardsetes vaadetes.
  - Iga CentOpsi komponenti saab eraldi jälgida (filtreerimine komponendi/klastri kaupa).

- **Telemeetria jälgib ainult CentOpsi komponente, mitte klientide äppe:**
  - Eraldi dokumentatsioon selgitab, mida jälgitakse ja mida mitte.
  - Süsteem suudab eristada CentOpsi sisemisi ja väliseid mõõdikuid.
