#print tiene cuatro formas de uso
"""
1.- Con comas
2.- Con signo '+'
3.- Con la función format()
4.- Con una variante de la función format()
"""
#1.- Con comas, concatenar agregando un espacio y haciendo casting de tipo
edad = 10
nombre = "Juan"
estatura = 1.67
print(edad , estatura , nombre)

#2.- Con '+' hace lo mismo pero no realiza el casting automático y no agreda espacio,
#es decir, hace una concatenación tal cual 
print(str(edad) + str(estatura) + nombre)

#3.- función format()
print("Nombre:{} Edad:{}".format(nombre, edad))
print("Nombre:{1} Edad:{0}".format(nombre, edad))
print("Nombre:{} Edad:{}".format(nombre, edad, estatura))

#4.- Con una variante en la función format () simplificada
print(f"Nombre:\"{nombre}\" \nEdad:\t{edad}")

#\n siguiente párrafo
#\t tabular
#\" \"

#print y el argumento end
print("Sólo hay diez tipos de personas, las que saben binario y las que no", end = "\n")
print("Otra línea")

print("Sólo hay diez tipos de personas, las que saben binario y las que no", end = " ")
print("Otra línea")


