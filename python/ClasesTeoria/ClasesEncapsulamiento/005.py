class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.__nombre = nombre
        self.__puesto = puesto
        self.__salario = salario

    def obtener_nombre(self):
        return self.__nombre

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def obtener_puesto(self):
        return self.__puesto

    def establecer_puesto(self, puesto):
        self.__puesto = puesto

    def obtener_salario(self):
        return self.__salario

    def establecer_salario(self, salario):
        if salario > 0:
            self.__salario = salario
        else:
            print("El salario debe ser un valor positivo")

# Prueba de la clase
empleado = Empleado("Carlos", "Gerente", 50000)
print(empleado.obtener_nombre())  # Carlos
print(empleado.obtener_puesto())  # Gerente
print(empleado.obtener_salario())  # 50000
empleado.establecer_salario(60000)
print(empleado.obtener_salario())  # 60000
empleado.establecer_salario(-30000)  # El salario debe ser un valor positivo
