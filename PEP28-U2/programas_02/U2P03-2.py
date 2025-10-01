"""
programa02
Escribe un que lea por teclado un número comprendido entre 1 y 10. No se dejara de
pedir el número hasta que no se introduzca correctamente
"""
a = int(input("Introduce un numero del 1 al 10: "))
while a < 1 or a > 10:
    a = int(input("Numero incorrecto, vuelve a intentar: "))
