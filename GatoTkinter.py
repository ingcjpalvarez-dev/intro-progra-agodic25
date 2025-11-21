# JuegoGatoConFunciones - AVANCE DEL PROYECTO
# Este es solo un avance, falta integrar completamente con Tkinter

from random import choice
import tkinter as tk
from tkinter import messagebox

# --- Funciones ORIGINALES (sin modificar) --- #

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

# --- NUEVAS FUNCIONES PARA EL AVANCE --- #

def mostrar_tablero_grafico(tab):
    # AVANCE: Muestra el tablero en una ventana Tkinter básica
    ventana_tablero = tk.Tk()
    ventana_tablero.title("Tablero - AVANCE")
    ventana_tablero.geometry("200x250")
    
    for i in range(3):
        for j in range(3):
            tk.Label(ventana_tablero, text=tab[i][j], font=("Arial", 20), 
                    borderwidth=2, relief="solid", width=3, height=1).grid(row=i, column=j, padx=2, pady=2)
    
    tk.Button(ventana_tablero, text="Cerrar", command=ventana_tablero.destroy).grid(row=3, column=0, columnspan=3, pady=10)
    ventana_tablero.mainloop()

def guardar_partida(ganador, modo):
    # Esta función guarda en archivo (avance de persistencia)
    try:
        with open("partidas.txt", "a") as archivo:
            archivo.write(f"Ganador: {ganador}, Modo: {modo}\n")
        print("Partida guardada en archivo")
    except:
        print("Error al guardar")

def ver_ultimo_resultado():
    try:
        with open("partidas.txt", "r") as archivo:
            lineas = archivo.readlines()
            if lineas:
                messagebox.showinfo("Último resultado", lineas[-1])
            else:
                messagebox.showinfo("Último resultado", "No hay partidas guardadas")
    except:
        messagebox.showinfo("Último resultado", "No hay partidas guardadas")

def mostrar_ventana_inicio():
    # Esta muestra una ventana simple de Tkinter (avance de GUI)
    ventana = tk.Tk()
    ventana.title("Mi Tic Tac Toe - AVANCE")
    ventana.geometry("300x250")
    
    tk.Label(ventana, text="MI JUEGO DE GATO", font=("Arial", 16)).pack(pady=20)
    tk.Label(ventana, text="AVANCE DEL PROYECTO").pack()
    
    def empezar_consola():
        ventana.destroy()
        jugar_en_consola()
    
    tk.Button(ventana, text="Jugar en Consola", command=empezar_consola).pack(pady=10)
    tk.Button(ventana, text="Ver último resultado", command=ver_ultimo_resultado).pack(pady=5)
    tk.Button(ventana, text="Salir", command=ventana.quit).pack()
    
    ventana.mainloop()

def jugar_en_consola():
    # Tu juego original funciona igual en consola
    print("\n" + "="*40)
    print("JUGANDO EN CONSOLA (modo original)")
    print("="*40)
    
    # Combinaciones ganadoras (posiciones)
    ganadoras = [
        (0,1,2), (3,4,5), (6,7,8),  # filas
        (0,3,6), (1,4,7), (2,5,8),  # columnas
        (0,4,8), (2,4,6)            # diagonales
    ]

    # Crear tablero
    tablero = crear_tablero()

    # AVANCE: Mostrar tablero gráfico una vez
    if input("¿Ver tablero gráfico? (s/n): ").lower() == 's':
        mostrar_tablero_grafico(tablero)

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
            # AVANCE: Guardar partida
            guardar_partida(jugadorActual, "CPU" if modo == "2" else "2 jugadores")
            break

        if turnos == 9:
            mostrar_tablero(tablero)
            print("Empate! No hay más movimientos")
            # AVANCE: Guardar empate
            guardar_partida("Empate", "CPU" if modo == "2" else "2 jugadores")
            break

        jugadorActual = cambiar_jugador(jugadorActual)

# --- PROGRAMA PRINCIPAL MODIFICADO --- #
if __name__ == "__main__":
    print("Cargando avance del proyecto...")
    
    # AVANCE: Ahora muestra una ventana de inicio
    mostrar_ventana_inicio()
    
    print("\nGracias por jugar!")