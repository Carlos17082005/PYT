"""
programa08
Escribe un programa que simule un juego en el que dos jugadores tiran dos dados. El que
saque mayor puntuación total, gana. Si la puntuación total coincide, gana quien haya
sacado el dado con el valor más alto. Si el valor más alto también coincide, empatan.
Puedes pedir el valor de cada tirada de dados por teclado o usar la la función
random.randrange(1, 7) para obtener un número aleatorio entre 1 y 6 (para ello
debes poner import random al inicio del programa)
"""
import random
j1d1=random.randrange(1, 7)
j1d2=random.randrange(1, 7)
j2d1=random.randrange(1, 7)
j2d2=random.randrange(1, 7)

if (j1d1+j1d2 > j2d1+j2d2):
    print("El jugador 1 gana")
elif (j1d1+j1d2 < j2d1+j2d2):
    print("El jugador 2 gana")
else:
    if (j1d1 > j1d2):
        mj1=j1d1
    else:
        mj1=j1d2
    if (j2d1 > j2d2):
        mj2=j2d1
    else:
        mj2=j2d2
    if (mj1 > mj2):
        print("El jugador 1 gana")
    elif (mj1 < mj2):
        print("El jugador 2 gana")
    else:
        print("Empate")