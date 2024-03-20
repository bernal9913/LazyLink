import csv

def generar_enlace(titulo_libro, token):
    return f"http://api.redalyc.org/search/title({titulo_libro})/output(xml)/download(yes)/token({token})"

archivo_csv = 'lista_libros.csv'
token = "UW5ueFp1b1RidmZZZHlaeVI2T0dxUT09" # separado para mas placer
archivo_txt = 'enlaces_generados.txt'

# Abrir el archivo de texto en modo escritura
with open(archivo_txt, 'w', encoding='utf-8') as archivo_texto:
    with open(archivo_csv, 'r', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        # saltillo porque hay peditos
        next(lector_csv, None)
        for fila in lector_csv:
            titulo_libro = fila[0]
            enlace_descarga = generar_enlace(titulo_libro, token)
            archivo_texto.write(enlace_descarga + '\n')

print("Los enlaces generados se han guardado en el archivo 'enlaces_generados.txt'.")