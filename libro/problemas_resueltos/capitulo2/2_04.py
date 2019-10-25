mat = int(input("Ingresa tu número de matrícula: "))
cal1 = float(input("Ingresa tu calificación de química: "))
cal2 = float(input("Ingresa tu calificación de español: "))
cal3 = float(input("Ingresa tu calificación de matemáticas: "))
cal4 = float(input("Ingresa tu calificación de historia: "))
cal5 = float(input("ingresa tu calificación de geografía: "))
prom = (cal1 + cal2 + cal3 + cal4 + cal5) / 5
if prom >= 6:
	print(f"Hola, {mat}. Tu promedio es de {prom}, estás aprobado")
else:
	print(f"Hola, {mat}. Tu promedio es de {prom}, estás reprobado")
