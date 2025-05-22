## Epic: Automatiseeritud arendus- ja tarneprotsessid (NoOps)

**Kirjeldus**  
Selle Epicu eesmärk on luua täielikult automatiseeritud arendus-, testimis- ja tarnetsükkel, mis vastab NoOps põhimõtetele. Kõik protsessid peavad toimuma GitHubis GitHub Actions töövoogude abil ning tagama konteineriseeritud ja skaleeritava lahenduse Kuberneteses.

### Subtaskid

- [ ] Loo GitHub Actions töövood CI/CD protsessiks
- [ ] Seadista automatiseeritud testide käivitamine PR-ide puhul
- [ ] Loo Dockeri arendus- ja produktsioonipildid
- [ ] Kujunda Kubernetese-põhine tarneprotsess (Helm/Kustomize)
- [ ] Integreeri GitHub Actions ja Kubernetes
- [ ] Kirjelda ja dokumenteeri kogu CI/CD protsess
- [ ] Testi kogu töövoogu lokaalselt ja staging-keskkonnas

**Seotud dokumendid:**
- [NoOps ADR](https://github.com/buerokratt/Buerokratt-onboarding/tree/main/Architectural-Decision-Records-ADR/CentOps)
