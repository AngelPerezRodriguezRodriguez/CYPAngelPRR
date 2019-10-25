sumotr = 0
sumpos = 0
cuepos = 0
n = int(input("Número de enteros que vas a ingresar: "))
for i in range(1,n+1,):
    num = int(input("Ingresa otro número entero: "))
    if num > 0:
        sumpos += num
        cuepos += 1
    else:
        sumotr += num
progen = (sumpos + sumotr) / n
propos = sumpos / cuepos
print(f"El número total de positivos es de: {cuepos}")
print(f"El promedio de los números positivos es de: {propos}")
print(f"El promedio general es de: {progen}")
