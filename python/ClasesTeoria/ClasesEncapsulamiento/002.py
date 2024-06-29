class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo=0):
        self.__numero_cuenta = numero_cuenta
        self.__titular = titular
        self.__saldo = saldo

    def obtener_numero_cuenta(self):
        return self.__numero_cuenta

    def obtener_titular(self):
        return self.__titular

    def obtener_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
        else:
            print("El monto debe ser positivo")

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Fondos insuficientes o monto inválido")

# Prueba de la clase
cuenta = CuentaBancaria("1234567890", "Ana Perez", 1000)
print(cuenta.obtener_saldo())  # 1000
cuenta.depositar(-100)  # El monto debe ser positivo
cuenta.retirar(5000)  # Fondos insuficientes o monto inválido
