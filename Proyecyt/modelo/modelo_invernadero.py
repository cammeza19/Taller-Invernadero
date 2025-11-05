from modelo.conexion import conectar

class ModeloInvernadero:
    def guardar_invernadero(self, datos):
        """
        datos: dict con keys:
        nombre, tipo_cultivo, fecha_creacion (YYYY-MM-DD), capacidad_produccion, responsable, superficie_m2
        """
        conexion = conectar()
        cursor = conexion.cursor()
        sql = """
            INSERT INTO invernadero
            (nombre, tipo_cultivo, fecha_creacion, capacidad_produccion, responsable, superficie_m2)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (
            datos.get('nombre'),
            datos.get('tipo_cultivo'),
            datos.get('fecha_creacion'),
            datos.get('capacidad_produccion'),
            datos.get('responsable'),
            datos.get('superficie_m2'),
        ))
        conexion.commit()
        cursor.close()
        conexion.close()

    def listar_invernaderos(self):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id, nombre, tipo_cultivo, fecha_creacion, capacidad_produccion, responsable, superficie_m2, fecha_registro
            FROM invernadero
            ORDER BY fecha_registro DESC
        """)
        filas = cursor.fetchall()
        cursor.close()
        conexion.close()
        return filas

    def eliminar_invernadero(self, id_invernadero):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM invernadero WHERE id = %s", (id_invernadero,))
        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_invernadero(self, id_invernadero):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id, nombre, tipo_cultivo, fecha_creacion, capacidad_produccion, responsable, superficie_m2, fecha_registro
            FROM invernadero
            WHERE id = %s
        """, (id_invernadero,))
        fila = cursor.fetchone()
        cursor.close()
        conexion.close()
        return fila
