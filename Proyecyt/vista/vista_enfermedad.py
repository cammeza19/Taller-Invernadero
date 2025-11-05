import tkinter as tk
from controlador.controlador_enfermedad import ControladorEnfermedad

class VistaEnfermedad:
    def __init__(self, root):
        self.controlador = ControladorEnfermedad()
        root.title("Módulo Enfermedades")
        root.config(bg="#E8F5E9")

        tk.Label(root, text="Registro de Enfermedades", bg="#E8F5E9", fg="#2E7D32", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(root, text="Nombre:", bg="#E8F5E9", fg="#2E7D32").pack()
        self.nombre = tk.Entry(root)
        self.nombre.pack()

        tk.Label(root, text="Descripción:", bg="#E8F5E9", fg="#2E7D32").pack()
        self.descripcion = tk.Entry(root)
        self.descripcion.pack()

        tk.Button(root, text="Registrar", bg="#66BB6A",
                  command=lambda: self.registrar()).pack(pady=5)

        tk.Button(root, text="Guardar en BD", bg="#A5D6A7",
                  command=lambda: self.guardar()).pack(pady=5)

    def registrar(self):
        self.controlador.registrar_enfermedad(self.nombre.get(), self.descripcion.get())

    def guardar(self):
        self.controlador.guardar_en_bd()
