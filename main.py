


import os
from Modulos.Mod_programaEstructurado import ProgramaEstructurado

#--SET INICIAL--
directorioInicial=u'D:/Karpeta/1_-_Programacion/1_-_Python/Proyectos_-_Iniciados/Programas/Asistente_GitHub'
directorioDeConfiguraciones=directorioInicial+u'/_Configuraciones'

os.chdir(directorioInicial)

#--PROGRAMA----
miPrograma=ProgramaEstructurado()


#--RUTINA INICIAL--
miPrograma.archivoDeConfiguracion=directorioDeConfiguraciones+u'/configuracion_base.txt'
miPrograma.archivoDeConfiguracionInterfaz=directorioDeConfiguraciones+u'/configuracion_interfaz.txt'
# ESTO DEBE SER OPCIONAL:
miPrograma.archivoDeActividadReciente=directorioDeConfiguraciones+u'/actividad_reciente.txt'

miPrograma.cargar()
miPrograma.directorioRepositoriosLocales=miPrograma.configuracion.configuracion['directorioRepositoriosLocales']

# INSTRUCCIONES

miPrograma.iniciarInterfaz()

