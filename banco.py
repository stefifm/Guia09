print("Estadística de las cuentas de clientes de un banco")


n = int(input("Cantidad de clientes: "))
cuenta_corriente = 0
caja = 0
flag_may = False
flag_men = False
id_men = ""
id_may = ""
for i in range(n):
    n_cuenta = int(input("Ingrese el número de cuenta: "))
    nom_cliente = input("Ingrese el nombre del clientes: ")
    tipo_cuenta = int(input("Ingrese 0- Caja o 1- Cuenta corriente: "))
    saldo = float(input("Ingrese el saldo del cliente: "))

    if tipo_cuenta == 0:
        caja += 1
        if flag_men == False or saldo < men:
            men = saldo
            id_men = nom_cliente
    else:
        cuenta_corriente += 1

    if flag_may == False or saldo > may:
        may = saldo
        id_may = n_cuenta
        flag_may = True

#resultados
print("Cantidad de cuentas en caja de ahorro:",caja)
print("Cantidad de cuentas en cuenta corriente:",cuenta_corriente)
print("La cuenta número",id_may,"tiene el mayor saldo y es de:",may)
print("El cliente",id_men,"es el de menor saldo y es de:",men)
