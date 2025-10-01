"""
programa02
Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no
es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o
negativo) y si el valor no es correcto, mostrará un aviso
"""
par=int(input("Introduce un numero par: "))
if (par % 2 == 0):
    impar=int(input("Introduce un numero impar: "))
    if (impar % 2 == 0):
        print ("Alguno de los numeros introducidos no es valido")
else:
    print ("Alguno de los numeros introducidos no es valido")
