cuecer = 0
num = int(input("Dame un número entero positivo: "))
for i in range(0,num,1):
    num = int(input("Ingresa un número entero: "))
    if num == 0:
        cuecer += 1
print(f"La cantidad de ceros capturados fue de: {cuecer}")
