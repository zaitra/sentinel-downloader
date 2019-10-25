import os

from sentinelhub import WmsRequest, CustomUrlParam, CRS, BBox

from sentinel_downloader.config import Config
from sentinel_downloader.utils import save_image

# from sentinel_downloader.api.api import SentinelDownloaderAPI
# api = SentinelDownloaderAPI()


class SentinelDownloaderAPI:

    def __init__(self):
        self.config = Config.get_config()
        self.bounding_box = BBox(bbox=self.config.bounding_box, crs=CRS.WGS84)
        self.custom_url_params = {CustomUrlParam.SHOWLOGO: False}  # remove Sentinel logo

    def download(self):
        for time in self.config.times:
            # FIXME ranges has to be all from the different years right now
            # this is just folder path for one time range
            path = self.config.image_dir + "/" + self._get_year_from_time(time[0]) + "/"
            if not os.path.exists(path):
                os.mkdir(path)
            time = tuple(time)
            self.download_image(time, path)

    def download_image(self, time, path=None):
        request = WmsRequest(layer=self.config.layer,
                                            bbox=self.bounding_box,
                                            time=time,  # download from this time ranges
                                            maxcc=self.config.max_cloud_percentage,
                                            width=self.config.width, height=self.config.height,  # photo dimensions
                                            custom_url_params=self.custom_url_params,
                                            instance_id=self.config.instance_id)

        if request.get_data():
            images = request.get_data()
            for index, image in enumerate(images):
                if path:
                    save_image(image, path + str(index) + ".png")
                else:
                    raise Exception("Path to image folder does not exists!")

    def _get_year_from_time(self, time):
        # FIXME this is workaround, this can be done by converting to datetime
        return time.split('-')[0]
