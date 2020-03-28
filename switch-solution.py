import sys
import argparse

from lib.filter import filterArgument
from lib.menu import initMenu
from model.project import Project


def main():
    # starter program
    initMenu()

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

        print(project.name)
        print(project.type)
        print(project.enviroment)
        print(project.branch)
        print(project.demanda)

        # Menu.solutionMenu(project)
    except Exception as e:
        raise Exception(e.args)

    # ambiente = Ambiente(arguments)

    # try:
    #     showProjectScreen(ambiente)
    # except Exception as ex:
    #     raise Exception('Ocorreu um erro ao mostrar as informações: $s' % (ex))


if __name__ == '__main__':
    main()
