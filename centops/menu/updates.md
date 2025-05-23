```mermaid
graph TD
    UpdatesMenu[Updates Menu]

    UpdateManifests["Update Manifests"]
    DeliveryStatus["Delivery Status"]
    API["Manifest update publishing - Hetkel infoks, aga peaks olema taustal ja menüüs ei pea olema"]

    UpdatesMenu --> UpdateManifests
    UpdatesMenu --> DeliveryStatus
    UpdatesMenu --> API

    UpdateManifests --> UMList["Manifest List"]
    UpdateManifests --> UMDetail["Manifest Detail View"]

    DeliveryStatus --> Progress["Delivery Progress - Kas peaks nägema kas klöient on võtnud vastu uuenduse"]

    API --> APIDocs["API Documentation"]
    API --> APITest["API Test Interface - kas kliendi endpoint vastab"]
