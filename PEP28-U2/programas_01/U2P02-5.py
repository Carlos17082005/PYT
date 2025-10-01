"""
programa05
Escribe un programa que pida dos números y que indique cuál es el menor, cuál el mayor
o que indique que son iguales.
"""
a=float(input("Introduce un numero: "))
b=float(input("Introduce otro numero: "))

if (a > b):
    print(f"{a} es mayor que {b}")
elif (b > a):
    print(f"{b} es mayor que {a}")
else:
    print(f"{a} es igual a {b}")