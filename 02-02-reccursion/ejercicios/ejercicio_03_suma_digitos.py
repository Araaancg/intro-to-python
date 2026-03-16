"""
Ejercicio 3: Suma de Dígitos
============================

Calcula la suma de todos los dígitos de un número de forma recursiva.

Ejemplos:
    suma_digitos(123) = 1 + 2 + 3 = 6
    suma_digitos(9999) = 9 + 9 + 9 + 9 = 36
    suma_digitos(7) = 7

TAREA: Implementa la función suma_digitos de forma recursiva.

Pista: 
    - El último dígito de n es: n % 10
    - El número sin el último dígito es: n // 10
"""


def suma_digitos(n: int) -> int:
    """Suma todos los dígitos de un número de forma recursiva.
    
    Args:
        n: Número entero no negativo
        
    Returns:
        La suma de sus dígitos
    """
    # TODO: Implementa aquí
    # Pista:
    #   - Caso base: n < 10 (un solo dígito)
    #   - Caso recursivo: (n % 10) + suma_digitos(n // 10)
    pass


# ============================================
# TESTS - No modificar
# ============================================

def test_suma_digitos():
    print("Probando suma_digitos()...")
    
    # Casos de un dígito (casos base)
    assert suma_digitos(0) == 0, "suma_digitos(0) = 0"
    assert suma_digitos(5) == 5, "suma_digitos(5) = 5"
    assert suma_digitos(9) == 9, "suma_digitos(9) = 9"
    
    # Casos múltiples dígitos
    assert suma_digitos(12) == 3, "suma_digitos(12) = 3"
    assert suma_digitos(123) == 6, "suma_digitos(123) = 6"
    assert suma_digitos(9999) == 36, "suma_digitos(9999) = 36"
    assert suma_digitos(12345) == 15, "suma_digitos(12345) = 15"
    
    print("  ✓ Todos los tests pasaron!")


if __name__ == "__main__":
    # Descomenta para probar manualmente
    # print(f"suma_digitos(123) = {suma_digitos(123)}")
    # print(f"suma_digitos(9999) = {suma_digitos(9999)}")
    
    test_suma_digitos()
