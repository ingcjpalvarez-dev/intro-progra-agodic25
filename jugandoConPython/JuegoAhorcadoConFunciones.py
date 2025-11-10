from random import choice

# Escoge una palabra al azar
def elegir_palabra():
    lista = ["computadora", "programa", "ingenieria", "python", "teclado"]
    return choice(lista)

# Crea la lista de guiones bajos
def crear_guiones(palabra):
    guiones = []
    for letra in palabra:
        guiones.append("_")
    return guiones

# Muestra la palabra actual
def mostrar(palabra_lista):
    print(" ".join(palabra_lista))

# Pide una letra al usuario
def pedir_letra():
    letra = input("\nEscribe una letra: ").lower()
    return letra

# Revisa si la letra está en la palabra
def revisar_letra(letra, palabra, palabra_mostrada):
    acierto = False
    for i in range(len(palabra)):
        if palabra[i] == letra:
            palabra_mostrada[i] = letra
            acierto = True
    return acierto

# Juego principal
def jugar():
    palabra = elegir_palabra()
    mostrada = crear_guiones(palabra)
    vidas = 3
    usadas = []

    print("Bienvenido al juego del ahorcado!")
    print("Tienes", vidas, "vidas.")
    mostrar(mostrada)

    while True:
        letra = pedir_letra()

        if letra in usadas:
            print("Ya habías usado esa letra.")
            continue
        else:
            usadas.append(letra)

        if revisar_letra(letra, palabra, mostrada):
            print("¡Correcto!")
        else:
            vidas -= 1
            print("Incorrecto. Te quedan", vidas, "vidas.")

        mostrar(mostrada)

        if "_" not in mostrada:
            print("¡Ganaste! La palabra era:", palabra)
            break

        if vidas == 0:
            print("Perdiste. La palabra era:", palabra)
            break

# Ejecuta el juego
jugar()
