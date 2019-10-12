cate = int(input("Ingresa tu categoría: "))
sue = float(input("Ingresa tu sueldo: "))
nsue = 0              #Segunda forma de "Default" en una seleción múltiple (Reducida)
if cate == 1: 
	nsue = sue * 1.15
elif cate == 2:
	nsue = sue * 1.10
elif cate == 3:
	nsue = sue * 1.08
elif cate == 4:
	nsue = sue * 1.07
print(f"Tu nuevo sueldo es de {nsue} por pertenecer a la categoría {cate}")
print("Fin del programa")