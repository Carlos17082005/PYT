"""
programa04
El módulo turtle es una biblioteca estándar de Python que permite crear gráficos y dibujos
de manera sencilla, moviendo una “tortuga” virtual por la pantalla. El módulo está instalado
por defecto en el interprete de Python.
Investiga la documentación del módulo https://docs.python.org/3/library/turtle.html y
escribe un programa que:
• Dibuje un cuadrado rojo sin rellenar.
• Dibuje un circulo verde relleno
"""
import turtle

turtle.color('red')
for i in range(0,4,1):
    turtle.forward(100)
    turtle.left(90)
    
turtle.up()
turtle.left(180)
turtle.forward(100)
turtle.left(180)
turtle.down()

turtle.begin_fill()
turtle.fillcolor('green')
turtle.color('green')
turtle.circle(50)
turtle.end_fill()


turtle.done()

