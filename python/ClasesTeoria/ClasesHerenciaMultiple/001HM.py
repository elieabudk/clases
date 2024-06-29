# Dispositivos electrónicos

class Dispositivo:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def encender(self):
        print(f"{self.nombre} está encendido")

class Bluetooth:
    def __init__(self, version):
        self.version = version
    
    def conectar_bluetooth(self):
        print(f"Conectado por Bluetooth versión {self.version}")

class AltavozBluetooth(Dispositivo, Bluetooth):
    def __init__(self, nombre, version):
        Dispositivo.__init__(self, nombre)
        Bluetooth.__init__(self, version)
    
    def reproducir_musica(self):
        print(f"{self.nombre} está reproduciendo música")
altavoz = AltavozBluetooth("JBL", "5.0")
altavoz.encender()           # JBL está encendido
altavoz.conectar_bluetooth() # Conectado por Bluetooth versión 5.0
altavoz.reproducir_musica()  # JBL está reproduciendo música
