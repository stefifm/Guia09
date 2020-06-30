print("Primer ejemplo de funciones")

def menor(a, b, c):
    if a < b and a < c:
        men = a
    else:
        if b < c:
            men = b
        else:
            men = c
    return men

def calcular_cuad(men):
    cuad = men ** 2
    return cuad

def calcular_cub(men):
    cubo = men ** 3
    return cubo

# def calcular_cuad_cub(men):
#     r1 = men ** 2
#     r2 = men ** 3
#     return r1, r2


#Programa Principal
a = int(input("Cargue el primer número: "))
b = int(input("Cargue el segundo número: "))
c = int(input("Cargue el tercer número: "))
men = menor(a, b, c)
cuadrado = calcular_cuad(men)
cubo = calcular_cub(men)
# cuadrado, cubo = calcular_cuad_cub(men)
print("El menor es:",men)
print("El cuadrado del menor es:",cuadrado)
print("El cubo del menor es:",cubo)
# print("El cuadrado del menor es:",cuadrado)
# print("El cubo del menor es:",cubo)



# def suma(num1, num2):
#     r = num1 + num2
#     return r
#
# n1 = int(input("Ingrese un número: "))
# n2 = int(input("Ingrese un número: "))
# resultado = suma(n1, n2)
# print(resultado)

