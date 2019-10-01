sue = float(input("Ingres tu sueldo mensual en pesos: "))
if sue < 1000:
	aum = (sue * 15) / 100
	nsue = sue + aum
	print("Dado que consideramos tu sueldo es insufieciente")
	print("recibirás un aumento del 15%  respecto a tu sueldo actual.")
	print(f"Por lo tanto tu nuevo sueldo mensual es de {nsue}$")
else: 
	aum = (sue * 12) / 100
	nsue = sue + aum
	print("Dado que consideramos tu sueldo es suficiente")
	print("recibirás un aumento del 12%  respecto a tu sueldo actual.")
	print(f"Por lo tanto tu nuevo sueldo mensual es de {nsue}$")