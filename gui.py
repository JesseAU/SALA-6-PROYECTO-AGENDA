import tkinter as tk
from tkinter import ttk
import logic  # Importar el módulo de lógica

def crear_gui():
    root = tk.Tk()
    root.title("Agenda de Tareas Personales")
    root.geometry("700x500")

    # Widgets
    tk.Label(root, text="Descripción:").grid(row=0, column=0, padx=5, pady=5)
    entry_descripcion = tk.Entry(root, width=40)
    entry_descripcion.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Fecha límite (DD/MM/YYYY):").grid(row=1, column=0, padx=5, pady=5)
    entry_fecha = tk.Entry(root)
    entry_fecha.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(root, text="Prioridad:").grid(row=2, column=0, padx=5, pady=5)
    combo_prioridad = ttk.Combobox(root, values=["Alta", "Media", "Baja"], state="readonly")
    combo_prioridad.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(root, text="Estado:").grid(row=3, column=0, padx=5, pady=5)
    combo_estado = ttk.Combobox(root, values=["Pendiente", "En proceso", "Completo"], state="readonly")
    combo_estado.grid(row=3, column=1, padx=5, pady=5)

    # Treeview
    columnas = ("Descripción", "Fecha Límite", "Prioridad", "Estado")
    tabla = ttk.Treeview(root, columns=columnas, show="headings")
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=150)
    tabla.grid(row=5, column=0, columnspan=4, padx=10, pady=10)
    tabla.bind("<<TreeviewSelect>>", lambda event: logic.seleccionar_tarea(event, entry_descripcion, entry_fecha, combo_prioridad, combo_estado, tabla))

    # Botones
    tk.Button(root, text="Agregar", command=lambda: logic.agregar_tarea(entry_descripcion, entry_fecha, combo_prioridad, combo_estado, tabla), bg="lightgreen").grid(row=4, column=0, pady=10)
    tk.Button(root, text="Editar", command=lambda: logic.editar_tarea(entry_descripcion, entry_fecha, combo_prioridad, combo_estado, tabla), bg="lightblue").grid(row=4, column=1, pady=10)
    tk.Button(root, text="Eliminar", command=lambda: logic.eliminar_tarea(tabla), bg="salmon").grid(row=4, column=2, pady=10)
    tk.Button(root, text="Limpiar", command=lambda: logic.limpiar_campos(entry_descripcion, entry_fecha, combo_prioridad, combo_estado)).grid(row=4, column=3, pady=10)

    # Inicializar tareas
    logic.cargar_tareas(tabla)

    root.mainloop()

if __name__ == "__main__":
    crear_gui()
