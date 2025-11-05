# vista/vista_invernadero.py
import tkinter as tk
from tkinter import ttk, messagebox
from controlador.controlador_invernadero import ControladorInvernadero

class VistaInvernadero:
    def __init__(self, root):
        self.root = root
        self.root.title("Módulo Invernadero - GreenGrowth")
        self.root.config(bg="#E8F5E9")
        self.ctrl = ControladorInvernadero()

        # Título
        tk.Label(root, text="Módulo Invernadero", font=("Arial", 16, "bold"),
                 bg="#E8F5E9", fg="#2E7D32").pack(pady=8)

        # Frame formulario (registro)
        form = tk.Frame(root, bg="#E8F5E9")
        form.pack(padx=10, pady=6, fill="x")

        # Labels + Inputs (sin imagenes)
        tk.Label(form, text="Nombre:", bg="#E8F5E9").grid(row=0, column=0, sticky="e", padx=4, pady=4)
        self.nombre = tk.Entry(form, width=30); self.nombre.grid(row=0, column=1, padx=4, pady=4)

        tk.Label(form, text="Tipo de cultivo:", bg="#E8F5E9").grid(row=1, column=0, sticky="e", padx=4, pady=4)
        self.tipo = ttk.Combobox(form, values=["Hortalizas", "Flores", "Ornamentales"], width=28)
        self.tipo.grid(row=1, column=1, padx=4, pady=4)

        tk.Label(form, text="Fecha creación (YYYY-MM-DD):", bg="#E8F5E9").grid(row=2, column=0, sticky="e", padx=4, pady=4)
        self.fecha = tk.Entry(form, width=30); self.fecha.grid(row=2, column=1, padx=4, pady=4)

        tk.Label(form, text="Capacidad de producción:", bg="#E8F5E9").grid(row=3, column=0, sticky="e", padx=4, pady=4)
        self.capacidad = tk.Entry(form, width=30); self.capacidad.grid(row=3, column=1, padx=4, pady=4)

        tk.Label(form, text="Responsable:", bg="#E8F5E9").grid(row=4, column=0, sticky="e", padx=4, pady=4)
        self.responsable = tk.Entry(form, width=30); self.responsable.grid(row=4, column=1, padx=4, pady=4)

        tk.Label(form, text="Superficie (m²):", bg="#E8F5E9").grid(row=5, column=0, sticky="e", padx=4, pady=4)
        self.superficie = tk.Entry(form, width=30); self.superficie.grid(row=5, column=1, padx=4, pady=4)

        # Botones de acción (usar lambda)
        btn_frame = tk.Frame(root, bg="#E8F5E9")
        btn_frame.pack(pady=8)
        tk.Button(btn_frame, text="Guardar", bg="#66BB6A",
                  command=lambda: self._guardar()).pack(side="left", padx=6)
        tk.Button(btn_frame, text="Limpiar", bg="#A5D6A7",
                  command=lambda: self._limpiar_campos()).pack(side="left", padx=6)
        tk.Button(btn_frame, text="Mostrar Invernaderos", bg="#8BC34A",
                  command=lambda: self._mostrar_lista()).pack(side="left", padx=6)

        # Separador
        ttk.Separator(root, orient="horizontal").pack(fill="x", pady=6)

        # Area de lista con Treeview + botones para ver/eliminar
        tk.Label(root, text="Lista de Invernaderos", bg="#E8F5E9", fg="#2E7D32", font=("Arial", 12, "bold")).pack(pady=4)
        cols = ("id", "nombre", "tipo_cultivo", "superficie_m2", "responsable", "fecha_creacion")
        self.tree = ttk.Treeview(root, columns=cols, show="headings", height=8)
        for c in cols:
            self.tree.heading(c, text=c.capitalize())
            self.tree.column(c, anchor="center")
        self.tree.pack(padx=10, pady=6, fill="x")

        action_frame = tk.Frame(root, bg="#E8F5E9")
        action_frame.pack(pady=6)
        tk.Button(action_frame, text="Ver Detalle", bg="#66BB6A",
                  command=lambda: self._ver_detalle_seleccionado()).pack(side="left", padx=6)
        tk.Button(action_frame, text="Eliminar", bg="#EF9A9A",
                  command=lambda: self._eliminar_seleccionado()).pack(side="left", padx=6)
        tk.Button(action_frame, text="Refrescar", bg="#A5D6A7",
                  command=lambda: self._mostrar_lista()).pack(side="left", padx=6)

        # cargar lista inicial
        self._mostrar_lista()

    def _validar_campos(self):
        if not self.nombre.get().strip():
            messagebox.showwarning("Validación", "El nombre es obligatorio")
            return False
        # superficie debe ser convertible a float
        try:
            if self.superficie.get().strip() != "":
                float(self.superficie.get().strip())
        except ValueError:
            messagebox.showwarning("Validación", "Superficie debe ser un número (ej: 12.5)")
            return False
        # fecha si no está vacía comprobar formato simple YYYY-MM-DD
        f = self.fecha.get().strip()
        if f:
            parts = f.split("-")
            if len(parts) != 3 or not all(p.isdigit() for p in parts):
                messagebox.showwarning("Validación", "Fecha debe tener formato YYYY-MM-DD o dejarla vacía")
                return False
        return True

    def _guardar(self):
        if not self._validar_campos():
            return
        datos = {
            'nombre': self.nombre.get().strip(),
            'tipo_cultivo': self.tipo.get().strip(),
            'fecha_creacion': self.fecha.get().strip() or None,
            'capacidad_produccion': self.capacidad.get().strip(),
            'responsable': self.responsable.get().strip(),
            'superficie_m2': float(self.superficie.get().strip()) if self.superficie.get().strip() else None
        }
        try:
            self.ctrl.guardar(datos)
            messagebox.showinfo("Guardado", "Invernadero registrado correctamente")
            self._limpiar_campos()
            self._mostrar_lista()  # refrescar inmediatamente
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar: {e}")

    def _limpiar_campos(self):
        self.nombre.delete(0, tk.END)
        self.tipo.set("")
        self.fecha.delete(0, tk.END)
        self.capacidad.delete(0, tk.END)
        self.responsable.delete(0, tk.END)
        self.superficie.delete(0, tk.END)

    def _mostrar_lista(self):
        # vaciar tree
        for fila in self.tree.get_children():
            self.tree.delete(fila)
        try:
            filas = self.ctrl.listar()
            for r in filas:
                # r = (id, nombre, tipo_cultivo, fecha_creacion, capacidad_produccion, responsable, superficie_m2, fecha_registro)
                # mostramos columnas relevantes
                self.tree.insert("", "end", values=(r[0], r[1], r[2] or "", r[6] if r[6] is not None else "", r[5] or "", r[3] or ""))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar lista: {e}")

    def _get_id_seleccionado(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Seleccionar", "Selecciona un invernadero de la lista")
            return None
        item = sel[0]
        valores = self.tree.item(item, "values")
        if not valores:
            return None
        return int(valores[0])

    def _eliminar_seleccionado(self):
        id_sel = self._get_id_seleccionado()
        if id_sel is None:
            return
        confirmar = messagebox.askyesno("Confirmar", "¿Eliminar el invernadero seleccionado?")
        if not confirmar:
            return
        try:
            self.ctrl.eliminar(id_sel)
            messagebox.showinfo("Eliminado", "Invernadero eliminado")
            self._mostrar_lista()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar: {e}")

    def _ver_detalle_seleccionado(self):
        id_sel = self._get_id_seleccionado()
        if id_sel is None:
            return
        detalle = self.ctrl.obtener(id_sel)
        if not detalle:
            messagebox.showerror("Error", "No se pudo obtener detalle")
            return
        # detalle es tuple: (id, nombre, tipo_cultivo, fecha_creacion, capacidad_produccion, responsable, superficie_m2, fecha_registro)
        top = tk.Toplevel(self.root)
        top.title(f"Detalle - Invernadero {detalle[1]}")
        top.config(bg="#F1F8E9")
        campos = [
            ("ID", detalle[0]),
            ("Nombre", detalle[1]),
            ("Tipo de cultivo", detalle[2] or ""),
            ("Fecha creación", detalle[3] or ""),
            ("Capacidad de producción", detalle[4] or ""),
            ("Responsable", detalle[5] or ""),
            ("Superficie (m2)", detalle[6] if detalle[6] is not None else ""),
            ("Fecha registro", detalle[7] or "")
        ]
        for i, (etq, val) in enumerate(campos):
            tk.Label(top, text=f"{etq}:", bg="#F1F8E9", anchor="e", width=20).grid(row=i, column=0, sticky="e", padx=6, pady=4)
            tk.Label(top, text=str(val), bg="#F1F8E9", anchor="w", width=40, relief="sunken").grid(row=i, column=1, sticky="w", padx=6, pady=4)
        tk.Button(top, text="Cerrar", command=lambda: top.destroy(), bg="#A5D6A7").grid(row=len(campos), column=0, columnspan=2, pady=8)
