import json
import os


class Ambiente():
    def _loadConfigs(self, arguments):
        with open('.\\switch-solution\\config\\config.json', 'r') as archive:
            configs = json.load(archive)

            # loading #
            self.name = arguments.name.upper()
            self._type = str((arguments.name[0] + arguments.name[1])).upper()
            
            if arguments.dev == True:
                self._enviroment = "DS"
            elif arguments.hom == True:
                self._enviroment = "HO"
            elif arguments.pro == True:
                self._enviroment = "PR"
            else:
                self._enviroment = "DS"

            self._path = configs["path"]

            if self._type == 'WS':
                self.projectType = 'Web Service'
                self._pathType = configs["webService"]
            elif self._type == 'MS':
                self.projectType = 'Micro Service'
                self._pathType = configs["microService"]
            else:
                print('Tipo do web service não existe ou não está habilitado.')
                return False

            if self._enviroment == 'DS':
                self.enviroment = 'Desenvolvimento'
                self.branch = configs["desenvolvimento"]["branch"]
            elif self._enviroment == 'HO':
                self.enviroment = 'Homologação'
                self.branch = configs["homologacao"]["branch"]
            else:
                print('Ambiente informado não existe ou não está habilitado.')
                return False

            archive.close()
            return True

    def getFolderProject(self):
        return self._path + '\\' + self._pathType + '\\Branches\\' + self.branch + '\\' + self.name + '\\Fontes'

    def __init__(self, arguments: None):

        if arguments == None:
            return
        try:
            if(not self._loadConfigs(arguments)):
                os._exit
        except:
            pass
