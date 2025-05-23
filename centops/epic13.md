Manifests generating and Delivery System to central centops

**Kirjeldus:**  
Tarkvarauuenduste ja tarneprotsesside haldamine, kasutades GitHub Actions töövooge. 
Süsteem peab võimaldama uuenduste manifestide genereerimist (üle rääkima et saan ikka aru et manifest tehakse workflow käigus githubs?), 
valideerimist, talletamist ja kättesaadavaks tegemist klientide agentidele.

```mermaid
flowchart TD
    A["Koodihoidla (GitHub)"] --> B[CI/CD töövoog käivitub]
    B --> C[Andmete kogumine: komponendid, versioonid, konfiguratsioonid]
    C --> D["Manifesti koostamine (JSON/YAML)"]
    D --> E["Manifesti valideerimine (skeem, keelatud väljad)"]
    E -->|Õnnestus| F[CENTRAL CENTOPS Manifest salvestatakse registrisse]
    E -->|Ebaõnnestus| G[Vigade logimine ja teavitamine]
    F --> H[CENTRAL CENTOPS API kaudu kättesaadav kliendiagentidele]
    H --> I[CENTRAL&CLIENT CENTOPS Kliendiagent küsib või saab teate uuendustest]
    I --> J[CLIENT CENTOPS Manifesti rakendamine kliendikeskkonnas]

    style A fill:#a2d2ff,stroke:#333,stroke-width:2px
    style B fill:#90be6d,stroke:#333,stroke-width:2px
    style C fill:#f9c74f,stroke:#333,stroke-width:2px
    style D fill:#f9844a,stroke:#333,stroke-width:2px
    style E fill:#f94144,stroke:#333,stroke-width:2px
    style F fill:#43aa8b,stroke:#333,stroke-width:2px
    style G fill:#f3722c,stroke:#333,stroke-width:2px
    style H fill:#577590,stroke:#333,stroke-width:2px
    style I fill:#277da1,stroke:#333,stroke-width:2px
    style J fill:#4caf50,stroke:#333,stroke-width:2px


