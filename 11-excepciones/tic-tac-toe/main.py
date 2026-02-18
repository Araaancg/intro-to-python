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

def comprobarGanador(tablero):
    ganador = ""

    # comprobar la fila
    for item in tablero:
        if item[0] == item[1] == item[2] and item[0] != " ":
            print("tenemos ganador")
            ganador = item[0]
    i = 0
    while i < 3 and ganador == "":
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != " ":
            ganador = tablero[i][0]
        i += 1

    # comprobar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
        ganador = tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[2][0] != " ":
        ganador = tablero[0][0]
    
    return ganador 

jugador1 = pedirNombre(1)
jugador2 = pedirNombre(2)

tablero = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
turno = jugador1
fichas = {
    jugador1: "X",
    jugador2: "O"
}

hayGanador = False
empate = False

while not hayGanador and not empate: 
    mostrarTablero(tablero)
    print(f"{turno} es tu turno")

    # PEDIR LA JUGADA Y VALIDARLA
    celdaValida = False
    jugada = ()
    while not celdaValida:
        jugada = pedirJugada()
        if tablero[jugada[0]][jugada[1]] == " ":
            celdaValida = True
        else:
            print("Esta celda esta ocupada, por favor elige otra")

    tablero[jugada[0]][jugada[1]] = fichas[turno]

    # HAY GANADOR?
    ganador = comprobarGanador(tablero)
    if ganador != "":
        hayGanador = True
        nombreGanador = jugador1 if ganador == "X" else jugador2
        print(f"\n{nombreGanador} has ganado!")

        # Podemos usar un 'break' para no ejecutar el resto del codigo
        # break

    # HAY EMPATE?
    # empate = False -> while funciona
    # celdas llenas -> empate = True
    # mientras tanto -> empate = False
    i = 0
    e = 0
    empate = True
    while i < 3:
        while e < 3:
            if tablero[i][e] == " ":
                empate = False
                
            e += 1
        e = 0 # Fallo de la clase anterior
        i += 1
    
    if empate:
        print(f"\nEmpate!")
        # Podemos usar un 'break' para no ejecutar el resto del codigo
        # break

    # CAMBIO DE TURNO  
    # Usando un If en una linea
    turno = jugador1 if turno == jugador2 else jugador2

    # Usando la forma tradicional de hacer Ifs
    # if turno == jugador1:
    #     turno = jugador2
    # else:
    #     turno = jugador1
    
mostrarTablero(tablero)
