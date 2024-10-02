import tkinter as tk
from tkinter import messagebox

# Clase principal de la aplicación
class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Lista para almacenar tareas
        self.tareas = []

        # Crear la interfaz gráfica
        self.crear_interfaz()

    def crear_interfaz(self):
        # Entrada de texto para nuevas tareas
        self.entry_tarea = tk.Entry(self.root, width=30)
        self.entry_tarea.grid(row=0, column=0, padx=10, pady=10)
        self.entry_tarea.bind("<Return>", self.agregar_tarea)  # Evento para tecla Enter

        # Botón para añadir tarea
        btn_añadir = tk.Button(self.root, text="Añadir Tarea", command=self.agregar_tarea)
        btn_añadir.grid(row=0, column=1, padx=10, pady=10)

        # Listbox para mostrar las tareas
        self.listbox_tareas = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50, height=10)
        self.listbox_tareas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.listbox_tareas.bind("<Double-Button-1>", self.marcar_completada)  # Evento para doble clic

        # Botón para marcar tarea como completada
        btn_completar = tk.Button(self.root, text="Marcar como Completada", command=self.marcar_completada)
        btn_completar.grid(row=2, column=0, padx=10, pady=10)

        # Botón para eliminar tarea
        btn_eliminar = tk.Button(self.root, text="Eliminar Tarea", command=self.eliminar_tarea)
        btn_eliminar.grid(row=2, column=1, padx=10, pady=10)

    # Función para agregar una nueva tarea
    def agregar_tarea(self, event=None):
        tarea = self.entry_tarea.get().strip()
        if tarea:
            self.tareas.append(tarea)
            self.listbox_tareas.insert(tk.END, tarea)
            self.entry_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    # Función para marcar una tarea como completada
    def marcar_completada(self, event=None):
        seleccion = self.listbox_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            tarea = self.tareas[indice]
            if not tarea.startswith("[Completada]"):
                self.tareas[indice] = "[Completada] " + tarea
                self.listbox_tareas.delete(indice)
                self.listbox_tareas.insert(indice, self.tareas[indice])
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada.")

    # Función para eliminar una tarea
    def eliminar_tarea(self):
        seleccion = self.listbox_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            del self.tareas[indice]
            self.listbox_tareas.delete(indice)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminarla.")

# Función principal
if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()
