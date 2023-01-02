#escribir una funcion que encuetre el elemento menor de una lista
lista=[1,2,3,4,5,55,-24,-13]
menor='inicio'

for x in lista:
    if menor=='inicio':
        menor=x
    else:
        menor=x if x<menor else menor

print('menor',menor)