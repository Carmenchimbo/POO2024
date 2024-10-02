import tkinter as tk
from tkinter import messagebox


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("400x400")
        self.tasks = []

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", self.add_task)  # Atajo de teclado Enter

        # Botones
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.mark_completed)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Lista para mostrar las tareas
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Atajos de teclado
        root.bind("<c>", lambda event: self.mark_completed())  # Tecla "C" para completar tarea
        root.bind("<d>", lambda event: self.delete_task())  # Tecla "D" para eliminar tarea
        root.bind("<Delete>", lambda event: self.delete_task())  # Tecla "Delete" para eliminar tarea
        root.bind("<Escape>", lambda event: self.close_app)  # Tecla "Escape" para cerrar app

    def add_task(self, event=None):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")

    def mark_completed(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index]["completed"] = True
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def delete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = task["task"]
            if task["completed"]:
                display_text = f"[Completada] {display_text}"
            self.task_listbox.insert(tk.END, display_text)

    def close_app(self, event=None):
        self.root.quit()


# Configuración de la ventana principal
root = tk.Tk()
app = TaskManager(root)
root.mainloop()
