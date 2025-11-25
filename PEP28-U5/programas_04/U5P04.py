"""
Crea el siguiente diccionario en tu programa:
pais = {
"nombre": "Islandia",
"capital": "Reikiavik",
"idiomas": ["Islandés", "Inglés"],
"superficie_km2": 103000
}
• Convierte el diccionario en una cadena JSON con json.dumps().
• Usa los parámetros indent=2 y sort_keys=True.
• Imprime la cadena generada.
"""

import json

pais = {
    "nombre": "Islandia",
    "capital": "Reikiavik",
    "idiomas": ["Islandés", "Inglés"],
    "superficie_km2": 103000,
}

pais_json = json.dumps(pais, indent=4, sort_keys=True)
print(type(pais_json))
print(pais_json)
