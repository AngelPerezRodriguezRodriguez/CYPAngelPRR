sue = float(input("Ingresa tu sueldo actual: "))
cate = int(input("Ingresa la categoría a la que perteneces: "))
he = int(input("Ingresa el número de horas extras que trabajaste: "))
if cate == 1:
	phe = 30
elif cate == 2:
	phe = 38
elif cate == 3:
	phe = 50
elif cate == 4:
	phe = 70
else:
	phe = 0 
if he > 30: 
	nsue = sue + 30 * phe
else:
	nsue = sue + he * phe
print(f"De acuerdo con tu suelto, categoría y horas extra: {sue}, {cate} y {he} respectivamente.")
print(f"Tu sueldo actual es de {nsue}$") 