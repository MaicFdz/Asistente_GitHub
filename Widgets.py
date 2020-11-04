


from tkinter import *
import tkinter as tk
from tkinter import ttk, font 

def cargarWidgetsIniciales(self_Ventana, self_ventanita):

 def listarRepositoriosLocales():
  listado=self_Ventana.Master.funciones.listarRepositoriosLocales(self_Ventana.Master)
  self_ventanita.comboBoxA.set(listado[0])
  return(listado)

 self_ventanita.listadoRepositorios=[]

 self_ventanita.etiquetaProyecto=Label(self_ventanita, text="_Proyecto__", foreground=self_Ventana.colorLetras, background=self_Ventana.colorFondo)
 self_ventanita.etiquetaProyecto.pack()
 self_ventanita.etiquetaProyecto.place(x=20, y=18)

 self_ventanita.nombreDelProyecto=StringVar()
 self_ventanita.comboBoxA=ttk.Combobox(self_ventanita, values=self_ventanita.listadoRepositorios, textvariable=self_ventanita.nombreDelProyecto, width=35, height=20, state="readonly")
 self_ventanita.comboBoxA.place(x=20, y=40)

# self_Ventana.encabezado=PhotoImage(file=u"D:/Karpeta/1_-_Programacion/1_-_Python/Proyectos_-_Iniciados/Programas/Interfaz_Arduino/_Imagenes/encabezado.png")
# self_Ventana.fondo=Label(self_Ventana.ventana, image=self_Ventana.encabezado, background=self_Ventana.colorFondo).place(x=-2, y=-2)

# self_ventanita.logo=PhotoImage(file=DIRECTORIO/IMAGEN.png")
# self_ventanita.fondo=Label(self_ventanita, image=self_ventanita.logo, background=self_Ventana.colorFondo).place(x=335, y=140)

 self_ventanita.comboBoxA.config(values=listarRepositoriosLocales())


#------------------------------------------------------------------------------------------------------------
