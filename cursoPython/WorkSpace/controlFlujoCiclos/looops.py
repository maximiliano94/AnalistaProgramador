#-----------------------------------
#           ciclo while
#-----------------------------------
i=0
'''
while i<5:
    print(i)
    i=i+1
    #o i+=1
'''
#---------------------------------------
#            while continue break
#---------------------------------------
'''''
while i<5:
 # break
 if i == 3:
  continue
i=i+1
print(i)
'''
#---------------------------------
#            ciclo for
#---------------------------------
''''
usuarios=["pedro","juan","felipe","roberto"]
for usuario in usuarios:
    print(usuario)
'''
''''
usuario='perro culeta'
for c in usuario:
    print(c)
'''
''''
usuarios=["pedro","juan","felipe","roberto"]
for usuario in usuarios:
    if usuario=="felipe":
        #break
        continue
    print(usuario)
'''
'''
for x in range(3,30,6):
    print(x)
else:
    print("hemos terminado")    
'''
usuarios=["pedro","juan","felipe","roberto"]
edades=[24,25,28,30]
for ususario in usuarios:
    for edad in edades:
       print(ususario,edad) 