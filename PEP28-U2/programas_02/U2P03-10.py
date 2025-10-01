"""
programa10
Modifica el programa anterior par que pida en primer lugar el número de jugadores que
van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la
banca.
"""
import random

num = random.randrange(17, 22)
p = ""
g = ""

a = int(input("Cuantos jugadores van a jugar: "))

for i in range(1, (a + 1), 1):
    print(f"\n--------------Jugador {i}--------------\n")
    bool = True
    j1 = 0
    while bool and j1 < 22:
        bool = int(input(f"Jugador {i}, tienes {j1}, quieres una carta? (1) ")) == 1
        if bool:
            j1 += random.randrange(1, 6)
    if j1 > 21 or j1 < num:
        if p == "":
            p += "Jugador " + str(i)
        else:
            p += ", Jugador " + str(i)
    else:
        if g == "":
            g += "Jugador " + str(i)
        else:
            g += ", Jugador " + str(i)

print("\n--------------Resultados--------------\n")
if g != "":
    print(f"{g}     ¡Ganaron! :)")
if p != "":
    print(f"{p}     Perdieron :(")
