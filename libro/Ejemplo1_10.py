print("Calculadora del área y perímetro de un rectángulo")
print("Por favor ingresa los siguientes datos:")
base = int(input("Base del rectángulo: "))
altu = int(input("Altura del rectángulo: "))
area = base * altu 
peri = 2 * (base + altu)
print(f"El área de tu rectángulo es de {area} y el perímetro de {peri}")