"""
programa09
Escribe un programa en Python que simule el juego de piedra, papel o tijera. En primer
lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle
qué opción desea elegir. Por ejemplo:
1. Piedra
2. Papel
3. Tijera
Seleccione una opción (1, 2 o 3):
Después de leer la opción seleccionada por el usuario el programa generará un número
aleatorio para simular una jugada y mostrará un mensaje indicando si el usuario ha
ganado o ha perdido dependiendo del resultado.
Ten en cuenta que:
• La piedra gana a la tijera pero pierde contra el papel.
• El papel gana a la piedra pero pierde contra la tijera.
• La tijera gana al papel pero pierde contra la piedra.
"""
import random
print("1. Piedra \n2. Papel \n3. Tijeras")
j1=int(input("Que opcion deseas elegir: "))
j2=random.randrange(1, 4)

match (j1, j2):
    case (1, 2):
        print("Perdiste")
    case (1, 3):
        print("Ganaste")
    case (2 , 1):
        print("Ganaste")
    case (2, 3):
        print("Perdiste")
    case (3, 1):
        print("Perdiste")
    case (3, 2):
        print("Ganaste")
    case (1, 1):
        print("Empate")
    case (2, 2):
        print("Empate")
    case (3, 3):
        print("Empate")
    case _:
        print("Numero fuera de rango")