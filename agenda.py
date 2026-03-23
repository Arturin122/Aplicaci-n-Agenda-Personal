import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Necesita instalación: pip install tkcalendar

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # ===== Frame de lista =====
        frame_lista = tk.Frame(root)
        frame_lista.pack(pady=10)

        # Treeview
        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripcion"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripcion", text="Descripción")
        self.tree.pack()

        # ===== Frame de entrada =====
        frame_entrada = tk.Frame(root)
        frame_entrada.pack(pady=10)

        # Fecha
        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.fecha_entry = DateEntry(frame_entrada)
        self.fecha_entry.grid(row=0, column=1)

        # Hora
        tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0)
        self.hora_entry = tk.Entry(frame_entrada)
        self.hora_entry.grid(row=1, column=1)

        # Descripción
        tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.desc_entry = tk.Entry(frame_entrada)
        self.desc_entry.grid(row=2, column=1)

        # ===== Frame de botones =====
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Eliminar Evento", command=self.eliminar_evento).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=5)

    def agregar_evento(self):
        """Agrega un evento al TreeView"""
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if not hora or not descripcion:
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos")
            return

        self.tree.insert('', 'end', values=(fecha, hora, descripcion))

        # Limpiar campos
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def eliminar_evento(self):
        """Elimina el evento seleccionado"""
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Selección vacía", "Selecciona un evento para eliminar")
            return

        confirmar = messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar este evento?")
        if confirmar:
            self.tree.delete(seleccionado)

# ===== Ejecutar aplicación =====
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()


