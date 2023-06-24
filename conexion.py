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
                password="Ismael07",
                db="legislacion_bd",
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listarLeyes(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM ley ORDER BY nro_leyes ASC")
                resultados = cursor.fetchall()
                return resultados
            except mysql.connector.Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def registrarLey(self, ley):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO ley (id_leyes, nro_leyes, fecha, descripcion, categoria, jurisdiccion, or_legislativo, palabra_clave) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}','{5}', '{6}', '{7}')"
                cursor.execute(
                    sql.format(
                        ley[0], ley[1], ley[2], ley[3], ley[4], ley[5], ley[6], ley[7]
                    )
                )
                self.conexion.commit()
                print("¡Ley registrada!\n")
            except mysql.connector.Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarLey(self, ley):
        if self.conexion.is_connected():
            try:
                cursor = ley.conexion.cursor()
                sql = "UPDATE ley SET fecha = '{2}',, descripcion = '{3}', categoria = '{4}', jurisdiccion = '{5}', or_legislativo = '{6}', palabra_clave = '{7}' WHERE id_leyes = '{0}'"
                cursor.execute(
                    sql.format(
                        ley[0], ley[1], ley[2], ley[3], ley[4], ley[5], ley[6], ley[7]
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
                sql = "DELETE FROM ley WHERE id_leyes = '{0}'"
                cursor.execute(sql.format(numeroEliminar))
                self.conexion.commit()
                print("Ley eliminada!\n")
            except mysql.connector.Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
