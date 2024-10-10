import os

nombre_archivo = '05manejo_ficheros\ ventas.txt'


def buscar_producto(nombre):
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            if nombre in linea:
                return linea.strip()  # Devuelve la línea completa sin saltos de línea
    return None  # Retorna None si no se encuentra el producto


def insertar_producto():
    print("Para insertar un producto introduzca los siguientes datos:")
    nombre = input("Nombre: ")
    while buscar_producto(nombre) is not None:
        nombre = input("El producto ya existe, introduzca otro: ")   
    cantidad = int(input("Cantidad: "))
    precio = input("Precio: ")
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(f"NOMBRE: {nombre}. CANTIDAD: {cantidad}. PRECIO: {precio}\n")
    print("Producto agregado correctamente.")


def consultar_producto():
    nombre = input("Introduzca el nombre del producto a consultar: ")
    producto = buscar_producto(nombre)
    if producto:
        print(f"Información del producto:\n {producto}")
    else:
        print("El producto no existe.")


def actualizar_producto():
    nombre = input("Introduzca el nombre del producto a actualizar: ")
    producto = buscar_producto(nombre)
    if producto is None:
        print("El producto no existe.")
        return
    nueva_cantidad = int(input("Introduzca la nueva cantidad: "))
    nuevo_precio = input("Introduzca el nuevo precio: ")
    # Leer todas las líneas y actualizar la necesaria
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    with open(nombre_archivo, 'w') as archivo:
        for linea in lineas:
            if f"NOMBRE: {nombre}" in linea:
                archivo.write(f"NOMBRE: {nombre}. CANTIDAD: {nueva_cantidad}. PRECIO: {nuevo_precio}.\n")
            else:
                archivo.write(linea)  # Escribir la línea original si no es la que se está actualizando
    print("Producto actualizado correctamente.")
 

def borrar_producto():
    nombre = input("Introduzca el nombre del producto a eliminar: ")
    producto = buscar_producto(nombre)
    if producto is None:
        print("El producto no existe.")
        return
    # Leer todas las líneas y filtrar la que se va a eliminar
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    with open(nombre_archivo, 'w') as archivo:
        for linea in lineas:
            if f"NOMBRE: {nombre}" not in linea:  # Escribe solo las líneas que no coinciden
                archivo.write(linea)  # Escribir la línea original si no es la que se está eliminando
    print("Producto eliminado correctamente.")


def mostrar_productos():
    with open(nombre_archivo, 'r') as archivo:
        print(f"PRODUCTOS:\n{archivo.read()}")



# Crea el archivo si no existe
if not os.path.exists(nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        pass  # Solo se crea el archivo vacío

opcion = -1
while (opcion != 0):
    print("\nEMPRESA\n1. Añadir producto\n2. Consultar producto\n3. Actualizar producto" + 
        "\n4. Borrar producto\n5. Mostrar todos los productos\n6. Calcular venta total" +
        "\n7. Calcular venta por producto\n--------------------------------\n0. Salir")
    opcion = int(input("Selecciona una opción: "))
    match opcion:
        case 1:
            insertar_producto()
        case 2:
            consultar_producto()
        case 3:
            actualizar_producto()
        case 4:
            borrar_producto()
        case 5:
            mostrar_productos()
        case 6:
            2
        case 7:
            2
        case 0:
            os.remove(nombre_archivo)
            print(f"Archivo '{nombre_archivo}' eliminado.")
            exit
        case _:
            print("Error")



