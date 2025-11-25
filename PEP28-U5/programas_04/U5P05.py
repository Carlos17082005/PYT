"""
Crea un programa que:
• Lea el archivo paises.json del ejercicio 1.
• Pida al usuario el nombre de un continente.
• Muestre solo los países pertenecientes a ese continente.
• Guarde esos resultados en un nuevo archivo JSON llamado paises_filtrados.json
"""

from os import strerror
import json

try:
    with open(
        "./Ejercicios/U5/programas_04/ficheros/paises.json", "r", encoding="utf-8"
    ) as fichero_json1:
        datos = json.load(fichero_json1)
        continente = input("Introduce el nombre de un continente: ")
        for fila in datos:
            if fila["continente"].lower() == continente.lower():
                print(
                    f"{fila['nombre']} está en {fila['continente']} y tiene {fila['poblacion']} millones de habitantes."
                )
                with open("./Ejercicios/U5/programas_04/ficheros/paises_filtrados.json", "w", encoding="utf-8",) as fichero_json2:
                    json.dump(fila, fichero_json2, ensure_ascii=False, indent=4)
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)
