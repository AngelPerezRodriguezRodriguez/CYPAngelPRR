#Otras formas de crear listas
print("Otras formas de crear listas")

#Duplas
print()
print("###A través de duplas")

#String
print()
print("###A partir de un string")
fecha = "12/05/2015"
print(fecha)
lista_fecha = fecha.split('/')
#Determinamos una variable para la lista que vamos a generar a partir de un string
##En "fecha" vamos a hacer una división, es decir un "split" marcando como elemento
##divisor el '/'
print(lista_fecha)

print()
print("###Ejercicio de listas a partir de string")
crudos = " 13 , 56 , 85 , 78 , 34 , 2 , 7 , 3 , 5 "
print(crudos)
lista_numeros = crudos.split(',')
print(lista_numeros)

print()
print(lista_numeros[0])

lista_numeros[0] = lista_numeros[0].strip()
print(lista_numeros[0])
#Strip: función que quita los espacios en blanco adelante y atras, y saltos de linea
print(lista_numeros)


print()
print("Uso de for")#Investigar la función de "len"
for i in range (len(lista_numeros)):
    lista_numeros[i] = int(lista_numeros[i].strip())
print(lista_numeros)
print("Fin de for")

print()
lista_numeros.sort() #Función para ordenar números
print(lista_numeros)

print()
lista_numeros.reverse() #Función que invierte el orden de los valores
print(lista_numeros)

print()
lista_numeros.append(0) #Función que agrega un elemento deseado al final de la lista
print(lista_numeros)
lista_numeros.append(500)
lista_numeros.append(200)
lista_numeros.append(900)
print(lista_numeros)
lista_numeros.reverse()
print(lista_numeros)
lista_numeros.sort()
print(lista_numeros)


