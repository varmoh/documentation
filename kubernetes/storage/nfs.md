# Arhitektuur: Namespace-põhised NFS-serverid

## Eesmärk

Luua Kubernetes’i klastrisse lahendus, kus iga namespace saab oma **RWX (ReadWriteMany)** võimekuse, kasutades:

- **Longhorn RWO (ReadWriteOnce)** block volume
- **Namespace’i siseselt** jooksvat NFS serverit
- **Namespace’i sees** jagatavat NFS mounti, mida rakendused kasutavad läbi oma **PersistentVolumeClaim-i**

## Komponendid ja töövoog

### 1. Longhorn Storage (RWO)

- Longhorn provisioner loob igale namespace’ile **PersistentVolumeClaim-i** (RWO režiimis).
- Iga PVC on seotud konkreetse **NFS-serveri podiga**.
- See RWO PVC mountitakse ainult **NFS serveri podi sisse**.

### 2. NFS Server (per namespace)

- Igas namespace’is jookseb **üks NFS serveri pod**, mis mountib Longhorni PVC.
- See NFS server jagab mountitud kataloogi üle **NFS protokolli** namespace’i sees.

### 3. Service

- NFS server on eksponeeritud **ClusterIP Service’iga** (või headless teenusena).
- Teenust kasutatakse RWX mountimiseks namespace’i sees olevatesse **rakendustesse**.

### 4. NFS PersistentVolume (PV)

- Loome namespace’i sees **PersistentVolume kirjelduse**, mis viitab NFS serveri teenusele ja jagatud kataloogile.
- PV kasutab `ReadWriteMany` access mode’i.
- See PV ühendab namespace’i sees oleva NFS teenuse rakendustega.

### 5. Kasutavad rakendused

- Rakenduste **PersistentVolumeClaim-id** viitavad sellele NFS PV-le.
- Rakenduste podid mountivad oma PVC-de kaudu selle RWX mahu.

## Töövoog (näiteks namespace `foo`)

1. `foo` namespace loob **PersistentVolumeClaim-i** `foo-nfs-backend-pvc` (RWO), mida mountib `foo-nfs-server`.
2. NFS serveri **Deployment** `foo-nfs-server` mountib `foo-nfs-backend-pvc` ja jagab selle `/nfsshare`.
3. **Service** `foo-nfs-service` eksponeerib NFS serveri ClusterIP või headless teenusena.
4. Loome **PersistentVolume** `foo-nfs-pv`, mis viitab `foo-nfs-service` kaudu jagatud `/nfsshare` kataloogile.
5. Rakenduste **PersistentVolumeClaim-id** viitavad `foo-nfs-pv` peale.
6. Rakenduste podid mountivad PVC kaudu selle RWX mahu.

## Visuaalne arhitektuuri skeem

**Namespace: foo**

```plaintext
+-------------------------------+
|  +------------------------+   |
|  | Longhorn PVC (RWO)      |   |
|  +------------+------------+   |
|               |                |
|        +------v-------+        |
|        |  NFS Server   |        |
|        +------+--------+        |
|               |                 |
|        +------+--------+        |
|        |               |        |
|   +----v----+     +----v----+   |
|   |   PV    |     |   PV    |   |
|   +----+----+     +----+----+   |
|        |               |        |
|   +----v----+     +----v----+   |
|   |   PVC   |     |   PVC   |   |
|   +----+----+     +----+----+   |
|        |               |        |
|    +---v---+       +---v---+    |
|    |  Pod  |       |  Pod  |    |
|    +-------+       +-------+    |
+---------------------------------+
```

#### Eelised

- Namespace’i-põhine isoleeritus.

- Ei teki klastriüleseid RWX konflikte.

- Kasutab olemasolevat Longhorni storage lahendust.

- Skaalub namespace’i-põhiselt — lisades uusi namespaces, lisad juurde lokaalse NFS serveri.

- Rakendused saavad RWX mahu läbi standardse PVC/PV süsteemi — ei pea ise NFS mounti haldama.

#### Miinused

- Igas namespace’is eraldi NFS serveri pod (täiendav ressurss ja haldus).

- Pole päris distributed file system, pigem namespace’i-sisene lokaalne lahendus.

- Vajab manuaalset PersistentVolume kirjeldamist (või automatiseerimist Helm chartiga).

    Võrreldes CephFS või Portworxiga ei ole ideaalne väga suurtel klastritel või väga intensiivsete RWX workloadide jaoks.
