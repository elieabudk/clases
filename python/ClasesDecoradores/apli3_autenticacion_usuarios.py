'''
Autenticación de Usuarios
Imagina que tienes una aplicación web donde algunas funciones solo deben ser accesibles por usuarios autenticados.
'''
def requiere_autenticacion(func):
    def envoltura(usuario, *args, **kwargs):
        if not usuario.esta_autenticado:
            raise PermissionError("Usuario no autenticado")
        return func(usuario, *args, **kwargs)
    return envoltura

class Usuario:
    def __init__(self, nombre, esta_autenticado):
        self.nombre = nombre
        self.esta_autenticado = esta_autenticado

@requiere_autenticacion
def ver_datos_sensibles(usuario):
    return "Datos sensibles del usuario"

usuario_autenticado = Usuario("Carlos", True)
usuario_no_autenticado = Usuario("Ana", False)

print(ver_datos_sensibles(usuario_autenticado))  # Funciona correctamente
try:
    print(ver_datos_sensibles(usuario_no_autenticado))  # Levanta una excepción
except PermissionError as e:
    print(e)
