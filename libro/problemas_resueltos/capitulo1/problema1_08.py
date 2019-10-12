x1 = float(input("Ingresa la coordenada x del primer punto: "))
y1 = float(input("Ingresa la coordenada y del primer punto: "))
x2 = float(input("Ingresa la coordenada x del segundo punto: "))
y2 = float(input("Ingresa la coordenada y del segundo punto: "))
dis = ((x1 - x2) ** 2 + (y1 - y2) **2) ** 0.5
print(f"La distancia entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es de {dis} U")
