#identacion
#if 5>3:
   # print("5 es mayor a 3")
#if 3>5:
    #print("esto esto no  se  imprime")
#--------------------------------------------------------
  # lo siguente es una variable
from ctypes.wintypes import PINT
from itertools import count


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