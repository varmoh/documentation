#### piiratud kontrollvõimalused, rollback näiteks
**Kirjeldus:**  
Kliendi GUI peab integreeruma olemasoleva Bürokratt kasutajaliidesega.

**Kirjeldus:**  
Vaikimisi peaks olema GUI read-only, kuid peaks võimaldama rollbacki

**Tegevused:**  
- Määratle juhtumidkus rollback on vajalik 
- Rakenda kontrollmehhanismid koos autentimisega  
- Logi kõik muudatused auditlogides - Kas peaks tegema, et logid jõuaksid central centopsi ?

**Valmisoleku kriteeriumid:**  
- [ ] tegevused on piiratud ja turvatud  
- [ ] Rollipõhine juurdepääs toimib  - Peaks ära kasutama meie praegust lahendust, lisama näieks eraldi rolli ?
- [ ] Logimine

### Tagada turvaline, autentitud ligipääs (RBAC, scoping)

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
