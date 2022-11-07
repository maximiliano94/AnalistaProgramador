#-----------------------------
#   CLASES 
#-----------------------------
#como crear una clase
'''''
class Usuario:
 def __init__(self, nombre, apellido):# ESTE METODO SE OCUPA PARA QUE LOS
        self.nombre = nombre          # PARA  LOS DATOS NO SE DUPLIQUE
        self.apellido = apellido


usuario = Usuario('Felipe', 'Feliz') # ESTO UNA INSTANCIA DE UN OBJETO
usuario2 = Usuario('tomas', 'perez')
print(usuario.nombre ,usuario.apellido,usuario2.nombre,usuario2.apellido)
'''
#---------------------------------
#      Metodos
#---------------------------------
'''
class Usuario:
 def __init__(self, nombre, apellido):# ESTE METODO SE OCUPA PARA QUE LOS
        self.nombre = nombre          # PARA  LOS DATOS NO SE DUPLIQUE
        self.apellido = apellido

 def saludo(self): #-> esto es un metodo
# que se hace referencia asi mismo    
        print("hola mi nombre es ",self.nombre,self.apellido) #-> esto es un parametro

usuario = Usuario('Felipe', 'Feliz') # ESTO UNA INSTANCIA DE UN OBJETO
usuario2 = Usuario('tomas', 'perez')
#print(usuario.nombre ,usuario.apellido,usuario2.nombre,usuario2.apellido)

#para llamar un metodo 
#usuario.saludo()
#usuario2.saludo()
'''
#--------------------------------
#  self elimina propidades  y metodos
#-------------------------------
'''
class Usuario:
 def __init__(self, nombre, apellido):# ESTE METODO SE OCUPA PARA QUE LOS
        self.nombre = nombre          # PARA  LOS DATOS NO SE DUPLIQUE
        self.apellido = apellido

 def saludo(self): #-> esto es un metodo
# que se hace referencia asi mismo    
        print("hola mi nombre es ",self.nombre,self.apellido) #-> esto es un parametro

usuario = Usuario('Felipe', 'Feliz') # ESTO UNA INSTANCIA DE UN OBJETO
#print(usuario.nombre ,usuario.apellido,usuario2.nombre,usuario2.apellido)

#para llamar un metodo 
#usuario.saludo()
#tambien se puede cambiar la  propiedad de metodo
usuario.nombre="hola pepe"
usuario.saludo()
#elimina instancia
del usuario.nombre
#usuario.saludo()
#eliminar objeto
del usuario
print(usuario)
'''
#--------------------------------
#             herencia
#--------------------------------
'''
class Usuario:
 def __init__(self, nombre, apellido):# ESTE METODO SE OCUPA PARA QUE LOS
        self.nombre = nombre          # PARA  LOS DATOS NO SE DUPLIQUE
        self.apellido = apellido

 def saludo(self): #-> esto es un metodo
# que se hace referencia asi mismo    
        print("hola mi nombre es ",self.nombre,self.apellido) #-> esto es un parametro

usuario = Usuario('Felipe', 'Feliz') # ESTO UNA INSTANCIA DE UN OBJETO
#print(usuario.nombre ,usuario.apellido,usuario2.nombre,usuario2.apellido)

class Admin(Usuario):
        def  SuperSaludo(self):
                print("hola me llamo",self.nombre,"y soy adminstrador")



#para llamar un metodo 
#usuario.saludo()
#tambien se puede cambiar la  propiedad de metodo
usuario.nombre="hola pepe"
usuario.saludo()

admin=Admin("super","feliz")
admin.saludo
admin.SuperSaludo()
#no se peuede llamar los metodos desde las clases hijas
#usuario.SuperSaludo()
'''
#------------------------------------
#  ejercicio 
#------------------------------------
'''''
class Usuario:
 def __init__(self, nombre, apellido):# ESTE METODO SE OCUPA PARA QUE LOS
        self.nombre = nombre          # PARA  LOS DATOS NO SE DUPLIQUE
        self.apellido = apellido

 def saludo(self): #-> esto es un metodo
# que se hace referencia asi mismo    
        print("hola mi nombre es ",self.nombre,self.apellido) #-> esto es un parametro

usuario = Usuario('Felipe', 'Feliz') # ESTO UNA INSTANCIA DE UN OBJETO
#print(usuario.nombre ,usuario.apellido,usuario2.nombre,usuario2.apellido)

class Admin(Usuario):
        def  SuperSaludo(self):
                print("hola me llamo",self.nombre,"y soy adminstrador")
'''

'''''
#para llamar un metodo 
#usuario.saludo()
#tambien se puede cambiar la  propiedad de metodo
usuario.nombre="hola pepe"
usuario.saludo()

admin=Admin("super","feliz")
admin.saludo
admin.SuperSaludo()
#no se peuede llamar los metodos desde las clases hijas
#usuario.SuperSaludo()
'''
'''''
class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un', self.tipo, 'y mi sonido es el', self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'
     

class Perro(Animal):
    tipo = 'perro'
    

class Canario(Animal):
    tipo = 'canario'


gato=Gato("mancha","maullido")
gato.saludo()
perro=Perro("chuleta","ladrido")
perro.saludo()
canario=Canario("fly","silvido")
canario.saludo()
'''
#--------------------------------------
# Extendiendo el metodo init del padre
#--------------------------------------
class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un', self.tipo, 'y mi sonido es el', self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'
    #extender el comportamiento metodo init del padre
    def __init__(self, nombre, onomatopeya):
         Animal.__init__(self,nombre,onomatopeya)
         print("hola soy un gato extendido")
     

class Perro(Animal):
    tipo = 'perro'
    #otra forma
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print("hola soy un perro extendido")

    

class Canario(Animal):
    tipo = 'canario'


gato=Gato("mancha","maullido")
gato.saludo()
perro=Perro("chuleta","ladrido")
perro.saludo()
canario=Canario("fly","silvido")
canario.saludo()