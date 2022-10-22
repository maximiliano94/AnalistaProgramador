#identacion
#if 5>3:
   # print("5 es mayor a 3")
#if 3>5:
    #print("esto esto no  se  imprime")
#--------------------------------------------------------
  # lo siguente es una variable
from ctypes.wintypes import PINT
from itertools import count
from pickle import TRUE


x=5
y="perro chuleta"
#esto es como hacer una referencia  llamar una variable 
#print(x,y)

correo="perrochuleta@gmail.com"
#print(correo)
#FORMA DE VARIABLES
#mivar="chuleta"

#_usuario="chancho"
#FORMA DE CAMELCASE DE VARIABLE
#Va="JAMOM"
#print(mivar ,_usuario,Va)
#---------------------------------------------------------------------
#varibles Multiples
#otra forma una de tener mutiples variables en una sola linea 
_mi_var='perro chuleta'
MiVAR='PERRO CHANCHO CHULETA'
a,b,c='lala','lele','lili'
#print(_mi_var,MiVAR,a,b,c)
#otra manera  hayan muchas variables que tienga un  mismo valor
valor1=valor2=valor3='chancho feliz'
#print(valor1,valor2,valor3)

#----------------------------------------------------------------
#concatenacion de Strings
inicio='hola'
final='mundo'
#print(inicio + final)
#-----------------------------------------------------------------
#tipos de datos introduccion de la seccion String y numeros 
palabra='hola mundo con comillas simples' #String
fraces="hola mundo comilla dobles"
#print(palabra,fraces)
#-----------------------------------------------------
entero=20 # esto es un interger
conDecimales=20.5 # esto es un flotatante
complejo=1j #numeros complejos
#print(entero,conDecimales,complejo,palabra,fraces)
#----------------------------------------------------------
#lista
lista=['hola','perro','chuleta']
#metodos para trabajar con listas 
#para  agregar un elemento 
lista.append('goku')
#limpia la lista
#lista.clear()
#metodo para copiar una lista
lista2=lista.copy()

#otros mmetodos
#----------------------------------------
# metodos para contar una lista 
#print(lista,lista2.count(2))

#elimina un elemento de la lista
#lista2.remove('4')

#metodo para saber el largo de un array
#print(len(lista), len(lista2))
#--------------------------------------
#otra forma
largoLista=len(lista)
largoLista2=len(lista2)
#print(largoLista,largoLista2)
#-----------------------------------------
# las listas  los array  se componen de indices estos comienzan del 0 
#em adelante
# para acceder a un elemento de la lista 
#print(lista[2])
#--------------------------------------------------
        #ELIMINAR ELEMENTOS DE UNA LISTA
#-------------------------------------------------
#elimina el ultimo elemento de la lista
#lista.pop()
#lista.pop()
#elimina un elemento especifico del array/lista
#lista.remove('hola')
#lista.remove(4)
#print(lista)
#------------------------------------------------------
             #REVESE Y SORT DE LA LISTA
#------------------------------------------------------
#lista.reverse() #iniverte la lista
#lista.sort()# ingresa un elemento  en la parte del medio de la lista
#print(lista)
#--------------------------------------------------------------------
                       #Tuplas
#--------------------------------------------------------------------
# esto  es similar a una lista con la unca diferencias que estas
# no se pueden modificar
# esta se crea de la esta forma
tupla=("hola","perro","chuleta",4)
#metodos para las tuplas
#print(tupla.count("hola"))#muestra que numero  se elemento 
#print(tupla.index("perro"))
#devuelve el indice donde este se encuentra
#nose puede agregar un elemento 
#---------------------------------------------------
#como transformar una tupla en una lista?
#listaTuplas=list(tupla)
#listaTuplas.append("chimuela")
#print(listaTuplas)
#---------------------------------------------------------------
                       #Range
#---------------------------------------------------------------

#como declarar un rango en  pythom 
#rango=range(6) #aca señala  el  rango de donde inicia has
#print(rango)                       
#------------------------------------------------------------
                        # Diccionarios
#------------------------------------------------------------
# los diccionarios  son similares a las lista
# en lugar para acceder a los elementos mediante indice  
# sino  mediante cadena de String 
rango=range(6)
diccionario={
    'nombre del perro':'chimulo',
    'raza':'buldog ingles',
    'edad':3
}
#print(diccionario)
#print(diccionario['nombre del perro'])
#tambien se puede usar un metodo
#print(diccionario.get('nombre del perro'))

#para modificar un elemento del diccionario
diccionario['nombre del perro']='chuleta'
#print(diccionario)
#print(len(diccionario))#para saber le largo del diccionario
#----------------------------------------------
            #MAS SOBRE LOS DICCIONARIOS
#----------------------------------------------
#agregar un elemento al diccionario
diccionario['ronronea']='si'
#print(diccionario)
#agregar un elemento al diccionario
#diccionario.pop('ronronea')
#otra forma
#diccionario.popitem()
#del diccionario['ronronea']
#eliminar todo el diccionario
diccionario.clear()
#hacer una copia
#copiagato=diccionario.copy()
#copiagato=dict(diccionario)
#print(diccionario,copiagato)
#------------------------------------------
# DICCIONARIOS ANIDADOS Y CONSTRUCTORES
#------------------------------------------
perro ={
    
 #"GORDO":{
   #" nombre":"gordo",
    #"edad" :3
    #},
     #"CHULETA":{
       # "NOMBRE":"chuleta",
        #"Edad":10
   # }
}

gordo={
 "nombre":"Gordo San",
 "edad":3
}
chuleta={
    "nombre":"CHueleta",
    "edad":10

}
perros={
    "Gordo":gordo,
    "Chueleta":chuleta
}
#print(perros)
#otra forma de crear diccionario funcion dict
perritosLindos=dict(nombre="chuleta",edad=10)
#print(perritosLindos)
#---------------------------------------------
             #TIPO BOOLEANO
#---------------------------------------------
# estos solo puede tener dos valores de salido
# true= Verdadero O false = FALSO

estadoCivil=False
#if estadoCivil!=False:{
    #print('estas casado')
#}
#else:{
    #print("estas soltero")

#}
# otro ejemplo
#no puedes colocar una palabra RESERVADA en MAYUSCULAS
verdadero=True
falso=False
#print(verdadero,falso)
#----------------------------------------------------
             #INTRODUCCION AL CONTROL DE FLUJO
#---------------------------------------------------
#EN ESTEMODULO VERE LAS DISTINTAS FORMAS DE DE DESICIONES
#Y COMO SE IMPLEMENTAN
#--------------------------------------------------------
 




