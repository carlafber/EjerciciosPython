"""
Definición de un objeto JSON:
Un objeto JSON es un conjunto de pares clave-valor, donde las claves son cadenas
y los valores pueden ser cadenas, números, objetos JSON, arreglos, true, false o null.

Características de JSON:
1. Ligero: JSON es más ligero que otros formatos como XML, lo que lo hace ideal 
   para el intercambio de datos.
2. Texto: JSON es un formato basado en texto, lo que facilita su manipulación y 
   almacenamiento.
3. Compatible: JSON es un estándar que puede ser utilizado por diferentes lenguajes 
   de programación.

Usos principales de JSON:
- Intercambio de datos entre cliente y servidor en aplicaciones web.
- Almacenamiento de configuraciones en archivos.
- Serialización de objetos en aplicaciones.
- APIs RESTful que devuelven datos en formato JSON.
"""

import json
import os

# Función para guardar datos en un archivo JSON
def guardar_datos_json(archivo, datos):
    # archivo (str): Ruta del archivo JSON donde guardar los datos.
    # datos (dict): Datos a guardar en el archivo JSON.
       with open(archivo, 'w') as f: json.dump(datos, f)  # Guardar datos en el archivo JSON

# Datos a guardar en el archivo JSON
datos_personales = {
    "nombre": "Juan Ruiz",
    "edad": 25,
    "fecha_nacimiento": "1998-05-15",  # Formato: AAAA-MM-DD
    "modulos": ["Bases de datos", "Java", "Python"]
}

# Nombre del archivo JSON
nombre_archivo = '08json\datos_personales.json'

# Guardar los datos en un archivo JSON
guardar_datos_json(nombre_archivo, datos_personales)

print(f"Los datos se han guardado en {nombre_archivo}.")

with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)


os.remove(nombre_archivo)
print(f"Archivo '{nombre_archivo}' eliminado.")