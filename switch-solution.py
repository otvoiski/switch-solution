import sys
import argparse

from service.commandService import *
from model.ambiente import Ambiente


def loading(argv):
    # exemplo -a ho -t ws -n WSXYZ
    parser = argparse.ArgumentParser(description="Switch Solution")
    parser.add_argument("-e", required=True, action='store', dest='enviroment', type=str,
                        help='Ambiente da branch: ds - desenvolvimento, ho - homologacao')
    parser.add_argument("-t", required=False, action='store', dest='type', type=str, default='ws',
                        help='Tipo do sistema: ws - web service, ms - micro service (Default: ws)')
    parser.add_argument("-n", required=True, action='store',
                        dest='name', type=str, help='Nome do projeto: ex=wsxyz')
    return parser.parse_args()


def main(argv: None):
    arguments = loading(argv)
    ambiente = Ambiente(arguments)

    if ambiente.enviroment != None:
        # direct command this is optional, use to be fast!
        if arguments.enviroment is not None and arguments.name is not None:
            showProjectScreen(ambiente)
    else:
        pass


main(sys.argv)
