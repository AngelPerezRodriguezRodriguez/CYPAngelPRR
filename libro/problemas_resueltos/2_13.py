mat = int(input("Ingresa tu matrícula: "))
carr = input("Ingresa la carrera en la que estás inscrito: ")
sem = int(input("Ingresa el semestre que estás cursando: "))
prom = float(input("Ingresa tu promedio actual: "))
if carr == "Economía":
	if sem >= 6 and prom >= 8.8:
		print(f"Felicidades, {mat}. Has sido aceptado en la carrera de {carr}")
elif carr == "Computación":
	if sem > 6 and prom > 8.5:
		print(f"Felicidades, {mat}. Has sido aceptado en la carrera de {carr}")
elif carr == "Contabilidad" or "Administración":
	if sem > 5 and prom > 8.5:
		print(f"Felicidades, {mat}. Has sido aceptado en la carrera de {carr}")