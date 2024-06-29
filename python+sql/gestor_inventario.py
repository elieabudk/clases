'''
nicio
Menú Principal
Opción 1: Añadir nuevo producto
Opción 2: Actualizar existencias
Opción 3: Gestionar pedidos
Opción 4: Generar informes de inventario
Opción 5: Salir
'''

import mysql.connector

class BaseDatos():
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def conectar(self):
        
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Conexión exitosa a la base de datos")
        except mysql.connector.Error as err:
            print(f"Error: {err}")


class Producto(BaseDatos):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)
        self.nombre = ""
        self.precio = ""
        self.cantidad = ""

    def Añadir_producto(self):
        self.nombre = input("Ingrese el nombre del producto: ")
        self.precio = float(input("Ingrese el precio del producto: "))
        self.cantidad = int(input("Ingrese la cantidad del producto: "))
        self.conectar()
        cursor = self.connection.cursor()
        query = "INSERT INTO productos (nombre, precio, cantidad) VALUES (%s, %s, %s)"
        values = (self.nombre, self.precio, self.cantidad)
        try:
            cursor.execute(query, values)
            self.connection.commit()
            print("Producto añadido exitosamente")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            self.connection.close()

    def AtualizarExistencia(self):
        nombre_producto = input("Ingrese el nombre del producto a buscar: ")
        self.conectar()
        cursor = self.connection.cursor()
        query = "SELECT * FROM productos WHERE nombre = %s"
        cursor.execute(query, (nombre_producto,))
        producto = cursor.fetchone()
        if producto:
            print(f"Producto encontrado: {producto}")
            opcion = input("¿Desea editar (e) o eliminar (d) el producto? (e/d): ").lower()
            if opcion == 'e':
                nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
                update_query = "UPDATE productos SET nombre = %s, precio = %s, cantidad = %s WHERE nombre = %s"
                update_values = (nuevo_nombre, nuevo_precio, nueva_cantidad, nombre_producto)
                try:
                    cursor.execute(update_query, update_values)
                    self.connection.commit()
                    print("Producto actualizado exitosamente")
                except mysql.connector.Error as err:
                    print(f"Error: {err}")
            elif opcion == 'd':
                delete_query = "DELETE FROM productos WHERE nombre = %s"
                try:
                    cursor.execute(delete_query, (nombre_producto,))
                    self.connection.commit()
                    print("Producto eliminado exitosamente")
                except mysql.connector.Error as err:
                    print(f"Error: {err}")
        else:
            print("Producto no encontrado")
        cursor.close()
        self.connection.close()

class Pedido(Producto):
    def __init__(self, host, user, password, database):
        Producto.__init__(self, host, user, password, database)

    def gestionarPedido(self):
        producto = input("Ingrese el producto para el pedido: ")
        self.conectar()
        cursor = self.connection.cursor()
        query = "SELECT * FROM productos WHERE nombre = %s"
        cursor.execute(query, (producto,))
        producto = cursor.fetchone()
        if producto:
            print("Producto gestionado")
            if producto[3] < 2:
                print("La cantidad es menor a 2, solicitar nuevo pedido.")
        else:
            print("Producto no encontrado")
        cursor.close()
        self.connection.close()

class Ionforme(Producto):
    def __init__(self, host, user, password, database):
        Producto.__init__(self, host, user, password, database)

    def generarInforme(self):
        self.conectar()
        cursor = self.connection.cursor()
        query = "SELECT * FROM productos"
        cursor.execute(query)
        productos = cursor.fetchall()
        if productos:
            print("Productos disponibles:")
            print("{:<20} {:<10} {:<10} {:<10}".format("Nombre", "Precio", "Cantidad", "Descripción"))
            print("-" * 60)
            for producto in productos:
                print("{:<20} {:<10} {:<10} {:<10}".format(producto[0], producto[1], producto[2], producto[3]))
        else:
            print("No hay productos disponibles.")
        cursor.close()
        self.connection.close()

def main():
    basedatos = BaseDatos("localhost", "root", "Elie.117", "inventario_db")
    if basedatos.conectar():
        print("Conexión a la base de datos exitosa.")
    else:
        print("Error al conectar con la base de datos.")

    while   True:    
        opcion = input("Menú Principal \n "
                    "Opción 1: Añadir nuevo producto: \n"
                    "Opción 2: Actualizar existencias: \n"
                    "Opción 3: Gestionar pedidos: \n"
                    "Opción 4: Generar informes de inventario: \n"
                    "Opción 5: Salir: ")
        if opcion == "1":
            producto = Producto("localhost", "root", "Elie.117", "inventario_db")
            producto.Añadir_producto()
        elif opcion == "2":
            producto = Producto("localhost", "root", "Elie.117", "inventario_db")
            producto.AtualizarExistencia()
        elif opcion == "3":
            pedido = Pedido("localhost", "root", "Elie.117", "inventario_db")
            pedido.gestionarPedido()
        elif opcion == "4":
            informe = Ionforme("localhost", "root", "Elie.117", "inventario_db")
            informe.generarInforme()

main()










