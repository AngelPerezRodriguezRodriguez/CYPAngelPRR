a = float(input("Ingresa el coeficiente cuadrático: "))
b = float(input("Ingresa el coeficiente lineal: "))
c = float(input("Ingresa el término independiente: "))
dis = b ** 2 - 4 * a * c
if dis >= 0:
	x1 = (-b + dis ** 0.5) / (2 * a)
	x2 = (-b - dis ** 0.5) / (2 * a)
	print(dis)
	print(f"Raices reales: ")
	print(f"x1 = {x1}")
	print(f"x2 = {x2}")
