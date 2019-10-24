print("###Listas")
lista = []                      #Primera forma de representar una lista
lista2 = list()                 #Segunda forma de representar una lista
         #Función constructor
print(lista)
print(lista2)

numeros = [2,5,6,8,5,6,3,9,1,9]
#Cada uno de elos elementos, al igual que los strings, están INDEXADOS
print(numeros)
print(numeros[2])#6
print(numeros[-1])#9

#Slicing
print()
print("###Listas con slicing")
print(numeros[2:5:])
print(numeros[1:9:])
print(numeros[:-6:-1])

#Se pueden almacenar elementos de diferentes tipos de elementos
#Incluso SUBLISTAS
print()
print("###Almacenaje de diferentes tipos de elementos")
cosas = ["Angel",14.5,18,True,None,[1,2,3,4,5]]
print(cosas)
print(cosas[3])
print(cosas[5])
print(cosas[5][2])
#Selección de elementos de una sublista

#Son mutables. Se puede modificar cualquiera de los valores
#Los STRINGS NO son MUTABLES, las LISTAS SI
print()
print("###Se puede modificar cualquiera de los valores")
print("Valores base:")
print(cosas)
print()
print("Cambios:")
cosas[1] = 33
print(cosas)
cosas[3] = False
print(cosas)
