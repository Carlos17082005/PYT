"""
programa11
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo
de viaje hasta llegar a otra ciudad B es de N segundos. Escribie un programa que
determine la hora de llegada a la ciudad B
"""

aH=int(input("A que hora sales de la ciudad A? (HH)"))
aM=int(input("minutos? (MM)"))
aS=int(input("segundos? (SS)"))

b=int(input("A cuantos segundos esta la ciudad B?"))

print(f"Hora de llegada estimada: {aH+round(b/3600)}:{aM+round((b%3600)/60)}:{aS+round((b%3600)%60)}")