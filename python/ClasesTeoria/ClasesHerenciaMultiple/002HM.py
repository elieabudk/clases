# Vehiculos

class Terrestre:
    def __init__(self, ruedas):
        self.ruedas = ruedas
    
    def conducir(self):
        print(f"Conduciendo un vehículo con {self.ruedas} ruedas")

class Acuatico:
    def __init__(self, motores):
        self.motores = motores
    
    def navegar(self):
        print(f"Navegando con {self.motores} motores")

class VehiculoAmfibio(Terrestre, Acuatico):
    def __init__(self, ruedas, motores):
        Terrestre.__init__(self, ruedas)
        Acuatico.__init__(self, motores)
    
    def transformar(self):
        print("Transformando de modo terrestre a modo acuático")
amfibio = VehiculoAmfibio(4, 2)
amfibio.conducir()     # Conduciendo un vehículo con 4 ruedas
amfibio.navegar()      # Navegando con 2 motores
amfibio.transformar()  # Transformando de modo terrestre a modo acuático
