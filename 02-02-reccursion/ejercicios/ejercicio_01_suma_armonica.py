"""
Ejercicio 1: Suma Armónica
==========================

La suma armónica hasta n es:
    H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

Ejemplos:
    H(1) = 1
    H(2) = 1 + 0.5 = 1.5
    H(4) = 1 + 0.5 + 0.333... + 0.25 = 2.083...

TAREA: Implementa la función suma_armonica de forma recursiva.
"""


def suma_armonica(n: int) -> float:
    """Calcula la suma armónica hasta n de forma recursiva.
    
    Args:
        n: Número entero positivo
        
    Returns:
        La suma armónica H(n)
    """
    # TODO: Implementa aquí
    # Pista: 
    #   - Caso base: ¿cuánto vale H(1)?
    #   - Caso recursivo: H(n) = 1/n + H(n-1)
    pass


# ============================================
# TESTS - No modificar
# ============================================

def test_suma_armonica():
    print("Probando suma_armonica()...")
    
    # Test caso base
    assert abs(suma_armonica(1) - 1.0) < 0.0001, "H(1) debería ser 1"
    
    # Tests básicos
    assert abs(suma_armonica(2) - 1.5) < 0.0001, "H(2) debería ser 1.5"
    assert abs(suma_armonica(4) - 2.0833) < 0.01, "H(4) debería ser ~2.083"
    assert abs(suma_armonica(10) - 2.9289) < 0.01, "H(10) debería ser ~2.928"
    
    print("  ✓ Todos los tests pasaron!")


if __name__ == "__main__":
    # Descomenta para probar manualmente
    # print(f"H(1) = {suma_armonica(1)}")
    # print(f"H(4) = {suma_armonica(4)}")
    # print(f"H(10) = {suma_armonica(10)}")
    
    test_suma_armonica()
