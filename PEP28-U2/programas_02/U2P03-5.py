"""
programa05
Escribe un programa que pida un número y muestre una lista de números desde 1 al
número. Se debe controlar que el número no se menor que 1 ni mayor que 10, si es así se
pedirá que si introduzca de nuevo, y así hasta que se introduzca el número correcto.
"""
a = int(input("Introduce un numero del 1 al 10: "))
while a < 1 or a > 10:
    a = int(input("Numero fuera de rango, vuelve a intentar: "))

for i in range(1, (a + 1), 1):
    print(i)
