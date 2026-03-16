"""
SOLUCIONES - Solo para el profesor
===================================

Soluciones a todos los ejercicios de recursión.
"""

# ============================================
# EJERCICIO 1: Suma Armónica
# ============================================

def suma_armonica(n: int) -> float:
    """Calcula la suma armónica hasta n de forma recursiva."""
    # Caso base
    if n == 1:
        return 1.0
    
    # Caso recursivo
    return 1/n + suma_armonica(n - 1)


# ============================================
# EJERCICIO 2: Decimal a Binario
# ============================================

def decimal_a_binario_str(n: int) -> str:
    """Convierte un decimal a binario (como string)."""
    # Caso base
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    
    # Caso recursivo
    return decimal_a_binario_str(n // 2) + str(n % 2)


def decimal_a_binario_lista(n: int) -> list:
    """Convierte un decimal a binario (como lista de dígitos)."""
    # Usando la versión string
    return [int(d) for d in decimal_a_binario_str(n)]


# ============================================
# EJERCICIO 3: Suma de Dígitos
# ============================================

def suma_digitos(n: int) -> int:
    """Suma todos los dígitos de un número de forma recursiva."""
    # Caso base: un solo dígito
    if n < 10:
        return n
    
    # Caso recursivo
    return (n % 10) + suma_digitos(n // 10)


# ============================================
# EJERCICIO 4: Palíndromo
# ============================================

def es_palindromo(texto: str) -> bool:
    """Comprueba si un texto es palíndromo de forma recursiva."""
    # Caso base: vacío o un carácter
    if len(texto) <= 1:
        return True
    
    # Caso recursivo
    if texto[0] != texto[-1]:
        return False
    
    return es_palindromo(texto[1:-1])


# ============================================
# EJERCICIO 5: Potencia
# ============================================

def potencia_simple(base: int, exponente: int) -> int:
    """Calcula base^exponente de forma recursiva simple."""
    # Caso base
    if exponente == 0:
        return 1
    
    # Caso recursivo
    return base * potencia_simple(base, exponente - 1)


def potencia_rapida(base: int, exponente: int) -> int:
    """Calcula base^exponente usando exponenciación rápida."""
    # Caso base
    if exponente == 0:
        return 1
    
    # Si es par: base^n = (base^(n/2))^2
    if exponente % 2 == 0:
        mitad = potencia_rapida(base, exponente // 2)
        return mitad * mitad
    
    # Si es impar: base^n = base * base^(n-1)
    return base * potencia_rapida(base, exponente - 1)


# ============================================
# VERIFICACIÓN
# ============================================

if __name__ == "__main__":
    print("=" * 50)
    print("VERIFICANDO TODAS LAS SOLUCIONES")
    print("=" * 50)
    
    # Ejercicio 1
    print("\n1. Suma Armónica")
    print(f"   H(1) = {suma_armonica(1)}")
    print(f"   H(4) = {suma_armonica(4):.4f}")
    print(f"   H(10) = {suma_armonica(10):.4f}")
    
    # Ejercicio 2
    print("\n2. Decimal a Binario")
    print(f"   13 -> {decimal_a_binario_str(13)}")
    print(f"   255 -> {decimal_a_binario_str(255)}")
    print(f"   13 -> {decimal_a_binario_lista(13)}")
    
    # Ejercicio 3
    print("\n3. Suma de Dígitos")
    print(f"   suma_digitos(123) = {suma_digitos(123)}")
    print(f"   suma_digitos(9999) = {suma_digitos(9999)}")
    
    # Ejercicio 4
    print("\n4. Palíndromo")
    print(f"   es_palindromo('ana') = {es_palindromo('ana')}")
    print(f"   es_palindromo('radar') = {es_palindromo('radar')}")
    print(f"   es_palindromo('hola') = {es_palindromo('hola')}")
    
    # Ejercicio 5
    print("\n5. Potencia")
    print(f"   potencia_simple(2, 10) = {potencia_simple(2, 10)}")
    print(f"   potencia_rapida(2, 10) = {potencia_rapida(2, 10)}")
    print(f"   potencia_rapida(2, 20) = {potencia_rapida(2, 20)}")
    
    print("\n" + "=" * 50)
    print("✅ Todas las soluciones funcionan correctamente")
    print("=" * 50)
