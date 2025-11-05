# controlador/controlador_invernadero.py
from modelo.modelo_invernadero import ModeloInvernadero

class ControladorInvernadero:
    def __init__(self):
        self.modelo = ModeloInvernadero()

    def guardar(self, datos):
        # puedes añadir validaciones básicas aquí si lo deseas
        self.modelo.guardar_invernadero(datos)

    def listar(self):
        return self.modelo.listar_invernaderos()

    def eliminar(self, id_invernadero):
        self.modelo.eliminar_invernadero(id_invernadero)

    def obtener(self, id_invernadero):
        return self.modelo.obtener_invernadero(id_invernadero)
