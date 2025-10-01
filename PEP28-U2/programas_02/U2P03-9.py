"""
programa09
Escribe un programa para jugar a una versión muy simplificada del black jack. En primer
lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A
continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando
para obtener su puntuación, hasta que el quiera. Si se pasa de 21 pierde, si obtiene una puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la
banca gana
"""
import random

num = random.randrange(17, 22)
j1 = 0
bool = True

while bool and j1 < 22:
    bool = int(input(f"Tienes {j1}, quieres una carta? (1) ")) == 1
    if bool:
        j1 += random.randrange(1, 6)
if j1 > 21 or j1 < num:
    print(f"Prediste, Banca: {num}   Jugador: {j1}")
else:
    print(f"Ganaste, Banca: {num}   Jugador: {j1}")
