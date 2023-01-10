#escribe una funcion que determine si el ususario es mayor de edad
def mayoedad(usuario):
    return usuario.edad >17
 
class Usuario:
    def __init__(self,edad):
     self.edad=edad

usuario=Usuario(15)
Usuario2=Usuario(22)

resultado=mayoedad(usuario)
resultado2=mayoedad(Usuario2)

print(resultado,resultado2)