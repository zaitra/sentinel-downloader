import logging
import click

from sentinel_downloader.api.api import SentinelDownloaderAPI

logger = logging.getLogger(__name__)


@click.command("download")
@click.option("-c", "--config", help="Path to sentinel-downloader configuration.")
def download(config):
    """
    Download image(s) from sentinel-hub
    """

    api = SentinelDownloaderAPI(config)
    api.download()
