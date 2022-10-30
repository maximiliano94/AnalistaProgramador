#-----------------------------
#   CLASES 
#-----------------------------
#como crear una clase
class Usuario:
 def __init__(self, nombre, apellido):# ESTE METODO SE OCUPA PARA QUE LOS
        self.nombre = nombre          # PARA  LOS DATOS NO SE DUPLIQUE
        self.apellido = apellido


usuario = Usuario('Felipe', 'Feliz') # ESTO UNA INSTANCIA DE UN OBJETO
usuario2 = Usuario('tomas', 'perez')
print(usuario.nombre ,usuario.apellido,usuario2.nombre,usuario2.apellido)