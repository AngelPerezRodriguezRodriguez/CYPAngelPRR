#cell_db.py

def leer_datos(path):
    file = open(path, 'rt')
    lista_final = []        #2
    dic_cel = {}            #2
    datos = file.readlines()
    print(datos)
    print("")
    for ren in range(len(datos)):
        datos[ren] = datos[ren].strip().split(',')
    print(datos)
    #1Hasta aquí hemos eliminado los espacios "\n" con strip del prin. y final. Y con split..."separa"

    print("")                                        #2 hacia abajo
    for ren in range(1, len(datos), 1):
        dic_cel = {}
        for col in range(len(datos[ren])):
            dic_cel[datos[0][col].strip()] = datos[ren][col] #Se agrega el .strip para quitar los espacios de la columna col.
        lista_final.append(dic_cel)
    print(lista_final)
    return lista_final

def salida_formato(celular):                         #3 hacia abajo
    print("")
    print(f"Celular marca:{celular['marca']}")
    print(f"\tModelo:{celular['modelo']}")
    print(f"\tAlmacenamiento:{celular['almacenamiento']}")
    print(f"\tVelocidad:{celular['velocidad']}")
    print(f"\tRam:{celular['ram']}")
    print(f"\tColor:{celular['color']}")

def main():                                          #2 hacia abajo
    archivo = "celulares.txt"
    bd = leer_datos(archivo)
    print("")
    print(f"DB = {bd}")
    salida_formato(bd[1])                            #3

main()
