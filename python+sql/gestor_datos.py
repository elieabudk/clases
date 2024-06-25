import mysql.connector  # Importa el módulo para conectar con MySQL
import bcrypt  # Importa el módulo para encriptación de contraseñas
import pyotp  # Importa el módulo para 2FA
import qrcode  # Importa el módulo para generar códigos QR
from PIL import Image
from cryptography.fernet import Fernet
import traceback
import getpass
#usuario_id = 0;

# Intenta establecer conexión con la base de datos y maneja posibles errores de conexión
try:
    conexion = mysql.connector.connect(
        host="localhost",  # Servidor donde se encuentra la base de datos
        user="root",  # Usuario de la base de datos
        password="Elie.117",  # Contraseña del usuario
        database="mydb"  # Nombre de la base de datos
    )
    print("Conexión establecida exitosamente.")  # Mensaje de éxito en la conexión
except mysql.connector.Error as e:
    print(f"Error al conectar a la base de datos: {e}")  # Mensaje de error si la conexión falla
    conexion = None  # Establece la conexión como None si hay errores

#Variable global
usuario_id = None

class Registro():
    def __init__(self):
        self.usuario = ""
        self.correo = ""
        self.clave = ""
        self.secret = ""

    # Se encarga de registrar datos solo a la tabla USUARIOS
    def Registrar(self):
        if conexion is None:
            print("No hay conexión a la base de datos. No se puede registrar.")
            return
        
        cursor = conexion.cursor()  # Crea un cursor para ejecutar operaciones en la base de datos

        while True:
            self.usuario = input("Ingrese un usuario: ")  # Solicita al usuario ingresar un nombre de usuario
            if self.usuario.strip() == "":
                print("El campo de usuario no puede estar vacío.")  # Verifica que el campo no esté vacío
                continue
            cursor.execute("SELECT usuario FROM registro_usuarios WHERE usuario = %s;", (self.usuario,))
            if cursor.fetchone():
                print("El usuario ya está registrado. Intente con otro nombre de usuario.")
                continue
            break

        while True:
            self.correo = input("Ingrese un correo: ")  # Solicita al usuario ingresar un correo electrónico
            if "@" not in self.correo or "." not in self.correo:
                print("Ingrese un correo válido.")  # Verifica que el correo sea válido
            elif self.correo.strip() == "":
                print("El campo de correo no puede estar vacío.")  # Verifica que el campo no esté vacío
            else:
                cursor.execute("SELECT correo FROM registro_usuarios WHERE correo = %s;", (self.correo,))
                if cursor.fetchone():
                    print("El correo ya está registrado. Intente con otro correo electrónico.")
                    continue
                break

        # Etapa de encriptación de contraseña con bcrypt
        while True:
            clave1 = input("Ingrese una clave: ")  # Solicita al usuario ingresar una contraseña
            clave2 = input("Confirme la clave: ")  # Solicita la confirmación de la contraseña
            if clave1.strip() == "" or clave2.strip() == "":
                print("El campo de clave no puede estar vacío.")  # Verifica que el campo no esté vacío
            elif clave1 != clave2:
                print("Las claves no coinciden. Intente nuevamente.")  # Verifica que las claves coincidan
            else:
                self.clave = clave1
                self.password = bytes(self.clave, 'utf-8')  # Convierte la contraseña a bytes
                self.salt = bcrypt.gensalt(rounds=12)  # Genera un salt para la encriptación; ajustar round para mayor proteccion (pero se vuelve lento)
                self.hashed_password = bcrypt.hashpw(self.password, self.salt)  # Encripta la contraseña
                break

        # Generar clave secreta para 2FA
        self.secret = pyotp.random_base32()
        #print("Secret:", self.secret)

        # Crear un URI para la clave secreta (esto es lo que se escanea en la aplicación de autenticación)
        uri = pyotp.totp.TOTP(self.secret).provisioning_uri(name=self.correo, issuer_name='Gestion_Datos')
        #print("URI:", uri)

        # Crear un código QR para escanear en la aplicación de autenticación
        qr = qrcode.make(uri)
        if qr is not None:
            qr.show()
        else:
            print("Error al mostrar QR")    

        # Etapa de guardado de datos en la tabla USUARIOS
        datos = "INSERT INTO registro_usuarios (usuario, correo, clave, secret) VALUES (%s, %s, %s, %s);"  # Prepara la sentencia SQL para insertar datos
        cursor.execute(datos, (self.usuario, self.correo, self.hashed_password, self.secret))  # Ejecuta la sentencia SQL
        print("Registro exitoso")  # Imprime mensaje de registro exitoso
        conexion.commit()  # Confirma la transacción
