"""
Debe:
• Escribir los datos en formato JSON con json.dump().
• Usar los parámetros ensure_ascii=False y indent=4 para mejorar la legibilidad.
• Mostrar el mensaje: "Archivo 'capitales.json' creado correctamente.
"""

from os import strerror
import json

try:
    capitales = [
        {"país": "Francia", "capital": "París"},
        {"país": "Australia", "capital": "Canberra"},
        {"país": "Kenia", "capital": "Nairobi"},
        {"país": "Brasil", "capital": "Brasilia"},
    ]
    with open("./Ejercicios/U5/programas_04/ficheros/capitales.json", "w") as fichero_json:
        json.dump(capitales, fichero_json, ensure_ascii=False, indent=4)
        print("Archivo 'capitales.json' creado correctamente.")
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)
