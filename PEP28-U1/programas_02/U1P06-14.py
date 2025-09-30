"""
programa14
Escribe un programa que reciba un número de bytes y muestre por pantalla cuantos
GBytes, MBytes, KBytes y Bytes son. Tanto para el sistema decimal como el binario.
"""
import math
a=int(input("Introduce el numero de bytes: "))
print (f"{a} bytes en sistema decimal (SI): {math.trunc(a/1000000000)} GB, {math.trunc((a%1000000000)/1000000)} MB, {math.trunc(((a%1000000000)%1000000)/1000)} KB, {math.trunc(((a%1000000000)%1000000)%1000)} bytes")
print (f"{a} bytes en sistema binario (IEC): {math.trunc(a/1073741824)} GB, {math.trunc((a%1073741824)/1048576)} MB, {math.trunc(((a%1073741824)%1048576)/1024)} KB, {math.trunc(((a%1073741824)%1048576)%1024)} bytes")