print("Sílaba pa")

def es_vocal(c):
    vocales = "aeiouAEIOU"
    if c in vocales:
        return True
    return False
def porcentaje(suma, total):
    if total != 0:
        p = (suma * 100) / total
    else:
        p = 0
    return p

flag_p = flag_pa = flag_n = False
pa_n = 0
cont_letras = 0
acu_letras = 0
cont_vocales = 0
cont_pal_dos_vocales = 0
pal_cinco = 0
texto = input("Ingrese un texto. Termina en punto: ")
for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if cont_letras == 1 and caracter == "p":
            flag_p = True
        else:
            if flag_p and caracter == "a":
                flag_pa = True
            flag_p = False
        if caracter == "n":
            flag_n = True

        if cont_letras > 3:
            if es_vocal(caracter):
                cont_vocales += 1
    else:
        if cont_letras == 0:
            continue
        acu_letras += cont_letras
        if flag_pa and flag_n:
            pa_n += 1
        if cont_vocales > 2:
            cont_pal_dos_vocales += 1
        if cont_letras > 5:
            pal_cinco += 1
        flag_n = flag_pa = False
        cont_letras = 0
porc_dosvocales = porcentaje(cont_pal_dos_vocales, acu_letras)

print("Cantidad de palabras que inician con pa y terminan con n:",pa_n)
print("Cantidad de palabras que tienen más de dos vocales a partir de la "
      "tercera letra:",cont_pal_dos_vocales)
print("Porcentaje de palabras con dos vocales tras la tercera letra:",
      porc_dosvocales)
print("Cantidad de palabras con más de cinco letras:",pal_cinco)
