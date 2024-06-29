#Gestor bancario

class Cliente:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
    
    def mostrar_info(self):
        print(f"Cliente: {self.nombre}, DNI: {self.dni}")

class Cuenta:
    def __init__(self, numero_cuenta, saldo=0):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depositados {cantidad}. Saldo actual: {self.saldo}")
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes")
        else:
            self.saldo -= cantidad
            print(f"Retirados {cantidad}. Saldo actual: {self.saldo}")
class CuentaCliente(Cliente, Cuenta):
    def __init__(self, nombre, dni, numero_cuenta, saldo=0):
        Cliente.__init__(self, nombre, dni)
        Cuenta.__init__(self, numero_cuenta, saldo)

    def mostrar_detalles(self):
        self.mostrar_info()
        print(f"Número de Cuenta: {self.numero_cuenta}, Saldo: {self.saldo}")
cliente1 = CuentaCliente("Juan Pérez", "12345678A", "ES1234567890", 1000)
cliente1.mostrar_detalles()

cliente1.depositar(500)
cliente1.retirar(200)
cliente1.mostrar_detalles()
