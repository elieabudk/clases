class Vehiculo:
    def __init__(self, marca, modelo, anio, kilometraje):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__kilometraje = kilometraje

    def obtener_marca(self):
        return self.__marca

    def establecer_marca(self, marca):
        self.__marca = marca

    def obtener_modelo(self):
        return self.__modelo

    def establecer_modelo(self, modelo):
        self.__modelo = modelo

    def obtener_anio(self):
        return self.__anio

    def establecer_anio(self, anio):
        if anio > 0:
            self.__anio = anio
        else:
            print("El año debe ser un valor positivo")

    def obtener_kilometraje(self):
        return self.__kilometraje

    def establecer_kilometraje(self, kilometraje):
        if kilometraje >= self.__kilometraje:
            self.__kilometraje = kilometraje
        else:
            print("El kilometraje no puede disminuir")

# Prueba de la clase
vehiculo = Vehiculo("Toyota", "Corolla", 2020, 50000)
print(vehiculo.obtener_marca())  # Toyota
print(vehiculo.obtener_modelo())  # Corolla
print(vehiculo.obtener_anio())  # 2020
print(vehiculo.obtener_kilometraje())  # 50000
vehiculo.establecer_anio(2021)
vehiculo.establecer_kilometraje(60000)
print(vehiculo.obtener_anio())  # 2021
print(vehiculo.obtener_kilometraje())  # 60000
vehiculo.establecer_anio(-2021)  # El año debe ser un valor positivo
vehiculo.establecer_kilometraje(40000)  # El kilometraje no puede disminuir
