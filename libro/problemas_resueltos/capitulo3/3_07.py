med = 0
chi = 0
gra = 0
n = int(input("Número de enteros que vas a ingresar: "))
for i in range (1, n+1,):
    v = float(input("Ingresa el costo de tu venta: "))
    if v <= 200:
        chi += 1
    elif v < 400:
        med += 1
    else:
        gra += 1
print(f"Número de ventas menores a 200$: {chi}")
print(f"Número de ventas menores a 400$: {med}")
print(f"Número de ventas mayores a 400$: {gra}")
