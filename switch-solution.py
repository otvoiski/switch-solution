import sys
import argparse

from service.commandService import *
from model.ambiente import Ambiente


def loading(argv):
    # exemplo -a ho -t ws -n WSXYZ
    parser = argparse.ArgumentParser(description="Switch Solution")
    parser.add_argument("name", type=str, help='Nome do projeto: ex=wsxyz')
    parser.add_argument("-ds", "--dev", action="store_true",
                        help='Ambiente de Desenvolvimento.', default=False)
    parser.add_argument("-ho", "--hom", action="store_true",
                        help='Ambiente de Homologação.',  default=False)
    parser.add_argument("-i", "--info", action="store_true",
                        help='Informações do sistema',  default=False)
    parser.add_argument("-c", "--config", action="store_true",
                        help='Arquivo de configuração do sistema', default=False)
    return parser.parse_args()


def main(argv: None):
    arguments = loading(argv)
    ambiente = Ambiente(arguments)

    if arguments.config == True:
        os.system(".\\switch-solution\\config\\config.json")
        return

    if ambiente.enviroment != None:
        # direct command this is optional, use to be fast!
        if arguments.name is not None:
            showProjectScreen(ambiente)
    else:
        pass


main(sys.argv)
