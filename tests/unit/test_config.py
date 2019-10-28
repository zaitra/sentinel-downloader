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
Unit tests for configuration loading and validation
"""

import pytest
from yaml import safe_load

from sentinel_downloader.config import Config
from tests.spellbook import DATA_DIR


def get_config_full():
    return safe_load(open(DATA_DIR / "config" / "config-full.yaml"))


def get_config_minimal():
    return safe_load(open(DATA_DIR / "config" / "config-minimal.yaml"))


@pytest.mark.parametrize(
    "raw, is_valid",
    [
        ({}, False),
        ({"debug": True}, False),
        ([], False),
        ({"asd"}, False),
        (get_config_full(), True),
        (get_config_minimal(), True),
    ],
)
def test_config_validate(raw, is_valid):
    if is_valid:
        Config.validate(raw)
    else:
        with pytest.raises(Exception):
            Config.validate(raw)
