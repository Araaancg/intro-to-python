from validaciones import *
from excepciones import *

def pedirNombre(num):
    nombre = ""
    nombreValido = False
    while not nombreValido:
        # validar que es correcto
        # No puede estar vacio
        # Solo letras
        try:
            entrada = input(f"Nombre jugador {num}: ")
            nombre = validarNombre(entrada)
            nombreValido = True
        except NombreError as error:
            print(f"ERROR: {error}" )

    return nombre

def pedirJugada():
    filaValida, colValida = False, False
    fila, columna = 0, 0

    while not filaValida:
        fila = int(input("fila (1-3) -> "))
        if fila <= 3 and fila >= 1:
            filaValida = True
        if not filaValida:
            # print("El numero introducido esta fuera de rango")
            raise CeldaError("El numero introducido esta fuera de rango")

    while not colValida:
        columna = int(input("columna (1-3) -> "))
        if columna <= 3 and columna >= 1:
            colValida = True
        if not colValida:
            # print("El numero introducido esta fuera de rango")
            raise CeldaError("El numero introducido esta fuera de rango")
    
    return fila - 1 , columna - 1