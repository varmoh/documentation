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

Erandina võib Notifications Node suhelda otse OpenSearchiga, näiteks reaalajas andmete vahendamiseks või otsingupäringute teenindamiseks.

Frontend **ei tee kunagi päringuid** otse ühegi komponendi suunas, vältides Ruuterit.

```mermaid

flowchart LR
    FE[Frontend] --> R[Ruuter<br/>DSL orkestreerija]

    R <--> DM[DataMapper]
    R <--> N[Notifications Node]
    R <--> OS[OpenSearch]
    R <--> CM[CronManager]
    R <--> S3[s3ferry]

    R <--> RESQL[ResQL]
    RESQL <--> PG[(PostgreSQL)]

    R <--> TIM[TIM]
    TIM <--> PG2[(TIM PostgreSQL)]

    %% ERAND: Notifications -> OpenSearch
    N --> OS



    classDef core fill:#f5f5f5,stroke:#333,stroke-width:2px;
    classDef db fill:#eef,stroke:#333,stroke-width:2px;
    classDef service fill:#fff,stroke:#666;

    class R core;
    class PG,PG2 db;
```
