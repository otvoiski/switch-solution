import configs
import os
from logging42 import logger
from pathlib import Path


class Constante:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.config = None
        self.config_file = None

    def mainPath(self) -> str:
        return Path(os.path.dirname(os.path.abspath(__file__)))

    def configFile(self) -> str:
        path = os.path.join(self.mainPath(), 'config', 'data.conf')
        self.config_file = Path(path)
        return self.config_file

    def getConfig(self):
        try:
            self.config = configs.load(self.configFile())
            return self.config
        except Exception:
            self.getLogger().exception('Error: ')

    def getLogger(self):
        return logger
