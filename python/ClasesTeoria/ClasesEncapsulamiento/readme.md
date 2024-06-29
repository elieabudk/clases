## Teoría de la Encapsulación en Python

La encapsulación es uno de los pilares fundamentales de la Programación Orientada a Objetos (POO). 

Su propósito principal es restringir el acceso directo a algunos de los componentes de un objeto, lo cual ayuda a proteger los datos y asegurar la integridad de los mismos.

Conceptos Clave

Atributos Públicos: Son accesibles desde cualquier parte del programa.

Atributos Privados: Son accesibles solo dentro de la clase en la que se definen. En Python, se indica que un atributo es privado utilizando dos guiones bajos (__) al comienzo del nombre del atributo.

Atributos Protegidos: Son accesibles desde la clase en la que se definen y desde las subclases. En Python, se indica que un atributo es protegido utilizando un guión bajo (_) al comienzo del nombre del atributo.

Métodos Getters y Setters: Se utilizan para obtener y establecer valores de los atributos privados de una clase.

### Ejemplo básico de encapsulación

```python
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # atributo privado
        self.__edad = edad  # atributo privado

    def obtener_nombre(self):
        return self.__nombre

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def obtener_edad(self):
        return self.__edad

    def establecer_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser un número positivo")

# Uso de la clase Persona
persona = Persona("Juan", 30)
print(persona.obtener_nombre())  # Juan
persona.establecer_edad(31)
print(persona.obtener_edad())  # 31

```