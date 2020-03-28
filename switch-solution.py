import sys
import argparse

from lib.questions import askOptions
from lib.filter import filterArgument, filterAnswerMenu
from lib.menu import initMenu
from lib.menu import solutionMenu
from model.Project import Project


def main():

    from helper.console import Console

    console = Console()
    console.error('Error xisjadsoi')

    exit()

    # starter program
    # initMenu()
    # select parse
    parser = argparse.ArgumentParser(description="Switch Solution")
    parser.add_argument(
        "name", type=str, help='Nome do projeto: ex=wsxyz', nargs="?")
    parser.add_argument("-ds", "--dev", action="store_true",
                        help='Ambiente de Desenvolvimento.', default=False)
    parser.add_argument("-ho", "--hom", action="store_true",
                        help='Ambiente de Homologação.',  default=False)
    parser.add_argument("-pr", "--pro", action="store_true",
                        help='Ambiente de Produção.',  default=False)
    parser.add_argument("-t", "--tfs", action="store_true",
                        help='Busca no diretorio remoto do TFS',  default=False)
    parser.add_argument("-c", "--config", action="store_true",
                        help='Arquivo de configuração do sistema', default=False)
    parser.add_argument("-d", dest="branch", metavar="demanda",
                        type=str, help='Branch na aplicação, -d D445566', nargs="?")
    arguments = parser.parse_args()

    try:
        # filter arguments
        filterArgument(arguments)

        # init object project
        project = Project().initProject(arguments)

        # carrega o menu da solution
        solutionMenu(project)

        # pergunta as possibilidades
        answer = askOptions()

        # fltra as respostas do menu
        filterAnswerMenu(answer, project)

        # fim
    except Exception as e:
        raise Exception(e.args)


if __name__ == '__main__':
    main()
