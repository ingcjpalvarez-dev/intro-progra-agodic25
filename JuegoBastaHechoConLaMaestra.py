# Importamos solo lo necesario
from random import choice
from time import time, sleep
from os import system

# Diccionario donde se guardarán las categorías
categorias = {}
letras = "abcdefghijklmnopqrstuvwxyz"
puntosTotales = 0
contadorRondas = 0

print("\n--- ¡Bienvenido al asistente del juego Basta! ---")
print("Configura las categorías para jugar\n")

# Ciclo para configurar las categorías del juego
contadorCategoria = 0
while True:
    contadorCategoria += 1
    categoria = input("Ingresa categoría (deja vacío para salir): ")
    if categoria == "":
        break
    categorias[contadorCategoria] = categoria.capitalize()

# Pausa antes de limpiar pantalla
sleep(2)
system("cls" if system == "nt" else "clear")

# Inicia el juego
while True:
    contadorRondas += 1
    letra = choice(letras)  # se elige una letra aleatoria
    letras = letras.replace(letra, "")
    print(f"\n¡Comienza la ronda {contadorRondas} con la letra: {letra.upper()}!")
    print("Categorías:", ", ".join(map(str, categorias.values())))
    print("\nTienes 60 segundos para responder las categorías de esta ronda.\n")

    # Cuenta regresiva antes de empezar
    for i in range(3, 0, -1):
        print(f"Empieza en {i}...")
        sleep(1)
    print("¡YA!\n")

    palabras = {}  # aquí se guardan las palabras que vaya escribiendo el jugador

    # Empieza el tiempo
    inicio = time()
    limite = 60  # segundos por ronda

    # Mientras no se acabe el tiempo y queden categorías
    while True:
        # Verificamos el tiempo transcurrido
        tiempoActual = time() - inicio
        if tiempoActual >= limite:
            print("\n Tu tiempo para responder se agotó.")
            break

        # Mostramos las categorías para que el jugador elija
        for llave, valor in categorias.items():
            print(f"{llave}. {valor}")
        categoriaSeleccionada = input("\nSelecciona categoría (-1 para salir): ")

        # Si el jugador quiere salir antes de que acabe el tiempo
        if categoriaSeleccionada == "-1" or categoriaSeleccionada.isalpha():
            break

        # Si no escribió nada, vuelve a mostrar
        if categoriaSeleccionada == "":
            continue

        # Si aún hay tiempo, pedimos la palabra
        if time() - inicio < limite:
            categoriaSeleccionada = int(categoriaSeleccionada)
            palabra = input(f"{categorias[categoriaSeleccionada]} con la letra {letra.upper()}: ")
            palabras[categorias[categoriaSeleccionada]] = palabra.capitalize()
        else:
            print("\nSe acabó tu tiempo de espera")
            break

    # Mostrar lo que alcanzó a responder
    print("\n-- Tus respuestas --")
    if len(palabras) == 0:
        print("No escribiste nada")
    else:
        for categoria, palabra in palabras.items():
            print(f"{categoria} --> {palabra}")

    sleep(2)

    # Puntuación de la ronda
    print("\n-- Ingresa tus puntos por categoría --")
    puntosRonda = 0
    for llave, categoria in categorias.items():
        puntosCategoria = input(f"Puntos obtenidos en {categoria}: ")
        if puntosCategoria == "":
            puntosCategoria = 0
        elif puntosCategoria.isnumeric():
            puntosRonda += int(puntosCategoria)
        else:
            puntosCategoria = 0

    print(f"\nPuntos Ronda: {puntosRonda}")
    puntosTotales += puntosRonda

    # Espera antes de limpiar pantalla
    sleep(3)
    system("cls" if system == "nt" else "clear")

    continuar = input("\n¿Quieres seguir jugando? (s/n): ")
    if continuar.lower() != "s":
        break

# Al final del juego
print("\nPuntos Totales:", puntosTotales)
print("¡Gracias por jugar Basta! 🎉")
