"""
programa07
Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la
suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza
la instrucción break y otra no
"""
sumaA = 0
contadorA = 0
a = int(input("Introduce un numero: "))
while True:
    if a == 0:
        break
    else:
        sumaA = sumaA + a
        contadorA = contadorA + 1
        a = int(input("Introduce un numero: "))
print(f"Suma = {sumaA}      Media = {sumaA/contadorA}")


sumaB = 0
contadorB = 0
b = int(input("Introduce un numero: "))
while b != 0:
    sumaB = sumaB + b
    contadorB = contadorB + 1
    b = int(input("Introduce un numero: "))
print(f"Suma = {sumaB}      Media = {sumaB/contadorB}")
