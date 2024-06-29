#Gestion de usuarios con mysql

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

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def insertar_en_bd(self):
        query = f"INSERT INTO empleados (nombre, salario) VALUES ('{self.nombre}', {self.salario})"
        self.db.ejecutar_query(query)
        print(f"Empleado {self.nombre} insertado en la base de datos")

class Departamento:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion

    def insertar_en_bd(self):
        query = f"INSERT INTO departamentos (nombre, ubicacion) VALUES ('{self.nombre}', '{self.ubicacion}')"
        self.db.ejecutar_query(query)
        print(f"Departamento {self.nombre} insertado en la base de datos")
class EmpleadoDepartamento(Empleado, Departamento):
    def __init__(self, nombre_empleado, salario, nombre_departamento, ubicacion_departamento, db_connector):
        Empleado.__init__(self, nombre_empleado, salario)
        Departamento.__init__(self, nombre_departamento, ubicacion_departamento)
        self.db = db_connector
# Configuración de la conexión a la base de datos
db = DBConnector(host='localhost', user='usuario', password='contraseña', database='empresa')

# Creación de instancia de EmpleadoDepartamento y uso
empleado_departamento = EmpleadoDepartamento('Juan', 2500, 'Ventas', 'Piso 5', db)
empleado_departamento.insertar_en_bd()

# Cierre de la conexión a la base de datos
db.cerrar_conexion()
