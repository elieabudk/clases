'''
Ejercicio de Programación: Gestor de Inventario con Encapsulación

Objetivo: Implementar un gestor de inventario utilizando programación orientada a objetos en Python, asegurando la encapsulación adecuada de los atributos de los productos.

Instrucciones:

Definición de Clase Producto:

Crea una clase Producto con los siguientes atributos privados:

_codigo: entero, código único del producto.
_nombre: cadena, nombre del producto.
_precio: float, precio unitario del producto.
_cantidad: entero, cantidad disponible en el inventario.
La clase Producto debe tener los siguientes métodos:

Un constructor (__init__) que inicialice los atributos _codigo, _nombre, _precio y _cantidad.
Métodos getter para cada atributo (codigo, nombre, precio, cantidad), implementados como propiedades de solo lectura.
Definición de Clase Inventario:

Crea una clase Inventario que gestione una colección de productos.

Utiliza un atributo privado _inventario que sea un diccionario donde la clave sea el código del producto y el valor sea un objeto Producto.

La clase Inventario debe tener los siguientes métodos públicos:

agregar_producto(producto): Agrega un objeto Producto al inventario. Si el producto ya existe (mismo código), muestra un mensaje de error.
consultar_producto(codigo): Consulta y muestra la información de un producto dado su código. Si el producto no existe, muestra un mensaje de error.
actualizar_cantidad(codigo, nueva_cantidad): Actualiza la cantidad disponible de un producto dado su código. Si la cantidad nueva es negativa, muestra un mensaje de error.
eliminar_producto(codigo): Elimina un producto del inventario dado su código. Si el producto no existe, muestra un mensaje de error.
Ejemplo de Uso:

Crea una instancia de Inventario.
Agrega varios productos al inventario utilizando la instancia de Producto.
Realiza consultas, actualizaciones de cantidad y eliminaciones de productos para verificar el correcto funcionamiento del programa.
Consideraciones:

Implementa la encapsulación adecuada utilizando convenciones de nomenclatura (_atributo_privado).
Asegúrate de validar los datos de entrada donde sea necesario (por ejemplo, no permitir cantidades negativas al actualizar).
'''