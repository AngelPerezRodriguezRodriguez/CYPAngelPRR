radio = float(input("Ingresa el radio del cilindro: "))
altu = float(input("Ingresa la altura del cilindro: "))
volu = 3.141592 * (radio ** 2) * altu 
area = 2 * 3.141592 * radio * altu
print(f"Dado un cilindro con {radio} U de radio y {altu} U de altura, su volumen es de {volu} U al cubo,\ny su área es de {area} U al cuadrado")