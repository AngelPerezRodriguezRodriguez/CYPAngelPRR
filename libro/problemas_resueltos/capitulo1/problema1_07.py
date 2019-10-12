l1 = float(input("Ingresa el primer lado del triángulo: "))
l2 = float(input("Ingresa el segundo lado del triángulo: "))
l3 = float(input("Ingresa el tercer lado del triángulo: "))
s =  (l1 + l2 + l3) / 2
area = (s * (s - l1) * (s - l2) * (s - l3)) ** 0.5
print(f"Dados los tres lado del triángulo: {l1}, {l2} y {l3} U\nsu área es de {area} U al cuadrado")
