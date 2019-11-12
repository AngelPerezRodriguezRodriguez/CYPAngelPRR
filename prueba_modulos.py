#Módulos
#Esta caractèrística nos permite reutilizar código

#IMPORTA TODO EL ARCHIVO
import modulos
modulos.mi_print("Hola")

#SOLO IMPORTA LAS FUNCIONES QUE NOS INTERESA USAR
#(recomendable a menos que quieras importar todo)
#Hace más eficiente la ejecución si solo importas lo que vas a ocupar
from modulos import *         #El * abarca todas la funciones del doc que importas
import time
import sys

from asciistuff import Banner

print("!------------------!")
mi_print("Hola de nuevo")
otro_print("Otro print usado")
print(sumar(3,5))
print(restar(10,7))

print("!------------------!")
for i in range (10,0,-1):
    print(i, "...")
    time.sleep(0.125)
    
print("BOOOM!")
print(Banner("Booom!"))#Banner, un anuncio

print("!------------------!")
print(dir(sys.platform))
print("")
print(sys.platform)


