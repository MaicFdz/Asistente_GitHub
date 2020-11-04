

#v2.0

import string

class ArchivoDeConfiguracion():

 def __init__(self, Master):
  self.Master=Master
  self.archivoDeConfiguracion=''
  self.configuracionEnProceso=[]
  self.configuracion={}
  self.separador='='

# def importar(self, archivo):
#  self.archivoDeConfiguracion=archivo
#  self.cargarArchivo()

 def cargar(self):
  archivo=self.archivoDeConfiguracion
  f=open(archivo,"r")

# ---arreglo I-------------------------------------------------------------------------
  for renglon in f:
   if renglon=="":    #Éste es un arreglo para las líneas que están vacías
    self.configuracionEnProceso.append("\n")
   else: 
    self.configuracionEnProceso.append(renglon) #Copia el renglon incluyendo el salto de línea
  f.close()

# ---arreglo II------------------------------------------------------------------------
  copia=self.configuracionEnProceso
  self.configuracionEnProceso=[]
  for renglon in copia:
   if renglon[-1:]=="\n":  # Éste arreglo elimina los saltos de todas las líneas, incluyendo la última
    self.configuracionEnProceso.append(renglon[:-1])
   else:
    self.configuracionEnProceso.append(renglon)

# ---arreglo III-----------------------------------------------------------------------
# Arma los pares

  copia=self.configuracionEnProceso
  self.configuracionEnProceso=[]
  for par in copia:
   par_temporal=str.split(par, self.separador)
   self.configuracion[par_temporal[0]]=par_temporal[1]

  copia=[]
#  self.verConfiguraciones()
#  self.exportar()

 def verConfiguraciones(self):
  print("")
  print(self.configuracion)


 def exportar(self):
#----------------- FORMATEA LOS PARES DEL DICCIONARIO Y LOS COLOCA EN UNA LISTA
  print("Exportando")
  self.renglones=[]
  for par in self.configuracion.items():
   print(par[0]+self.separador+par[1])
   self.renglones.append(par[0]+self.separador+par[1])

#----------------- EXPORTA LA LISTA COMO UN ARCHIVO
  archivo=self.archivoDeConfiguracion
  f=open(archivo,"w")

  ultimoIndice=len(self.renglones)-1
  indice=0

  while indice<ultimoIndice:

   f.write(str(self.renglones[indice])+"\n") # Añade salto de líneas hasta la anteúltima linea...,
   indice=indice+1

  f.write(str(self.renglones[indice])) # A la última línea la deja con el salto original
  f.close()
