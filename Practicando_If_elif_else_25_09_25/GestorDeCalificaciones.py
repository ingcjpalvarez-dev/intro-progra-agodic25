# Gestor de Calificaciones super noob

while True:
    print("\n--- MENÚ ---")
    print("1. Calcular promedio")
    print("2. Calcular calificación final con ponderaciones")
    print("3. Mostrar mayor y menor calificación")
    print("4. Verificar si aprueba o reprueba")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        c1 = float(input("Ingresa calificación del parcial 1: "))
        c2 = float(input("Ingresa calificación del parcial 2: "))
        c3 = float(input("Ingresa calificación del parcial 3: "))
        promedio = (c1 + c2 + c3) / 3
        print("Tu promedio es:", promedio)

    elif opcion == "2":
        c1 = float(input("Ingresa calificación del parcial 1: "))
        c2 = float(input("Ingresa calificación del parcial 2: "))
        c3 = float(input("Ingresa calificación del parcial 3: "))
        p1 = float(input("Porcentaje del parcial 1 (ejemplo 30): ")) / 100
        p2 = float(input("Porcentaje del parcial 2: ")) / 100
        p3 = float(input("Porcentaje del parcial 3: ")) / 100
        final = (c1 * p1) + (c2 * p2) + (c3 * p3)
        print("Tu calificación final es:", final)

    elif opcion == "3":
        c1 = float(input("Ingresa calificación del parcial 1: "))
        c2 = float(input("Ingresa calificación del parcial 2: "))
        c3 = float(input("Ingresa calificación del parcial 3: "))
        mayor = max(c1, c2, c3)
        menor = min(c1, c2, c3)
        print("La mayor calificación es:", mayor)
        print("La menor calificación es:", menor)

    elif opcion == "4":
        c1 = float(input("Ingresa calificación del parcial 1: "))
        c2 = float(input("Ingresa calificación del parcial 2: "))
        c3 = float(input("Ingresa calificación del parcial 3: "))
        p1 = float(input("Porcentaje del parcial 1: ")) / 100
        p2 = float(input("Porcentaje del parcial 2: ")) / 100
        p3 = float(input("Porcentaje del parcial 3: ")) / 100
        final = (c1 * p1) + (c2 * p2) + (c3 * p3)
        print("Tu calificación final es:", final)
        if final >= 6:
            print("APROBADO")
        else:
            print("REPROBADO ")

    elif opcion == "5":
        print("Adiós")
        break

    else:
        print("Opción inválida, intenta de nuevo")
