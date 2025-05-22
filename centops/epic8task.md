**Kirjeldus:**  
Kaardista, millist infot operaatorid vajavad: komponentide staatus, deploymenti olek, pipeline'i diagnostika, telemeetria jne.

**Tegevused:**  
- Koosta kasutusstsenaariumid
- Kirjelda vajalikud andmeallikad
- Prioriseeri vaadete olulisus ja kriitilisus

**Valmisoleku kriteeriumid:**  
- [ ] Ülevaade nõutavatest andmevaadetest  
- [ ] Dokumenteeritud vajadused ja andmeallikad


**Kirjeldus:**  
Vältimaks üleliigset arendust, kasutatakse olemasolevaid tööriistu visualiseerimiseks.

**Tegevused:**  
- Seadista Prometheus andmete kogumiseks  
- Loo Grafana dashboard’id vajalikest vaadetest  
- Vajadusel seadista K8s dashboard juurdepääs

**Valmisoleku kriteeriumid:**  
- [ ] Dashboardid olemas ja töökorras  
- [ ] Turvaline juurdepääs tagatud  
- [ ] Dokumentatsioon koostatud


**Kirjeldus:**  
GUI peab toetama mitut klienti/keskkonda ning hoida andmed rangelt eraldatuna.

**Tegevused:**  
- Rakenda keskkonnaspetsiifiline filtreerimine  
- Testi eraldatuse mehhanisme (nt namespace, RBAC)  
- Kontrolli, et GUI ei kuvaks toorlogisid ega tundlikku sisu

**Valmisoleku kriteeriumid:**  
- [ ] Andmed on klientide vahel eraldatud  
- [ ] GUI toetab mitut keskkonda  
- [ ] Kontrollitud andmelekke puudumine

**Kirjeldus:**  
Vaikimisi on GUI read-only, kuid valitud juhtudel peab võimaldama kontrolli (nt rollback).

**Tegevused:**  
- Määratle juhtumid, kus kontroll on lubatud  
- Rakenda kontrollmehhanismid koos autentimisega  
- Logi kõik muudatused auditlogides

**Valmisoleku kriteeriumid:**  
- [ ] Kontrolltoimingud on piiratud ja turvatud  
- [ ] Rollipõhine juurdepääs toimib  
- [ ] Auditlogimine töötab korrektselt

**Kirjeldus:**  
Kasutajate jaoks tuleb koondada kõik GUI sissepääsupunktid koos info, eesmärkide ja juurdepääsunõuetega.

**Tegevused:**  
- Koosta index-leht GUI-de URLide, kirjelduste ja autentimisnõuetega  
- Avalda see turvalises keskkonnas (nt wiki või CentOps portaalis)  
- Testi ligipääsu kõikidesse paneelidesse

**Valmisoleku kriteeriumid:**  
- [ ] Ühtne dokument/portaal ligipääsude kohta olemas  
- [ ] Kõik lingid töötavad ja on dokumenteeritud  
- [ ] Autentimisinfo on kaasas

**Kirjeldus:**  
Kõik GUI-d peavad olema kättesaadavad ainult autentitud, õigustega kasutajatele, kelle ligipääs on piiratud nende keskkonnaga.

**Tegevused:**  
- Rakenda turvaline sisselogimine (SSO, OAuth vms)  
- Lisa rollipõhine juurdepääs  
- Testi eri stsenaariume ligipääsu skopeerimiseks

**Valmisoleku kriteeriumid:**  
- [ ] Autentimine töötab ja on turvaline  
- [ ] RBAC piirab ligipääsu korrektselt  
- [ ] Dokumentatsioon on olemas

**Kirjeldus:**  
Kuna GUI tugineb ka kolmandate osapoolte tööriistadele, peab tagama nende sünkroonsuse CentOps komponentide muudatustega.

**Tegevused:**  
- Kirjelda ja testida GUI-sünkroonsuse töövooge  
- Loo automatiseeritud testid muutuste tuvastamiseks  
- Dokumenteeri hooldusjuhised

**Valmisoleku kriteeriumid:**  
- [ ] Sünkroniseerimine toimib ja on jälgitav  
- [ ] Dokumenteeritud hooldusjuhend  
- [ ] Automatiseeritud kontroll olemas

