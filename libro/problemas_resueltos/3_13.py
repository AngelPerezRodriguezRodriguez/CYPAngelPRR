#REVISAR EL PROBLEMA!!!
arsu = 0
arno = 0
mersu = 50000
mes = 0               #Variable agregada en clase que no está en el libro
arce = 0
for i in range (1,13,1):
    print (f"Mes {1}")
    rno = int(input("Ingresa el promedio mensual de lluvias Región Norte: "))
    rce = int(input("Ingresa el promedio mensual de lluvias Región Centro: "))
    rsu = int(input("Ingresa el promedio mensual de lluvias Región Sur: "))

    arno = arno + rno  #arno += rno
    arce = arce + rce
    arsu = arsu + rsu

    if resu < mersu:
        mersu = rsu    
        mes = i         #hasta aquí termina el primer for

prorce = arce / 12
print(f"Promedio de la Región Centro:{proce}")
print(f"Mes con menor lluvia en Región Sur:{mes}")
print(f"Regsitro del mes con menor lliva es:{mersu}")

#Hasta este momento se han resulto los incisos a y b

if arno > arce:
    if arno > arsu:
        print("La región con mayor lluvia es la Región Norte")
    else:
        print("La región con mayor lluvia es la Región Sur")
elif arce > arsu:
    print("La región con mayor lluvia es la Región Centro")
else:
    print("La región con mayor lluvia es la Región Sur")

#Se resuelve el inciso c

    
    
    
