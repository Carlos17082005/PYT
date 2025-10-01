"""
programa04
Escribe un programa que use un bucle while y le pida continuamente al usuario que
introduzca un número hasta que ingrese 45 como la número de salida secreto, en cuyo
caso el mensaje "¡Has dejado el bucle con éxito" debe imprimirse en la pantalla y el bucle
debe terminar.
Haz dos dos versiones del programa:
• Versión 1: Utiliza el concepto de ejecución condicional y la instrucción break. En
este caso el bucle no evaluará ninguna condición, es decir, será un bucle infinito.
• Versión 2: Realmente no es necesario usar la instrucción break. Diseña una
solución donde no se use break y el bucle while controle la condición de salida
"""
a = int(input("Introduce un numero: "))
while True:
    if a == 45:
        break
    else:
        a = int(input("Introduce un numero: "))
print("¡Has dejado el bucle con exito!")


b = int(input("Introduce un numero: "))
while b != 45:
    b = int(input("Introduce un numero: "))
print("¡Has dejado el bucle con exito!")
