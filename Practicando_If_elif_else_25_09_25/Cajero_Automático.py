#CAJERO AUTOMÁTICO
#CREA UN PROGRAMA QUE SIMULE UN CAJERO CON SALDO INICIAL

#~~~~~Menú con opciones~~~~~#

saldo = 100000000000000000000000000000000000
print("Bienvenido a su ATM de confianza")
print("1. Consultar Saldo")
print("2. Retirar Saldo")
print("3. Depositar Saldo")
print("4. Salir del menú")

accion = input("Seleccione la acción a realizar (1-4): ")

if accion == "1":
    print(f"Su saldo es: {saldo} Cielos es usted millonario")

elif accion == "2":
    saldoRetirado = int(input("Ingrese la cantidad que desea retirar: "))
    if saldo < saldoRetirado:
        print("El saldo disponible no es suficiente")
    else:
        retirarDinero = saldo - saldoRetirado
        print(f"Su nuevo saldo es: {retirarDinero}")

elif accion == "3":
    cantidadDeposito = int(input("Ingrese la cantidad que desea depositar: "))
    añadirDeposito = saldo + cantidadDeposito
    print(f"Su nuevo saldo es: {añadirDeposito}")

elif accion == "4":
    print("Hasta luego, gracias por usar su ATM de confianza")   











