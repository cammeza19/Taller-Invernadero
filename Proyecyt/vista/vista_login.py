import tkinter as tk
from tkinter import messagebox
from controlador.controlador_usuario import ControladorUsuario
from vista.vista_menu import VistaMenu

class VistaLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("GreenGrowth - Login")
        self.root.config(bg="#E8F5E9")

        self.controlador = ControladorUsuario()

        tk.Label(root, text="GreenGrowth 🌿", font=("Arial", 18, "bold"), bg="#E8F5E9", fg="#2E7D32").pack(pady=10)
        tk.Label(root, text="Usuario:", bg="#E8F5E9", fg="#2E7D32").pack()
        self.usuario = tk.Entry(root)
        self.usuario.pack()

        tk.Label(root, text="Contraseña:", bg="#E8F5E9", fg="#2E7D32").pack()
        self.contrasena = tk.Entry(root, show="*")
        self.contrasena.pack()

        tk.Button(root, text="Ingresar", bg="#66BB6A", command=lambda: self.login()).pack(pady=5)
        tk.Button(root, text="Registrar", bg="#A5D6A7", command=lambda: self.registrar()).pack()

    def login(self):
        user = self.usuario.get()
        pwd = self.contrasena.get()
        datos = self.controlador.verificar(user, pwd)
        if datos:
            self.root.destroy()
            nueva = tk.Tk()
            VistaMenu(nueva)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def registrar(self):
        self.controlador.registrar("Nuevo", self.usuario.get(), self.contrasena.get())
        messagebox.showinfo("Éxito", "Usuario registrado correctamente")
