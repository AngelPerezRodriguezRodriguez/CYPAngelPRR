may = -100000
men = 100000
n = int(input("Número de enteros que vas a ingresar: "))
for i in range (1,n+1,):
    num = int(input("Ingresa un número entero: "))
    if num > may:
        may = num
    if num < men:
        men = num
print(f"El máximo valor es de: {may}")
print(f"El mínimo valor es de: {men}")
