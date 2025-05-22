### Ülesanne: Toeta dünaamilist N arvu klienti/mitme kliend haldus

**Kirjeldus:**  
Lahendus peab toetama suvalist arvu kliente, keda saab dünaamiliselt lisada ja eemaldada, ilma teenuse katkestuseta. Igal kliendil peab olema eraldatud keskkond või loogiline eristamine (nt namespace’id, tenant-id’d).

**Tegevused:**
- Rakenda namespace-põhine isoleerimine või tenant-id lahendus
- Lisa kliendi haldusliides või CLI tööriist (nt `add-client.sh`)
- Testi skaleeruvust vähemalt 3-5 kliendiga

**Valmisoleku kriteeriumid:**
- [ ] Uue kliendi lisamine toimub skriptiga või API kaudu
- [ ] Kliendi isoleeritus (logid, ressursid) on tagatud
- [ ] Dokumentatsioon kirjeldab kliendi lisamise protsessi
