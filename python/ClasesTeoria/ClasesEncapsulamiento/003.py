class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad

    def obtener_nombre(self):
        return self.__nombre

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def obtener_precio(self):
        return self.__precio

    def establecer_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            print("El precio debe ser un valor positivo")

    def obtener_cantidad(self):
        return self.__cantidad

    def establecer_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            print("La cantidad debe ser un valor no negativo")

# Prueba de la clase
producto = Producto("Laptop", 1000, 10)
print(producto.obtener_nombre())  # Laptop
print(producto.obtener_precio())  # 1000
print(producto.obtener_cantidad())  # 10
producto.establecer_precio(1200)
producto.establecer_cantidad(15)
print(producto.obtener_precio())  # 1200
print(producto.obtener_cantidad())  # 15
producto.establecer_precio(-200)  # El precio debe ser un valor positivo
producto.establecer_cantidad(-5)  # La cantidad debe ser un valor no negativo
