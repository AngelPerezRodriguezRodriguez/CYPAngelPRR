archivo = open ("numeros.txt","rt")
lista = archivo.readlines()
print(lista)

print("")
lista_num = []
for elem in lista:
    print(elem.strip(),end='')
    for numero in elem.split(','):
        lista_num.append(int(numero))

lista_num.sort()

print("")
print(f"\nLista ordenada: {lista_num}\n")#Usar más seguido "\n" de esta forma 
print(f"El número más pequeño de la lista es el {lista_num[1]} y el más grande es el {lista_num[-1]} ")

archivo.close
