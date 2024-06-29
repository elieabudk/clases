# Ejemplo básico de herencia múltiple

class Mamifero:
    def __init__(self, nombre):
        self.nombre = nombre

    def amamantar(self):
        print(f"{self.nombre} está amamantando a sus crías")

class Volador:
    def __init__(self, nombre):
        self.nombre = nombre

    def volar(self):
        print(f"{self.nombre} está volando")

class Murcielago(Mamifero, Volador):
    def __init__(self, nombre):
        Mamifero.__init__(self, nombre)
        Volador.__init__(self, nombre)
    
    def colgarse(self):
        print(f"{self.nombre} está colgado boca abajo")

bat = Murcielago("Bruce")
bat.amamantar()  # Bruce está amamantando a sus crías
bat.volar()      # Bruce está volando
bat.colgarse()   # Bruce está colgado boca abajo
