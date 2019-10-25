a = int(input("Ingresa un número: "))
if a == 0:
	print(f"{a} es un número nulo")
elif (-1) ** a > 0:
	print(f"{a} es un número par")
else:
	print(f"{a} es un número impar")