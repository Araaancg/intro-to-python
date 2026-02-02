
def mostrar_menu() -> None:
    """Muestra el menú de opciones de la calculadora"""
    print("")
    print("===== CALCULADORA =====")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("=======================")


def pedir_numeros() -> tuple:
    """Pide dos números al usuario
    
    Returns:
        tuple: (num1, num2) los dos números introducidos
    """
    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))
    return num1, num2


def mostrar_resultado(num1: float, operador: str, num2: float, resultado: float) -> None:
    """Muestra el resultado de una operación con formato
    
    Args:
        num1: Primer operando
        operador: Símbolo de la operación (+, -, *, /)
        num2: Segundo operando
        resultado: Resultado de la operación
    """
    print("------------------------")
    print(f"{num1} {operador} {num2} = {resultado}")
    print("------------------------")


def sumar(a: float, b: float) -> float:
    """Suma dos números"""
    return a + b


def restar(a: float, b: float) -> float:
    """Resta dos números"""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Multiplica dos números"""
    return a * b


def dividir(a: float, b: float) -> float:
    """Divide dos números
    
    Returns:
        El resultado de la división, o None si b es 0
    """
    if b != 0:
        return a / b
    else:
        return None

