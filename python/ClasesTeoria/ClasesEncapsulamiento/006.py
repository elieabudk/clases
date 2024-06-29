class Libro:
    def __init__(self, titulo, autor, precio, num_paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__precio = precio
        self.__num_paginas = num_paginas

    def obtener_titulo(self):
        return self.__titulo

    def establecer_titulo(self, titulo):
        self.__titulo = titulo

    def obtener_autor(self):
        return self.__autor

    def establecer_autor(self, autor):
        self.__autor = autor

    def obtener_precio(self):
        return self.__precio

    def establecer_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            print("El precio debe ser un valor positivo")

    def obtener_num_paginas(self):
        return self.__num_paginas

    def establecer_num_paginas(self, num_paginas):
        if num_paginas > 0:
            self.__num_paginas = num_paginas
        else:
            print("El número de páginas debe ser un valor positivo")

# Prueba de la clase
libro = Libro("El Quijote", "Miguel de Cervantes", 25, 1000)
print(libro.obtener_titulo())  # El Quijote
print(libro.obtener_autor())  # Miguel de Cervantes
print(libro.obtener_precio())  # 25
print(libro.obtener_num_paginas())  # 1000
libro.establecer_precio(30)
libro.establecer_num_paginas(1050)
print(libro.obtener_precio())  # 30
print(libro.obtener_num_paginas())  # 1050
libro.establecer_precio(-10)  # El precio debe ser un valor positivo
libro.establecer_num_paginas(-50)  # El número de páginas debe ser un valor positivo
