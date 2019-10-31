---
layout: default
---

## O aplikácii

Sentinel Downloader je aplikace postavená nad open-source knihovnou [sentinelhub-py](https://github.com/sentinel-hub/sentinelhub-py). 
Aplikace je v jazyku Python a poskytuje rozhraní pro stahování volně přístupných dat ze satelitů v programu [Copernicus](https://scihub.copernicus.eu/) a [Landstat](https://landsat.gsfc.nasa.gov/). 
Velkou výhodou aplikace je jednoduchá konfigurace a minimální nutná znalost programování v Pythonu.

### Proč jsme vyvinuli Sentinel Downloader?

Potřebovali jsme jako tým během hackathonu pracovat s daty, které bylo možné buď stahovat ručně, nebo pomocí [poměrně zdlouhavého kódu]((https://sentinelhub-py.readthedocs.io/en/latest/examples/ogc_request.html)). 
Při stahování samotném je totiž nutné nadefinovat vícero parametrů, které požadujete od výsledku. Sentinel Downloader dokáže stáhnout požadovaná data jedním příkazem v terminálu, a to ihned po napsaní přehledného konfiguračního souboru.


### Pro koho je aplikace určená

Aplikace je pro všechny, kteří chtějí stahovat vetší množství dat specifických pro určitou oblast na mapě. Pomocí aplikace je možné stahovat data z programů [Copernicus](https://scihub.copernicus.eu/) a [Landstat](https://landsat.gsfc.nasa.gov/).


#### Příklad použití:

Představme si, že chceme zanalyzovat oblast Nízkých Tater. 
Chceme stáhnout data z vícero vrstev, které nás zajímají - např. NDVI a True color. Také chceme tyto data strukturovat podle časového období. 
Se Sentinel Downloaderem je to možné udělat ve třech jednoduchých krocích:

1. Uložíme si přístupový token ze [sentinel-hub.com](https://sentinel-hub.com/) do proměnné prostředí. Tento krok je nutný, aby se Sentinel Downloader mohl autentizovat na API Sentinel Hubu.
```shell
$ export "export SD_SENTINEL_INSTANCE_ID=<INSTANCE_ID>"
```
- `<INSTANCE_ID>` - Je potřebné nahradit tokenem, který najdeme v Configuration sekci po přihlášení na Sentinel Hub.

2. Vytvoříme konfigurační soubor:

```yaml
layers: # Vrstvy ze satelitu, které nás zajímají
  - "TRUE-COLOR-S2-L1C" 
  - "NDVI-S2-L1C" 
times: # Pole časových období
  -  ["2015-05-01", "2015-08-30"]
  -  ["2016-05-01", "2016-08-30"]
  -  ["2017-05-01", "2017-08-30"]
  -  ["2018-05-01", "2018-08-30"]
  -  ["2019-05-01", "2019-08-30"]

# Oblast na mapě, která nás zajímá. Souřadnice jsou v pořadí levý horní roh (x,y) a pravý dolní roh (x,y)
bounding_box: [19.46547813713551, 48.96805013122616, 19.57534141838551, 49.00685748937818]

width: 1223 # Šířka obrázku v pixelech
height: 658 # Výška obrázku v pixelech

max_cloud_percentage: 0.42 # Maximální oblačnost v procentech

images_dir: "/tmp/images/" # Složka, kam mají být data stažena
```

3. Spustíme Sentinel Downloader:
```
sentinel-downloader download -c <CESTA_KE_KONFIGURACNIMU_SOUBORU>
```

Data je následně možné najít ve složce, kterou jsme specifikovali výše.

## Dokumentace

Kompletní technická dokumentace je k nalezené v [Github repozitáři](https://github.com/zaitra/sentinel-downloader).

