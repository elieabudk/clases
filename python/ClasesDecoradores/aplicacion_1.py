'''
Decorador para Medir el Tiempo de Ejecución
Un decorador que mide cuánto tiempo tarda en ejecutarse una función.
'''

import time

def temporizador(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio} segundos")
        return resultado
    return envoltura

@temporizador
def contar_hasta(n):
    for i in range(n):
        pass

contar_hasta(1000000)
