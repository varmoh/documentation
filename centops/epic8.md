**Kirjeldus:**  
Loo central CentOps haldusliides   
IDEE - Välja mõelda arhidektuur, et lisada pluginitena teisi mooduleid (DMR, commonknowledge, classifier)  
A-la placehlderid tulevikus, et ei peaks tegema mitut "tagatuba"

Kontekst:
CentOps peab võimaldama operaatoritel reaalajas nähtavust süsteemi oleku, telemeetria ja diagnostika kohta. Selleks kasutatakse peamiselt olemasolevaid tööriistu nagu Prometheus, Grafana, vältides uute GUI-de loomist, kui see pole hädavajalik.

Eesmärk:
Arendada või integreerida graafiline kasutajaliides, mis:

- eksponeerib CentOps komponentide ja pipeline'ide käitusoleku (RAM,CPU)

- austab klientide vahelist andmeeraldatust

- võimaldab piiratud juhtimistoiminguid (nt rollback) -- tõsta see ymber kliendi GUI alla

- on mitmekeskkonnateadlik ja turvaline
