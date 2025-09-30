"""
programa04
Escribe un programa que pregunte la base y altura de una rectángulo y calcule su área y
perímetro
"""
base=int(input("Cual es la base: "))
altura=int(input("Cual es la altura: "))

print (f"El area del rectangula es {base} * {altura} = {base * altura} m^2")
print (f"El perimetro del rectangula es 2 * ({base} * {altura}) = {2 * base * altura} m")