a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))
if a < b:
	if b < c:
		print("Los números están en orden creciente")
	else:
		print("Los números no están en orden creciente")
else:
	print("Los números no están en orden creciente")