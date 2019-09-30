import os
import fnmatch

from model.ambiente import Ambiente


def _openSoluction(folder):
    result = []
    for root, dirs, files in os.walk(folder):
        dirs = dirs
        for name in files:
            if fnmatch.fnmatch(name, '*.sln'):
                result.append(os.path.join(root, name))
    os.system('start ' + result[0])


def _drawMenu(ambiente: Ambiente): 
    print("═════╣ Selecione Opção de abertura ╠═══════")
    print(" Ambiente:                   "+ambiente.enviroment)
    print(" Branch:                     "+ambiente.branch)
    print(" Nome do projeto:            "+ambiente.name)
    print(" Tipo do projeto:            "+ambiente.projectType)
    print("╔═════════════════════════════════════════╗")
    print("║    1) Abrir sem GLV                     ║")
    print("║    2) Abrir com GLV                     ║")
    print("║    3) Abrir com GLV sem auto resolve    ║")
    print("║    4) Realizar OVERWRITE                ║")
    print("║    5) Historico                         ║")
    print("║                                         ║")
    print("║    0) Sair                              ║")
    print("╚═════════════════════════════════════════╝")


def showProjectScreen(ambiente: Ambiente):
    if ambiente is None:
        print('Não encontrado.')
        return False
    
    if not os.path.isdir(ambiente.getFolderProject()):
        print("Projeto não existe, tente baixar o projeto manualmente.")
        return False

    os.system('cls')

    _drawMenu(ambiente)

    try:
        print()
        op = int(input("$: "))

        if op == 0:
            os._exit
        elif op == 1:
            _openSoluction(ambiente.getFolderProject())
            os._exit
        elif op == 2:
            os.system("tf get " + ambiente.getFolderProject() +
                      " /recursive /version:T")
            _openSoluction(ambiente.getFolderProject())
            os._exit
        elif op == 3:
            os.system("tf get " + ambiente.getFolderProject() +
                      " /recursive /version:T /noautoresolve")
            os.system("tf resolve " +
                      ambiente.getFolderProject() + " /recursive")
            _openSoluction(ambiente.getFolderProject())
        elif op == 4:
            sim = input(" --> Confirma um GLV com OVERWRITE? [S/N]: ")
            if sim == "s" or sim == "S":
                os.system("tf get " + ambiente.getFolderProject() +
                          " /recursive /version:T /all /overwrite /force")
            showProjectScreen(ambiente)
        elif op == 5:
            os.system("tf history " + ambiente.getFolderProject() +
                      " /recursive /stopafter:1 /format:detailed")
            showProjectScreen(ambiente)
    except:
        print("Comando invalido!")
        pass
