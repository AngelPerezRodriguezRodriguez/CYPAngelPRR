a = int(input("Ingresa el primer número entero: "))
b = int(input("Ingresa el segundo número entero: "))
c = int(input("Ingresa el tercer número entero: "))
if a > b: 
	if a > c:
		if b > c: 
			print(f"{a}, {b} y {c}")
		else: 
			print(f"{a}, {c} y {b}")
	else: 
		print(f"{c}, {a} y {b}")
elif b > c:
	if a > c:
		print(f"{b}, {a} y {c}")
	else:
		print(f"{b}, {c} y {a}")
else: 
	print(f"{c}, {b} y {a}")
print("Fin del programa")