diccionario = {"nombre": "Alicia", "edad": 30}
print(diccionario)



#INSERCCIÓN
diccionario["ciudad"] = "Madrid"
print(diccionario)

#update() para agregar múltiples pares
diccionario.update({"profesión": "Ingeniera", "hobbies": ["lectura", "ciclismo"]})
print(diccionario)



#BORRADO
del diccionario["edad"]
print(diccionario)

#pop(), también devuelve el valor eliminado
ciudad = diccionario.pop("ciudad")
print(ciudad)
print(diccionario)

#el último par clave-valor usando popitem()
ultimo_elemento = diccionario.popitem()
print(ultimo_elemento)
print(diccionario)



#ACTUALIZACIÓN
diccionario["nombre"] = "Bob"
print(diccionario)


#ORDENACIÓN
diccionario_desordenado = {"b": 2, "a": 1, "c": 3}


diccionario_ordenado = {k: diccionario_desordenado[k] for k in sorted(diccionario_desordenado)}
print(diccionario_ordenado)
