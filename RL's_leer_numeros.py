archivo = open ("numeros.txt","rt")
lista = archivo.readlines()

lista_num = []
for elem in lista:
    for numero in elem.split(','):
        lista_num.append(int(numero))

lista_num.sort()

print(f"\nLista ordenada: {lista_num}\n")#Usar más seguido "\n" de esta forma 
print(f"El número más pequeño de la lista es el {lista_num[1]} y el más grande es el {lista_num[-1]} ")

archivo.close



