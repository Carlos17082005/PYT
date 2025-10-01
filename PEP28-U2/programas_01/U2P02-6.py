"""
programa06
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta
"""
dia=int(input("Introduce un dia: "))
mes=int(input("Introduce un mes: "))
anno=int(input("Introduce un año: "))
bool=False

if (anno > 0):
    match mes:
        case 1|3|5|7|8|10|12:
            if (dia > 0 and dia < 32):
                bool=True
        case 4|6|9|11:
            if (dia > 0 and dia < 31):
                bool=True
        case 2:
            if (dia > 0 and dia < 29):
                bool=True

if (bool): 
    print(f"La fecha {dia}/{mes}/{anno} es correta")
else: 
    print(f"La fecha {dia}/{mes}/{anno} es incorrecta")
