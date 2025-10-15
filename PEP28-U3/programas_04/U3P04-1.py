'''
programa01
Crea un paquete llamado matemáticas que contenga tres módulos:
 operaciones: creado en la práctica anterior.
 figuras: tendrá las siguientes funciones.
◦ area_rectangulo(base, altura): devuelve el área.
◦ area_triangulo(base, altura): devuelve el área.
◦ area_circulo(radio): devuelve el área.
 conversiones.py: tendrá las siguientes funciones
◦ a_binario(n): devuelve la representación binaria de un número entero en forma
de cadena.
◦ a_hexadecimal(n): devuelve la representación hexadecimal de un número
entero en forma de cadena.
◦ a_entero(texto): convierte una cadena numérica en un entero (controlando
errores si el texto no es válido)
Recuerda que debes incluir el fichero __init__.py aunque esté vacío.
Crea un programa principal main.py que muestre un menú que permita elegir entre:
 Operaciones matemáticas
 Cálculo de áreas geométricas
Según la opción elegida, pida al usuario los datos necesarios y muestre el resultado
correspondiente.
# imports de la librería estándar
# imports de librerías de terceros
# imports de módulos propios
# Definición de funciones principales
def main():
"""Función principal del programa"""
print("Hola, este es el programa principal")
# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
# Se pueden procesar argumentos, inicializar variables, etc.
main()
'''

from matematicas import operaciones, figuras


def menu():
    print(
        "1. Operaciones matemáticas\n" "2. Cálculo de áreas geométricas\n" "3. Salir\n"
    )


def mat():
    a = float(input("Introduce un numero: "))
    b = float(input("Introduce otro numero: "))
    return (a, b)


def menu_mat():
    print("1. Suma\n" "2. Resta\n" "3. Multiplicacion\n" "4. Divicion\n" "5. Salir\n")
    opcion = input("Introduce una opción (1-5): ")
    match opcion:
        case "1":
            a, b = mat()
            print(operaciones.suma(a, b))
        case "2":
            a, b = mat()
            print(operaciones.resta(a, b))
        case "3":
            a, b = mat()
            print(operaciones.multiplicacion(a, b))
        case "4":
            a, b = mat()
            print(operaciones.divicion(a, b))
        case "5":
            print("Programa fianlizado")
        case _:
            print("Opcion invalida")
            menu_mat()


def aC():
    r = float(input("Introduce el radio: "))
    return r


def ar():
    a = float(input("Introduce la base: "))
    b = float(input("Introduce la altura: "))
    return (a, b)


def menu_ag():
    print("1. area_circulo\n" "2. area_triangulo\n" "3. area_rectangulo\n" "4. Salir\n")
    opcion = input("Introduce una opción (1-5): ")
    match opcion:
        case "1":
            a = aC()
            print(figuras.area_circulo(a))
        case "2":
            a, b = ar()
            print(figuras.area_triangulo(a, b))
        case "3":
            a, b = ar()
            print(figuras.area_rectangulo(a, b))
        case "4":
            print("Programa fianlizado")
        case _:
            print("Opcion invalida")
            menu_mat()


def main():
    menu()
    opcion = input("Introduce una opción (1-3): ")
    match opcion:
        case "1":
            menu_mat()
        case "2":
            menu_ag()
        case "3":
            print("Programa finalizado")
        case _:
            print("Opcion invalida")
            main()


if __name__ == "__main__":
    main()
