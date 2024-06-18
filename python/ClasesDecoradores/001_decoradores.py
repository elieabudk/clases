## Teoría

'''
Un decorador en Python es una función que toma otra función como argumento y extiende o 
altera su comportamiento sin modificar su código de manera explícita. Los decoradores permiten 
la adición de funcionalidades a funciones o métodos existentes de una manera modular y reutilizable.

¿Cómo funcionan los Decoradores?
La idea básica detrás de un decorador es que toma una función, la envuelve en otra función que 
añade alguna funcionalidad adicional, y luego devuelve la función envuelta. Esto se hace 
típicamente mediante una función interna, llamada wrapper (envoltura).
'''

# Definimos el decorador
def mi_decorador(func):
    def envoltura():
        print("Antes de ejecutar la función")
        func()
        print("Después de ejecutar la función")
    return envoltura

# Usamos el decorador en una función
@mi_decorador
def di_hola():
    print("Hola, mundo!")

# Llamamos a la función decorada
di_hola()
