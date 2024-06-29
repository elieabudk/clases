'''
Decorador para Validar Argumentos
Un decorador que valida los argumentos pasados a una función.
'''

def verificar_positivos(func):
    def envoltura(*args, **kwargs):
        for arg in args:
            if arg < 0:
                raise ValueError("Todos los argumentos deben ser positivos")
        return func(*args, **kwargs)
    return envoltura

@verificar_positivos
def sumar(a, b):
    return a + b

try:
    print(sumar(5, 3))
    print(sumar(-1, 4))
except ValueError as e:
    print(e)
