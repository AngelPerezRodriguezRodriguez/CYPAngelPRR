edad = int(input("Dame tu edad: "))
INE = bool(int(input("Tienes INE:\nNo....0\nSí....1\n")))
if edad >= 18 and INE == True:
    print("Es mayor de edad")
    print("Puedes entrar al bar")
print("Fin del programa")

