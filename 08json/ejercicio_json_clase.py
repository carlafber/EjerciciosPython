import json
import os

def guardar_datos_json(archivo, datos):
   with open(archivo, 'w') as f: json.dump(datos, f)

datos = [
    {
        "nombre": "Juan Ruiz",
        "edad": 25,
        "fecha_nacimiento": "1998-05-15",
        "modulos": ["Bases de datos", "Java", "Python"]
    },
    {
        "nombre": "Pepe",
        "edad": 20,
        "fecha_nacimiento": "2004-05-15",
        "modulos": ["Bases de datos", "Java", "Python"]
    }
]


nombre_archivo = '08json\datos.json'

guardar_datos_json(nombre_archivo, datos)


class Persona():
    def __init__(self, nombre, edad, fecha_nacimiento, modulos):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.modulos = modulos

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Fecha de Nacimiento: {self.fecha_nacimiento}")
        print(f"Módulos: {', '.join(self.modulos)}\n")


with open(nombre_archivo, 'r') as archivo:
    datos_cargados = json.load(archivo)  # Cargar datos del archivo JSON

for persona_data in datos_cargados:
    persona = Persona(
        nombre = persona_data["nombre"], 
        edad = persona_data["edad"], 
        fecha_nacimiento = persona_data["fecha_nacimiento"], 
        modulos = persona_data["modulos"]
    )
    persona.mostrar_info()
    


#os.remove(nombre_archivo)
print(f"Archivo '{nombre_archivo}' eliminado.")