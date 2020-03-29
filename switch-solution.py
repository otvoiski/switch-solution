import argparse

from constante import Constante
from lib.filter import filterAnswerMenu, filterArgument
from lib.menu import initMenu, solutionMenu
from lib.questions import askOptions
from model.Project import Project

# load logger
logger = Constante().getLogger()


def argumentsParser():
    parser = argparse.ArgumentParser(description="Switch Solution")
    parser.add_argument(
        "name", type=str, help='Nome do projeto: ex=wsxyz', nargs="?")
    parser.add_argument("-ds", "--dev", action="store_true",
                        help='Ambiente de Desenvolvimento.', default=False)
    parser.add_argument("-ho", "--hom", action="store_true",
                        help='Ambiente de Homologação.', default=False)
    parser.add_argument("-pr", "--pro", action="store_true",
                        help='Ambiente de Produção.', default=False)
    parser.add_argument("-t", "--tfs", action="store_true",
                        help='Busca no diretorio remoto do TFS', default=False)
    parser.add_argument(
        "-c",
        "--config",
        action="store_true",
        help='Arquivo de configuração do sistema',
        default=False)
    parser.add_argument("--debug", action="store_true",
                        help='Executa o sistema como debug', default=False)
    parser.add_argument(
        "-d",
        dest="branch",
        metavar="demanda",
        type=str,
        help='Branch na aplicação, -d D445566',
        nargs="?")
    arguments = parser.parse_args()
    return arguments


def main():
    # load arguments
    arguments = argumentsParser()

    # filter logs
    if(not arguments.debug):
        logger.remove()

    # filter arguments
    filterArgument(arguments)
    # starter program
    initMenu()
    # init object project
    project = Project().initProject(arguments)
    # carrega o menu da solution
    solutionMenu(project)
    # pergunta as possibilidades
    answer = askOptions()
    # fltra as respostas do menu
    filterAnswerMenu(answer, project)

if __name__ == '__main__':
    try:
        main()
    except Exception:
        logger.exception("")
