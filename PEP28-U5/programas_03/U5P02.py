"""
Crea un programa que lea el archivo ciudades.csv usando csv.DictReader().
Debe:
 Mostrar los nombres de las columnas (fieldnames).
 Recorrer las filas e imprimir información como:{Ciudad} ({País}) tiene una población aproximada de {Población(millones)} millones.
 Si el archivo no incluye cabecera, define manualmente los campos necesarios
"""

from os import strerror
import csv

try:
    with open("./Ejercicios/U5/programas_03/ficheros/ciudades.csv") as fichero_csv:
        reader = csv.DictReader(fichero_csv)
        cabeceras = reader.fieldnames
        print(f"Los nombres de las columnas son {cabeceras}")
        for fila in reader:
            print(
                f"La ciudad de {fila[cabeceras[0]]} está en {fila[cabeceras[1]]} y tiene {fila[cabeceras[2]]} de habitantes."
            )
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)