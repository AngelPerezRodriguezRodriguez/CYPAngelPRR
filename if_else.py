edad =int(input("Dame tu edad: "))
INE = bool(int(input("¿Tienes INE?\nNo....0\nSí....1\n")))
if edad >= 18 and INE == True:
    print("Es mayor de edad")
    print("Puede entrar al bar")
else:
    print("Eres menor de edad")
    print("Puedes ir a jugar LoL")
print("Fin del programa")
