"""
Escribe un programa que:
 Lea el fichero usando csv.reader().
 Muestre en pantalla frases como:
 La ciudad de Tokio está en Japón y tiene 37.4 millones de habitantes.
 Controle las posibles excepciones
"""

from os import strerror
import csv

try:
    with open("./Ejercicios/U5/programas_03/ficheros/ciudades.csv") as fichero_csv:
        reader = csv.reader(fichero_csv, delimiter=",")
        cabecera_fila = next(reader)
        for fila in reader:
            print(
                f"La ciudad de {fila[0]} está en {fila[1]} y tiene {fila[2]} de habitantes."
            )
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)
