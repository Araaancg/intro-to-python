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