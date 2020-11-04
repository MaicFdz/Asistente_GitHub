


class Interfaz():

 def __init__(self_Interfaz, self_Master):
  self_Interfaz.Master=self_Master
  self_Interfaz.archivoDeConfiguracion=''

 def cargar(self_Interfaz):
  self_Interfaz.importarRecursos()
  self_Interfaz.cargarConfiguraciones(self_Interfaz.archivoDeConfiguracion)
  self_Interfaz.establecerConfiguraciones()

 def importarRecursos(self_Interfaz):
  import tkinter as tk
  from tkinter import Tk, ttk
  self_Interfaz.ventanita=Tk()
  import Widgets
  self_Interfaz.ventanita.widgets=Widgets

 def cargarConfiguraciones(self_Interfaz, archivo):
  self_Interfaz.archivoDeConfiguracion=archivo
 # self_Interfaz.configuraciones=self_Interfaz.Master.funciones.cargarConfiguraciones(self_Interfaz.Master, archivo)

 def establecerConfiguraciones(self_Interfaz):

  self_Interfaz.titulo=self_Interfaz.Master.configuracionInterfaz.configuracion['titulo']
#  self_Interfaz.icono=self_Interfaz.Master.configuracionInterfaz.configuracion['icono']
  self_Interfaz.dimensiones=self_Interfaz.Master.configuracionInterfaz.configuracion['dimensiones']
  self_Interfaz.colorFondo=self_Interfaz.Master.configuracionInterfaz.configuracion['colorFondo']
  self_Interfaz.colorLetras=self_Interfaz.Master.configuracionInterfaz.configuracion['colorLetras']
  self_Interfaz.colorLetras2=self_Interfaz.Master.configuracionInterfaz.configuracion['colorLetras2']
  self_Interfaz.colorLetras3=self_Interfaz.Master.configuracionInterfaz.configuracion['colorLetras3']
  self_Interfaz.colorLetras4=self_Interfaz.Master.configuracionInterfaz.configuracion['colorLetras4']
  self_Interfaz.colorLetrasBoton=self_Interfaz.Master.configuracionInterfaz.configuracion['colorLetrasBoton']
  self_Interfaz.colorFondoBoton=self_Interfaz.Master.configuracionInterfaz.configuracion['colorFondoBoton']
  self_Interfaz.colorFondoImagen=self_Interfaz.Master.configuracionInterfaz.configuracion['colorFondoImagen']
  self_Interfaz.colorFondoScrollText=self_Interfaz.Master.configuracionInterfaz.configuracion['colorFondoScrollText']

 def iniciar(self_Interfaz):

  self_Interfaz.ventanita.title(self_Interfaz.titulo)
  self_Interfaz.ventanita.iconbitmap(self_Interfaz.icono)
  self_Interfaz.ventanita.geometry(self_Interfaz.dimensiones)
  self_Interfaz.ventanita.configure(background=self_Interfaz.colorFondo)
  self_Interfaz.ventanita.widgets.cargarWidgetsIniciales(self_Interfaz, self_Interfaz.ventanita)

  self_Interfaz.ventanita.mainloop()
