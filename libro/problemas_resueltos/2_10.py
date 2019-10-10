a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))
if a > b:
    if a > c:
        print(f"{a} es el número más grande")
    elif a == c:
        print(f"{a} y {c} son los mayores")
    else:
        print(f"{c} es el mayor")
elif a == b:
    if a > c:
        print(f"{a} y {b} son los mayores")
    elif a == c:
        print(f"{a}, {b} y {c} son iguales")
    else:
        print(f"{c} es el mayor")
elif b > c:
    print(f"{b} es el mayor")
elif b == c:
    print(f"{b} y {c} son los mayores")
else:
    print(f"{c} es mayor")
