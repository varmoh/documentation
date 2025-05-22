### Ülesanne: Rakenda reaalaja logide ja jõudluse analüüs ilma tundliku info tsentraliseerimiseta

**Kirjeldus:**  
Süsteem peab võimaldama jälgida logisid ja jõudlust klientide keskkondades reaalajas, ilma andmete tsentraliseerimiseta. Lahendus võib kasutada log forwardingut, anonymizerit või lokaliseeritud dashboard’e.

**Tegevused:**
- Vali sobiv logihalduslahendus (nt Loki, FluentBit, ELK stack)
- Konfigureeri logide saatmine lokaalsesse analüüsikeskkonda
- Lisa metrikad (nt response time, error rate)
- Kindlusta, et logide sisu ei sisalda isikuandmeid või muud tundlikku infot
- Lisa lokaliseeritud visualiseerimisvõimekus (nt Grafana lokaalne datasource)

**Valmisoleku kriteeriumid:**
- [ ] Logid on kogutavad ja jälgitavad igas keskkonnas
- [ ] Logides ei ole tundlikku infot
- [ ] Tulemused kuvatavad lokaalselt või anonymiseeritult
- [ ] Dokumentatsioon ja konfiguratsioonijuhis on olemas

### Ülesanne: Tuvasta anomaaliaid ja tõrkeid automaatselt

**Kirjeldus:**  
Süsteem peab suutma automaatselt avastada jõudlusprobleeme, veateateid või ootamatut käitumist (anomaaliad). Võimalik kasutada ML-põhiseid lahendusi või reeglitel põhinevat lähenemist.

**Tegevused:**
- Kasuta näiteks Prometheus + Alertmanager või ML-mootorit (nt Grafana Mimir, Loki LogQL koos threshold'idega)
- Määra anomaaliad (nt latentsuse järsk tõus, restartide hüppeline kasv)
- Lisa visualiseering ja notifikatsioonid

**Valmisoleku kriteeriumid:**
- [ ] Vähemalt 2 anomaalia tüüpi on avastatavad ja dokumenteeritud
- [ ] Süsteem saadab automaatseid teavitusi
- [ ] Lahendus töötab lokaalselt või staging-keskkonnas

