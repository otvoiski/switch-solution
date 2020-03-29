import os

from constante import Constante


class Project:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.logger = Constante().getLogger()

    def initProject(self, arguments):
        from lib.filter import filterBranchs, filterEnviroment, filterDemanda, filterName, filterType
        from lib.command import findFile, getApiPath, getUtilPath

        self.demanda = arguments.demanda
        self.name = filterName(arguments.name)
        self.logger.success('Name -> OK')
        self.type = filterType(self.name)
        self.logger.success('Type -> OK')
        self.enviroment = filterEnviroment(arguments)
        self.logger.success('Enviroment -> OK')
        self.branch = filterBranchs(self.enviroment, arguments.tfs)
        self.logger.success('Branch -> OK')
        if self.name != 'UTIL':
            # default api
            self._path = getApiPath()
            if(self.enviroment == 'Desenvolvimento'):
                if(arguments.demanda == None):
                    self.demanda = filterDemanda(
                        self._path, os.path.join(self.type, self.branch))

                self.logger.success('Demanda -> OK')
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
            self.logger.info('Path -> OK')
        else:
            # default util
            self._path = getUtilPath()
            if(self.enviroment == 'Desenvolvimento'):
                if(arguments.demanda == None):
                    self.demanda = filterDemanda(self._path, self.branch)

                # mount full path
                self._path = os.path.join(
                    str(self._path),
                    # enviroment
                    str(self.branch),
                    # demanda
                    str(self.demanda)
                )
            else:
                # util solution
                # mount full path
                self._path = os.path.join(
                    # default util
                    str(self._path),
                    # enviroment
                    str(self.branch)
                )
            self.logger.success('Path -> OK')
        # set full path
        self._fullPath = findFile(
            '*%s.sln' % str(self.name),
            str(self._path)
        )
        self.logger.success('FullPath -> OK')
        self.logger.success('Project -> OK')
        return self
