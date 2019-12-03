import json
import os


class Ambiente():
    def _loadConfigs(self, arguments):
        with open('.\\switch-solution\\config\\config.json', 'r') as archive:
            # Abre o arquivo de configuração nessa pasta acima /\ /\ /\
            configs = json.load(archive)

            # loading #
            self.name = arguments.name.upper()

            # Correção referente aos ambientes complexos ex: Ambiente mongo que se encontra dentro de micro serviços
            self._type = str(
                (arguments.name[0] + arguments.name[1])).upper()

            # Ambiente Default
            if(arguments.dev == False and arguments.hom == False and arguments.pro == False):
                arguments.dev = True

            # Tipos de projetos tais como Web Service e micro serviços.
            if self.name == "WSATE":
                self.projectType = 'Projeto Complexo'
                self._path = configs["project"]["wsate"]["path"]
                self.getEnvironment(
                    arguments, configs["project"]["wsate"]["enviroment"]
                )

            elif self._type == 'WS':
                self.projectType = 'Web Service'
                self._pathType = configs["webService"]
                self._path = configs["project"]["apiComercial"]["path"]
                self.getEnvironment(
                    arguments, configs["project"]["apiComercial"]["enviroment"]
                )

            elif self._type == 'MS':
                self.projectType = 'Micro Service'
                self._pathType = configs["microService"]
                self._path = configs["project"]["apiComercial"]["path"]
                self.getEnvironment(
                    arguments, configs["project"]["apiComercial"]["enviroment"]
                )

            elif self._type == 'AM':
                self.projectType = 'Micro Service'
                self._pathType = configs["microService"]
                self._path = configs["project"]["apiComercial"]["path"]
                self.getEnvironment(
                    arguments, configs["project"]["apiComercial"]["enviroment"]
                )

            elif self._type == 'UT':
                self.projectType = 'Projeto Utilitário'
                self._path = configs["project"]["util"]["path"]
                self.getEnvironment(
                    arguments, configs["project"]["util"]["enviroment"]
                )

            else:
                print('Tipo do web service não existe ou não está habilitado.')
                return False

            #print(self.getFolderProject())

            # Fecha o arquivo de configuração
            archive.close()
            return True

    def getEnvironment(self, arguments, enviroment):
        # De acordo com as TAG's é possivel informar diretamente qual o ambiente.
        # Ambientes de desenvolvimento, homologação e produção
        if arguments.dev == True:
            self._enviroment = "DS"
            self.enviroment = 'Desenvolvimento'
            self.branch = enviroment["development"]
        elif arguments.hom == True:
            self._enviroment = "HO"
            self.enviroment = 'Homologação'
            self.branch = enviroment["homologation"]
        elif arguments.pro == True:
            self._enviroment = "PR"
            self.enviroment = 'Produção'
            self.branch = enviroment["production"]
        else:
            print('Ambiente informado não existe ou não está habilitado.')

        if self.branch == 'Trunk':
            self._enviroment = "PR"
            self.enviroment = 'Produção'

    def getFolderProject(self):
        if self.name == 'UTIL':
            return self._path + '\\' + self.branch
        elif self.name == 'WSATE':
            return self._path + '\\' + self.branch + '\\Fontes'
        else:
            return self._path + '\\' + self._pathType + '\\Branches\\' + self.branch + '\\' + self.name + '\\Fontes'

    def __init__(self, arguments: None):

        if arguments == None:
            return
        if(not self._loadConfigs(arguments)):
            os._exit
