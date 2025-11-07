# Importamos solo lo necesario
from random import choice
from time import time, sleep
from os import system, name  # <-- corregido aquí

# Variables globales
letras = "abcdefghijklmnopqrstuvwxyz"
puntosTotales = 0
contadorRondas = 0

# Función para limpiar pantalla
def limpiar_pantalla():
    system("cls" if name == "nt" else "clear")  # <-- corregido aquí

# Función para configurar las categorías
def configurar_categorias():
    categorias = {}
    contadorCategoria = 0
    print("\n--- ¡Bienvenido al asistente del juego Basta! ---")
    print("Configura las categorías para jugar\n")
    while True:
        contadorCategoria += 1
        categoria = input("Ingresa categoría (deja vacío para salir): ")
        if categoria == "":
            break
        categorias[contadorCategoria] = categoria.capitalize()
    sleep(2)
    limpiar_pantalla()
    return categorias

# Función para jugar una ronda
def jugar_ronda(contadorRondas, letras, categorias):
    contadorRondas += 1
    letra = choice(letras)
    letras = letras.replace(letra, "")
    print(f"\n¡Comienza la ronda {contadorRondas} con la letra: {letra.upper()}!")
    print("Categorías:", ", ".join(map(str, categorias.values())))
    print("\nTienes 60 segundos para responder las categorías de esta ronda.\n")

    # Cuenta regresiva
    for i in range(3, 0, -1):
        print(f"Empieza en {i}...")
        sleep(1)
    print("¡YA!\n")

    palabras = {}
    inicio = time()
    limite = 60

    # Ciclo de respuestas
    while True:
        tiempoActual = time() - inicio
        if tiempoActual >= limite:
            print("\nTu tiempo para responder se agotó.")
            break

        for llave, valor in categorias.items():
            print(f"{llave}. {valor}")
        categoriaSeleccionada = input("\nSelecciona categoría (-1 para salir): ")

        if categoriaSeleccionada == "-1" or categoriaSeleccionada.isalpha():
            break
        if categoriaSeleccionada == "":
            continue

        categoriaSeleccionada = int(categoriaSeleccionada)
        palabra = input(f"{categorias[categoriaSeleccionada]} con la letra {letra.upper()}: ")
        palabras[categorias[categoriaSeleccionada]] = palabra.capitalize()

    # Mostrar respuestas
    print("\n-- Tus respuestas --")
    if len(palabras) == 0:
        print("No escribiste nada")
    else:
        for categoria, palabra in palabras.items():
            print(f"{categoria} --> {palabra}")

    sleep(2)

    # Pedir puntos
    print("\n-- Ingresa tus puntos por categoría --")
    puntosRonda = 0
    for llave, categoria in categorias.items():
        puntosCategoria = input(f"Puntos obtenidos en {categoria}: ")
        if puntosCategoria.isnumeric():
            puntosRonda += int(puntosCategoria)

    print(f"\nPuntos Ronda: {puntosRonda}")
    return puntosRonda, letras, contadorRondas

# --- Programa principal ---
categorias = configurar_categorias()

while True:
    puntosRonda, letras, contadorRondas = jugar_ronda(contadorRondas, letras, categorias)
    puntosTotales += puntosRonda

    sleep(3)
    limpiar_pantalla()

    continuar = input("\n¿Quieres seguir jugando? (s/n): ")
    if continuar.lower() != "s":
        break

# Fin del juego
print("\nPuntos Totales:", puntosTotales)
print("¡Gracias por jugar Basta! 🎉")
