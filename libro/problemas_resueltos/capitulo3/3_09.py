serie = 0
n = int(input("Ingres un número entero: "))

for i in range(1,n+1,):
    serie += i ** i
print(serie)
