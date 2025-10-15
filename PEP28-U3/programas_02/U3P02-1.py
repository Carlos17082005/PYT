"""
programa01
Escribe un programa en Python que importe el modulo math completo y que le pregunte al
usuario que operación matemática quiere hacer:
1. Seno de un ángulo
2. Coseno de ángulo
3. Raíz cuadrada de un número
4. Potencia de dos números.
Le pida los datos necesarios y muestre los resultados por pantalla
"""

import math


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
            print(math.sin(float(input("Intoduce el angulo: "))))
            mostrar_menu()
            main()
        case "2":
            print(math.cos(float(input("Intoduce el angulo: "))))
            mostrar_menu()
            main()
        case "3":
            print(math.sqrt(float(input("Intoduce un numero: "))))
            mostrar_menu()
            main()
        case "4":
            print(
                math.pow(
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
