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
