nom = 0
sue = float(input("Hola empleado, ingresa tu sueldo: "))
while sue != (-1):
    if sue < 1000:
        nsue = sue * 1.15
    else:
        nsue = sue * 1.12
    nom += nsue
    print(f"Tu nuevo sueldo es de {nsue}$")
    print("Si eres el úlimo empleado, escribe: -1")
    sue = float(input("Hola empleado, ingresa tu sueldo: "))
print(f"La nómina total de la empresa es de: {nom}$")
