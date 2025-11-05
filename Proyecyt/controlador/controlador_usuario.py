from modelo.modelo_usuario import ModeloUsuario

class ControladorUsuario:
    def __init__(self):
        self.modelo = ModeloUsuario()

    def registrar(self, nombre, usuario, contrasena):
        self.modelo.registrar_usuario(nombre, usuario, contrasena)

    def verificar(self, usuario, contrasena):
        return self.modelo.verificar_usuario(usuario, contrasena)
