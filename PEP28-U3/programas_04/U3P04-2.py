'''
programa02
Investiga usos habituales del fichero __init__.py de un paquete y usa el ejemplo anterior
para configurar y probar alguno de ellos.
Programación en Python (PEP) - IES Leonardo Da Vinci - Álvaro García
'''

import matematicas


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
            print(matematicas.suma(a, b))
        case "2":
            a, b = mat()
            print(matematicas.resta(a, b))
        case "3":
            a, b = mat()
            print(matematicas.multiplicacion(a, b))
        case "4":
            a, b = mat()
            print(matematicas.divicion(a, b))
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
            print(matematicas.area_circulo(a))
        case "2":
            a, b = ar()
            print(matematicas.area_triangulo(a, b))
        case "3":
            a, b = ar()
            print(matematicas.area_rectangulo(a, b))
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
