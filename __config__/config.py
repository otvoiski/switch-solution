import configs
from pathlib import Path
from __init__ import logger

_config = None

def openConfigFile():
    return Path(__file__).with_name('data.conf')

try:
    if _config == None:
        _config = configs.load(openConfigFile())
        
        logger.info('Configuração carregada!')
except Exception:
    logger.exception('Error: ')

