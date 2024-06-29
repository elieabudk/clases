'''
Ejercicio: Gestor de Inventario con Decoradores
Descripción del Problema
Crear un sistema de gestión de inventario para una tienda utilizando Python. El sistema debe permitir agregar, actualizar, eliminar y mostrar productos, aplicando validaciones y registrando cada operación utilizando decoradores.

Especificaciones
Clase Producto:

Atributos:
_nombre: Nombre del producto.
_cantidad: Cantidad disponible en el inventario.
_precio: Precio unitario del producto.
Métodos:
__init__(self, nombre, cantidad, precio): Constructor para inicializar el producto.
Métodos getter y setter para _nombre, _cantidad y _precio.
Clase Inventario:

Atributos:
productos: Lista para almacenar los objetos de tipo Producto.
Métodos:
agregar_producto(self, producto): Agrega un nuevo producto al inventario.
actualizar_stock(self, producto, nueva_cantidad): Actualiza la cantidad de un producto en el inventario.
eliminar_producto(self, producto): Elimina un producto del inventario.
mostrar_inventario(self): Muestra todos los productos en el inventario.
Decoradores:
validar_cantidad: Decorador para asegurar que la cantidad no sea negativa en el método actualizar_stock.
registrar_operacion: Decorador para registrar cada operación realizada en el inventario.
Instrucciones:

Implementa las clases Producto y Inventario según las especificaciones dadas.
Utiliza decoradores para validar y registrar las operaciones según se indica.
Crea al menos dos objetos Producto y realiza varias operaciones sobre ellos utilizando métodos de la clase Inventario.
Muestra el inventario después de cada operación para verificar los cambios.
Asegúrate de manejar correctamente cualquier error o excepción que pueda surgir durante las operaciones (por ejemplo, intentos de actualizar con una cantidad negativa).
'''