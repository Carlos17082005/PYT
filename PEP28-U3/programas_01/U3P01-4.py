"""
programa04
Mejora el programa anterior de forma que compruebe si el usuario está introduciendo
valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así
que pida muestre un aviso y vuelva a pedir el valor.
"""

import math


def calcular_area_circulo(radio):
    return math.pi * radio * radio


def calcular_area_triangulo(base, altura):
    return (base * altura) / 2


def calcular_area_rectangulo(base, altura):
    return base * altura


def mostrar_menu():
    print(
        "1. Calcular el área de un círculo\n"
        "2. Calcular el área de un triángulo\n"
        "3. Calcular el área de un rectángulo\n"
        "4. Salir\n"
    )


def main():
    opcion = input("Introduce una opción (1-4): ")
    match opcion:
        case "1":
            print(opcion1())
            mostrar_menu()
            main()
        case "2":
            print(opcion2())
            mostrar_menu()
            main()
        case "3":
            print(opcion3())
            mostrar_menu()
            main()
        case "4":
            print("Programa finalizado")
        case _:
            print("Opcion invalida")
            main()


def opcion1():
    a = int(input("Introduce el radio: "))
    if a > 0:
        return "El area del circulo es = " + str(calcular_area_circulo(a)) + "\n"
    else:
        print("Error")
        opcion1()


def opcion2():
    a = int(input("Introduce la base: "))
    b = int(input("Introduce la altura: "))
    if a > 0 and b > 0:
        return "El area del triangulo es = " + str(calcular_area_triangulo(a, b)) + "\n"
    else:
        print("Error")
        opcion2()


def opcion3():
    a = int(input("Introduce la base: "))
    b = int(input("Introduce la altura: "))
    if a > 0 and b > 0:
        return (
            "El area del rectangulo es = " + str(calcular_area_rectangulo(a, b)) + "\n"
        )
    else:
        print("Error")
        opcion3()


mostrar_menu()
main()