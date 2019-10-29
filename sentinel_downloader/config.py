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
Sentinel downloader configuration.
"""


from pathlib import Path

from jsonschema import Draft4Validator, ValidationError
from yaml import safe_load

from sentinel_downloader.constants import CONFIG_FILE_NAME
from sentinel_downloader.log import logger
from sentinel_downloader.schema import CONFIG_SCHEMA


class Config:
    def __init__(self):
        self.debug = False
        self.times = []
        self.layer = ""
        self.bounding_box = []
        self.width = 0
        self.height = 0
        self.max_cloud_percentage = 1  # take all images by default
        self.image_dir = ""

    @staticmethod
    def validate(raw_dict: dict) -> None:
        """
        Validate config file according to validation schema defined in schema.py file.

        :param raw_dict: dictionary with config options
        :return: None
        """
        try:
            Draft4Validator(CONFIG_SCHEMA).validate(raw_dict)
        except ValidationError as ex:
            logger.error("Provided configuration is not valid", **raw_dict)
            raise Exception(f"Provided configuration is not valid: {ex}.")

    @staticmethod
    def get_from_dict(raw_dict: dict, validate=True) -> "Config":
        """
        Get Config object from python dict.

        :param raw_dict: Dict loaded from file
        :param validate: validate if config is correct according to schema in schema.py
        :return: Config
        """
        if validate:
            Config.validate(raw_dict)

        config = Config()

        config.debug = raw_dict.get("debug", False)
        config.times = raw_dict.get("times", None)
        config.layer = raw_dict.get("layer", None)
        config.bounding_box = raw_dict.get("bounding_box", None)
        config.width = raw_dict.get("width", 400)
        config.height = raw_dict.get("height", 400)
        config.max_cloud_percentage = raw_dict.get("max_cloud_percentage", 1)
        config.image_dir = raw_dict.get("images_dir", None)

        logger.debug("Loaded config", **config.__dict__)

        return config

    @staticmethod
    def get_config(path=None) -> "Config":
        """
        Load configuration file from provided path or current working directory.

        :param path: Absolute path to config file.
        :return: Config
        """
        directory = Path(path) or Path.cwd()
        if not path:
            # try to find config in current directory with default name
            config_file_name_full = directory / CONFIG_FILE_NAME
        else:
            # full path to config is provided from command line
            config_file_name_full = directory

        logger.debug("Loading config", directory=directory)

        try:
            loaded_config = safe_load(open(config_file_name_full))
        except Exception as ex:
            logger.error(
                "Cannot load config", config_file_name_full=config_file_name_full
            )
            raise Exception(f"Cannot load config: {ex}.")

        return Config.get_from_dict(raw_dict=loaded_config)
