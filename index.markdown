---
layout: default
---

## O aplikácii

Sentinel Downloader je aplikácia postavená nad open-source knižnicou `sentinelhub-py` ktorá poskytuje rozhranie v jazyku Python
pre sťahovanie voľne prístupných dát zo satelitov z programov [Copernicus](https://scihub.copernicus.eu/) alebo [Landstat](https://landsat.gsfc.nasa.gov/).
Hlavná výhoda používania aplikácie je jednoduchá konfigurácia a minimálna nutná znalosť programovania v Pythone.

### Prečo sme vyvinuli Sentinel Downloader

Ako tím sme potrebovali pracovat s dátami ktoré treba buď to ručne sťahovať alebo napísať pomerne [zdlhavý
kód](https://sentinelhub-py.readthedocs.io/en/latest/examples/ogc_request.html) na ich získanie. Pri sťahovaní je totiž nutné
definovať rôzne parametre ktoré požadujete od výsledku. Sentinel Downloader dokáže stiahnuť požadované dáta
jedným príkazom v termináli ihned po napisani prehľadného konfiguračného súboru.

### Pre koho je aplikácia určená

Aplikácia je určená všetkým ktorý chcú stahovať vačšie množstvo dát špecifických pre určitú oblasť na mape.
Pomocou aplikaćie je možné stahovat dáta z programov [Copernicus](https://scihub.copernicus.eu/) alebo [Landstat](https://landsat.gsfc.nasa.gov/)

#### Prípad užiti

Predstavme si že chceme zanalyzovať oblasť nízkych tatier. Chceme stiahnuť dáta z viacerých vrstiev ktoré nás zaujímajú (napriklád NDVI a True color).
Taktiez chceme tieto data strukturovat podla casoveho obdobia. So sentinel downloader-om vieme toto spravit v troch jednoduchych krokoch:

1. Ulozime si pristupovy token zo sentinel-hub.com do premennej prostredia. Tento krok je nutny aby sa
Sentinel downloader vedel autentizovat na API sentinel hub-u.
```shell
$ export "export SD_SENTINEL_INSTANCE_ID=<INSTANCE_ID>"
```
- `<INSTANCE_ID>` - je potrebne nahradit tokenom ktory najdete v Configurtion sekcii po prihlaseni na [sentinel-hub.com](https://sentinel-hub.com/).

2. vytvorime konfiguracny subor:

```yaml
layers: # vrstvy zo satelitu ktore nas zaujimaju
  - "TRUE-COLOR-S2-L1C" 
  - "NDVI-S2-L1C" 
times: # pole casovych obdobi
  -  ["2015-05-01", "2015-08-30"]
  -  ["2016-05-01", "2016-08-30"]
  -  ["2017-05-01", "2017-08-30"]
  -  ["2018-05-01", "2018-08-30"]
  -  ["2019-05-01", "2019-08-30"]

# Oblast na mape ktora nas zauijma. Suradnice su v poradi lavy horny roh (x,y) a pravy dolny roh (x,y)
bounding_box: [19.46547813713551, 48.96805013122616, 19.57534141838551, 49.00685748937818]

width: 1223 # sirka obrazku v pixeloch
height: 658 # vyska obrazku v pixeloch

max_cloud_percentage: 0.42 # maximalna oblacnost v percentach

images_dir: "/tmp/images/" # priecinok kde maju byt obrazky stiahnute
```

3. spustime Sentinel Downloader:
```
sentinel-downloader download -c <CESTA_KU_KONFIGURACNEMU_SUBORU>
```

Obrazky je nasledne mozne najst v priecinku ktory sme zadali v konfiguracii pod klucom `image_dir`.

## Dokumentacia

Kompletnú technickú dokumentáciu je možné nájsť v [Github repozitari](https://github.com/zaitra/sentinel-downloader)
