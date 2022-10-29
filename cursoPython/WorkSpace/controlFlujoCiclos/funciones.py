#----------------------------------------------
#                 funciones 
#----------------------------------------------
# son bloques de codigo los cuales no se ejecutaran
#a menos que nostros llamemos a estas

#Para que se usa ?
#para reutilizar codigo y no volver invertar la misma solucion

#como declaramos la funcion? con la palabra def
''''
def mifuncion():
     print("mi primera funcion")

#mifuncion()
'''
# ventajas de las funciones
# podemos ocupar argumentos
#que es ?
#son  variables que se pueden usar dentro de las funciones 
# para que nuestras funciones   sean mas flexibles
# al momento de usarlas esto segun nuetra necesidad 

#para definir los argumentos dentro del parentesis
##def imprimeDato(nombre,apellido ):#-> esto es un argumento
    #print("mi nombre completo es" ,nombre,apellido  )

#imprimeDato("Maximiliano","Jara")#-> esto es un parametro
#otra forma
''''
def imprimeDato(*nombre):
    print("mi nombre completo es : ",nombre)
imprimeDato("Maximiliano","Jara","lala")#->este pasaria como una tupla
'''
# forma de acceder a un elemento
'''
def imprimeDato(*nombre):
    print("mi nombre completo es : ",nombre[0])
imprimeDato("Maximiliano","Jara","lala")
'''
'''
def imprimeDato(*nombre):
    print("mi nombre completo es : ",nombre[1])
#imprimeDato("Maximiliano","Jara","lala")
'''
 # no puedes implementar una funcion en dado que no  imprimira la
# funcion  que ya miplementaste
#otra forma de recorrer los elementos

def nombrecompleto(apellido,nombre):
    print(nombre,apellido)
#nombrecompleto(nombre="perro",apellido="chuleta")

#agrupas los argumentos como si fuera un diccionario
'''
def nombrecompleto2(**kwoargs):#-> con kwoargs  puedes acceder lo 
    #elementos de  diccionario
    print(kwoargs["nombre"],kwoargs["apellido"])

nombrecompleto2(nombre="maximiliano",apellido="Jara")
'''
#---------------------------------------
#          Mas Funciones
#--------------------------------------
'''''
def mifuncion2(argumento="perro chuleta"):
    print(argumento)
'''''

#mifuncion2("superman")
#mifuncion2()
def mifuncionLista(lista):
 for el in lista:
     print(el)
#mifuncionLista(["lala","lele"])
'''
def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '	
    return i # siempre retornar un valor se retotn el indice sino no 
    #retorna nada
#nombres = concatenaNombres(['Chanchito', 'Feliz'])
#print(nombres)
'''
#------------------------------------------------
#                 Recursividad
# ----------------------------------------------
 
def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(6)
#la recusividad sive para trabajar con colecciones de datos
# reintentar  la conexion a uma base de datos  en caso qeu esta falle
# o cuando queremos hacer un procesaniento en bach