# Clase que se ejecuta después del registro o solo al iniciar sesión (Se ejecuta después del rebote del registro)
class Inicio_Secion(Registro):
    def __init__(self):
        super().__init__()

    def Inicio(self):
        
        
        
        if conexion is None:
            print("No hay conexión a la base de datos. No se puede iniciar sesión.")
            return None

        #usuario_id = None  # Inicializa usuario_id como None para manejar casos donde el usuario no sea encontrado
        cursor = conexion.cursor()  # Crea un cursor para ejecutar operaciones en la base de datos

        while True:
            self.usuario = input("Ingrese un usuario: ")
            if self.usuario.strip() != "":
                cursor.execute("SELECT usuario, clave, secret FROM registro_usuarios WHERE usuario = %s;", (self.usuario,))
                resultado = cursor.fetchone()
                if resultado:
                    break
                else:
                    print("Usuario no encontrado. Por favor, intente nuevamente.")
            else:
                print("El campo de usuario no puede estar vacío.")

        while True:
            opcion = input("Ingrese '1' para iniciar sesión o '2' si olvidó su contraseña: ")
            if opcion == '1':
                while True:
                    self.clave = getpass.getpass("Ingrese una clave: ")
                    if self.clave.strip() != "":
                        hashed_password = resultado[1]
                        if bcrypt.checkpw(bytes(self.clave, 'utf-8'), bytes(hashed_password, 'utf-8')):
                            print("Contraseña verificada. Ingrese el código 2FA.")
                            secret = resultado[2]
                            totp = pyotp.TOTP(secret)
                            while True:
                                try:
                                    codigo_2fa = input("Ingrese el código 2FA: ")
                                    if totp.verify(codigo_2fa):
                                        print("Inicio de sesión exitoso con 2FA.")
                                        cursor.execute("SELECT id_registro FROM registro_usuarios WHERE usuario = %s;", (self.usuario,))
                                        usuario_ingresado = cursor.fetchone()
                                        if usuario_ingresado is not None:
                                            global usuario_id
                                            usuario_id = usuario_ingresado[0]
                                            print("Atencion ",usuario_id)
                                            
                                        
                                        gestion = RegistrarInfo()
                                        gestion.Gestion_datos()
                                        # Aquí puedes realizar cualquier acción adicional después del inicio de sesión exitoso
                                        return  # Salir del método después del inicio de sesión exitoso
                                    else:
                                        print("Código 2FA incorrecto. Por favor, intente nuevamente.")
                                except Exception as e:
                                    print(f"Error al verificar el código 2FA: {e}")
                        else:
                            print("Contraseña incorrecta. Por favor, intente nuevamente.")
                    else:
                        print("El campo de clave no puede estar vacío.")
            elif opcion == '2':
                print("Proceso de recuperación de contraseña iniciado.")
                secret = resultado[2]
                totp = pyotp.TOTP(secret)
                codigo_2fa = input("Ingrese el código 2FA para verificar su identidad: ")
                if totp.verify(codigo_2fa):
                    nueva_clave = input("Ingrese su nueva contraseña: ")
                    confirmar_clave = input("Confirme su nueva contraseña: ")
                    if nueva_clave == confirmar_clave:
                        hashed_password = bcrypt.hashpw(bytes(nueva_clave, 'utf-8'), bcrypt.gensalt())
                        cursor.execute("UPDATE registro_usuarios SET clave = %s WHERE usuario = %s;", (hashed_password, self.usuario))
                        conexion.commit()
                        print("Su contraseña ha sido actualizada exitosamente.")
                    else:
                        print("Las contraseñas no coinciden. Intente nuevamente.")
                else:
                    print("Código 2FA incorrecto. No se puede verificar su identidad.")
            else:
                print("Opción incorrecta. Por favor, intente nuevamente.")

            '''
            cursor.execute("SELECT id_registro FROM registro_usuarios WHERE usuario = %s;", (self.usuario,))
            usuario_ingresado = cursor.fetchone()
            if usuario_ingresado is not None:
                global usuario_id
                usuario_id = usuario_ingresado[0]
                print("Atencion ",usuario_id)
                return usuario_id
            '''    
        


