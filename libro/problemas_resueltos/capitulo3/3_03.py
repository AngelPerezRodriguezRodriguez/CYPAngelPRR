serie = 0
n = int(input("Ingresa un número entero: "))
band = "T"
for i in range(1,n+1,): 
    if band == "T":
        serie += 1 / i
        band = "F"
    else:
        serie -= 1 / i
        band = "T"
print(f"El resultado de la serie es de: {serie}")
