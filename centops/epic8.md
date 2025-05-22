**Kirjeldus:**  
Loo central CentOps haldusliides 

Kontekst:
CentOps peab võimaldama operaatoritel reaalajas nähtavust süsteemi oleku, telemeetria ja diagnostika kohta. Selleks kasutatakse peamiselt olemasolevaid tööriistu nagu Prometheus, Grafana, Kubernetes Dashboard, vältides uute GUI-de loomist, kui see pole hädavajalik.

Eesmärk:
Arendada või integreerida graafiline kasutajaliides, mis:

- eksponeerib CentOps komponentide ja pipeline'ide käitusoleku

- austab klientide vahelist andmeeraldatust

- võimaldab piiratud juhtimistoiminguid (nt rollback)

- on mitmekeskkonnateadlik ja turvaline
