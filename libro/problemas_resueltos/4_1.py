n = int(input("Ingrese el número de elementos del arreglo: "))
vec = []
if 1 <= n <= 500:
    for i in range (0,n):
        vec.append(int(input("Ingresa valor: ")))
    vec.sort()#No está en el libro pero lo podemos agregar para ordenarlos
    print("Lista de números sin repeticiones")

    i = 0
    while i <= n - 1:
        print(vec[i])
        repet = vec[i]
        while i <= n-1 and repet == vec[i]:
            i += 1

else:
    print("El número de elementos del arreglo es incorrecto")
