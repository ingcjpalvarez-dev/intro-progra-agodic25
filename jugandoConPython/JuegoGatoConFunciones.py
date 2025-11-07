#JuegoGatoConFunciones

from random import choice

# --- Funciones --- #

# Crear tablero vacío 3x3
def crear_tablero():
    return [["1","2","3"],
            ["4","5","6"],
            ["7","8","9"]]

# Convertir tablero 3x3 a lista lineal
def tablero_lineal(tab):
    linea = []
    for fila in tab:
        for celda in fila:
            linea.append(celda)
    return linea

# Mostrar tablero
def mostrar_tablero(tab):
    print(f"""
 {tab[0][0]} | {tab[0][1]} | {tab[0][2]}
---+---+---
 {tab[1][0]} | {tab[1][1]} | {tab[1][2]}
---+---+---
 {tab[2][0]} | {tab[2][1]} | {tab[2][2]}
""")

# Pedir movimiento jugador
def movimiento_jugador(jugador, tab):
    while True:
        mov = input(f"Jugador {jugador}, ingresa la posición: ")
        if not mov.isnumeric():
            print("Ingresa un número válido")
            continue
        mov = int(mov)
        if mov < 1 or mov > 9:
            print("Número fuera de rango")
            continue
        fila = (mov-1)//3
        col = (mov-1)%3
        if tab[fila][col] in ["X","O"]:
            print("Casilla ocupada")
            continue
        return fila, col

# Movimiento CPU simple
def movimiento_cpu(tab):
    disponibles = []
    for i in range(3):
        for j in range(3):
            if tab[i][j] not in ["X","O"]:
                disponibles.append((i,j))
    fila, col = choice(disponibles)
    print("CPU elige la posición:", tab[fila][col])
    return fila, col

# Revisar ganador
def revisar_ganador(tab, ganadoras):
    linea = tablero_lineal(tab)
    for c in ganadoras:
        if linea[c[0]] == linea[c[1]] == linea[c[2]]:
            return True
    return False

# Cambiar jugador
def cambiar_jugador(jugador):
    return "O" if jugador == "X" else "X"

# --- Programa principal --- #

# Combinaciones ganadoras (posiciones)
ganadoras = [
    (0,1,2), (3,4,5), (6,7,8),  # filas
    (0,3,6), (1,4,7), (2,5,8),  # columnas
    (0,4,8), (2,4,6)            # diagonales
]

# Crear tablero
tablero = crear_tablero()

# Preguntar modo
modo = input("Modo de juego (1=Jugador vs Jugador, 2=Jugador vs CPU): ")

jugadorActual = "X"
turnos = 0
ganador = False

while True:
    mostrar_tablero(tablero)

    if modo == "2" and jugadorActual == "O":
        fila, col = movimiento_cpu(tablero)
    else:
        fila, col = movimiento_jugador(jugadorActual, tablero)

    tablero[fila][col] = jugadorActual
    turnos += 1

    if revisar_ganador(tablero, ganadoras):
        mostrar_tablero(tablero)
        print("Gana el jugador", jugadorActual)
        break

    if turnos == 9:
        mostrar_tablero(tablero)
        print("Empate! No hay más movimientos")
        break

    jugadorActual = cambiar_jugador(jugadorActual)
