# MIT License
#
# Copyright (c) 2019 zaitra.io

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Python interface for Sentinel downloader.
"""

import os

import cv2
from sentinelhub import WmsRequest, CustomUrlParam, CRS, BBox, WcsRequest

from sentinel_downloader.api.exceptions import ExceptionMissingAccessToken
from sentinel_downloader.config import Config
from sentinel_downloader.log import logger
from sentinel_downloader.settings import sentinel_hub_instance_id


class SentinelDownloaderAPI:

    image_path_template = "{image_dir}{layer}/{date_from}-{date_to}/"
    image_name_template = "{path}{index}.png"
    instance_id = sentinel_hub_instance_id

    def __init__(self, config_path=None):
        """
        :param config_path: Path to configuration file.
        """
        self.config = Config.get_config(config_path)
        self.bounding_box = BBox(bbox=self.config.bounding_box, crs=CRS.WGS84)
        self.custom_url_params = {
            CustomUrlParam.SHOWLOGO: False
        }  # remove SentinelHub logo
        self._check_access_token()

    def _check_access_token(self):
        """
        Validate if access token is provided.

        :return: None
        """
        if not self.instance_id:
            raise ExceptionMissingAccessToken

    def download(self):
        """
        Download images for time ranges provided in config file.
        This method will create following directory structure:
        project

        └─── layer
        │   └─── <time_from>_<time_to>
        |           │   0.png
        |           │   1.png
        |   └─── <time_from>_<time_to>
        |           │   0.png
        |           │   1.png

        :return: None
        """
        logger.info("Download has started")
        for layer in self.config.layers:
            for time in self.config.times:
                path = self.image_path_template.format(
                    image_dir=self.config.image_dir,
                    layer=layer,
                    date_from=time[0],
                    date_to=time[1],
                )
                if not os.path.exists(path):
                    os.makedirs(path, exist_ok=True)
                time = tuple(time)
                logger.info("Downloading images", date_range=time, layer=layer)
                self.download_image(time, layer, path)

    def create_wms_request(self, time, layer):
        """
        Create Sentinel Hub WMS (Web Map Service) get map request.

        If one of the photo resolution (width or height) is not specified,
        it would be set automatically in a way that image would best fit bounding box ratio.

        :param time: time range in format ('time_from', 'time_to')
        :param layer: layer from sentinel-hub configuration
        :return: obj WmsRequest
        """
        return WmsRequest(
            layer=layer,
            bbox=self.bounding_box,
            time=time,
            maxcc=self.config.max_cloud_percentage,
            width=self.config.width if self.config.width else None,
            height=self.config.height if self.config.height else None,
            custom_url_params=self.custom_url_params,
            instance_id=self.instance_id,
        )

    def create_wcs_request(self, time, layer):
        """
        Create Sentinel Hub WCS (Web Coverage Service) get map request.

        Used for getting image in highest resolution - 10 metres per pixel.

        :param time: time range in format ('time_from', 'time_to')
        :param layer: layer from sentinel-hub configuration
        :return: obj WcsRequest
        """
        return WcsRequest(
            layer=layer,
            bbox=self.bounding_box,
            time=time,
            maxcc=self.config.max_cloud_percentage,
            resx="10m",
            resy="10m",
            custom_url_params=self.custom_url_params,
            instance_id=self.instance_id,
        )

    def download_image(self, time, layer, path=None):
        """
        Download images from single time range.

        If no photo resolution is specified, the highest resolution will be used.

        :param time: time range in format ('time_from', 'time_to')
        :param layer: layer from sentinel-hub configuration
        :param path: path where to save images
        :return: None
        """
        if self.config.width or self.config.height:
            # wms request for using specific resolution
            request = self.create_wms_request(time=time, layer=layer)
        else:
            # wcs request for using highest resolution
            request = self.create_wcs_request(time=time, layer=layer)

        images = request.get_data()
        if images:
            for index, image in enumerate(images):
                if path:
                    image_name = self.image_name_template.format(path=path, index=index)
                    logger.info("Saving image", image=image_name)
                    SentinelDownloaderAPI._save_image(image, image_name)
                else:
                    raise Exception("Path to image folder does not exists!")

    @staticmethod
    def _save_image(image_array, path):
        """
        save numpy array image to specific path
        :param image_array: Numpy array
        :param path: Path to save
        :return: None
        """
        cv2.imwrite(path, image_array)
