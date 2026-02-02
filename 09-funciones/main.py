from funcs import *

opcion = 0

while opcion != 5:
    
    mostrar_menu()
    opcion = int(input("Elige opción: "))
    
    if opcion >= 1 and opcion <= 4:
        # Todas las operaciones necesitan dos números
        num1, num2 = pedir_numeros()
        
        if opcion == 1:
            resultado = sumar(num1, num2)
            mostrar_resultado(num1, "+", num2, resultado)
            
        elif opcion == 2:
            resultado = restar(num1, num2)
            mostrar_resultado(num1, "-", num2, resultado)
            
        elif opcion == 3:
            resultado = multiplicar(num1, num2)
            mostrar_resultado(num1, "*", num2, resultado)
            
        elif opcion == 4:
            resultado = dividir(num1, num2)
            if resultado is not None:
                mostrar_resultado(num1, "/", num2, resultado)
            else:
                print("Error: No se puede dividir entre 0")
                
    elif opcion == 5:
        print("¡Hasta luego!")
        
    else:
        print("Opción no válida")