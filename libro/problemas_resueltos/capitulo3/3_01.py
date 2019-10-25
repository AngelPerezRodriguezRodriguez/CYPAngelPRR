sumpar = 0
sumimp = 0
cuepar = 0
for i in range(1,271,):
    num = int(input("Ingresa un número entero: "))
    if num != 0:
        if (-1) ** num > 0:
            sumpar += num
            cuepar += 1
        else:
            sumimp += num
propar = sumpar / cuepar
print(f"El promedio de los números pares es de: {propar},")
print(f"y la suma de los números impares es de: {sumimp}")
