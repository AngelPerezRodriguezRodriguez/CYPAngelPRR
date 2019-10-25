prebas = float(input("Ingresa el precio del artículo: "))
if prebas > 500:
	imp = 20 * 0.30 + (prebas - 40) * 0.5
elif prebas > 40:
	imp = 20 * 0.30 + (prebas - 40) * 0.4
elif prebas > 20:
	imp = (prebas - 20) * 0.30
else:
	imp = 0
pretot = prebas + imp
print(f"A partir del precio base del producto: {prebas}$. El costo total del producto es de {pretot}$")