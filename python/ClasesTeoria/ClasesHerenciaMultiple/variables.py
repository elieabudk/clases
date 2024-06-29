num = 4

class Numero:
    def __init__(self, valor):
        self.valor = valor


    def obtener_numero(self):
        print(num)
        return self.valor

# Crear una instancia de la clase Numero con el valor 10
mi_numero = Numero(10)

# Llamar al método obtener_numero para obtener el valor
print(mi_numero.obtener_numero())
