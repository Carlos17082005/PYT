"""
programa07
Escriba un programa que pida un año y que escriba si es bisiesto o no. Un año es bisiesto
si es múltiplos de 4 pero no múltiplos de 100, aunque si los múltiplos de 400
"""
anno=int(input("Introduce un año: "))
if (anno % 4 == 0 and anno % 100 != 0):
    print(f"El año {anno} es bisiesto")
elif (anno % 4 == 0 and anno % 100 == 0 and anno % 400 == 0):
    print(f"El año {anno} es bisiesto")
else:
    print(f"El año {anno} es no bisiesto")
