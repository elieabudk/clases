'''
Retraso en la Ejecución (Retry)
Para reintentar la ejecución de una función en caso de que falle.
'''

import time
import random

def reintentar(veces, retraso=1):
    def decorador(func):
        def envoltura(*args, **kwargs):
            for _ in range(veces):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}, reintentando en {retraso} segundos...")
                    time.sleep(retraso)
            raise Exception(f"Falló después de {veces} intentos")
        return envoltura
    return decorador

@reintentar(3, retraso=2)
def tarea_riesgosa():
    if random.choice([True, False]):
        raise ValueError("Algo salió mal")
    return "Tarea completada"

try:
    print(tarea_riesgosa())
except Exception as e:
    print(e)
