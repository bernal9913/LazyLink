import csv
import requests

def descargar_archivo(enlace, nombre_archivo):
    response = requests.get(enlace)
    if response.status_code == 200:
        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(response.content)
        print(f"Archivo '{nombre_archivo}' descargado exitosamente.")
    else:
        print(f"No se pudo descargar el archivo desde '{enlace}'.")

archivo_csv = 'lista_libros.csv'

url_base = 'http://api.redalyc.org/search/title({})/output(xml)/download(yes)/token(UW5ueFp1b1RidmZZZHlaeVI2T0dxUT09)'

with open(archivo_csv, 'r', encoding='utf-8') as archivo:
    lector_csv = csv.reader(archivo)
    # saltillo porque #pedillos
    next(lector_csv, None)
    for fila in lector_csv:
        titulo_libro = fila[0]
        enlace_descarga = url_base.format(titulo_libro)
        nombre_archivo = f"{titulo_libro}.xml"
        descargar_archivo(enlace_descarga, nombre_archivo)
