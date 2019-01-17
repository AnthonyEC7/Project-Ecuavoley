

def verPartidos():
   from gestorArchivos import Archivo
   Archivo.generaArchivo()
   archivo = open('encuentro.txt', 'r')
   lineas=archivo.readlines()
   for line in lineas:
       print(line)