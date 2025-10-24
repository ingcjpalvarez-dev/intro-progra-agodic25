from random import choice

# Crear tablero vacío 3x3
tablero = [["1", "2", "3"],
           ["4", "5", "6"],
           ["7", "8", "9"]]

# Guardar combinaciones ganadoras (posiciones)
ganadoras = [
    (0,1,2), (3,4,5), (6,7,8),  # filas
    (0,3,6), (1,4,7), (2,5,8),  # columnas
    (0,4,8), (2,4,6)            # diagonales
]

# Convertir tablero a lista lineal para comprobar combinaciones
def tablero_lineal(tab):
    linea = []
    for fila in tab:
        for celda in fila:
            linea.append(celda)
    return linea

# Preguntar modo de juego
modo = input("Modo de juego (1=Jugador vs Jugador, 2=Jugador vs CPU): ")

# Inicializamos variables
jugadorActual = "X"
turnos = 0
ganador = False

# Ciclo principal del juego
while True:
    # Mostrar tablero
    print("\nTablero actual:")
    print(f"""
 {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]}
---+---+---
 {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]}
---+---+---
 {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]}
""")

    # Pedir movimiento
    if modo == "2" and jugadorActual == "O":
        # Movimiento CPU simple
        disponibles = []
        for i in range(3):
            for j in range(3):
                if tablero[i][j] not in ["X", "O"]:
                    disponibles.append((i,j))
        fila, col = choice(disponibles)
        print("CPU elige la posición:", tablero[fila][col])
    else:
        # Movimiento jugador
        mov = input(f"Jugador {jugadorActual}, ingresa la posición: ")
        if not mov.isnumeric():
            print("Ingresa un número válido")
            continue
        mov = int(mov)
        if mov < 1 or mov > 9:
            print("Número fuera de rango")
            continue
        # Convertir número a coordenadas
        fila = (mov-1)//3
        col = (mov-1)%3
        if tablero[fila][col] in ["X","O"]:
            print("Casilla ocupada")
            continue

    # Colocar la ficha
    tablero[fila][col] = jugadorActual
    turnos += 1

    # Revisar si alguien ganó
    linea = tablero_lineal(tablero)
    for c in ganadoras:
        if linea[c[0]] == linea[c[1]] == linea[c[2]]:
            ganador = True
            break

    if ganador:
        print("\nTablero final:")
        print(f"""
 {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]}
---+---+---
 {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]}
---+---+---
 {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]}
""")
        print("Gana el jugador", jugadorActual)
        break

    if turnos == 9:
        print("Empate! No hay más movimientos")
        break

    # Cambiar jugador
    if jugadorActual == "X":
        jugadorActual = "O"
    else:
        jugadorActual = "X"
