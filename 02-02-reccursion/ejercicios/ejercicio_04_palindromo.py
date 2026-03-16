"""
Ejercicio 4: Detector de Palíndromos
=====================================

Un palíndromo es una palabra que se lee igual de izquierda a derecha
que de derecha a izquierda.

Ejemplos:
    "ana" -> True
    "radar" -> True
    "hola" -> False
    "a" -> True
    "" -> True

TAREA: Implementa la función es_palindromo de forma recursiva.

Idea recursiva:
    - Si el primer y último carácter son iguales
    - Y el resto (sin primero ni último) también es palíndromo
    - Entonces es palíndromo
"""


def es_palindromo(texto: str) -> bool:
    """Comprueba si un texto es palíndromo de forma recursiva.
    
    Args:
        texto: String a comprobar (asume minúsculas sin espacios)
        
    Returns:
        True si es palíndromo, False si no
    """
    # TODO: Implementa aquí
    # Pista:
    #   - Caso base: texto vacío o un solo carácter -> True
    #   - Caso recursivo: 
    #       * Si primer != último -> False
    #       * Si no, comprobar es_palindromo(texto[1:-1])


    if len(texto) <= 1:
        print("m")
        return True
    
    if texto[0] == texto[-1]:
        resto = texto[1:-1]
        print("m")
        return es_palindromo(resto) # True
    else:
        return False
    

# radar -> r y r | ada
# ada -> a y a | d
# d -> True

resultado = es_palindromo("radar")
print(resultado)

# ============================================
# TESTS - No modificar
# ============================================

# def test_es_palindromo():
#     print("Probando es_palindromo()...")
    
#     # Casos base
#     assert es_palindromo("") == True, "'' es palíndromo"
#     assert es_palindromo("a") == True, "'a' es palíndromo"
    
#     # Palíndromos
#     assert es_palindromo("aa") == True, "'aa' es palíndromo"
#     assert es_palindromo("ana") == True, "'ana' es palíndromo"
#     assert es_palindromo("radar") == True, "'radar' es palíndromo"
#     assert es_palindromo("anilina") == True, "'anilina' es palíndromo"
#     assert es_palindromo("reconocer") == True, "'reconocer' es palíndromo"
    
#     # No palíndromos
#     assert es_palindromo("ab") == False, "'ab' no es palíndromo"
#     assert es_palindromo("hola") == False, "'hola' no es palíndromo"
#     assert es_palindromo("python") == False, "'python' no es palíndromo"
    
#     print("  ✓ Todos los tests pasaron!")


# if __name__ == "__main__":
#     # Descomenta para probar manualmente
#     # print(f"es_palindromo('ana') = {es_palindromo('ana')}")
#     # print(f"es_palindromo('radar') = {es_palindromo('radar')}")
#     # print(f"es_palindromo('hola') = {es_palindromo('hola')}")
    
#     test_es_palindromo()
