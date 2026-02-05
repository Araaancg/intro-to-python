from inputs import *

# TRES EN RAYA MULTIJUGADOR - 2 JUGADORES

# 1. Pedir el nombre de los jugadores - asignarles una ficha (X, O)
# 2. Preparar la zona de juego
    # 1.1 Tablero
    # 1.2 Turno
# 3. Lógica de juego
    # while
    # mostrar el tablero
    # pedir jugada
    # comprobar que es valido - celda este vacia, este dentro de rango
    # ganador
# 4. meter la partida en un archivo csv

def mostrarTablero(tablero):

    for i, fila in enumerate(tablero):
        print(f" {fila[0]} | {fila[1]} | {fila[2]} ")
        if i < len(tablero) - 1:
            print("---|---|---")

# jugador1 = pedirNombre(1)
# jugador2 = pedirNombre(2)

tablero = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
mostrarTablero(tablero)
# turno = jugador1
# fichas = {
#     jugador1: "X",
#     jugador2: "O"
# }

# ganador = False
# tableroLleno = False

# while not ganador or not tableroLleno:

#     pass

