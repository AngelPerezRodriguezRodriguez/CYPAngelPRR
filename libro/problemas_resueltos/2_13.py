mat = int(input("Ingresa tu matrícula: "))
carr = input("Ingresa la carrera en la que estás inscrito: ")
sem = int(input("Ingresa el semestre que estás cursando: "))
prom = float(input("Ingresa tu promedio actual: "))
if carr == "Economía":
	if sem >= 6 and prom >= 8.8:
		print(f"Felicidades {mat}, de la carrera de {carr}, has sido aceptado")
elif carr == "Computación":
	if sem > 6 and prom > 8.5:
		print(f"Felicidades {mat}, de la carrera de {carr}, has sido aceptado")
elif carr == "Contabilidad" or "Administración":
	if sem > 5 and prom > 8.5:
		print(f"Felicidades {mat}, de la carrera de {carr}, has sido aceptado")