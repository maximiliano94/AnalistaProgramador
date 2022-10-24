#--------------------------------
# verificador de datos
#--------------------------------
'''''
dato= input("ingrese dato  ")

lista=["hola","mundo","perro chuleta","chimuela"] 
 
if lista.count(dato) >0:
    print("el dato existe", dato)
else:
    print("el dato no  existe :(" , dato)
'''
#------------------------------------------
#         calculadora  solo suma
#------------------------------------------
''''
primero=input("ingrese primer numero ")
try:
    primero= int(primero)
except: 
    primero="perro chuleta"
segundo=input("ingrese segundo numero ")
try:
    segundo= int(segundo)
except: 
    segundo="perro chuleta"

if primero =="perro chuleta" or segundo=="perro chuleta":
    print("ingresaste mal un dato, prueba de nuevo  solo con numeros")
else:
    priemerNumero=int(primero)
    segundoNumero=int(segundo)
    resultado=int (priemerNumero +segundoNumero)
    print("el resultado de la suma es ", resultado)
'''
#---------------------------------------------------


primero = input('Ingrese primer número: ')

try:
    primero = int(primero)
except:
    primero = 'chanchito feliz'

if primero == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

segundo = input('Ingrese segundo número: ')

try:
    segundo = int(segundo)
except:
    segundo = 'chanchito feliz'

if segundo == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

simbolo=input("ingrese la operacion a realizar")
if simbolo=="+":
 print(primero+segundo)
elif simbolo=="-":
    print(primero-segundo)
elif simbolo=="*":
    print(primero*segundo)
elif simbolo=="/":
    print(primero/segundo)
else:
    print("simbolo ingresado no valido")    