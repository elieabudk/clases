## Conceptos previos para la aplicación de decoradores

Funciones
Definición y llamadas: Saber cómo definir una función con def y cómo llamarla.
```
def mi_funcion():
    print("Hola, mundo")

mi_funcion()
```
Funciones con parámetros y retorno de valores: Entender cómo pasar argumentos a funciones y cómo retornar valores.
```
def sumar(a, b):
    return a + b

resultado = sumar(3, 4)
print(resultado)  # Salida: 7
```
2. Ámbito de las Variables
Ámbito Local y Global: Comprender la diferencia entre variables locales (definidas dentro de una función) y globales (definidas fuera de todas las funciones).
```
x = 10  # Variable global

def mi_funcion():
    x = 5  # Variable local
    print(x)

mi_funcion()  # Salida: 5
print(x)  # Salida: 10
```

3. Funciones Anidadas
Definir funciones dentro de otras funciones: Saber cómo definir una función dentro de otra y entender su ámbito.
```
def funcion_externa():
    print("Hola desde la función externa")

    def funcion_interna():
        print("Hola desde la función interna")

    funcion_interna()

funcion_externa()
```

4. Funciones de Primera Clase
Pasar funciones como argumentos: Saber que las funciones en Python pueden ser tratadas como objetos, pasadas como argumentos a otras funciones, y retornadas desde otras funciones.
```
def saludar(nombre):
    return f"Hola, {nombre}"

def procesar_funcion(func, valor):
    return func(valor)

resultado = procesar_funcion(saludar, "Mundo")
print(resultado)  # Salida: Hola, Mundo
```
5. Clausuras (Closures)
Entender las clausuras: Comprender que una función anidada puede recordar el ámbito en el que fue creada.
```
def generador_de_mensajes(mensaje):
    def mostrar_mensaje():
        print(mensaje)
    return mostrar_mensaje

mensaje_hola = generador_de_mensajes("Hola")
mensaje_hola()  # Salida: Hola

```
