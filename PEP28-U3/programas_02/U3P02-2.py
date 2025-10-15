"""
programa02
Modifica el programa anterior para que solo se importen las funciones del módulo math
que se usan en el programa
"""

from math import sin, cos, sqrt, pow


def mostrar_menu():
    print(
        "1. Seno de un ángulo\n"
        "2. Coseno de ángulo\n"
        "3. Raíz cuadrada de un número\n"
        "4. Potencia de dos números\n"
        "5. Salir\n"
    )


def main():
    opcion = input("Introduce una opción (1-5): ")
    match opcion:
        case "1":
            print(sin(float(input("Intoduce el angulo: "))))
            mostrar_menu()
            main()
        case "2":
            print(cos(float(input("Intoduce el angulo: "))))
            mostrar_menu()
            main()
        case "3":
            print(sqrt(float(input("Intoduce un numero: "))))
            mostrar_menu()
            main()
        case "4":
            print(
                pow(
                    float(input("Intoduce un numero: ")),
                    float(input("Intoduce otro numero: ")),
                )
            )
            mostrar_menu()
            main()
        case "5":
            print("Programa finalizado")
        case _:
            print("Opcion invalida")
            main()


mostrar_menu()
main()
