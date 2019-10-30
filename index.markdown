---
layout: default
---

## O aplikácii

Sentinel Downloader je aplikácia postavená nad open-source knižnicou `sentinelhub-py` ktorá poskytuje rozhranie v jazyku Python
pre sťahovanie voľne prístupných dát zo satelitov z programov [Copernicus](https://scihub.copernicus.eu/) alebo [Landstat](https://landsat.gsfc.nasa.gov/).
Hlavná výhoda používania aplikácie je jednoduchá konfigurácia a minimálna nutná znalosť programovania v Pythone.


## Návod na použitie

### Inštalácia

Balík môžeme nainštalovať pomocou nástroju [pip](https://packaging.python.org/tutorials/installing-packages/) nasledovným príkazom:

```shell
$ pip3 install git+https://github.com/zaitra/sentinel-downloader
```

### Konfiguracny subor

## Ukazkovy konfiguracny subor

```yaml
debug: true # zobrazit ladiace vystupy
layer: "TRUE-COLOR-S2-L1C" # vrstvy zo satelitu ktore nas zaujimaju
times: # pole casovych obdobi
  -  ["2015-05-01", "2015-08-30"]
  -  ["2016-05-01", "2016-08-30"]
  -  ["2017-05-01", "2017-08-30"]
  -  ["2018-05-01", "2018-08-30"]
  -  ["2019-05-01", "2019-08-30"]

# Oblast na mape ktora nas zauijma. Suradnice su v poradi lavy horny roh (x,y) a pravy dolny roh (x,y)
bounding_box: [14.42, 50.42, 14.42, 50.42]

width: 42 # sirka obrazku v pixeloch
height: 42 # vyska obrazku v pixeloch

max_cloud_percentage: 0.42 # maximalna oblacnost v percentach

images_dir: "/tmp/images/" # priecinok kde maju byt obrazky stiahnute
```

### Pouzitie

```
sentinel-downloader download -c <CESTA_KU_KONFIGURACNEMU_SUBORU>
```

### Bez inštalácie (v docker kontajnery)

Sentinel downloader je mozne pouzit bez instalacie pomocou nastroju [docker](https://docs.docker.com/). Potom staci jediny prikaz:

```shell
docker run -it --rm -v <CESTA_K_PRIECINKU>:/tmp/images \
                    -v <CESTA_KU_KONFIGURACNEMU_SUBORU>:/.sd.yaml \
                    zaitra/sentinel-downloader \
                    bash -c "sentinel-downloader download -c /.sd.yaml"
```

Kde musite nahradit nasledovne premenne:
- `<CESTA_K_PRIECINKU>` - nahradte cestou k priecinku kde chcete dáta stiahnut
- `<CESTA_KU_KONFIGURACNEMU_SUBORU>` - nahradte cestou ku konfiguracnemu suboru ktory sme vytvorili v predoslich krokoch.
``
