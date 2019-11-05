#Diccionarios {'llave':'valor'}
alumno = {'num_cuenta':'2016749','nombre':'José','paterno':'Pérez'}
print(alumno['nombre'])

alumno = {'num_cuenta':'2016749',
          'nombre':('Angel','Pérez','Rodríguez'),
          #Se pone "()" porque queremos que el valor sea inmutable
          'semestre':1,#int
          'promedio':0.0,#float
          'materias':['CyP','Algebra','Cálculo','Geometría','IntroICO'],#Lista de string's
          'regular':True,#bool
          'lagrimas_por_examen':5,#int
          'direccion':{
              #Dirección en otra dirección
              'calle':'Rancho Secho',
              'colonia':'Impulsora Popular Avícola',
              'numero':1000,
              'cp':17570,
              'del_mun':'Nezahualcoyotl',
              'estado':{
                  'id':15,
                  'nombre':'Estado de México',
                  'corto':'EdoMex',
                       }
                      }
          }
print(alumno['nombre'])
print(alumno)
print(alumno['nombre'][1])
print(alumno['direccion']['cp'])
print(alumno['direccion']['estado']['corto'])
print(alumno['materias'][3::])
#Investigar qué relación tiene con Json

#Función para seleccionar un elemento y escribirlo en mayusculas 
print(alumno['materias'][1].upper())


print(alumno['direccion']['estado']['nombre'][10::].upper())

print("---------")
#Otra forma de hacer los diccionarios
#Revisar el nuevo documento del profesor

mi_lista = [['a','b'],['c',10],['d',True]]
diccionario = dict(mi_lista)
print(diccionario)


print("---------")
#SON MUTABLES

alumno['lagrimas_por_examen'] = 10
print(alumno)

#Estamos agregadon una nueva llave
alumno['cursa_ingles'] = True
print(alumno)


#Nos sirve para ver las ¿funciones? para diccionario
dir(dict)

print("------------------------")
#Función keys()

llaves = alumno.keys()
print(llaves)

for llave in llaves:
    print("---------")
    print(llave)
    print("...")
    print(alumno[llave])

print("------------------------")
#Función values
for val in alumno.values():
    print("---------")
    print(val)

print("------------------------")
#Función items()
for elem in alumno.items():
    print("---------")
    print(elem)
