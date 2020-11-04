


import os
from os import listdir

def listarRepositoriosLocales(self_Master):
 listado=listdir(self_Master.directorioRepositoriosLocales)
# self_Master.actividadReciente.configuracion['libro']=nombreLibro
# self_Master.actividadReciente.exportar()
 return(listado)

def actualizarRepositorioRemoto(self_Master, directorio):
 os.chdir(directorio)
 os.system('git init')
 os.system('git add .')

 elCommit='No se especificaron los cambios (version beta)'
 os.system('git commit --m "'+elCommit+'"')

 url_repositorio='https://github.com/MaicFdz/Asistente_GitHub'
 nombreURL='unaURL'

 os.system('git remote add '+nombreURL+' '+url_repositorio)

 os.system('git pull '+nombreURL+' cambios')
 os.system('git push -f -u '+nombreURL+' cambios')

 print('Hecho!')