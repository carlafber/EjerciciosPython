tupla = (1, 2, 3)
print(tupla)
#LAS TUPLAS SON INMUTABLES, HAY QUE IR CREANDO/ACTUALIZANDO TUPLAS NUEVAS

#INSERCIÓN
tupla = tupla + (4,)
print(tupla)


#BORRADO
tupla = tuple(x for x in tupla if x != 2)
print(tupla)


#ACTUALIZACIÓN
tupla = (tupla[0], 5, tupla[2])
print(tupla)


#ORDENACIÓN
tupla = tuple(sorted(tupla))
print(tupla)