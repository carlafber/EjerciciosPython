sets = {1, 2, 3, 4}

#INSERCIÓN
sets.add(5)
print(sets)

#No se puede agregar un elemento duplicado
sets.add(3)
print(sets)


#BORRADO
sets.remove(2)
print(sets)

sets.discard(3)
print(sets)


#ACTUALIZACIÓN
sets.update([6, 7, 8])
print(sets)


#ORDENACIÓN
sets = {3, 1, 4, 2,}
lista = sorted(sets)
print(lista)
sets = set(lista)
print(sets) 