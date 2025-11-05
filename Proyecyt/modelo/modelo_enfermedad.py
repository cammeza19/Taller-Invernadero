from modelo.conexion import conectar

class ModeloEnfermedad:
    def __init__(self):
        self.enfermedades_dict = {}

    def registrar_en_diccionario(self, nombre, descripcion):
        self.enfermedades_dict[nombre] = descripcion

    def guardar_en_bd(self):
        conexion = conectar()
        cursor = conexion.cursor()
        for nombre, descripcion in self.enfermedades_dict.items():
            cursor.execute("INSERT INTO enfermedades (nombre, descripcion) VALUES (%s, %s)", (nombre, descripcion))
        conexion.commit()
        conexion.close()
