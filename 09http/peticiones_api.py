"""
API de POKEMON es abierta; no hace falta validarse para obtener información de ella. Tiene documentación
Para acceder a la API, se usan peticiones HTTP
Existen librerías ya escritas
Endpoint en una API: URL que puede dar una respuesta
"""
import requests

pokemon = input("Dime el nombre o número del POKEMON a buscar: ").lower()

# La ayuda de la página nos da este ENDPOINT: https://pokeapi.co/api/v2/pokemon/{id or name}/

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")

if response.status_code == 200:
    #print(response.text)
    data = response.json() # convierte el json en un diccionario
    print("Nombre: ", data["name"])
    print("ID: ", data["id"])
    print("Peso: ", data["weight"])
    print("Altura: ", data["height"])
    print("Tipo(s): ")
    for type in data["types"]: # types es una lista
        print(type["type"]["name"])

else:
    print(f"Error: {response.status_code}; el pokemon {pokemon} no se ha encontrado")


