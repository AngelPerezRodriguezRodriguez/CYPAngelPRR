num = int(input("Ingresa una opción del uno al cuatro: "))
v = int(input("Ingresa otro número entero positivo: "))
if num == 1:
	val = 100 * v
elif num == 2:
	val = 100 ** v
elif num == 3: 
	val = 100 / v
else:                           #Primera forma de colocar la opción
	val = 0                     #"Default" en una selección múltiple
print(f"El resultado es {val}")
print("Fin del programa")
