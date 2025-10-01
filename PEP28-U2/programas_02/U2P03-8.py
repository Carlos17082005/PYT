"""
programa08
Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación
solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va
respondiendo si el número a adivinar es mayor o menor que el introducido. El programa
termina cuando se acierta el número.
Puedes generar el número usando la función random.randrange(1, 21) para
obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio
del programa).
Mejora el programa de forma que el usuario tenga solo 3 intentos.
"""
import random

num = random.randrange(1, 21)

a = int(input("Introduce un numero (1 - 20): "))
while a != num:
    if a < num:
        print("El numero es mayor")
    else:
        print("El numero es menor")
    a = int(input("Introduce un numero: "))
print("¡Lo has adivinado!")
