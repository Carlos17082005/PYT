"""
programa03
Escribe un programa que pida dos numero y muestre su división. Se deben tener en
cuenta que no se puede dividir por 0 mostrando en ese caso un aviso
"""
a=int(input("Introduce un numero: "))
b=int(input("Introduce otro numero: "))

if (b == 0):
    print("No se puede dividir por 0")
else: 
    print(f"{a} / {b} = {a/b}")