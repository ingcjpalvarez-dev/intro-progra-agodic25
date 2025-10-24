#CONVERSOR DE UNIDADES 

print("Bienvenido al menú del conversor de unidades")
print("1. Convertir de Farenheit a Celsius")
print("2. Convertir de Celsius a Farenheit")
print("3. Convertir Metros a Centímetros")
print("4. Convertir Centímetros a Metros")
print("5. Convertir Kilogramos a Gramos")
print("6. Convertir Gramos a Kilogramos")
print("7. Salir del menú")

opcion = input("Seleccione la conversión de su preferencia (1-2): ")
if opcion == "1":
    valorConvertible = int(input("Ingrese el valor en Farenheit que desea convertir a Celsius: "))
    conversion_a_Celsius = (valorConvertible - 32) * (5/9)
    print(f"El resultado de la conversión es: {conversion_a_Celsius}")

elif opcion == "2":
    valorConvertible = int(input("Ingrese el valor en Celsius que desea convertir a Farenheit: "))
    conversion_a_Farenheit = (valorConvertible + 32) * (9/5)
    print(f"El resultado de la conversión es: {conversion_a_Farenheit}")

elif opcion == "3":
    valorConvertible = int(input("Ingrese la cantidad de Metros que desea converir a Centímetros: "))
    conversion_a_Centimetros = valorConvertible * 100
    print(f"El resultado de su conversión es: {conversion_a_Centimetros}")

elif opcion == "4":
    valorConvertible = int(input("Ingresa la cantidad de Centímetros que deseas convertir a Metros: "))
    conversion_a_Metros = valorConvertible / 100
    print(f"El resultado de su conversión es: {conversion_a_Metros}")

elif opcion== "5":
    valorConvertible = int(input("Ingrese la cantidad de Kilogramos que desea convertir a Gramos: "))
    conversion_a_Gramos = valorConvertible * 1000
    print(f"El resultado de su conversión es: {conversion_a_Gramos}")

elif opcion == "6":
    valorConvertible = int(input("Ingrese la cantidad de Gramos que desea convertir a Kilogramos: "))
    conversion_a_Kilogramos = valorConvertible / 1000
    print(f"El resultado de su conversión es: {conversion_a_Kilogramos}")

elif opcion == "7":
    print("Ha salido del conversor de unidades")





