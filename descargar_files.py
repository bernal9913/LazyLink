import csv
import requests
from threading import Thread
from tkinter import messagebox
from generar_links import generar_enlace

def descargar_archivo(enlace, nombre_archivo):
    response = requests.get(enlace)
    if response.status_code == 200:
        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(response.content)
        messagebox.showinfo("Descarga Exitosa", f"Archivo '{nombre_archivo}' descargado exitosamente.")
    else:
        messagebox.showerror("Error de Descarga", f"No se pudo descargar el archivo desde '{enlace}'.")

def descargar_libros(archivo_csv, token):
    if not archivo_csv:
        messagebox.showerror("Error", "Por favor selecciona un archivo CSV.")
        return
    with open(archivo_csv, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo)
        next(lector_csv, None)
        for fila in lector_csv:
            titulo_libro = fila[0]
            enlace_descarga = generar_enlace(titulo_libro, token)
            nombre_archivo = f"{titulo_libro}.xml"
            descargar_archivo(enlace_descarga, nombre_archivo)

def iniciar_descarga(archivo_csv, token):
    t = Thread(target=descargar_libros, args=(archivo_csv, token))
    t.start()

if __name__ == '__main__':
    print("Este script no se debe ejecutar directamente. Por favor ejecuta 'app.py' en su lugar.")