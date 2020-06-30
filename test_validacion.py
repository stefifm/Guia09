print("Test validación de cuenta de usuario")

def validacion(a):
    cl = 0
    c_arroba = 0
    flag_punto = False
    pos = 0
    caranterior = ""
    for caracter in a:
        cl += 1
        if cl == 1 and caracter == ".":
            flag_punto = True
        if caracter == "@":
            pos = cl
            c_arroba += 1
        caranterior = caracter
        cl = 0
    if c_arroba == 1 and pos > 0 and pos < len(a) and not flag_punto and \
            caranterior != ".":
        return True
    return False

c = 1
usuario = input("Ingrese el mail: ")
while c < 3:
    if validacion(usuario) == False:
        print("Error. Vuelva a cargar su usuario")
    else:
        print("usuario correcto")
        print("=" * 80)
        break
    c += 1
    usuario = input("Ingrese el email: ")
if c == 3:
    print("Sus intentos terminaron")
    exit(c)



print("Usuario",usuario, "es correcto")

# for caracter in a:
#     if "@@" in a:
#         return False
#     if ".." in a:
#         return False
#     if "@" == a[0] or "@" == a[cl - 1]:
#         return False
#     if "." == a[0] or "." == a[cl - 1]:
#         return False
#     return True