def sumar (x, y):
    z = x + y
    return z

def restar (x, y):
    return x - y   #Una forma más abreviada de hacerlo

def mi_print (texto):
    print(f"Este es mi print: {texto}")
    #Al no tener un 'return' está regresando un vacío

def multiplica (valor, veces):
    if veces == None:
        print("Debes de envíar el segundo argumento de la fución")
    else:
        print(valor * veces)

def commanda (mesa, comensal, entrada, medio, fuerte, postre = "Gela de limón"):
    print(f"Mesa: {mesa} Comensal: {comensal}")
    print(f"\t Entrada: {entrada}")
    print(f"\t Segundo tiempo: {medio}")
    print(f"\t Plato fuerte: {fuerte}")
    print(f"\t Postre: {postre}")

def imprime_argumentos (*argumentos):
    print('--->', argumentos, '<---')
    
    #for ele in argumentos:                 Nos sirve para colcar los elementos en forma de lista
        #print(ele)

    #for index in range(len(argumentos)):   Otra forma de colocar los elementos en forma de lista           
        #print(argumentos[index])

def commanda2(**comida):
    print(comida)
    
    #llaves = comida.keys()
    #print(llaves)

    #for elem in llaves:
        #print(elem, "-->", comida[elem])
    
    #\t sirve para agregar la sangría al print
    #El argumento son las variables internas de una función
    #Los parámetros son los valores que adquieren las varialbes de una función
    
def main ():
    a = 10
    b = 5
    
    c = sumar(a, b)
    print(f"La suma de {a} y {b} es {c}")
    
    c = restar(a, b)
    print(f"La resta de {a} y {b} es {c}")
    
    mi_print("¡Hola!")
    
    multiplica(10, 3)
    multiplica(10, None)
    multiplica('Hola', 3)

    commanda(2, 1, "Ensalada", "Sopa de rana", "Filete", "Flan")
    commanda("Ensalada", "Sopa de rana", "Filete", "Flan", 2, 1)
    #El paámetro tiene que ir en orden del argumento
    commanda(entrada = "Ensalada", medio = "Sopa de rana", fuerte = "Filete", postre = "Flan", mesa = 2, comensal = 1)
    #Pero podemos definirlos
    commanda(entrada = "Ensalada", medio = "Sopa de rana", fuerte = "Filete", mesa = 2, comensal = 1)

    imprime_argumentos('Hola', True, 3.1416, 1000, {'id' : 'sc01', 'nombre' : 'Angel'})
    imprime_argumentos()

    commanda2(entrada = "Ensalada", medio = "Sopa de rana", fuerte = "Filete", mesa = 2, comensal = 1, postre = "Strudel de manzana", bebida = "Coca light")

    
    
if __name__ == '__main__': #Se mantiene como una pregunta: 
        main()             #¿se mandó a ejecutar(interpretar) este archivo?


#Una forma menos formal pero funciona
print("------------")
def sumar (x, y):
    z = x + y
    return z

def restar (x, y):
    return x - y   

a = 10
b = 5
c = sumar(a, b)
print(f"La suma de {a} y {b} es {c}")
c = restar(a, b)
print(f"La resta de {a} y {b} es {c}")
    





