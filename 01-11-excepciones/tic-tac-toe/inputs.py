from validaciones import *
from excepciones import *

def pedirNombre(num: int) -> str:
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

    try:
        while not filaValida:
            inputUser = int(input("fila (1-3) -> "))
            filaValida, fila = validarFila(inputUser)
    except CeldaError as error:
        print(f"ERROR: {error}" )

    
    while not colValida:
        columna = int(input("columna (1-3) -> "))
        if columna <= 3 and columna >= 1:
            colValida = True
        if not colValida:
            print("El numero introducido esta fuera de rango")
            # raise CeldaError("El numero introducido esta fuera de rango")
    
    return fila - 1 , columna - 1