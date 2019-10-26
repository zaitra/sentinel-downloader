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
