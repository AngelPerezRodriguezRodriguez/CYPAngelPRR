clave = int(input("Ingresa la clave de tu llamada: "))
numin = int(input("Ingresa los minutos que tardó tu llamada: "))
if clave == 12: 
	cost = numin * 2
elif clave == 15:
	cost = numin * 2.2
elif clave == 18:
	cost = numin * 4.5
elif clave == 19:
	cost = numin * 3.5
elif clave == 23 or 25:                              #En este caso sí es válida la abreviación de: clave == 23 or clave == 25
	cost = numin * 6
elif clave == 29:
	cost = numin * 5
else: 
	cost = 0
print(f"El costo total de tu llamada es de {cost}$")