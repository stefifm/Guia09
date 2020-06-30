
import random

flag = False
autoc = 0
n = int(input("Ingrese una serie de números: "))
for i in range(n):
    edad = random.randint(10, 95)
    contacto = random.randint(0, 100) < 55
    personal_salud = random.randint(0, 100) < 10
    viaje_exterior = random.randint(0, 100) < 15
    test = random.randint(0, 100) < 60
    if test == True:
        if contacto == False and personal_salud == False and viaje_exterior \
                == False:
            autoc += 1
            if flag == False or edad < menor:
                menor = edad
                flag = True

print("Menor edad autoctono:",menor)