'''
Implementa un sistema donde los usuarios puedan registrarse con un nombre de usuario, correo electrónico y contraseña segura. 
Permite que los usuarios inicien sesión de manera segura para acceder a sus datos.
'''

import mysql.connector
import  bcrypt

# Establece los parámetros de conexión con control de errores
try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="mydb"
    )
    print("Conexión establecida exitosamente.")
except mysql.connector.Error as e:
    print(f"Error al conectar a la base de datos: {e}")
    conexion = None



class Registro():
    def __init__(self):
        self.usuario = ""
        self.correo  = ""
        self.clave= ""

    def Registrar(self):
        
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM registro_usuarios; ")
        base_datos = cursor.fetchall()
        print(base_datos)

        while True:
            self.usuario = input("Ingrese un usuario: ")
            if self.usuario.strip() == "":
                print("El campo de usuario no puede estar vacío.")
                continue
            break

        while True:
            self.correo = input("Ingrese un correo: ")
            if "@" not in self.correo or "." not in self.correo:
                print("Ingrese un correo válido.")
            elif self.correo.strip() == "":
                print("El campo de correo no puede estar vacío.")
            else:
                break

        while True:
            self.clave = input("Ingrese una clave: ")
            if self.clave.strip() == "":
                print("El campo de clave no puede estar vacío.")
            else:
                self.password = bytes(self.clave, 'utf-8')
                self.salt = bcrypt.gensalt(rounds=12)
                self.hashed_password = bcrypt.hashpw(self.password, self.salt)
                break

          
        datos = "INSERT INTO registro_usuarios (usuario, correo, clave) VALUES (%s, %s,%s );"
        cursor.execute(datos, (self.usuario, self.correo, self.hashed_password ))
        print("registro exitoso")
        conexion.commit()

class Inicio_Secion(Registro):
    def __init__(self):
        super().__init__()


    def Inicio(self):

        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM registro_usuarios; ")
        base_datos = cursor.fetchall()
        print(base_datos)
        
        self.usuario = input("Ingrese un usuario: ")
        self.clave = input("Ingrese una clave: ")

        # Verificar si el usuario y la clave están en la base de datos
        cursor.execute("SELECT usuario, clave FROM registro_usuarios WHERE usuario = %s;", (self.usuario,))
        resultado = cursor.fetchone()
        
        if resultado:
            hashed_password = resultado[1]  # Acceder al hash de la contraseña desde la base de datos
            if bcrypt.checkpw(bytes(self.clave, 'utf-8'), bytes(hashed_password, 'utf-8')):
                print("Inicio de sesión exitoso.")
            else:
                print("Contraseña incorrecta.")
        else:
            print("Usuario no encontrado.")



       


inicio_secion = Inicio_Secion()
inicio_secion.Inicio()        

#registro = Registro()
#registro.Registrar()