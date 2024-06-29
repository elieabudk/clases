#Control de acceso

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar_nombre(self):
        print(f"Usuario: {self.nombre}")

class Permiso:
    def __init__(self, permisos):
        self.permisos = permisos
    
    def mostrar_permisos(self):
        print(f"Permisos: {', '.join(self.permisos)}")
class UsuarioPermiso(Usuario, Permiso):
    def __init__(self, nombre, permisos):
        Usuario.__init__(self, nombre)
        Permiso.__init__(self, permisos)
    
    def mostrar_detalles(self):
        self.mostrar_nombre()
        self.mostrar_permisos()
usuario = UsuarioPermiso("Alice", ["leer", "escribir", "eliminar"])
usuario.mostrar_detalles()
