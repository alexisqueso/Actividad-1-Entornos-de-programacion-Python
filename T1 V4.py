# Se utiliza un bloque try-except para manejar posibles errores durante la ejecución del código.
try:
    # Solicita al usuario que ingrese un número para usarlo como divisor.
    divisor = int(input("Ingresa un número divisor: "))
    
    # Realiza una división de 100 por el número ingresado por el usuario.
    result = 100 / divisor
    
    # Imprime el resultado de la división.
    print(result)

# Maneja el error específico cuando se intenta dividir por cero.
except ZeroDivisionError as e:
    # Mensaje de error indicando que no se puede dividir por cero.
    print("Error: El divisor no puede ser cero")
    # Muestra el error original generado por Python para mayor detalle.
    print("Ha ocurrido un error:", e)

# Maneja el error específico cuando el usuario no ingresa un número válido.
except ValueError as e:
    # Mensaje de error indicando que la entrada debe ser un número entero.
    print("Error: Debes introducir un número válido")
    # Muestra el error original generado por Python para mayor detalle.
    print("Ha ocurrido un error:", e)
