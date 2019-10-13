compra = float(input("Ingresa el monto total de tu compra: "))
if compra < 500:
	pagar = compra
elif compra <= 1000:
	pagar = compra - (compra * 0.05)
elif compra <= 7000:
	pagar = compra - (compra * 0.11)
elif compra <= 15000:
	pagar = compra - (compra * 0.18)
else:
	pagar = compra - (compra * 0.25)
print(f"De acuerdo con tu compra tu nuevo pago correspondiente será de {pagar}$")