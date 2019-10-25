# Sentinel Downloader
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
$ make build
$ docker run -it --rm -v /tmp/images:/tmp/images $(IMAGE) bash -c "sentinel-downloader download -c /src/files"
```

**Note:** This will build image locally and you have to have your `sentinel-downloader` config in the ./files/.sd.yaml.

# Configuration


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
