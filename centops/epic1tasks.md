### Ülesanne: Loo GitHub Actions töövood CI/CD protsessiks

**Kirjeldus:**  
Loo automatiseeritud töövood GitHub Actionsi abil, mis toetavad pidevat integreerimist (CI) ja tarnet (CD). Töövood peavad hõlmama testimist, buildimist ja deploy'd Kubernetese klastri staging-keskkonda.

**Tegevused:**
- Dev to test ehitab image (PR) -       KEHTIB AINULT BÜROKRATI   komponentide ja moodulite repode suhtes  
  - CI töövoog peab:
    - Checkout’ima koodi
    - Käivitama testid (nt `pytest`, `jest`, `go test`?)
    - Ehita Docker image
- CD töövoog peab:
  - notifikation central centopsi
  - Teavitama ebaõnnestumisest (kui image build feilib aga see ei peaks olema centopsi jaoks oluline)
- Hoia töövood DRY – vajadusel kasuta eraldi `reusable workflows`.

**Valmisoleku kriteeriumid:**
- [ ] CI ja CD töövood on loodud ja testitud
- [ ] Workflow’d on versioneeritud ja commit’is
- [ ] Dokumentatsioon töövoogude käivitamiseks ja muutmiseks on olemas

### Ülesanne: Loo Dockeri arendus- ja produktsioonipildid

**Kirjeldus:**  
Koosta Dockerfile’id, mis võimaldavad arendajatel lokaalset arendust (dev-pilt) ning produktsiooniklastrisse tarnet (prod-pilt). Pildid peavad olema efektiivsed, väikesed ja versioonitavad.

**Tegevused:**
- Analüüsida hetke seisu repodes
- Loo `Dockerfile.dev`:
  - Sisaldab debug tööriistu ja hot-reload võimalust
  - Sobib lokaalseks arendamiseks
- Loo `Dockerfile`:
  - Optimeeritud pilt produktsiooniks (multi-stage build)
  - Vähendatud image-suurus ja turvalisusnõuded täidetud
- Seadista `docker-compose.yml` või Helm chart, kui vajalik
- Lisa `.dockerignore` fail ja versioonihaldus

**Valmisoleku kriteeriumid:**
- [ ] Dockerfile’id töötavad lokaalselt ja CI/CD keskkonnas
- [ ] Image’d on versioneeritud (nt semver või commit hash)
- [ ] Dokumentatsioon sisaldab: build käske, keskkonnamuutujate kasutust ja töövoogu
- [ ] 
### Ülesanne: Kujunda Kubernetese-põhine tarneprotsess (Helm/Kustomize)

**Kirjeldus:**  
Välja tuleb töötada standardiseeritud ja taaskasutatav Kubernetese deployment-lahendus, mis võimaldab automaatset rakenduste juurutamist staging- ja produktsioonikeskkondadesse. Lahendus peab toetama mitmekeskkonnalist seadistust ja olema sobiv CI/CD integreerimiseks.

**Tegevused:**
- Vali sobiv tööriist: Helm või Kustomize (või mõlemad koos)
- Loo järgmised komponendid:
  - Deployment, Service, ConfigMap, Secret, Ingress jne
  - Eraldi konfiguratsioonid staging ja prod jaoks
- Lisa Helm chart või `kustomization.yaml` vajalikesse kataloogidesse
- Tagada muutujapõhine deploy (nt `values.yaml` või `env overlays`)
- Seadista töövoog, mis kasutab loodud deployment-malle automaatselt (GitHub Actions kaudu)

**Valmisoleku kriteeriumid:**
- [ ] Staging deploy töötab lokaalselt või CI/CD kaudu
- [ ] Deployment-failid versioneeritud ja keskkonnast sõltumatud
- [ ] Lahendust saab kasutada vähemalt kahe eri keskkonna juurutamiseks
- [ ] Dokumentatsioon sisaldab juurutusjuhiseid ja konfiguratsiooni struktuuri

### Ülesanne: Integreeri GitHub Actions ja central centops

**Kirjeldus:**  
Tuleb seadistada mehhanism, mis võimaldab GitHub Actions töövoogudel automaatselt teavitada central centopsi.

**Tegevused:**
- Uurida weebhooki tööd

**Valmisoleku kriteeriumid:**
- [ ] GitHub Actions töövoog suudab edukalt suhelda central centopsiga

### Ülesanne: Seadista automatiseeritud testide käivitamine PR-ide puhul centops repos

**Kirjeldus:**  
Kõik Pull Requestid peavad läbima automaatsed testid enne mergimist. Töövoog peab olema konfigureeritud nii, et testid jooksevad igal PR-il ja tulemused on nähtavad GitHub UI-s (pass/fail).

**Tegevused:**
- Loo või uuenda `.github/workflows/ci.yml`, et testid jookseksid:
  - Igal `pull_request` sündmusel
  - Vastavalt projekti stackile (nt Python → `pytest`, Node.js → `jest`, Go → `go test`)
- Lisa vajalikud `test` käsud `package.json`, `Makefile` või `scripts` plokki
- Konfigureeri töövoog nii, et:
  - Failimuutused käivitavad vastavad testid (nt ainult backend/frontend)
  - Test coverage arvutamine, kui asjakohane
- Lisa testide ebaõnnestumise korral töövoogu stop/error mehhanism
- Uuri kas meil on mingid end-to-end testid juba olemas või mõtle kas on midagi mid saab kuskilt kasutada

**Valmisoleku kriteeriumid:**
- [ ] Testid käivituvad automaatselt igal PR-il
- [ ] Mergimine pole lubatud enne, kui testid on läbitud
- [ ] Testitulemused on nähtavad GitHub UI-s (checks tab)
- [ ] Dokumentatsioon sisaldab testide käivitamise juhiseid lokaalselt ja CI-s

### Ülesanne: Kirjelda ja dokumenteeri kogu CI/CD protsess

**Kirjeldus:**  
Dokumentatsioon peab kirjeldama kogu arendus- ja tarneprotsessi alates koodikirjutamisest kuni deploy’ni. See aitab uutel arendajatel süsteemist kiiresti aru saada ning võimaldab lihtsat hooldust ja tõrkeanalüüsi.

**Tegevused:**
- Lisa projekti juurkausta dokumentatsioonifail (nt `docs/ci-cd.md` või `README.md` alla uus lõik)
- Kirjelda järgmised komponendid:
  - CI töövoog: testid, build, lint
  - CD töövoog: docker image, deployment, staging/prod eristamine
  - GitHub Actionsi failide struktuur ja rollid
  - Secrets ja keskkonnamuutujate haldus
- Lisa skeem või joonis (soovi korral, nt mermaid või link välisele tööriistale)
- Lisa hädaolukorra juhised (kuidas katkestada, kuidas käsitsi deploy’da)

**Valmisoleku kriteeriumid:**
- [ ] Dokumentatsioon on olemas ja versioneeritud
- [ ] Protsess on selgelt loetav ka uuele tiimiliikmele
- [ ] Link dokumentatsioonile on lisatud töövoo kommentaaridesse ja README-sse

