from excepciones import * 

def validarNombre(nombre: str):
    nombre.strip()

    if len(nombre) == 0:
        raise NombreError("El nombre no puede estar vacio")
    
    if not nombre.isalpha():
        raise NombreError("El nombre que introduzcas solo puede contener letras")
    
    return nombre  