


import os
from os import listdir

def listarRepositoriosLocales(self_Master):
 listado=listdir(self_Master.directorioRepositoriosLocales)
# self_Master.actividadReciente.configuracion['libro']=nombreLibro
# self_Master.actividadReciente.exportar()
 return(listado)

