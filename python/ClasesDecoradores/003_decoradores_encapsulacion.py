'''
Ejemplo 1: Decorador para Ocultar Funciones Internas
Imagina que tienes una función que realiza varios pasos, 
pero solo quieres exponer la función principal y no los detalles internos.
'''

# Función interna que no queremos exponer
def _detalles_internos():
    print("Realizando pasos internos...")

# Decorador para encapsular detalles internos
def encapsular(func):
    def envoltura(*args, **kwargs):
        print("Encapsulando detalles internos...")
        _detalles_internos()
        return func(*args, **kwargs)
    return envoltura

# Uso del decorador
@encapsular
def operacion_principal():
    print("Operación principal ejecutada")

# Llamada a la función
operacion_principal()

'''
Ejemplo 2: Decorador para Encapsular la Conexión a una Base de Datos
Encapsular la conexión y desconexión de una base de datos.
'''

# Simulación de una conexión a una base de datos
class ConexionBD:
    def __init__(self, nombre_bd):
        self.nombre_bd = nombre_bd

    def conectar(self):
        print(f"Conectado a la base de datos {self.nombre_bd}")

    def desconectar(self):
        print(f"Desconectado de la base de datos {self.nombre_bd}")

# Decorador para encapsular la conexión a la base de datos
def gestionar_conexion(nombre_bd):
    def decorador(func):
        def envoltura(*args, **kwargs):
            conexion = ConexionBD(nombre_bd)
            conexion.conectar()
            resultado = func(conexion, *args, **kwargs)
            conexion.desconectar()
            return resultado
        return envoltura
    return decorador

# Uso del decorador
@gestionar_conexion('mi_base_de_datos')
def realizar_consulta(conexion, consulta):
    print(f"Ejecutando consulta: {consulta}")

# Llamada a la función
realizar_consulta("SELECT * FROM usuarios")
