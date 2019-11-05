#Tuplas
#Se declaran con "(" y ")"
#Son inmutables y organizan datos igual que las listas

datos_db = ('132.248.173.88','root','12345678')
print(datos_db[1])

datos_db = ('132.248.173.88','admin','12345678')
print(datos_db[1])

#dir(tuple) (Con esto vamos a ver las ¿funciones? disponibles para la opción "tuple"

print(datos_db.index('admin'))
print(datos_db.count('admin'))
