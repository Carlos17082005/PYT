"""
Crea un programa que genere un fichero nuevo llamado capitales.csv con los
siguientes datos:
Ciudad País Continente
París Francia Europa
Canberra Australia Oceanía
Nairobi Kenia África
Ottawa Canadá América
El programa debe:
 Escribir la cabecera y los datos con writerow() y writerows().
 Usar un bloque try/except con os.strerror() para capturar errores de E/S.
 Confirmar con un mensaje final: "Archivo 'capitales.csv' creado
correctamente.
"""

from os import strerror
import csv

cabeceras = ["Ciudad", "País", "Continente"]
data = [
    ["París", "Francia", "Europa"],
    ["Canberra", "Australia", "Oceanía"],
    ["Nairobi", "Kenia", "África"],
    ["Ottawa", "Canadá", "América"],
]
try:
    with open("./Ejercicios/U5/programas_03/ficheros/capitales.csv", "w") as fichero_csv:
        writer = csv.writer(fichero_csv)
        writer.writerow(cabeceras)
        writer.writerows(data)
        print("Archivo 'capitales.csv' creado correctamente.")
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)
