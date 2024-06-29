'''
Ejercicio Evaluativo: Gestor de Inventario con Polimorfismo

Objetivo: Implementar un gestor de inventario utilizando programación orientada a objetos en Python, haciendo uso del principio de polimorfismo para manejar diferentes tipos de productos de manera uniforme.

Instrucciones:

Define una clase base Producto con los siguientes métodos:

calcular_valor(): Método que deberá ser sobrescrito por las clases hijas para calcular el valor total del inventario para ese tipo de producto.
detalles(): Método que deberá ser sobrescrito por las clases hijas para mostrar detalles específicos del producto.
Crea dos clases hijas de Producto:

ProductoFresco: Representa productos perecederos como frutas o verduras frescas. Debe incluir:
Atributos: nombre, precio_por_kg, cantidad, fecha_caducidad.
Método calcular_valor(): Calcula el valor total basado en el precio por kilogramo y la cantidad.
Método detalles(): Muestra el nombre, cantidad en kilogramos y fecha de caducidad del producto.
ProductoNoFresco: Representa productos no perecederos como herramientas o utensilios. Debe incluir:
Atributos: nombre, precio_unitario, cantidad.
Método calcular_valor(): Calcula el valor total basado en el precio unitario y la cantidad.
Método detalles(): Muestra el nombre y la cantidad de unidades del producto.
Implementa una función o método llamado calcular_inventario() que tome una lista de productos (instancias de Producto) como argumento:

Itera sobre la lista y para cada producto, llama a los métodos calcular_valor() y detalles().
Al final, muestra el valor total del inventario sumando los valores calculados de todos los productos.
Crea al menos dos instancias de cada tipo de producto (ProductoFresco y ProductoNoFresco) y agrégalas a una lista.

Llama a la función calcular_inventario() con la lista de productos creada en el paso anterior para mostrar el funcionamiento del polimorfismo en la gestión del inventario.
'''