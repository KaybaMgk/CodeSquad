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
    