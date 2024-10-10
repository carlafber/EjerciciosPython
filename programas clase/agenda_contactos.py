class Persona:
    def __init__(self, nombre, tlf):
        self.nombre = nombre
        self.tlf = tlf
    def obtener_nombre(self):
        return self.nombre
    def obtener_tlf(self):
        return self.tlf
    


def buscar_contacto():
    if(not contactos):
        print("No hay contactos.")
    else:
        nombre = input("Para buscar un contacto, indroduzca su nombre: ")
        for contacto in contactos:
            if contacto.obtener_nombre() == nombre:
                print("TELÉFONO: " + str(contacto.obtener_tlf()))
                break
            else:
                print("El contacto no existe.")



def insertar_contacto():
    print("Para insertar un contacto introduzca los siguientes datos:")
    nombre = input("Nombre: ")
    for contacto in contactos:
            if contacto.obtener_nombre() == nombre:
                nombre = input("El contacto ya existe, introduzca otro: ")
                break
            return
    tlf = input("Número de teléfono: ")
    while((len(tlf) != 9) or (not tlf.isdigit)):
        tlf = int(input("Número incorrecto. Vuelve a introducirlo: "))
    contactos.append(Persona(nombre, tlf))
    print("Contacto agregado correctamente.")



def actualizar_contacto():
    if(not contactos):
        print("No hay contactos.")
    else:
        nombre = input("Para actualizar un contacto, introduzca su nombre: ")
        for contacto in contactos:
            if contacto.obtener_nombre() == nombre:
                tlf = input("Introduzca el nuevo número de teléfono: ")
                while(len(str(tlf)) != 9):
                    tlf = int(input("Número incorrecto. Vuelve a introducirlo: "))
                contactos.append(Persona(nombre, tlf))
                print("Contacto actualizado.")
                break
        print("Contacto no encontrado.")



def eliminar_contacto():
    if(not contactos):
        print("No hay contactos.")
    else:
        nombre = input("Para eliminar un contacto, introduzca su nombre: ")
        for contacto in contactos:
            if contacto.obtener_nombre() == nombre:
                contactos.remove(contacto)
                print("Contacto eliminado.")
                break
            else:
                print("El contacto no existe.")



def mostrar_contactos():
    if(not contactos):
        print("No hay contactos.")
    else:
        contactos_ordenados = sorted(contactos, key = Persona.obtener_nombre)
        print("CONTACTOS:")
        for contacto in contactos_ordenados:
            print(str(contacto.obtener_nombre()) + " - " + str(contacto.obtener_tlf()))

    

contactos = []
opcion = -1
while (opcion != 0):
    print("\nAGENDA\n1. Buscar contacto\n2. Insertar contacto\n3. Actualizar contacto" + 
        "\n4. Eliminar contacto\n5. Mostrar todos los contactos en orden ascendente" + 
        "\n---------------------------------------------------\n0. Salir")
    opcion = int(input("Selecciona una opción: "))
    match opcion:
        case 1:
            buscar_contacto()
        case 2:
            insertar_contacto()
        case 3:
            actualizar_contacto()
        case 4:
            eliminar_contacto()
        case 5:
            mostrar_contactos()
        case 0:
            exit
        case _:
            print("Error")