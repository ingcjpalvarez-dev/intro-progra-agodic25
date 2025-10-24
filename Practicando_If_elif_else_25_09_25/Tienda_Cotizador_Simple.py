# Ejercicio 5. Tienda / Cotizador Simple

while True:
    print("\n--- MENÚ TIENDA ---")
    print("1. Calcular total con IVA")
    print("2. Calcular total con descuento + IVA")
    print("3. Calcular precio unitario dado un total y cantidad")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        precio = float(input("Ingresa el precio del producto: "))
        cantidad = int(input("Ingresa la cantidad: "))
        subtotal = precio * cantidad
        iva = subtotal * 0.16  # IVA en México = 16%
        total = subtotal + iva
        print("Subtotal:", subtotal)
        print("IVA:", iva)
        print("Total:", total)

    elif opcion == "2":
        precio = float(input("Ingresa el precio del producto: "))
        cantidad = int(input("Ingresa la cantidad: "))
        subtotal = precio * cantidad

        # Descuento por cupón
        cupon = input("Ingresa tu cupón (VERANO, SALDOS, BBVA, BANORTE25): ")
        descuento = 0
        if cupon == "VERANO":
            descuento = 0.10
        elif cupon == "SALDOS":
            descuento = 0.35
        elif cupon == "BBVA":
            descuento = 0.05
        elif cupon == "BANORTE25":
            descuento = 0.25
        else:
            print("Cupón no válido, no se aplica descuento.")

        subtotal_con_descuento = subtotal - (subtotal * descuento)
        iva = subtotal_con_descuento * 0.16
        total = subtotal_con_descuento + iva

        print("Subtotal:", subtotal)
        print("Descuento aplicado:", descuento * 100, "%")
        print("Subtotal con descuento:", subtotal_con_descuento)
        print("IVA:", iva)
        print("Total final:", total)

    elif opcion == "3":
        total = float(input("Ingresa el total: "))
        cantidad = int(input("Ingresa la cantidad: "))
        if cantidad > 0:
            unitario = total / cantidad
            print("Precio unitario:", round(unitario, 2))
        else:
            print("La cantidad debe ser mayor que 0")

    elif opcion == "4":
        print("Adiós")
        break

    else:
        print("Opción inválida, intenta de nuevo")
