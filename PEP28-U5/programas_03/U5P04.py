"""
El programa debe:
 Usar DictWriter con fieldnames=["Ciudad", "País", "Lugar emblemático"].
 Escribir la cabecera con writeheader() y las filas con writerows().
 Cambiar el delimitador a ;.
 Mostrar un mensaje final: "Archivo 'patrimonios.csv' generado correctamente."
"""

from os import strerror
import csv

patrimonios = [
    {"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
    {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
    {"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"}
]

try:
    with open("./Ejercicios/U5/programas_03/ficheros/patrimonios.csv", "w") as fichero_csv:
        writer = csv.DictWriter(fichero_csv, fieldnames=["Ciudad", "País", "Lugar emblemático"], delimiter=";")
        writer.writeheader()
        writer.writerows(patrimonios)
        print("Archivo 'patrimonios.csv' generado correctamente.")
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)
