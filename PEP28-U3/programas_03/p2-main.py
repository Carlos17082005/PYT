"""
programa02
Modifica el programa principal (main,py) del ejercicio anterior para que siga la siguiente
estructura.
# imports de la librería estándar
# imports de librerías de terceros
# imports de módulos propios

# Definición de funciones principales
def main():
    '''Función principal del programa'''
    print("Hola, este es el programa principal")

# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    # Se pueden procesar argumentos, inicializar variables, etc.
    main()
"""

import operaciones


def main():
    a = float(input("Introduce un numero: "))
    b = float(input("Introduce otro numero: "))

    print(operaciones.suma(a, b))
    print(operaciones.resta(a, b))
    print(operaciones.multiplicacion(a, b))
    print(operaciones.divicion(a, b))


if __name__ == "__main__":
    main()
