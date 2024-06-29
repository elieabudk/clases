class Email:
    def __init__(self, email_address):
        self.email_address = email_address
    
    def enviar_email(self, mensaje):
        print(f"Enviando email a {self.email_address}: {mensaje}")

class SMS:
    def __init__(self, numero_telefono):
        self.numero_telefono = numero_telefono
    
    def enviar_sms(self, mensaje):
        print(f"Enviando SMS a {self.numero_telefono}: {mensaje}")
class Notificacion(Email, SMS):
    def __init__(self, email_address, numero_telefono):
        Email.__init__(self, email_address)
        SMS.__init__(self, numero_telefono)
    
    def enviar_notificacion(self, mensaje):
        self.enviar_email(mensaje)
        self.enviar_sms(mensaje)
notificacion = Notificacion("example@example.com", "123456789")
notificacion.enviar_notificacion("¡Tu pedido ha sido enviado!")
