### Ülesanne: Integreeri Kubernetes-native monitooring ja alerting

**Kirjeldus:**  
Monitooring peab toimuma Kubernetese tasemel, kasutades native lahendusi (nt Prometheus, Grafana, Alertmanager). Lahendus peab suutma jälgida klastri, podide ja rakenduse tervist ning reageerida dünaamiliselt.

**Tegevused:**
- Seadista Prometheus ja Grafana deployment
- Defineeri alert reeglid (nt CPU, mälu, pod restartid)
- Kasuta `ServiceMonitor` või `PodMonitor` CRD-sid, kui kasutad Prometheus Operatorit
- Lisa dashboard'id (staging ja prod eraldi)
- Lisa alertid Slacki, e-maili või muu kanaliga

**Valmisoleku kriteeriumid:**
- [ ] Prometheus ja Grafana jooksevad klastris
- [ ] Dashboard’id olemas, näitavad olulisi metrikaid
- [ ] Vähemalt 3 alert reeglit on seadistatud
- [ ] Dokumentatsioon olemas (kasutus, häälestamine, laiendamine)
