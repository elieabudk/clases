#Un decorador que puede aceptar argumentos para personalizar su comportamiento.

def repetir_veces(n):
    def decorador(func):
        def envoltura(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return envoltura
    return decorador

@repetir_veces(3)
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Carlos")
