"""
programa12
Sabiendo que 1 milla equivale a 1,61 Km escribe un programa que pida un número de
millas y un número de Km, muestre respectivamente el número de millas y kilómetros. Los
resultados deben estar redondeados a 2 decimales.
"""
a=float(input("Introduce un numero de millas: "))
b=float(input("Introduce un numero de kilometros: "))
print(f"{a} millas son {a*1.61} kilometros")
print(f"{b} kilometros son {b/1.61} millas")
