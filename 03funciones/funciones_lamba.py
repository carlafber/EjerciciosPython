#FUNCIÓN SENCILLA
#lambda argumentos: expresión
suma = lambda x, y: x + y
resultado = suma(5, 3)
print(resultado)


#FUNCIÓN DE ORDEN SUPERIOR
#map
numeros = [1, 2, 3, 4, 5] #iterador
cuadrados = list(map(lambda x: x ** 2, numeros)) #se aplica lambda a cada elemento de numeros
#list -> convertir map (iterable) en una lista
print(cuadrados)

#filter
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros)) #filtra los elementos, quedando solo los que cumplen la condición
print(pares)


#sorted
lista = [(1, "uno"), (2, "dos"), (3, "tres")]
lista_ordenada = sorted(lista, key=lambda x: x[0])
print(lista_ordenada)



#EXPRESIONES CONDICIONALES
maximo = lambda a, b: a if a > b else b
print(maximo(10, 5)) 