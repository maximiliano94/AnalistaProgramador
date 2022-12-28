#leer archivos 
'''
para gestionar archivos
1-se crea un  archivo 
2-se le escribe unos carcactetes

3- se crea una variable con la funcion open
'''
#c= open("chuleta.txt",'w')
#print(c.read())# lee lieneas
''''
print(c.readline())#lee 1 linea a la vez
print(c.readline())
print(c.readline())
print(c.readline())
'''
# es impresion por ciclco
'''
for x in c:{
    print(x)
}
c.close()
'''
#escribir archivo 
'''''
c=open('chuleta.txt','w')
c.write('\nagregando linea')
c.close()
x=open('chuleta.txt')
print(x.read())
'''
# eliminar archivos 
import os
# validacion para elminar archivo 
if os.path.exists('chuleta.txt'):
   os.remove('chuleta.txt')
else:
  print('el archivo no existe')

  #eliminar carpeta
  os.rmdir('micarpeta')







