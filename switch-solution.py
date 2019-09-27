import sys
import argparse

from service.commandService import *
from model.ambiente import Ambiente


def loading(argv):
    # exemplo -a ho -t ws -n WSXYZ
    parser = argparse.ArgumentParser(description="Switch Solution")
    parser.add_argument("name", type=str, help='Nome do projeto: ex=wsxyz')
    parser.add_argument("-ds", "--dev", metavar="", type=bool,
                        help='Ambiente de Desenvolvimento.', default=False, const=True, nargs="?")
    parser.add_argument("-ho", "--hom", metavar="", type=bool,
                        help='Ambiente de Homologação.',  default=False, const=True, nargs="?")
    parser.add_argument("-pr", "--pro", metavar="", type=bool,
                        help='Ambiente de Produção.', default=False, const=True, nargs="?")
    return parser.parse_args()


def main(argv: None):
    arguments = loading(argv)
    print(arguments)
    ambiente = Ambiente(arguments)

    if ambiente.enviroment != None:
        # direct command this is optional, use to be fast!
        if arguments.enviroment is not None and arguments.name is not None:
            showProjectScreen(ambiente)
    else:
        pass


main(sys.argv)
