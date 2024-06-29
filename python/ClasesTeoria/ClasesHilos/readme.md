Conceptos Básicos

Hilos (Threads): Un hilo es la unidad más pequeña de procesamiento que puede ser programada. Los hilos permiten la ejecución de múltiples operaciones simultáneamente en el mismo programa.

Multithreading: Es la capacidad de un programa para manejar múltiples hilos al mismo tiempo. En Python, el módulo threading se usa para trabajar con hilos.

GIL (Global Interpreter Lock): En Python, el GIL es un mutex que protege el acceso a los objetos de Python, evitando que múltiples hilos ejecuten código de Python al mismo tiempo. Esto significa que en una CPU de un solo núcleo, el multithreading no necesariamente mejora el rendimiento, pero aún puede ser útil para operaciones de I/O.

Ejemplo Básico de Uso de Hilos
Para crear y usar hilos en Python, puedes usar el módulo threading.


```python
import threading
import time

def tarea():
    print("Inicio de la tarea")
    time.sleep(2)
    print("Tarea completa")

# Crear un hilo
hilo = threading.Thread(target=tarea)

# Iniciar el hilo
hilo.start()

# Esperar a que el hilo termine
hilo.join()

print("Programa principal terminado")
```

Multithreading con Múltiples Hilos

Si se quiere ejecutar varias tareas en paralelo, se puede crear múltiples hilos:

```python
import threading
import time

def tarea(nombre):
    print(f"Inicio de la tarea {nombre}")
    time.sleep(2)
    print(f"Tarea {nombre} completa")

# Crear e iniciar múltiples hilos
hilos = []
for i in range(5):
    hilo = threading.Thread(target=tarea, args=(f'Hilo-{i}',))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print("Programa principal terminado")

```