class RegistrarInfo(Inicio_Secion): 
    
    def __init__(self):
        super().__init__()
        self.red_social = ""
        self.usuario_red_social = ""
        self.clave_red_social = ""
        self.banco = ""
        self.usuario_banco = ""
        self.clave_banco = ""
        self.tipo_correo = ""
        self.correo = ""
        self.clave_correo = ""
        self.pagina = ""
        self.usuario = ""
        self.clave_pagina = ""
        #usuario_id=None


    def Gestion_datos(self):
        
        
        
        try:
            with open('secret.key', 'rb') as key_file:
                key = key_file.read()
        except FileNotFoundError:
            print("Archivo de clave no encontrado. Generando una nueva clave.")
            key = Fernet.generate_key()
            with open('secret.key', 'wb') as key_file:
                key_file.write(key)

        #usuario_id = self.Inicio()

        while True:
            opcion = input("1- para registrar\n"
                        "2- para editar registros \n"
                        "3- para visualizar datos\n"
                        "4- para busqueda manual \n"
                        "5- para salir\n")

            if opcion == "1":
                while True:
                    try:
                        categoria = input("1- para categoria redes sociales\n"
                                        "2- para categoria bancos\n"
                                        "3- para categoria correos\n"
                                        "4- para categoria varios\n"
                                        "5- para salir al menu principal\n")

                        if categoria == "5":
                            break
                        if categoria == "1":
                            cursor = conexion.cursor()
                            cursor.execute("SELECT * FROM cat_redes_sociales;")
                            base_datos = cursor.fetchall()

                            self.red_social = input("Ingrese la red social: ")
                            self.usuario_red_social = input("Ingrese el usuario: ")
                            self.clave_red_social = input("Ingrese la clave: ")

                            cipher_suite = Fernet(key)
                            clave_encriptada = cipher_suite.encrypt(self.clave_red_social.encode('utf-8'))

                            datos = "INSERT INTO cat_redes_sociales (red_social, usuario, clave, relacion_registro_redes) VALUES (%s, %s, %s, %s);"
                            cursor.execute(datos, (self.red_social, self.usuario_red_social, clave_encriptada, usuario_id))
                            print("Registro exitoso.")
                            conexion.commit()
                            break

                        elif categoria == "2":
                            cursor = conexion.cursor()
                            cursor.execute("SELECT * FROM cat_bancos;")
                            base_datos = cursor.fetchall()

                            self.banco = input("Ingrese el tipo de banco: ")
                            self.usuario_banco = input("Ingrese el usuario: ")

                            self.clave_banco = input("Ingrese la clave del banco: ")

                            cipher_suite = Fernet(key)
                            clave_encriptada_banco = cipher_suite.encrypt(self.clave_banco.encode('utf-8'))

                            datos = "INSERT INTO cat_bancos (banco, usuario, clave_banco, relacion_registro_banco) VALUES (%s, %s, %s, %s);"
                            cursor.execute(datos, (self.banco, self.usuario_banco, clave_encriptada_banco, usuario_id))
                            print("Registro exitoso.")
                            conexion.commit()
                            break

                        elif categoria == "3":
                            cursor = conexion.cursor()
                            cursor.execute("SELECT * FROM cat_correos;")
                            base_datos = cursor.fetchall()

                            self.tipo_correo = input("Ingrese el tipo de correo: ")
                            self.correo = input("Ingrese el correo: ")
                            self.clave_correo = input("Ingrese la clave del correo: ")

                            cipher_suite = Fernet(key)
                            clave_encriptada_correo = cipher_suite.encrypt(self.clave_correo.encode('utf-8'))

                            datos = "INSERT INTO cat_correos (tipo_correo, correo, clave_correo, relacion_registro_correos) VALUES (%s, %s, %s, %s);"
                            cursor.execute(datos, (self.tipo_correo, self.correo, clave_encriptada_correo, usuario_id))
                            print("Registro exitoso.")
                            conexion.commit()
                            break

                        elif categoria == "4":
                            cursor = conexion.cursor()
                            cursor.execute("SELECT * FROM cat_varios;")
                            base_datos = cursor.fetchall()

                            self.pagina = input("Ingrese la página: ")
                            self.usuario = input("Ingrese el usuario: ")
                            self.clave_pagina = input("Ingrese la clave: ")

                            cipher_suite = Fernet(key)
                            clave_encriptada_pagina = cipher_suite.encrypt(self.clave_pagina.encode('utf-8'))

                            datos = "INSERT INTO cat_varios (pagina, usuario, clave_pagina, relacion_registro_varios) VALUES (%s, %s, %s, %s);"
                            cursor.execute(datos, (self.pagina, self.usuario, clave_encriptada_pagina, usuario_id))
                            print("Registro exitoso.")
                            conexion.commit()
                            break

                        else:
                            print("Ingrese una opción válida.")
                            break

                    except Exception as e:
                        print(f"Ocurrió un error: {e}")
                        traceback.print_exc()  # Esto imprimirá el traceback completo del error
                        continue


            elif opcion == "2":
                cursor = conexion.cursor()

                try:
                    print("Seleccione una opción:")
                    print("1. Editar datos")
                    print("2. Eliminar datos")
                    opcion_editar_eliminar = input("Ingrese una opción: ")

                    if opcion_editar_eliminar == "1":
                        print("Seleccione la categoría de datos a editar:")
                        print("1. Redes Sociales")
                        print("2. Correos")
                        print("3. Bancos")
                        print("4. Varios")
                        categoria_editar = input("Ingrese una opción: ")

                        if categoria_editar == "1":
                            cursor.execute("SELECT * FROM cat_redes_sociales WHERE relacion_registro_redes = %s;", (usuario_id,))
                            base_datos = cursor.fetchall()
                            for idx, entry in enumerate(base_datos):
                                print(f"{idx + 1}. {entry}")
                            seleccion = int(input("Seleccione el registro a editar: ")) - 1
                            self.red_social = input("Ingrese la nueva red social: ")
                            self.usuario_red_social = input("Ingrese el nuevo usuario: ")
                            self.clave_red_social = input("Ingrese la nueva clave: ")

                            cipher_suite = Fernet(key)
                            clave_encriptada_red_social = cipher_suite.encrypt(self.clave_red_social.encode('utf-8'))

                            datos = "UPDATE cat_redes_sociales SET red_social = %s, usuario = %s, clave = %s WHERE id_redes_sociales = %s;"
                            cursor.execute(datos, (self.red_social, self.usuario_red_social, clave_encriptada_red_social, base_datos[seleccion][0]))
                            print("Actualización exitosa.")
                            conexion.commit()

                        elif categoria_editar == "2":
                            cursor.execute("SELECT * FROM cat_correos WHERE relacion_registro_correos = %s;", (usuario_id,))
                            base_datos = cursor.fetchall()
                            for idx, entry in enumerate(base_datos):
                                print(f"{idx + 1}. {entry}")
                            seleccion = int(input("Seleccione el registro a editar: ")) - 1
                            self.tipo_correo = input("Ingrese el nuevo tipo de correo: ")
                            self.correo = input("Ingrese el nuevo correo: ")
                            self.clave_correo = input("Ingrese la nueva clave: ")

                            cipher_suite = Fernet(key)
                            clave_encriptada_correo = cipher_suite.encrypt(self.clave_correo.encode('utf-8'))

                            datos = "UPDATE cat_correos SET tipo_correo = %s, correo = %s, clave_correo = %s WHERE id_correos = %s;"
                            cursor.execute(datos, (self.tipo_correo, self.correo, clave_encriptada_correo, base_datos[seleccion][0]))
                            print("Actualización exitosa.")
                            conexion.commit()

                        elif categoria_editar == "3":
                            cursor.execute("SELECT * FROM cat_bancos WHERE relacion_registro_banco = %s;", (usuario_id,))
                            base_datos = cursor.fetchall()
                            for idx, entry in enumerate(base_datos):
                                print(f"{idx + 1}. {entry}")
                            seleccion = int(input("Seleccione el registro a editar: ")) - 1
                            self.banco = input("Ingrese el nuevo banco: ")
                            self.usuario_banco = input("Ingrese el nuevo usuario: ")
                            self.clave_banco = input("Ingrese la nueva clave: ")

                            cipher_suite = Fernet(key)
                            clave_encriptada_banco = cipher_suite.encrypt(self.clave_banco.encode('utf-8'))

                            datos = "UPDATE cat_bancos SET banco = %s, usuario = %s, clave_banco = %s WHERE id_banco = %s;"
                            cursor.execute(datos, (self.banco, self.usuario_banco, clave_encriptada_banco, base_datos[seleccion][0]))
                            print("Actualización exitosa.")
                            conexion.commit()

                        elif categoria_editar == "4":
                            cursor.execute("SELECT * FROM cat_varios WHERE relacion_registro_varios = %s;", (usuario_id,))
                            base_datos = cursor.fetchall()
                            for idx, entry in enumerate(base_datos):
                                print(f"{idx + 1}. {entry}")
                            seleccion = int(input("Seleccione el registro a editar: ")) - 1
                            self.pagina = input("Ingrese la nueva página: ")
                            self.usuario_varios = input("Ingrese el nuevo usuario: ")
                            self.clave_pagina = input("Ingrese la nueva clave: ")

                            cipher_suite = Fernet(key)
                            clave_encriptada_pagina = cipher_suite.encrypt(self.clave_pagina.encode('utf-8'))

                            datos = "UPDATE cat_varios SET pagina = %s, usuario = %s, clave_pagina = %s WHERE id_varios = %s;"
                            cursor.execute(datos, (self.pagina, self.usuario_varios, clave_encriptada_pagina, base_datos[seleccion][0]))
                            print("Actualización exitosa.")
                            conexion.commit()

                        else:
                            print("Ingrese una opción válida.")

                    elif opcion_editar_eliminar == "2":
                        print("Seleccione la categoría de datos a eliminar:")
                        print("1. Redes Sociales")
                        print("2. Correos")
                        print("3. Bancos")
                        print("4. Varios")
                        categoria_eliminar = input("Ingrese una opción: ")

                        if categoria_eliminar == "1":
                            cursor.execute("SELECT * FROM cat_redes_sociales WHERE relacion_registro_redes = %s;", (usuario_id,))
                            base_datos = cursor.fetchall()
                            for idx, entry in enumerate(base_datos):
                                print(f"{idx + 1}. {entry}")
                            seleccion = int(input("Seleccione el registro a eliminar: ")) - 1

                            datos = "DELETE FROM cat_redes_sociales WHERE id_redes_sociales = %s;"
                            cursor.execute(datos, (base_datos[seleccion][0],))
                            print("Eliminación exitosa.")
                            conexion.commit()

                        elif categoria_eliminar == "2":
                            cursor.execute("SELECT * FROM cat_correos WHERE relacion_registro_correos = %s;", (usuario_id,))
                            base_datos = cursor.fetchall()
                            for idx, entry in enumerate(base_datos):
                                print(f"{idx + 1}. {entry}")
                            seleccion = int(input("Seleccione el registro a eliminar: ")) - 1

                            datos = "DELETE FROM cat_correos WHERE id_correos = %s;"
                            cursor.execute(datos, (base_datos[seleccion][0],))
                            print("Eliminación exitosa.")
                            conexion.commit()

                        elif categoria_eliminar == "3":
                            cursor.execute("SELECT * FROM cat_bancos WHERE relacion_registro_banco = %s;", (usuario_id,))
                            base_datos = cursor.fetchall()
                            for idx, entry in enumerate(base_datos):
                                print(f"{idx + 1}. {entry}")
                            seleccion = int(input("Seleccione el registro a eliminar: ")) - 1

                            datos = "DELETE FROM cat_bancos WHERE id_banco = %s;"
                            cursor.execute(datos, (base_datos[seleccion][0],))
                            print("Eliminación exitosa.")
                            conexion.commit()

                        elif categoria_eliminar == "4":
                            cursor.execute("SELECT * FROM cat_varios WHERE relacion_registro_varios = %s;", (usuario_id,))
                            base_datos = cursor.fetchall()
                            for idx, entry in enumerate(base_datos):
                                print(f"{idx + 1}. {entry}")
                            seleccion = int(input("Seleccione el registro a eliminar: ")) - 1

                            datos = "DELETE FROM cat_varios WHERE id_varios = %s;"
                            cursor.execute(datos, (base_datos[seleccion][0],))
                            print("Eliminación exitosa.")
                            conexion.commit()

                        else:
                            print("Ingrese una opción válida.")

                    else:
                        print("Ingrese una opción válida.")

                except Exception as e:
                    print(f"Ocurrió un error: {e}")
                    traceback.print_exc()  # Esto imprimirá el traceback completo del error
                    continue



            elif opcion == "3":
                print("Op3")
                cursor = conexion.cursor()

                try:
                    query = """
                    SELECT
                        cr.id_redes_sociales,
                        cr.red_social,
                        cr.usuario AS usuario_red_social,
                        cr.clave AS clave_red_social,
                        cc.id_correos,
                        cc.tipo_correo,
                        cc.correo AS correo_tipo,
                        cc.clave_correo,
                        cb.id_banco,
                        cb.banco,
                        cb.usuario AS usuario_banco,
                        cb.clave_banco,
                        cv.id_varios,
                        cv.pagina,
                        cv.usuario AS usuario_varios,
                        cv.clave_pagina
                    FROM
                        registro_usuarios r
                    LEFT JOIN
                        cat_redes_sociales cr ON cr.relacion_registro_redes = r.id_registro
                    LEFT JOIN
                        cat_correos cc ON cc.relacion_registro_correos = r.id_registro
                    LEFT JOIN
                        cat_bancos cb ON cb.relacion_registro_banco = r.id_registro
                    LEFT JOIN
                        cat_varios cv ON cv.relacion_registro_varios = r.id_registro
                    WHERE
                        r.id_registro = %s;
                    """
                    cursor.execute(query, (usuario_id,))
                    user_data = cursor.fetchall()
                  
                    if user_data:
                        print("Datos del usuario:")
                        cipher_suite = Fernet(key)  # Assuming 'key' is defined and holds the correct Fernet key
                        categorized_entries = {
                            "red_social": set(),
                            "correo": set(),
                            "banco": set(),
                            "varios": set()
                        }
                        
                        for entry in user_data:
                            
                            if entry[1] is not None and entry[2] is not None and entry[3] is not None:
                                try:
                                    clave_desencriptada = cipher_suite.decrypt(entry[3]).decode()
                                    categorized_entries["red_social"].add((entry[1], entry[2], clave_desencriptada))
                                except Exception as e:
                                    print(f"Error desencriptando red_social: {e}")
                                    traceback.print_exc()
                            if entry[5] is not None and entry[6] is not None and entry[7] is not None:
                                try:
                                    clave_desencriptada = cipher_suite.decrypt(entry[7]).decode()
                                    categorized_entries["correo"].add((entry[5], entry[6], clave_desencriptada))
                                except Exception as e:
                                    print(f"Error desencriptando correo: {e}")
                                    traceback.print_exc()
                            if entry[9] is not None and entry[10] is not None and entry[11] is not None:
                                try:
                                    clave_desencriptada = cipher_suite.decrypt(entry[11]).decode()
                                    categorized_entries["banco"].add((entry[9], entry[10], clave_desencriptada))
                                except Exception as e:
                                    print(f"Error desencriptando banco: {e}")
                                    traceback.print_exc()
                            if entry[13] is not None and entry[14] is not None and entry[15] is not None:
                                try:
                                    clave_desencriptada = cipher_suite.decrypt(entry[15]).decode()
                                    categorized_entries["varios"].add((entry[13], entry[14], clave_desencriptada))
                                except Exception as e:
                                    print(f"Error desencriptando varios: {e}")
                                    traceback.print_exc()
                        
                        for category, entries in categorized_entries.items():
                            print(f"Categoría: {category}")
                            #if entries:
                            for entry in entries:
                                print(f"Tipo: {entry[0]}, Usuario: {entry[1]}, Clave: {entry[2]}")
                            #else:
                                # print("No hay datos disponibles en esta categoría.")
                            print("-" * 40)
                        
                    else:
                        print("No se encontraron datos para el usuario.")

                except Exception as e:
                    print(f"Error al recuperar datos: {e}")
                    traceback.print_exc()

            elif opcion == "4":

                cursor = conexion.cursor()

                try:
                    query = """
                    SELECT
                        cr.id_redes_sociales,
                        cr.red_social,
                        cr.usuario AS usuario_red_social,
                        cr.clave AS clave_red_social,
                        cc.id_correos,
                        cc.tipo_correo,
                        cc.correo AS correo_tipo,
                        cc.clave_correo,
                        cb.id_banco,
                        cb.banco,
                        cb.usuario AS usuario_banco,
                        cb.clave_banco,
                        cv.id_varios,
                        cv.pagina,
                        cv.usuario AS usuario_varios,
                        cv.clave_pagina
                    FROM
                        registro_usuarios r
                    LEFT JOIN
                        cat_redes_sociales cr ON cr.relacion_registro_redes = r.id_registro
                    LEFT JOIN
                        cat_correos cc ON cc.relacion_registro_correos = r.id_registro
                    LEFT JOIN
                        cat_bancos cb ON cb.relacion_registro_banco = r.id_registro
                    LEFT JOIN
                        cat_varios cv ON cv.relacion_registro_varios = r.id_registro
                    WHERE
                        r.id_registro = %s;
                    """
                    cursor.execute(query, (usuario_id,))
                    user_data = cursor.fetchall()
                    
                    if user_data:
                        print("Datos del usuario:")
                        cipher_suite = Fernet(key)  # Assuming 'key' is defined and holds the correct Fernet key
                        categorized_entries = {
                            "red_social": set(),
                            "correo": set(),
                            "banco": set(),
                            "varios": set()
                        }
                        
                        for entry in user_data:
                            if entry[1] is not None and entry[2] is not None and entry[3] is not None:
                                try:
                                    clave_desencriptada = cipher_suite.decrypt(entry[3]).decode()
                                    categorized_entries["red_social"].add((entry[1], entry[2], clave_desencriptada))
                                except Exception as e:
                                    print(f"Error desencriptando red_social: {e}")
                                    traceback.print_exc()
                            if entry[5] is not None and entry[6] is not None and entry[7] is not None:
                                try:
                                    clave_desencriptada = cipher_suite.decrypt(entry[7]).decode()
                                    categorized_entries["correo"].add((entry[5], entry[6], clave_desencriptada))
                                except Exception as e:
                                    print(f"Error desencriptando correo: {e}")
                                    traceback.print_exc()
                            if entry[9] is not None and entry[10] is not None and entry[11] is not None:
                                try:
                                    clave_desencriptada = cipher_suite.decrypt(entry[11]).decode()
                                    categorized_entries["banco"].add((entry[9], entry[10], clave_desencriptada))
                                except Exception as e:
                                    print(f"Error desencriptando banco: {e}")
                                    traceback.print_exc()
                            if entry[13] is not None and entry[14] is not None and entry[15] is not None:
                                try:
                                    clave_desencriptada = cipher_suite.decrypt(entry[15]).decode()
                                    categorized_entries["varios"].add((entry[13], entry[14], clave_desencriptada))
                                except Exception as e:
                                    print(f"Error desencriptando varios: {e}")
                                    traceback.print_exc()
                        
                        search_term = input("Ingrese el término de búsqueda: ").lower()
                        found = False
                        for category, entries in categorized_entries.items():
                            for entry in entries:
                                if search_term in entry[0].lower() or search_term in entry[1].lower() or search_term in entry[2].lower():
                                    print(f"Categoría: {category}")
                                    print(f"Tipo: {entry[0]}, Usuario: {entry[1]}, Clave: {entry[2]}")
                                    print("-" * 40)
                                    found = True
                        if not found:
                            print("No se encontraron datos que coincidan con el término de búsqueda.")
                    else:
                        print("No se encontraron datos para el usuario.")

                except Exception as e:
                    print(f"Error al recuperar datos: {e}")
                    traceback.print_exc()
        
            
            
            
            
            
            
            
            
            
            
            
            elif opcion == "5":

                print("Saliendo del programa...")
                exit()


    
# Ejemplo de uso

while True:

    var =input ("1- para registar "
            "2- para iniciar secion "
        )



    if var == "1":
        registro = Registro()
        registro.Registrar()

    elif var == "2":

        inicio_sesion = Inicio_Secion()
        inicio_sesion.Inicio()

    else:
        print("ingrese un opcion valida ")  




