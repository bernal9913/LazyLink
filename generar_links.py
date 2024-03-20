import csv
import tkinter as tk
from tkinter import messagebox

def generar_enlace(titulo_libro, token):
    return f"http://api.redalyc.org/search/title({titulo_libro})/output(xml)/download(yes)/token({token})"

def generar_enlaces(frame, archivo_csv, token):
    if not archivo_csv:
        messagebox.showerror("Error", "Por favor selecciona un archivo CSV.")
        return
    archivo_txt = 'enlaces_generados.txt'
    enlaces_generados = []
    with open(archivo_txt, 'w', encoding='utf-8') as archivo_texto:
        with open(archivo_csv, 'r', encoding='utf-8') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            next(lector_csv, None)
            for fila in lector_csv:
                titulo_libro = fila[0]
                enlace_descarga = generar_enlace(titulo_libro, token)
                enlaces_generados.append(enlace_descarga)
                archivo_texto.write(enlace_descarga + '\n')
    # Crear un campo de texto para mostrar los enlaces generados
    textfield = tk.Text(frame, width=50, height=10)
    textfield.grid(row=2, column=0, columnspan=3, pady=5)
    # Limpiar el campo de texto antes de insertar los enlaces
    textfield.delete(1.0, tk.END)
    # Insertar los enlaces en el campo de texto
    for enlace in enlaces_generados:
        textfield.insert(tk.END, enlace + '\n')
    messagebox.showinfo("Generación de Enlaces", "Los enlaces generados se han guardado en el archivo 'enlaces_generados.txt'.")

if __name__ == '__main__':
    print("Este script no se debe ejecutar directamente. Por favor ejecuta 'app.py' en su lugar.")