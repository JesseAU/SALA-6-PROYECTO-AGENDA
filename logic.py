from tkinter import messagebox
from datetime import datetime
import json
import os

# Nombre del archivo donde se guardarán las tareas
ARCHIVO_TAREAS = "tareas.json"

# Lista para almacenar las tareas
tareas = []

# ---------------------- Funciones de guardado/carga ---------------------- #
def guardar_tareas():
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
        json.dump(tareas, f, ensure_ascii=False, indent=4)

def cargar_tareas(tabla):
    global tareas
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
            try:
                tareas[:] = json.load(f)
            except json.JSONDecodeError:
                tareas[:] = []
    actualizar_tabla(tabla)

# ---------------------- Funciones de la app ---------------------- #
def actualizar_tabla(tabla):
    for item in tabla.get_children():
        tabla.delete(item)
    for i, tarea in enumerate(tareas):
        tabla.insert("", "end", iid=i, values=tarea)

def agregar_tarea(entry_descripcion, entry_fecha, combo_prioridad, combo_estado, tabla):
    descripcion = entry_descripcion.get()
    fecha_limite = entry_fecha.get()
    prioridad = combo_prioridad.get()
    estado = combo_estado.get()

    if not descripcion or not fecha_limite or not prioridad or not estado:
        messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
        return

    try:
        datetime.strptime(fecha_limite, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Formato de fecha", "La fecha debe estar en formato DD/MM/YYYY.")
        return

    tareas.append((descripcion, fecha_limite, prioridad, estado))
    guardar_tareas()
    actualizar_tabla(tabla)
    limpiar_campos(entry_descripcion, entry_fecha, combo_prioridad, combo_estado)

def editar_tarea(entry_descripcion, entry_fecha, combo_prioridad, combo_estado, tabla):
    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showwarning("Seleccionar", "Seleccione una tarea para editar.")
        return

    index = int(seleccion[0])
    descripcion = entry_descripcion.get()
    fecha_limite = entry_fecha.get()
    prioridad = combo_prioridad.get()
    estado = combo_estado.get()

    if not descripcion or not fecha_limite or not prioridad or not estado:
        messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
        return

    try:
        datetime.strptime(fecha_limite, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Formato de fecha", "La fecha debe estar en formato DD/MM/YYYY.")
        return

    tareas[index] = (descripcion, fecha_limite, prioridad, estado)
    guardar_tareas()
    actualizar_tabla(tabla)
    limpiar_campos(entry_descripcion, entry_fecha, combo_prioridad, combo_estado)

def eliminar_tarea(tabla):
    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showwarning("Seleccionar", "Seleccione una tarea para eliminar.")
        return
    index = int(seleccion[0])
    del tareas[index]
    guardar_tareas()
    actualizar_tabla(tabla)

def limpiar_campos(entry_descripcion, entry_fecha, combo_prioridad, combo_estado):
    entry_descripcion.delete(0, 'end')
    entry_fecha.delete(0, 'end')
    combo_prioridad.set("")
    combo_estado.set("")

def seleccionar_tarea(event, entry_descripcion, entry_fecha, combo_prioridad, combo_estado, tabla):
    seleccion = tabla.selection()
    if seleccion:
        index = int(seleccion[0])
        tarea = tareas[index]
        entry_descripcion.delete(0, 'end')
        entry_descripcion.insert(0, tarea[0])
        entry_fecha.delete(0, 'end')
        entry_fecha.insert(0, tarea[1])
        combo_prioridad.set(tarea[2])
        combo_estado.set(tarea[3])
