import sys
import argparse

from service.commandService import *
from model.ambiente import Ambiente


def loading():
    # exemplo -a ho -t ws -n WSXYZ
    parser = argparse.ArgumentParser(description="Switch Solution")
    parser.add_argument("name", type=str, help='Nome do projeto: ex=wsxyz', nargs="?")
    parser.add_argument("-ds", "--dev", action="store_true",
                        help='Ambiente de Desenvolvimento.', default=False)
    parser.add_argument("-ho", "--hom", action="store_true",
                        help='Ambiente de Homologação.',  default=False)
    parser.add_argument("-pr", "--pro", action="store_true",
                        help='Ambiente de Produção.',  default=False)
    parser.add_argument("-c", "--config", action="store_true",
                        help='Arquivo de configuração do sistema', default=False)
    return parser.parse_args()


def main(argv: None):
    arguments = loading()

    if arguments.config == True:
        os.system(".\\switch-solution\\config\\config.json")
        return

    if arguments.name == None:
        print("name is required.")
        return 

    ambiente = Ambiente(arguments)
    
    if ambiente.enviroment != None:
        # direct command this is optional, use to be fast!
        if arguments.name is not None:
            showProjectScreen(ambiente)
    else:
        pass


main(sys.argv)
