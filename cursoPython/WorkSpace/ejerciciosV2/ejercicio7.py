# escribir una funcion que indique cuantas vocales tiene
# una palabra
palabra="chuleta"
vocales=0
for x in palabra:
    vocales+=1 if x=='a'or x=='e'or x=='i' or x=='o'or x=='u' else 0

print(vocales)