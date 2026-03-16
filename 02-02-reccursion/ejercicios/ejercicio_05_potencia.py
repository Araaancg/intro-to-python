"""
Ejercicio 5: Potencia Recursiva
================================

Calcula base^exponente de forma recursiva (sin usar ** ni pow()).

Ejemplos:
    potencia(2, 3) = 8      (2 * 2 * 2)
    potencia(5, 0) = 1      (cualquier número elevado a 0 es 1)
    potencia(3, 4) = 81     (3 * 3 * 3 * 3)

TAREA: Implementa DOS versiones:
    1. potencia_simple: versión básica
    2. potencia_rapida: versión optimizada (exponenciación rápida)
"""


def potencia_simple(base: int, exponente: int) -> int:
    """Calcula base^exponente de forma recursiva simple.
    
    Args:
        base: La base
        exponente: El exponente (>= 0)
        
    Returns:
        base elevado a exponente
    """
    # TODO: Implementa aquí
    # Pista:
    #   - Caso base: exponente == 0 -> return 1
    #   - Caso recursivo: base * potencia_simple(base, exponente - 1)
    pass


def potencia_rapida(base: int, exponente: int) -> int:
    """Calcula base^exponente usando exponenciación rápida.
    
    Esta versión es más eficiente para exponentes grandes.
    
    Idea:
        - Si exponente es par: base^n = (base^(n/2))^2
        - Si exponente es impar: base^n = base * base^(n-1)
    
    Ejemplo: 2^8 = (2^4)^2 = ((2^2)^2)^2 = ((4)^2)^2 = (16)^2 = 256
    Solo 3 multiplicaciones en lugar de 7.
    """
    # TODO: Implementa aquí (más difícil)
    # Pista:
    #   - Caso base: exponente == 0 -> return 1
    #   - Si exponente es par: 
    #       mitad = potencia_rapida(base, exponente // 2)
    #       return mitad * mitad
    #   - Si exponente es impar:
    #       return base * potencia_rapida(base, exponente - 1)
    pass


# ============================================
# TESTS - No modificar
# ============================================

def test_potencia():
    print("Probando potencia_simple()...")
    
    assert potencia_simple(2, 0) == 1, "2^0 = 1"
    assert potencia_simple(2, 1) == 2, "2^1 = 2"
    assert potencia_simple(2, 3) == 8, "2^3 = 8"
    assert potencia_simple(2, 10) == 1024, "2^10 = 1024"
    assert potencia_simple(3, 4) == 81, "3^4 = 81"
    assert potencia_simple(5, 3) == 125, "5^3 = 125"
    
    print("  ✓ OK")
    
    print("Probando potencia_rapida()...")
    
    assert potencia_rapida(2, 0) == 1, "2^0 = 1"
    assert potencia_rapida(2, 1) == 2, "2^1 = 2"
    assert potencia_rapida(2, 3) == 8, "2^3 = 8"
    assert potencia_rapida(2, 10) == 1024, "2^10 = 1024"
    assert potencia_rapida(2, 20) == 1048576, "2^20 = 1048576"
    assert potencia_rapida(3, 4) == 81, "3^4 = 81"
    
    print("  ✓ OK")
    
    print("\n✅ Todos los tests pasaron!")


if __name__ == "__main__":
    # Descomenta para probar manualmente
    # print(f"potencia_simple(2, 10) = {potencia_simple(2, 10)}")
    # print(f"potencia_rapida(2, 10) = {potencia_rapida(2, 10)}")
    
    test_potencia()
