from modelo.modelo_enfermedad import ModeloEnfermedad

class ControladorEnfermedad:
    def __init__(self):
        self.modelo = ModeloEnfermedad()

    def registrar_enfermedad(self, nombre, descripcion):
        self.modelo.registrar_en_diccionario(nombre, descripcion)

    def guardar_en_bd(self):
        self.modelo.guardar_en_bd()
