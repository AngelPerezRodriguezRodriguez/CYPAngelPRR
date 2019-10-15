otra = True        #Agrega lo que implica la variable "otra"
suma = 0
cont = 0
while otra == True:
    cal = float(input("Ingresa la calificación: "))
    cont += 1
    suma += cal
    otra = bool(int(input("¿Quieres agregar otra calificación?(0 = No y 1 = Si): ")))
print(f"La suma total de las calificaciones es de: {suma}")
prom = suma / cont
print(f"El promedio es de: {prom}")
