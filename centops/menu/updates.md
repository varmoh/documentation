```mermaid
graph TD
    UpdatesMenu[Updates Menu]

    UpdateManifests["Update Manifests"]
    DeliveryStatus["Delivery Status"]
    DeliveryAPI["Delivery API Endpoints"]

    UpdatesMenu --> UpdateManifests
    UpdatesMenu --> DeliveryStatus
    UpdatesMenu --> DeliveryAPI

    UpdateManifests --> UMList["Manifest List"]
    UpdateManifests --> UMDetail["Manifest Detail View"]

    DeliveryStatus --> Progress["Delivery Progress - Kas peaks nägema kas klöient on võtnud vastu uuenduse"]

    DeliveryAPI --> APIDocs["API Documentation"]
    DeliveryAPI --> APITest["API Test Interface - kas kliendi endpoint vastab"]
