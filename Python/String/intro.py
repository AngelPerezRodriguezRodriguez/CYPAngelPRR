nombre = "Angel Perez"
print(nombre)

#Indexado positivo
print()
print("###Parte número 1: Indexado positivo")
print(nombre[0])
print(nombre[1])
print(nombre[2])
print(nombre[3])
print(nombre[4])
print(nombre[5])

print(nombre[6])
print(nombre[7])
print(nombre[8])
print(nombre[9])
print(nombre[10])


#Indexado negativo
print()
print("###Parte número 2: Indexado negativo")
print(nombre[-5])
print(nombre[-4])
print(nombre[-3])
print(nombre[-2])
print(nombre[-1])


#Slicing (rebanadas)
print()
print("###Parte número 3: Slicing")
print(nombre[0:4:1])
print(nombre[0:5:1])                                       #Recuerda incluir un número más al stop
print(nombre[6:11:1])


#Valores por defecto de slicing
print()
print("###Parte número 4: Valores por defecto de slicing")
print(nombre[::])#Angel Perez                              #<0> <tamaño de la cadena COMPLETA> <1>
print(nombre[:5:])#Angel
print(nombre[6::])#Perez
print(nombre[:5:2])#Agl
print(nombre[1:5:2])#ne


#Slicing negativo
print()
print("###Parte número 5: Slicing negativo")
print(nombre[-1:-12:-1])#zereP legnA                       #Aun no se agregan los valores por defecto


print(nombre[::-1]) #zereP legnA                           #Ya se agregaron los valores por defecto

#El número negativo interpreta la secuencia de igual forma, de manera implícita empieza en el -1 y
#termina en el número que complete la cadena


print(nombre[-7::-1])#legnA
print(nombre[:-6:-1])#zereP


#El inicio, como ya se vió, puede tomar valores negativos
#El tamaño de la cadena también puede tomar valores negativos
#El incremento también puede tomar valores negativos



print()
print("###Ejercicio de práctica")
frase = "Solo existen dos tipos de personas, las que saben binario y las que no"
print(frase)
print()

#Hacer un slicing para imprimir la palabra existen
print(frase[5:12:])

print(nombre[5])
#Hacer otra para escribir la palabra "personas" de forma inversa
print(frase[-37:-45:-1])

print(nombre[5])
#Hacer un slicing que imprima toda la frase en orden inverso
print(frase[::-1])