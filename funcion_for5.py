for v in range(3,31,3):
    print(f"Hola, {v}")

for v in range(20,-1,-1):
    print(f"Hola, {v}")
print('------------------')

num = int(input("Dame un número: "))
if num > 0:
    for x in range(0,num,1):
        print("+", end="")
else:
    print("No me has dado un número mayor que cero")
