import logging
from pathlib import Path

from jsonschema import Draft4Validator, ValidationError
from pprint import pformat
from yaml import safe_load

from sentinel_downloader.schema import CONFIG_SCHEMA
from sentinel_downloader.constants import CONFIG_FILE_NAME

logger = logging.getLogger(__name__)


class Config:
    def __init__(self):
        self.debug = False
        self.instance_id = ""
        self.times = []
        self.layer = ""
        self.bounding_box = []
        self.width = 0
        self.height = 0
        self.max_cloud_percentage = 1  # take all images by default
        self.image_dir = ""

    @staticmethod
    def validate(raw_dict: dict) -> None:
        try:
            Draft4Validator(CONFIG_SCHEMA).validate(raw_dict)
        except ValidationError as ex:
            logger.debug(f"{pformat(raw_dict)}")
            raise Exception(f"Provided configuration is not valid: {ex}.")

    @staticmethod
    def get_from_dict(raw_dict: dict, validate=True) -> "Config":
        if validate:
            Config.validate(raw_dict)

        config = Config()

        config.debug = raw_dict.get("debug", False)
        config.instance_id = raw_dict.get("instance_id", None)
        config.times = raw_dict.get("times", None)
        config.layer = raw_dict.get("layer", None)
        config.bounding_box = raw_dict.get("bounding_box", None)
        config.width = raw_dict.get("width", 400)
        config.height = raw_dict.get("height", 400)
        config.max_cloud_percentage = raw_dict.get("max_cloud_percentage", 1)
        config.image_dir = raw_dict.get("images_dir", None)

        logger.debug(config.__dict__)

        return config

    @staticmethod
    def get_config(path=None) -> "Config":
        directory = Path(path) or Path.cwd()
        if not path:
            # try to find config in current directory with default name
            config_file_name_full = directory / CONFIG_FILE_NAME
        else:
            # full path to config is provided from command line
            config_file_name_full = directory

        logger.debug(f"Loading config from directory: {directory}")

        try:
            loaded_config = safe_load(open(config_file_name_full))
        except Exception as ex:
            logger.error(f"Cannot load config '{config_file_name_full}'.")
            raise Exception(f"Cannot load config: {ex}.")

        return Config.get_from_dict(raw_dict=loaded_config)
