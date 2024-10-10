import os
# Nombre del archivo
nombre_archivo = '05manejo_ficheros\prueba'

#Crear y escribir en el archivo
with open(nombre_archivo, 'w') as archivo:
    archivo.write("1. nombre: Carla de la Fuente Bernardino\n" + 
                  "2. edad: 20 años \n3. lenguaje de programación usado: python\n")

print(f"Archivo '{nombre_archivo}' creado exitosamente.")


#Agregar texto a un archivo sin sobrescribirlo
with open(nombre_archivo, 'a') as archivo:
    archivo.write("4. curso: 2º DAM.")

print(f"Texto anexado al archivo '{nombre_archivo}'.")


#Leer
with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)


#Eliminar
os.remove(nombre_archivo)
print(f"Archivo '{nombre_archivo}' eliminado.")