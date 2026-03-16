"""
Ejercicio 2: Conversión Decimal a Binario
==========================================

Convierte un número decimal a su representación binaria usando recursión.

El algoritmo es:
    - Dividir entre 2 sucesivamente
    - Los restos (de atrás hacia adelante) forman el número binario

Ejemplo: 13 en binario
    13 / 2 = 6, resto 1
    6 / 2 = 3, resto 0
    3 / 2 = 1, resto 1
    1 / 2 = 0, resto 1
    
    Leyendo de abajo a arriba: 1101

TAREA: Implementa DOS versiones:
    1. decimal_a_binario_str: devuelve un string "1101"
    2. decimal_a_binario_lista: devuelve una lista [1, 1, 0, 1]
"""


def decimal_a_binario_str(n: int) -> str:
    """Convierte un decimal a binario (como string).
    
    Args:
        n: Número entero no negativo
        
    Returns:
        String con la representación binaria
        
    Ejemplos:
        decimal_a_binario_str(13) -> "1101"
        decimal_a_binario_str(0) -> "0"
        decimal_a_binario_str(1) -> "1"
    """
    # TODO: Implementa aquí
    # Pista:
    #   - Caso base: n == 0 o n == 1
    #   - Caso recursivo: decimal_a_binario_str(n // 2) + str(n % 2)
    pass


def decimal_a_binario_lista(n: int) -> list:
    """Convierte un decimal a binario (como lista de dígitos).
    
    Args:
        n: Número entero no negativo
        
    Returns:
        Lista con los dígitos binarios
        
    Ejemplos:
        decimal_a_binario_lista(13) -> [1, 1, 0, 1]
        decimal_a_binario_lista(0) -> [0]
    """
    # TODO: Implementa aquí
    # Puedes usar la versión string y convertirla,
    # o hacerlo directamente con listas
    pass


# ============================================
# TESTS - No modificar
# ============================================

def test_decimal_a_binario():
    print("Probando decimal_a_binario_str()...")
    
    assert decimal_a_binario_str(0) == "0", "0 en binario es '0'"
    assert decimal_a_binario_str(1) == "1", "1 en binario es '1'"
    assert decimal_a_binario_str(2) == "10", "2 en binario es '10'"
    assert decimal_a_binario_str(5) == "101", "5 en binario es '101'"
    assert decimal_a_binario_str(13) == "1101", "13 en binario es '1101'"
    assert decimal_a_binario_str(255) == "11111111", "255 en binario es '11111111'"
    
    print("  ✓ OK")
    
    print("Probando decimal_a_binario_lista()...")
    
    assert decimal_a_binario_lista(0) == [0], "0 en binario es [0]"
    assert decimal_a_binario_lista(1) == [1], "1 en binario es [1]"
    assert decimal_a_binario_lista(13) == [1, 1, 0, 1], "13 en binario es [1,1,0,1]"
    
    print("  ✓ OK")
    
    print("\n✅ Todos los tests pasaron!")


if __name__ == "__main__":
    # Descomenta para probar manualmente
    # print(f"13 -> {decimal_a_binario_str(13)}")
    # print(f"255 -> {decimal_a_binario_str(255)}")
    
    test_decimal_a_binario()
