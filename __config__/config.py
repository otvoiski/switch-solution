import configs
from pathlib import Path


def getPathConfig():
    return Path(__file__).with_name('data.conf')


def getConfig():
    c = configs.load(getPathConfig())
    return c

