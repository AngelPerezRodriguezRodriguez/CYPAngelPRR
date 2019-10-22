#Listas
lluvias_norte = [80,60,120,100,70,150,100,47,95,70,100,130] #Datos de la página 152

for indice in range(0,12,1):
    print(f"mes {indice + 1} en región norte es igual a:{lluvias_norte[indice]}")

print(f"El promedio del mes de mayo es de:{lluvias_norte[4]}")
print(f"Los promedio entre los meses de enero a junio son de:{lluvias_norte[:5:]}")


#Ejemplo 4_01.py

sueldos = []
suma = 0 
for indice in range (7):
    sueldos.append(int(input("sueldo: ")))  #Conceptos en los videos de la plataforma   

print(sueldos)

for indice in range(7):
    suma += sueldos [indice]
    
promedio = suma / 7
print(f"El promedio de sueldos es:{promedio}")

cont = 0
for indice in range(7):
    if sueldos[indice] > promedio:
        cont += 1
        print(f"Arriba:{sueldos[indice]}")
    




