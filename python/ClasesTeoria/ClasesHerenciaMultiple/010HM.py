#Herencia multiple y encapsulacion

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
        self._nombre = nombre  # Encapsulación del nombre como atributo protegido
        self._salario = salario  # Encapsulación del salario como atributo protegido

    def mostrar_info(self):
        print(f"Nombre: {self._nombre}, Salario: {self._salario}")

class Administrativo(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self._departamento = departamento

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Departamento: {self._departamento}")

class Tecnico(Empleado):
    def __init__(self, nombre, salario, area):
        super().__init__(nombre, salario)
        self._area = area

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Área: {self._area}")

class EmpleadoDB(DBConnector):
    def __init__(self, host, user, password, database):
        super().__init__(host, user, password, database)

    def insertar_empleado(self, empleado):
        if isinstance(empleado, Empleado):
            query = f"INSERT INTO empleados (nombre, salario) VALUES ('{empleado._nombre}', {empleado._salario})"
            self.ejecutar_query(query)
            print(f"Empleado {empleado._nombre} insertado en la base de datos")

    def cerrar_conexion(self):
        super().cerrar_conexion()
# Configuración de la conexión a la base de datos
db = EmpleadoDB(host='localhost', user='usuario', password='contraseña', database='empresa')

# Creación de instancias de empleados
admin1 = Administrativo("Ana López", 3000, "Administración")
tec1 = Tecnico("Carlos Martínez", 2500, "Soporte Técnico")

# Inserción de empleados en la base de datos
db.insertar_empleado(admin1)
db.insertar_empleado(tec1)

# Mostrar información de los empleados
admin1.mostrar_info()
tec1.mostrar_info()

# Cierre de la conexión a la base de datos
db.cerrar_conexion()
