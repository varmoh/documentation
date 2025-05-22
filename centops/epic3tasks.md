### Ülesanne: Koosta kliendi tehniline ülevaade

**Kirjeldus:**  
Igal kliendil peab olema nähtav tehniline seisund (nt versioonid, konfiguratsioonid, jõudlus). Selleks tuleb koguda andmed ja kuvada need sobival kujul.

**Tegevused:**
- Loo tehniliste andmete kogumise süsteem (nt Prometheus label’id, ConfigMap’id)
- Loo dashboard või CLI tööriist, mis kuvab versioonid, uptime jms
- Võimalusel eksport JSON või API kaudu

**Valmisoleku kriteeriumid:**
- [ ] Olemasolevate klientide andmed on kogutud
- [ ] Ülevaade on reaalajas ja ligipääsetav (CLI, GUI või API)

### Ülesanne: Arenda standardiseeritud liidesed klientide keskkondadega

**Kirjeldus:**  
Loo liidesed (nt REST API, k8s Service), mis võimaldavad klientide süsteemidega suhelda ühtsel moel. Võrkudevaheline suhtlus peab olema turvaline ja dokumenteeritud.

**Tegevused:**
- Määra suhtlusprotokollid (nt HTTPS, mTLS)
- Kirjelda API või service contract (OpenAPI vms)
- Lisa näiteks Ingress, ServiceEntry vms lahendus
- Kaalu side- või servicemesh'i kasutust (nt Istio)

**Valmisoleku kriteeriumid:**
- [ ] Liidesed töötavad vähemalt kahe kliendi peal
- [ ] API dokumentatsioon on olemas (OpenAPI või Markdown)
- [ ] Liikluse turvalisus (TLS, autentimine) on tagatud
