"""""
import tkinter as tk
from tkinter import messagebox
import random
import math
import csv
import os
proyectos = []
archivo_csv = 'registro.csv'


def cargar_proyectos():
    if os.path.exists(archivo_csv):
        with open(archivo_csv, newline='') as f:
            reader = csv.DictReader(f)
            for fila in reader:
                proyectos.append(fila)

def guardar_proyectos():
    if proyectos:
        with open(archivo_csv, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=proyectos[0].keys())
            writer.writeheader()
            writer.writerows(proyectos)

def registrar_proyecto():
    etiqueta = entry_nombre.get()
    try:
        valor_base = float(entry_longitud.get())
    except ValueError:
        messagebox.showerror("Error", "La longitud debe ser un número.")
        return

    angulo = random.uniform(30, 60)
    radianes = math.radians(angulo)
    resultado = math.tan(radianes) * valor_base

    fila = {
        'etiqueta': etiqueta,
        'angulo': round(angulo, 2),
        'valor_base': valor_base,
        'resultado': round(resultado, 2)
    }

    proyectos.append(fila)
    guardar_proyectos()

    entry_nombre.delete(0, tk.END)
    entry_longitud.delete(0, tk.END)
    messagebox.showinfo("listo :)", "Proyecto registrado.")

def ver_proyecto():
    try:
        index = int(entry_indice.get())
        fila = proyectos[index]
        texto = f"Etiqueta: {fila['etiqueta']}\nÁngulo: {fila['angulo']}°\nLongitud: {fila['valor_base']}\nResultado: {fila['resultado']}"
        messagebox.showinfo("Proyecto", texto)
    except:
        messagebox.showerror("Error", "Funcion invalida.")

def eliminar_proyecto():
    try:
        index = int(entry_indice.get())
        proyectos.pop(index)
        guardar_proyectos()
        messagebox.showinfo("Listo :)", "Proyecto eliminado.")
    except:
        messagebox.showerror("Error", "Funcion invalida")

# GUI
ventana = tk.Tk()
ventana.title("Registro de proyectos")

tk.Label(ventana, text="Nombre del proyecto:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Longitud (lado adyacente):").pack()
entry_longitud = tk.Entry(ventana)
entry_longitud.pack()

tk.Button(ventana, text="Registrar pryecto", command=registrar_proyecto).pack(pady=5)

tk.Label(ventana, text="Índice del proyecto:").pack()
entry_indice = tk.Entry(ventana)
entry_indice.pack()

tk.Button(ventana, text="Ver proyecto", command=ver_proyecto).pack(pady=2)
tk.Button(ventana, text="Eliminar proyecto", command=eliminar_proyecto).pack(pady=2)


cargar_proyectos()

ventana.mainloop()
"""""

import tkinter as tk
from tkinter import messagebox
import random
import math
import csv
import os


proyectos = []
archivo_csv = 'registro.csv'  

def cargar_proyectos():
    if os.path.exists(archivo_csv): 
        with open(archivo_csv, newline='') as f:  
            reader = csv.DictReader(f)  
            for fila in reader: 
                proyectos.append(fila)  
    else:
        print("Aún no hay archivo, se creará uno nuevo")  

def guardar_proyectos():
    if proyectos: 
        with open(archivo_csv, 'w', newline='') as f:
         
            writer = csv.DictWriter(f, fieldnames=proyectos[0].keys())
            writer.writeheader()  
            writer.writerows(proyectos) 


def registrar_proyecto():
    etiqueta = entry_nombre.get() 
    try:
        valor_base = float(entry_longitud.get())
    except ValueError:
        messagebox.showerror("Error", "La longitud debe ser un número, ¡no letras!")
        return

    angulo = random.uniform(30, 60)
    radianes = math.radians(angulo)  
    resultado = math.tan(radianes) * valor_base 


    fila = {
        'etiqueta': etiqueta,
        'angulo': round(angulo, 2),  
        'valor_base': valor_base,
        'resultado': round(resultado, 2)
    }

    proyectos.append(fila)  
    guardar_proyectos()  

    entry_nombre.delete(0, tk.END)
    entry_longitud.delete(0, tk.END)
    messagebox.showinfo("¡Listo!", "Proyecto registrado correctamente :)")

def ver_proyecto():
    try:
        index = int(entry_indice.get())  
        fila = proyectos[index]  
        texto = f"Nombre: {fila['etiqueta']}\nÁngulo: {fila['angulo']}°\nBase: {fila['valor_base']}\nAltura: {fila['resultado']}"
        messagebox.showinfo("Detalles del proyecto", texto)
    except:
        messagebox.showerror("Error", "¡Ese proyecto no existe o el índice es incorrecto!")

def eliminar_proyecto():
    try:
        index = int(entry_indice.get()) 
        proyectos.pop(index)  
        guardar_proyectos()  
        messagebox.showinfo("Eliminado", "Proyecto borrado sin problema")
    except:
        messagebox.showerror("Error", "No pude eliminar, ¿seguro que el índice es válido?")


ventana = tk.Tk()
ventana.title("Proyectos de Trigonometría")  # Título de la ventana

# Campos para el nombre del proyecto
tk.Label(ventana, text="Nombre del proyecto:").pack()
entry_nombre = tk.Entry(ventana, width=30)  # Un poco más ancho
entry_nombre.pack()

# Campo para la longitud (base del triángulo)
tk.Label(ventana, text="Longitud (lado adyacente):").pack()
entry_longitud = tk.Entry(ventana)
entry_longitud.pack()

# Botón para registrar (con typo deliberado)
tk.Button(ventana, text="Registrar Proyecto", command=registrar_proyecto).pack(pady=5)

# Campo para el índice (para ver/eliminar)
tk.Label(ventana, text="Índice del proyecto:").pack()
entry_indice = tk.Entry(ventana)
entry_indice.pack()

# Botones secundarios (más pequeños)
tk.Button(ventana, text="Ver proyecto", command=ver_proyecto).pack(pady=2)
tk.Button(ventana, text="Eliminar proyecto", command=eliminar_proyecto).pack(pady=2)

# Cargamos los proyectos al iniciar
cargar_proyectos()

ventana.mainloop()  # Esto hace que la ventana no se cierre


