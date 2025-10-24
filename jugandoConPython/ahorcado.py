# Importamos solo lo necesario
from random import choice

# Lista de palabras que se usarán en el juego
palabras = ["computadora", "programa", "ingenieria", "python", "teclado"]

# Elegimos una palabra al azar
palabraSecreta = choice(palabras)

# Creamos la representación de la palabra con guiones bajos
palabraMostrada = []
for letra in palabraSecreta:
    palabraMostrada.append("_")

# Número de vidas
vidas = 3

# Lista para almacenar las letras que ya ha usado el jugador
letrasUsadas = []

# Mensaje inicial
print("Bienvenido al juego del ahorcado")
print("Tienes 3 vidas")
print(" ".join(palabraMostrada))

# Ciclo principal del juego
while True:
    letra = input("\nIngresa una letra: ").lower()  # Pedimos letra al jugador

    # Si ya la había usado antes
    if letra in letrasUsadas:
        print("Ya usaste esa letra")
        continue
    else:
        letrasUsadas.append(letra)

    # Revisamos si la letra está en la palabra
    if letra in palabraSecreta:
        # Reemplazamos los guiones por la letra correcta
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] == letra:
                palabraMostrada[i] = letra
        print("Correcto!")
    else:
        # Si la letra no está, perdemos una vida
        vidas -= 1
        print("Incorrecto, te quedan", vidas, "vidas")

    # Mostramos el estado actual de la palabra
    print(" ".join(palabraMostrada))

    # Revisamos si ganó
    if "_" not in palabraMostrada:
        print("Felicidades! Adivinaste la palabra:", palabraSecreta)
        break

    # Revisamos si perdió
    if vidas == 0:
        print("Perdiste! La palabra era:", palabraSecreta)
        break
