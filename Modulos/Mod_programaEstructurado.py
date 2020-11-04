


class ProgramaEstructurado():
#---------------------------------------------------------------------------
 def __init__(self_Master):
  self_Master.archivoDeConfiguracion=''
  self_Master.archivoDeActividadReciente=''
  self_Master.archivoDeConfiguracionInterfaz=''

#---------------------------------------------------------------------------
 def cargar(self_Master):
  self_Master.importarRecursosComunes()
  self_Master.configurar()
  self_Master.interfaz.cargar()

#---------------------------------------------------------------------------
 def importarRecursosComunes(self_Master):
  import funciones
  self_Master.funciones=funciones

  from Modulos.Mod_InterfazGrafica_TKinter import Interfaz
  self_Master.interfaz=Interfaz(self_Master)

  from Modulos.Mod_cargaDeConfiguraciones import ArchivoDeConfiguracion
  self_Master.configuracion=ArchivoDeConfiguracion(self_Master)
  self_Master.configuracionInterfaz=ArchivoDeConfiguracion(self_Master)
  self_Master.actividadReciente=ArchivoDeConfiguracion(self_Master)

#---------------------------------------------------------------------------
 def configurar(self_Master):

  archivo=self_Master.archivoDeConfiguracion
  self_Master.configuracion.archivoDeConfiguracion=archivo
  self_Master.configuracion.cargar()

  archivo=self_Master.archivoDeConfiguracionInterfaz
  self_Master.configuracionInterfaz.archivoDeConfiguracion=archivo
  self_Master.configuracionInterfaz.cargar()

# Ésto debe ser opcional al momento de crear un proyecto nuevo:

  archivo=self_Master.archivoDeActividadReciente
  self_Master.actividadReciente.archivoDeConfiguracion=archivo
  self_Master.actividadReciente.cargar()

#---------------------------------------------------------------------------
 def iniciarInterfaz(self_Master):
  self_Master.interfaz.iniciar()

#---------------------------------------------------------------------------