"""
programa05
Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables
en Python (globales, no locales y locales).
"""

vGlobal = "Global"


def noLocal():
    vNoLocal = "No local"

    def noLocalAnidada():
        nonlocal vNoLocal
        print(vNoLocal)
        vNoLocal = "Esta variable cambio (nonlocal)"

    noLocalAnidada()
    print(vNoLocal)


def local():
    vLocal = "Local"
    print(vLocal)
    global localGlobal
    localGlobal = "Esta variable es global (global)"


print(vGlobal)
noLocal()
local()
print(localGlobal)
