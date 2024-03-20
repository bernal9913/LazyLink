# Description: Aplicación para descargar libros de Redalyc
import sys
import tkinter as tk
from tkinter import filedialog
from descargar_files import iniciar_descarga
from generar_links import generar_enlaces

# Token de acceso a la API de Redalyc
token = "UW5ueFp1b1RidmZZZHlaeVI2T0dxUT09"

def cargar_csv(entry):
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

def cerrar_aplicacion():
    sys.exit(0)

def main():
    global root
    root = tk.Tk()
    root.title("Descargar Libros")
    root.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    csv_label = tk.Label(frame, text="Archivo CSV:")
    csv_label.grid(row=0, column=0, sticky="w")

    csv_entry = tk.Entry(frame, width=50)
    csv_entry.grid(row=0, column=1, padx=5, pady=5)

    csv_button = tk.Button(frame, text="Buscar", command=lambda: cargar_csv(csv_entry))
    csv_button.grid(row=0, column=2, padx=5, pady=5)

    button_generar_enlaces = tk.Button(frame, text="Generar Enlaces", command=lambda: generar_enlaces(frame, csv_entry.get(), token))
    button_generar_enlaces.grid(row=1, column=0, columnspan=3, pady=5)

    button_descargar = tk.Button(frame, text="Descargar Libros", command=lambda: iniciar_descarga(csv_entry.get(), token))
    button_descargar.grid(row=3, column=0, columnspan=3, pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()
