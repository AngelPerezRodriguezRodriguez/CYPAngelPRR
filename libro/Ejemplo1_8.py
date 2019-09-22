mat = input("Ingresa tu número de matrícula: ")
cal1 = int(input("Ingresa tu calificación de química: "))
cal2 = int(input("Ingresa tu calificación de español: "))
cal3 = int(input("Ingresa tu calificación de matemáticas: "))
cal4 = int(input("Ingresa tu calificación de historia: "))
cal5 = int(input("ingresa tu calificación de geografía: "))
prom = (cal1 + cal2 + cal3 + cal4 + cal5) / 5
print(f"Hola, {mat}. Tu promedio final es de {prom}.")