import tkinter as tk
from vista.vista_invernadero import VistaInvernadero
from vista.vista_enfermedad import VistaEnfermedad

class VistaMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("GreenGrowth - Menú")
        self.root.config(bg="#E8F5E9")

        tk.Label(root, text="Panel de Control", font=("Arial", 16, "bold"), bg="#E8F5E9", fg="#2E7D32").pack(pady=10)

        tk.Button(root, text="Módulo Invernadero", bg="#66BB6A",
                  command=lambda: VistaInvernadero(tk.Toplevel(root))).pack(pady=5)

        tk.Button(root, text="Módulo Enfermedades", bg="#A5D6A7",
                  command=lambda: VistaEnfermedad(tk.Toplevel(root))).pack(pady=5)
