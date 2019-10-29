# Sentinel Downloader [![Build Status](https://travis-ci.com/zaitra/sentinel-downloader.svg?branch=master)](https://travis-ci.com/zaitra/sentinel-downloader)
Library and CLI tool for downloading satellite images from the [sentinel-hub.com](https://sentinel-hub.com/)

# Providing access to Sentinel Hub

Sentinel Downloader is automation tool for downloading imagery from [sentinel-hub.com](https://sentinel-hub.com/).
You need to have account in order to access the data and provide access token (instance ID) to start using this tool.
Instance ID can be found in your dashboard in Configuration Utility section. Add your instance ID to your environment.
```bash
$ echo "export SD_SENTINEL_INSTANCE_ID=<INSTANCE_ID>" >> .env
$ source .env
```

## Usage without installation

If you want to use this tool you can easily do it with [published docker image](https://hub.docker.com/r/zaitra/sentinel-downloader):

```bash
$ docker pull zaitra/sentinel-downloader
$ docker run -it --rm -v <PATH_TO_IMAGES>:/tmp/images -v <PATH_TO_CONFIG_FILE>:/.sd.yaml zaitra/sentinel-downloader bash -c "sentinel-downloader download -c /.sd.yaml"
```
* `<PATH_TO_IMAGES>` - directory where the images will be stored (absolute path on host)
* `<PATH_TO_CONFIG_FILE>` - absolute path on host to configuration file `.sd.yaml`

# Configuration

**Configuration file `.sd.yaml` contains sensitive data so it is recommended to keep it in private repository**.

## Example

```yaml
debug: true
layer: "TRUE-COLOR-S2-L1C"
times:
  -  ["2015-05-01", "2015-08-30"]
  -  ["2016-05-01", "2016-08-30"]
  -  ["2017-05-01", "2017-08-30"]
  -  ["2018-05-01", "2018-08-30"]
  -  ["2019-05-01", "2019-08-30"]

# area of interest. Coordinates representing top left x,y and right bottom x,y
bounding_box: [14.42, 50.42, 14.42, 50.42]

width: 42
height: 42

max_cloud_percentage: 0.42

images_dir: "/tmp/images/"
```

Here are the configuration options:

| Option                       | Description       | Required      |
|------------------------------|-------------------|---------------|
| `debug`            | Provide debug logs. Default is False | No |
| `instance_id`           | Instance ID from sentinel-hub account | Yes |
| `layer`               | Layer from sentinel-hub configuration | Yes |
| `bounding_box`            | Bounding box location | Yes |
| `times` | Array of time ranges | Yes |
| `width`              | Image width | Yes |
| `height`       | Image height | Yes |
| `max_cloud_percentage`           | Max cloud coverage. Default is 1 | No |
| `image_dir`                  | Path to directory where images should be saved. | Yes |

# Docker

## Installation

```bash
$ git clone https://github.com/zaitra/sentinel-downloader
$ cd sentinel-downloader
$ touch .sd.yaml  # configurarution file has to be in the root directory of this project
$ vim .sd.yaml  # edit as described in Configuration section
$ make build  # builds docker image
```

## Usage

```bash
$ docker run -it --rm -v <PATH_TO_IMAGES>:/tmp/images sd-image bash -c "sentinel-downloader download -c /src/.sd.yaml"
```

# CLI

## Installation

```bash
$ pip3 install git+https://github.com/zaitra/sentinel-downloader
```

## Usage

```bash
sentinel-downloader download -c <PATH_TO_CONFIG_FILE>
```

## Logging
The default logging level is `INFO`. If you want to enable `DEBUG` logs,
create `.env` file with variable `SD_DEBUG=1` and load it to your environment.
```bash
$ echo "export SD_DEBUG=1" >> .env
$ source .env
```
Since [structlog](http://www.structlog.org/en/stable/) is used for logging,
you can have nice **colorized output** in the CLI. You just need to install [colorama](https://github.com/tartley/colorama).
```bash
$ pip3 install colorama
```
You can also switch between JSON logs renderer good for logs management services (enabled by `SD_JSON_LOGS=1`) or console render.
```bash
$ echo "export SD_JSON_LOGS=1" >> .env
```

# References

This tool uses official [Sentinel hub python library](https://github.com/sentinel-hub/sentinelhub-py)
