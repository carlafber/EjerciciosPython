#LIBRERÍAS ESTÁNDAR
import math
from datetime import datetime

numero = 16
raiz = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es: {raiz}")


ahora = datetime.now()
print(f"Fecha y hora actual: {ahora}")



#LIBRERÍAS EXTERNAS
#primero hay que instalarlas -> en cmd con pip
import emoji #códigos emojis -> https://www.webfx.com/tools/emoji-cheat-sheet/

print(emoji.emojize("Hola :smile:. Soy un :T-Rex:. Voy a comer un :croissant:", language='alias'))
print(emoji.emojize("Han llegado los :zombie: y los :troll:. También hay :genie: y :fairy:", language='alias'))


