#realizar una  aplicacion que reciba una cantatidad infinita de numeros
#hasta decir basta, luego devuelva la suma de los numeros ingresados

lista=[]
print("ingrese numeros y para salir escriba basta")
while True:
    valor=input("ingrese un numero")
    if valor=="basta":
        break
    else:
        try:
          valor=int(valor)
          lista.append(valor)
        except:
             print("dato invalido")
             
             
             exit() 

    resultado=0
    for x in lista:
        resultado+=x
       
       
        print(resultado)