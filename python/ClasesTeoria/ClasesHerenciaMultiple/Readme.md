# Herencia múltiple

Conceptos Básicos
Clase Base (Padre): Es la clase cuyas características son heredadas por otra clase.

Clase Derivada (Hija): Es la clase que hereda las características de la clase base.

Sintaxis básica para recordar

```python
class ClaseBase:
    def __init__(self, atributo_base):
        self.atributo_base = atributo_base
    
    def metodo_base(self):
        print("Método de la clase base")

class ClaseDerivada(ClaseBase):
    def __init__(self, atributo_base, atributo_derivado):
        super().__init__(atributo_base)  # Llama al constructor de la clase base
        self.atributo_derivado = atributo_derivado
    
    def metodo_derivado(self):
        print("Método de la clase derivada")


```

super(): Es una función que se utiliza para dar acceso a métodos y propiedades de una clase padre o hermana.

Métodos y Atributos: La clase derivada hereda los métodos y atributos de la clase base, y puede añadir nuevos o sobreescribir los existentes.

Ventajas de la Herencia


Reutilización de Código: Permite reutilizar código existente.
Mantenimiento Fácil: Facilita el mantenimiento y la extensión de aplicaciones.
Jerarquía: Facilita la creación de jerarquías de clases que representan relaciones reales.