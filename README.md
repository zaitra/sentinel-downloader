# Sentinel Downloader [![Build Status](https://travis-ci.com/zaitra/sentinel-downloader.svg?branch=master)](https://travis-ci.com/zaitra/sentinel-downloader)
Library and CLI tool for downloading satellite images from the https://www.sentinel-hub.com/

# Installation

```bash
$ git clone https://github.com/zaitra/sentinel-downloader
$ cd sentinel-downloader
$ pip3 install .
```

# Usage

## CLI

```bash
sentinel-downloader download -c <PATH_TO_CONFIGURATION>
```

Configuration file is described in configuration section.


## Docker

If you want just try it out you can easily do it using docker:

```bash
$ docker run -it --rm -v /tmp/images:/tmp/images $(IMAGE) bash -c "sentinel-downloader download -c /src/files/.sd.yaml"
```

**Note:** This will build image locally and you have to have your `sentinel-downloader` config `.sd.yaml` in the root directory of this project.

# Configuration

**Configuration file contains sensitive data so it is recommended to keep it in private repository**.

## Example

```yaml
debug: true
instance_id: "secret-token"
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

# References

This tool uses official [Sentinel hub python library](https://github.com/sentinel-hub/sentinelhub-py)
