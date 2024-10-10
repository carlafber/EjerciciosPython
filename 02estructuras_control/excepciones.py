#Capturar Múltiples Excepciones
try:
    x = int(input("Ingrese un número: "))
    resultado = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print(f"Ocurrió un error: {e}")


#Uso de else y finally
try:
    x = int(input("Ingrese un número: "))
    resultado = 10 / x
except ZeroDivisionError:
    print("No se puede dividir por cero.")
else:
    print(f"El resultado es {resultado}.")
finally:
    print("Bloque final ejecutado.")


#Propagación de Excepciones
try:
    x = int(input("Ingrese un número: "))
    resultado = 10 / x
except ZeroDivisionError:
    print("No se puede dividir por cero.")
    raise  # Propaga la excepción


#Uso de assert
x = -1
assert x >= 0, "x debe ser no negativo."
