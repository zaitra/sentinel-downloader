import logging

import click
from pkg_resources import get_distribution
from sentinel_downloader.cli.download import download

logger = logging.getLogger("sentinel_downloader")


@click.version_option(
    version=get_distribution("sentinel-downloader").version, message="%(version)s"
)
@click.group()
def sentinel_downloader_base():
    """
    Download images from sentinel-hub with ease
    """
    sentinel_downloader_version = get_distribution("sentinel_downloader").version
    logger.info(f"Sentinel-downloader {sentinel_downloader_version} is being used.")


@click.command("version")
def version():
    """Display the version."""
    click.echo(get_distribution("sentinel-downloader").version)


sentinel_downloader_base.add_command(download)
sentinel_downloader_base.add_command(version)

if __name__ == "__main__":
    sentinel_downloader_base()
