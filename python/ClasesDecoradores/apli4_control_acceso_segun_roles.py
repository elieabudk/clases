'''
Control de Acceso según Roles
Para limitar el acceso a funciones dependiendo del rol del usuario.
'''

def requiere_rol(rol_requerido):
    def decorador(func):
        def envoltura(usuario, *args, **kwargs):
            if usuario.rol != rol_requerido:
                raise PermissionError(f"Se requiere rol {rol_requerido}")
            return func(usuario, *args, **kwargs)
        return envoltura
    return decorador

class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

@requiere_rol("admin")
def ver_panel_admin(usuario):
    return "Panel de administración"

usuario_admin = Usuario("Carlos", "admin")
usuario_normal = Usuario("Ana", "user")

print(ver_panel_admin(usuario_admin))  # Funciona correctamente
try:
    print(ver_panel_admin(usuario_normal))  # Levanta una excepción
except PermissionError as e:
    print(e)
