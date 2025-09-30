"""
programa07
Escribe un programa que reciba una cantidad de minutos y muestre por pantalla a
cuantas horas y minutos corresponde
"""
a=int(input("Cuantos minutos: "))
print(f"{a} son {int(round(a/60 , 0))} horas y {a%60} minutos")