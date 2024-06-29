# Sistema de Gestión de Productos y Categorías

import mysql.connector

class DBConnector:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def ejecutar_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor

    def cerrar_conexion(self):
        self.connection.close()

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def insertar_en_bd(self, db):
        query = f"INSERT INTO productos (nombre, precio) VALUES ('{self.nombre}', {self.precio})"
        db.ejecutar_query(query)
        print(f"Producto {self.nombre} insertado en la base de datos")

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def insertar_en_bd(self, db):
        query = f"INSERT INTO categorias (nombre) VALUES ('{self.nombre}')"
        db.ejecutar_query(query)
        print(f"Categoría {self.nombre} insertada en la base de datos")
class ProductoCategoria(Producto, Categoria):
    def __init__(self, nombre_producto, precio, nombre_categoria, db_connector):
        Producto.__init__(self, nombre_producto, precio)
        Categoria.__init__(self, nombre_categoria)
        self.db = db_connector
# Configuración de la conexión a la base de datos
db = DBConnector(host='localhost', user='usuario', password='contraseña', database='tienda')

# Creación de instancia de ProductoCategoria y uso
producto_categoria = ProductoCategoria('Laptop', 1200, 'Electrónica', db)
producto_categoria.insertar_en_bd(db)

# Cierre de la conexión a la base de datos
db.cerrar_conexion()
