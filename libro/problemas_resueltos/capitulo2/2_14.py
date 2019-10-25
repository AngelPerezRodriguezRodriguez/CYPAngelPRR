tipoenf = int(input("Ingresa tu tipo de enfermedad: "))
edad = int(input("Ingresa tu edad: "))
dias = int(input("Ingresa el número de días que llevas hospitalizado: "))
if tipoenf == 1:
	costot = dias * 25
elif tipoenf == 2:
	costot = dias * 16
elif tipoenf == 3:
	costot = dias * 20
elif tipoenf == 4:
	costot = dias * 32
if 14 <= edad <= 22:
	costot = costot * 1.10
print(f"El costo total por tu tipo de enfermedad, edad y días hospitalizado es de {costot}$")