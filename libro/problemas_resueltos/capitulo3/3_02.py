band = "T"
sumser = 0
i = 2
while i <= 1800:
    sumser += 1
    print(i)
    if band == "T":
        band = "F"
        i += 2
    else:
        band = "T"
        i += 3
print(f"El número de términos es igual a: {sumser}")
    
    
