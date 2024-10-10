""" 
Servicio web
Un servicio web es un sistema que permite la comunicación entre diferentes aplicaciones a través de la red.
Generalmente, se basa en estándares abiertos y protocolos como HTTP para enviar y recibir datos.
"""

""" 
RESTful API
Una API RESTful es un tipo de interfaz que utiliza el protocolo HTTP para permitir la comunicación entre un cliente y un servidor.
Se basa en los principios de la arquitectura REST, que incluye la utilización de recursos, métodos HTTP y un formato de datos común, como JSON.
"""

""" 
Protocolo HTTP
El Protocolo de Transferencia de Hipertexto (HTTP) es un protocolo de comunicación que se utiliza para la transmisión de información en la web.
Define cómo se envían y reciben los mensajes entre un cliente (como un navegador) y un servidor.
"""

""" 
Peticiones HTTP
Las peticiones HTTP son mensajes enviados por el cliente al servidor para solicitar información o realizar alguna acción.
Los métodos más comunes son GET (obtener información) y POST (enviar información).
"""

""" 
Respuestas HTTP
Las respuestas HTTP son los mensajes que envía el servidor en respuesta a una petición del cliente.
Los códigos de estado más comunes son:
    - 200: Éxito (la petición fue exitosa y se devolvió la información solicitada).
    - 404: No encontrado (el recurso solicitado no existe en el servidor).
    - 500: Error interno del servidor (ocurrió un error en el servidor al procesar la petición).
"""

# La librería de Python para realizar peticiones HTTP:
import requests

# Realizamos una petición GET para obtener el contenido de una página web
url = "https://www.google.com"  # Reemplaza con la URL de la página que desees consultar
response = requests.get(url)  # Enviamos la petición GET

# Verificamos si la petición fue exitosa (código de estado 200)
if response.status_code == 200:
    print("La petición fue exitosa. Contenido de la página:")
    print(response.text)  # Mostramos el contenido de la respuesta
else:
    # Si la petición no tuvo éxito, imprimimos el código de error
    print(f"La petición falló con el código de error: {response.status_code}")
