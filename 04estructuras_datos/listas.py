lista = [1, 2, 3, 4, 5]
lista1 = list("12345")


#INSERCIÓN
#Agregar un elemento al final
lista.append(6)
print(lista)

lista1.append("6")
print(lista1)

#Insertar un elemento en una posición específica
lista.insert(0,0)
print(lista)

lista1.insert(0,"0")
print(lista1)


#BORRADO
lista.remove(0)
print(lista)

lista1.remove("0")
print(lista1)


#ACTUALIZACIÓN
lista[5] = 7
print(lista)

lista1[5] = "7"
print(lista1)


#ORDENACIÓN
lista = [3, 5, 1, 4, 2,]
lista1 = list("35142")

lista.sort()
print(lista)

lista1.sort()
print(lista1)


lista.reverse()
print(lista)

lista1.reverse()
print(lista1)