#----------------------------------------------
#           importar modulos
#----------------------------------------------
'''''
import Modulos

print(Modulos.mascotas)
Modulos.saludo("Maxi")
'''
#-----------------------------------------------
#              renombrar modulos
#-----------------------------------------------
'''
import Modulos as xs

print(xs.mascotas)
xs.saludo("Maxi")
'''
#------------------------------------------------
#   seleccionar lo importado 
#-----------------------------------------------
'''''
from Modulos import saludo
saludo("Maxi")
'''''
#-----------------------------------------------
#                 CamelCase
#----------------------------------------------
import modulos as xs
from camelcase import CamelCase

print(xs.mascotas)
xs.saludo('Nicolas')

c = CamelCase()
s = 'esta oración necesita CamelCase!'

camelcased = c.hump(s)
print(camelcased)
# para instalar modulos pip intall desintalar pip unintaller
