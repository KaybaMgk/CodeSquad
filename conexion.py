# Importamos los conectores a MySQL
import mysql.connector
from mysql.connector import Error

# creando clase

class db_leyes:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                port=3307,
                user="root",
                password="",
                db="proyecto",
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listarLeyes(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM leyes ORDER BY nro_leyes ASC")
                resultados = cursor.fetchall()
                return resultados
            except mysql.connector.Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def registrarLey(self, leyes):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO leyes (id_leyes, nro_leyes, fecha, descripcion, categoria, jurisdiccion, or_legislativo, palabra_clave) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}','{5}', '{6}', '{7}')"
                cursor.execute(
                    sql.format(
                        leyes[0], leyes[1], leyes[2], leyes[3], leyes[4], leyes[5], leyes[6], leyes[7]
                    )
                )
                self.conexion.commit()
                print("¡Ley registrada!\n")
            except mysql.connector.Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarLey(self, leyes):
        if self.conexion.is_connected():
            try:
                cursor = leyes.conexion.cursor()
                sql = "UPDATE leyes SET fecha = '{2}',, descripcion = '{3}', categoria = '{4}', jurisdiccion = '{5}', or_legislativo = '{6}', palabra_clave = '{7}' WHERE id_leyes = '{0}'"
                cursor.execute(
                    sql.format(
                        leyes[0], leyes[1], leyes[2], leyes[3], leyes[4], leyes[5], leyes[6], leyes[7]
                    )
                )
                self.conexion.commit()
                print("Ley actualizada!\n")
            except mysql.connector.Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminarLey(self, numeroEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM leyes WHERE id_leyes = '{0}'"
                cursor.execute(sql.format(numeroEliminar))
                self.conexion.commit()
                print("Ley eliminada!\n")
            except mysql.connector.Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
