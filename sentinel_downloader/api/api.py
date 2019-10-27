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
