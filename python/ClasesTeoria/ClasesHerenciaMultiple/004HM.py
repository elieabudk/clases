#Gestor de inventario

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def mostrar_info(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}")

class Almacen:
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado al almacén {self.ubicacion}")

    def mostrar_inventario(self):
        print(f"Inventario del almacén {self.ubicacion}:")
        for producto in self.productos:
            producto.mostrar_info()
class ProductoAlmacen(Producto, Almacen):
    def __init__(self, nombre, precio, ubicacion):
        Producto.__init__(self, nombre, precio)
        Almacen.__init__(self, ubicacion)

    def agregar_a_almacen(self):
        self.agregar_producto(self)
p1 = ProductoAlmacen("Laptop", 1500, "Almacén Central")
p2 = ProductoAlmacen("Smartphone", 800, "Almacén Central")

p1.agregar_a_almacen()
p2.agregar_a_almacen()

p1.mostrar_inventario()
