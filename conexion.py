import mysql.connector
#creando clase
class db_leyes():
    def __init__(self,host,user,password,port ,database,auth_plugin='mysql_native_password'):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.connection = None
        self.auth_plugin = auth_plugin
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port, 
                database=self.database,
                auth_plugin=self.auth_plugin
                
            )
            print("Conexión exitosa a la base de datos.")
        except mysql.connector.Error as error:

            print("No se pudo establecer la conexión: {}".format(error))

    def close(self):  
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")

conexion = db_leyes(
    host = 'localhost',
    user = 'root',
    password = 'root',
    port = '3306',
    database = 'proyecto'
    )

class funciones():

    def listarLeyes(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM ley ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except mysql.connector.Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def registrarLey(self, ley):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO ley (id_leyes, nro_leyes, fecha, descripcion, categoria, jurisdiccion, or_legislativo, palabra_clave) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}','{5}', '{6}', '{7}')"
                cursor.execute(sql.format(ley[0], ley[1], ley[2], ley[3], ley[4], ley[5], ley[6], ley[7]))
                self.conexion.commit()
                print("¡Ley registrada!\n")
            except mysql.connector.Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarLey(self, ley):
        if self.conexion.is_connected():
            try:
                cursor = ley.conexion.cursor()
                sql = "UPDATE ley SET fecha = '{2}',, descripcion = '{3}', categoria = '{4}', jurisdiccion = '{5}', or_legislativo = '{6}', palabra_clave = '{7}' WHERE id_leyes = '{0}'"
                cursor.execute(sql.format(ley[0], ley[1], ley[2], ley[3], ley[4], ley[5], ley[6], ley[7]))
                self.conexion.commit()
                print("Ley actualizada!\n")
            except mysql.connector.Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminarLey(self, numeroEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM ley WHERE id_leyes = '{0}'"
                cursor.execute(sql.format(numeroEliminar))
                self.conexion.commit()
                print("Ley eliminada!\n")
            except mysql.connector.Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

conexion.connect()

#Aqui es donde escribiran el codigo para que se ejecuten en mysql

conexion.close()

=======
import mysql.connector
#creando clase
class db_leyes():
    def __init__(self,host,user,password,port ,database,auth_plugin='mysql_native_password'):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.connection = None
        self.auth_plugin = auth_plugin
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port, 
                database=self.database,
                auth_plugin=self.auth_plugin
                
            )
            print("Conexión exitosa a la base de datos.")
        except mysql.connector.Error as error:

            print("No se pudo establecer la conexión: {}".format(error))

    def close(self):  
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")

conexion = db_leyes(
    host = 'localhost',
    user = 'root',
    password = 'pon tu contraseña',
    port = '3306',
    database = 'proyecto'

)

#Crear un metodo o sea un def para llenar los valores de la leyes



conexion.connect()

#Aqui es donde escribiran el codigo para que se ejecuten en mysql


conexion.close()
