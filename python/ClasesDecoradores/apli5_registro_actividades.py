'''
Registro de Actividades (Logging)
Para registrar las actividades que realiza una función.
'''

def registrar_actividad(func):
    def envoltura(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"Función {func.__name__} fue llamada con args: {args}, kwargs: {kwargs}")
        return resultado
    return envoltura

@registrar_actividad
def sumar(a, b):
    return a + b

print(sumar(3, 4))
print(sumar(a=5, b=7))
