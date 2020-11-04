# -*- coding: utf-8 -*-
#!/bin/python3
import argparse, sys, os

#
# Esta funcion determina si existe Git instalado en la computadora
#
##### Se debe mejorar #####
#
def confirmGit():
    r = 0
    try:
        # Ejecutamos un comando de prueba
        os.system("git --help")
        os.system("clear")
    except:
        # si ocurre un error es porque git no se encuentra instalado
        print("You don't have git installed, please consult")
        r = 1
    return r

# Funcion para crear un repositorio en git
def gitInit(dr, repo, br):
    os.chdir(dr)
    os.system("git init")
    os.system("git remote add origin " + repo)
    os.system("git branch -M " + br)

def gitPush(dr, commit, branch):
    os.chdir(dr)
    os.system("git add .")
    os.system("git commit -m " + commit)
    os.system("git push -f -u origin " + branch)

# Por el momento es capaz de soportar parametros desde consola
parser = argparse.ArgumentParser(description="This program can help you with git commands")
# Define la rta de trabajo
parser.add_argument('-d', '--dir', metavar='path', help='This path contain git proyect or path to create git repository')
# Define el Commit
parser.add_argument('-m', '--commit', default="New Commit", metavar='text', help='This is a comment in your update to repository')
# Define la url del repositorio
parser.add_argument('-r', '--remote', metavar='url', help='This url is a link to git repository')
# Define la rama por defecto
parser.add_argument('-b', '--branch', default="main", help="This define branch default")
# indica si estamos creando un repositorio
parser.add_argument('--create', action='store_true', help='This flag set to create repository')
# Indica si solo hará push
parser.add_argument('--push', action='store_true', help='This flag set changes to remote repository')
# Procesamos los argumentos recibidos
args = parser.parse_args()


# If autoejecute
if __name__ == "__main__":
    #En caso de que no se reciban argumentos en la consola mostramos la pantalla de ayuda
    if len(sys.argv) <= 1:
        parser.print_help()
    else:
        # En caso de tener Git instalado se procede
        if confirmGit() == 0:
            if args.create and args.dir and args.remote and args.branch:
                gitInit(args.dir, args.remote, args.branch)
                gitPush(args.dir, args.commit, args.branch)
                os.system('pause>nul')
            else:
                print("Debes ejecutar el comando de la siguiente manera:")
                print("         ./subir_miRepositorio_a_GitHub.py --create -d '/path/to/proyect' -r 'https://github|gitlab.com/UserName/YourRepo' -m 'My Commit'")
                print("")
                print("")
                parser.print_help()
            if args.push and args.dir:
                gitPush(args.dir, args.commit, args.branch)
            else:
                print("Debes ejecutar el comando de la siguiente manera:")
                print("         ./subir_miRepositorio_a_GitHub.py --push -d '/path/to/proyect' -m 'My Commit'")
                print("")
                print("")
                parser.print_help()