import logging
import click

from sentinel_downloader.api.api import SentinelDownloaderAPI
from sentinel_downloader.config import Config

logger = logging.getLogger(__name__)


@click.command("download")
def download():
    """
    Download image(s) from sentinel-hub
    """

    api = SentinelDownloaderAPI()
    api.download()
