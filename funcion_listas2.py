#arreglos
#lectura
#escritura / asignación
#actualización: inserción, eliminación, modificación
#ordenamiento
#busqueda 


#dri(list)
#help(list.insert)


#escritura
frutas = ["Zapote", "Manzana", "Pera", "Aguacate", "Durazno", "Uva", "Sandía"]

#Lectura, el selector [índice]
print(frutas[2])


#Lectura con for

print("---------")
#for opción 1

for indice in range(0,7,1):
    print(frutas[indice])

print("---------")
#for opcion 2 -- por un iterador for each
#Hace lo mismo con lo anterior
#Solo funciona cuando la variable (frutas) es de tipo arreglo

for fr in frutas:
    print(fr)

print("---------")
#Asignación
frutas[2]="Melón"
print(frutas)

print("---------")
#Inserción al final
#Significa que vamos a agregar otro elemento
frutas.append("Naranaja")
print(frutas)
print(len(frutas))#Contador de elementos en la lista

print("---------")
#Inserción específica
frutas.insert(2,"Limón")
print(frutas)
print(len(frutas))#Contador de elementos en la lista

frutas.insert(0,"Mamey")
print(frutas)

print("---------")
#Eliminación con pop
print(frutas.pop())#Si no le das valor elimina el último elemento
print(frutas)

print(frutas.pop(1))
print(frutas)

print("---------")
#Remover. Remuevo el primer lemento de izquierda a derecha
frutas.append("Limón")
frutas.append("Limón")
print(frutas)
frutas.remove("Limón")
print(frutas)

print("---------")
#Ordenamiento
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)
frutas.sort()
print(frutas)

print("---------")
#Busqueda
print(f"El Limón está en la posición: {frutas.index('Limón')}")
print(f"La Uva está en la posición: {frutas.index('Uva')}")

print(f"El limón está {frutas.count('Limón')} veces en las lista")

print("---------")
#Concatenar
print(frutas)
OtrasFrutas = ["Rambutan", "Nispero", "Pitahaya"]
print(OtrasFrutas)
frutas.extend(OtrasFrutas)
print(frutas)
#frutas.append(OtrasFrutas)                       No queremos ésto
#print(frutas)

print("---------")
#Copiar
OtraCopia = frutas.copy()
OtraCopia.append("Fresa")
OtraCopia.append("Fresa")
print(frutas)
print(OtraCopia)
++#copia = frutas                                   No queremos ésto
#copia.append("Naranja")
#print(frutas)
#print(copia)
