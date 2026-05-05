### Byckstack arhidektuur

**Backend arhitektuur**

Bürokrati rakenduskiht on ehitatud keskse vahendaja (central mediator) põhimõttel.  
Frontend ei suhtle otse alamkomponentide ega andmebaasidega, vaid teeb kõik päringud `Ruuteri` kaudu.  


`Ruuter` on süsteemi keskne orkestreerija, mis juhib DSL-põhiseid töövooge ning vahendab liiklust teiste stacki komponentidega.


Andmebaasidele ligipääs on rangelt piiratud. PostgreSQL-andmebaasidega suhtlevad ainult selleks ettenähtud komponendid:

- `ResQL`, mis vastutab SQL-päringute käivitamise eest
- `TIM`, mis haldab TARA-põhist autentimist ning sellega seotud küpsiseid ja tokeneid

Stackis on **eraldatud andmebaasid** ning TIM suhtleb ainult oma andmebaasiga.

Ülejäänud komponendid — DataMapper, Notifications Node, OpenSearch, CronManager ja s3ferry — suhtlevad ainult Ruuteriga ning neil puudub otsene ligipääs:

- teistele komponentidele
- andmebaasidele
- frontendile

Frontend **ei tee kunagi päringuid** otse ühegi komponendi suunas, vältides Ruuterit.

```mermaid

flowchart LR
    FE[Frontend] --> R[Ruuter<br/>DSL orkestreerija<br/>keskne vahendaja]

    R <--> DM[DataMapper<br/>Handlebars / JSON teisendused]
    R <--> N[Notifications Node<br/>SSE ühendused frontendiga]
    R <--> OS[OpenSearch<br/>tekstipõhine otsinguandmebaas]
    R <--> CM[CronManager<br/>cronjob'ide käivitaja]
    R <--> S3[s3ferry<br/>S3 kopeerimise handler]

    R <--> RESQL[ResQL<br/>SQL päringute REST-kiht]
    RESQL <--> PG[(PostgreSQL<br/>relatsiooniline andmebaas)]

    R <--> TIM[TIM<br/>TARA Integration Module<br/>auth, cookies, JWT]
    TIM <--> PG

    %% Keelatud otsesuhtlus andmebaasiga
    R -. ei suhtle otse .-> PG

    classDef core fill:#f5f5f5,stroke:#333,stroke-width:2px;
    classDef db fill:#eef,stroke:#333,stroke-width:2px;
    classDef service fill:#fff,stroke:#666;

    class R core;
    class PG db;
    class FE,DM,N,OS,CM,S3,RESQL,TIM service;
```
