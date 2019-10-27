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


import os
import cv2

from sentinelhub import WmsRequest, CustomUrlParam, CRS, BBox

from sentinel_downloader.config import Config


class SentinelDownloaderAPI:
    def __init__(self, config_path=None):
        self.config = Config.get_config(config_path)
        self.bounding_box = BBox(bbox=self.config.bounding_box, crs=CRS.WGS84)
        self.custom_url_params = {
            CustomUrlParam.SHOWLOGO: False
        }  # remove SentinelHub logo

    def download(self):
        for time in self.config.times:
            path = (
                self.config.image_dir
                + self.config.layer
                + "/"
                + time[0]
                + "_"
                + time[1]
                + "/"
            )
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)
            time = tuple(time)
            self.download_image(time, path)

    def download_image(self, time, path=None):
        request = WmsRequest(
            layer=self.config.layer,
            bbox=self.bounding_box,
            time=time,  # download from this time ranges
            maxcc=self.config.max_cloud_percentage,
            width=self.config.width,
            height=self.config.height,  # photo dimensions
            custom_url_params=self.custom_url_params,
            instance_id=self.config.instance_id,
        )

        if request.get_data():
            images = request.get_data()
            for index, image in enumerate(images):
                if path:
                    SentinelDownloaderAPI._save_image(image, path + str(index) + ".png")
                else:
                    raise Exception("Path to image folder does not exists!")

    @staticmethod
    def _save_image(image_array, path):
        """
        save numpy array image to specific path
        :param image_array: Numpy array
        :param path: Path to save
        :return:
        """
        cv2.imwrite(path, image_array)
