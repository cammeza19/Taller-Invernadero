from modelo.conexion import conectar

class ModeloUsuario:
    def registrar_usuario(self, nombre, usuario, contrasena):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, usuario, contrasena) VALUES (%s, %s, %s)",
                       (nombre, usuario, contrasena))
        conexion.commit()
        conexion.close()

    def verificar_usuario(self, usuario, contrasena):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario=%s AND contrasena=%s", (usuario, contrasena))
        datos = cursor.fetchone()
        conexion.close()
        return datos
