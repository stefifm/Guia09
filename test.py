import random

cont_norte = 0
cont_sur = 0
cont_gcordoba = 0
cont_capital = 0
cont_positivo = 0
n = int(input("Cantidad de casos: "))
for i in range(n):
    region_num = random.randint(1, 10)
    test_positivo = random.randint(0, 100) < 60


    if test_positivo == True:
        cont_positivo += 1
        if region_num < 3:
            cont_norte += 1
        elif region_num < 5:
            cont_sur += 1
        elif region_num < 8:
            cont_gcordoba += 1
        else:
            cont_capital += 1








print("Cantidad de positivos:",cont_positivo)
print("Norte:",cont_norte)
print("Sur:",cont_sur)
print("Gran Córdoba:",cont_gcordoba)
print("Capital:",cont_capital)
if cont_norte == 0:
    print("Norte no tiene casos")
if cont_sur == 0:
    print("Sur no tiene casos")
if cont_gcordoba == 0:
    print("Gran Córdoba no tiene casos")
if cont_capital == 0:
    print("Capital no tiene casos")
