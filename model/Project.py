import os
from constante import Constante


class Project:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.logger = Constante().getLogger()

    def initProject(self, arguments):
        from lib.filter import filterBranchs, filterEnviroment, filterDemanda, filterName, filterType
        from lib.command import findFile, getApiPath, getUtilPath

        self.demanda = None
        self.name = filterName(arguments.name)
        self.type = filterType(self.name)
        self.enviroment = filterEnviroment(arguments)
        self.branch = filterBranchs(self.enviroment, arguments.tfs)
        if type != None:
            # default api            
            self._path = getApiPath()            
            if(self.enviroment == 'Desenvolvimento'):
                self.demanda = filterDemanda(self.enviroment)
                # mount full path
                self._path = os.path.join(
                    # default api
                    str(self._path),
                    # get type
                    str(self.type),
                    # enviroment
                    str(self.branch),
                    # demanda
                    str(self.demanda),
                    # name project
                    str(self.name)
                )
            else:
                self._path = os.path.join(
                    str(self._path),
                    # get type
                    str(self.type),
                    # enviroment
                    str(self.branch),
                    # name project
                    str(self.name)
                )
        else:
            # default util
            self._path = getUtilPath()
            if(self.enviroment == 'Desenvolvimento'):
                self.demanda = filterDemanda(self.enviroment)
                # mount full path
                self._path = os.path.join(
                    str(self._path),
                    # enviroment
                    str(self.branch),
                    # demanda
                    str(self.demanda)
                )

            # util solution
            # mount full path
            self._path = os.path.join(
                # default util
                str(self._path),
                # enviroment
                str(self.branch)
            )

        # set full path
        self._fullPath = findFile(
            '*%s.sln' % str(self.name),
            str(self._path)
        )

        self.logger.success('Project -> OK')
        return self
