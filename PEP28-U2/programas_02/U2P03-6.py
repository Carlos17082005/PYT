"""
programa06
Escribe un programa que realice las siguientes operaciones:
• Leer por teclado un número comprendido entre 1 y 10. Se vuelve a pedir hasta que
no se introduzca el número correcto.
• Una vez que ha leído el número se tiene que mostrar su tabla de multiplicar.
• Después de mostrar la tabla de multiplicar se tiene que preguntar al usuario si
desea introducir otro número o no. Si el usuario selecciona que quiere continuar el
programa tendrá que volver a ejecutarse y repetir los mismos pasos. Si el usuario
indica que no quiere continuar el programa finaliza.
"""
continuar = True
while continuar:
    a = int(input("Introduce un numero del 1 al 10: "))
    while a < 1 or a > 10:
        a = int(input("Numero fuera de rango, vuelve a intentar: "))

    for i in range(1, 11, 1):
        print(f"{a} * {i} = {a*i}")

    continuar = int(input("Deseas continuar (1) o quieres salir (2): ")) == 1
