"""
programa03
Escribe un programa que muestre los números pares que hay entre 0 y 10. Resuelve el
ejercicio de 4 formas diferentes. Usando los bucles for y while sin y con la sentencia
continue
"""
for i in range(0, 11, 1):
    if i % 2 == 0:
        print(i)

for i in range(0, 11, 1):
    if i % 2 != 0:
        continue
    print(i)

n = 0
while n < 11:
    if n % 2 == 0:
        print(n)
    n = n + 1

m = -1
while m < 11:
    m = m + 1
    if m % 2 != 0:
        continue
    print(m)
