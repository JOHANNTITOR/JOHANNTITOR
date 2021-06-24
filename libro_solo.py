#importaciones
import requests

#escribe en pantalla presentación
print ("")
print ("Libro de ordenes CryptoMarket:")
print ("")

#ingreso desde teclado
mercado = input("Elija par de mercado (ejemplo: ETHCLP or XLMCLP):")

#envía petición JSON mediante request.get y concatena variables 'mercado' y 'payload'
payload = {'market': mercado, 'type': 'buy', 'page': 0}
r = requests.get("https://api.cryptomkt.com/v1/book", params=payload)

#imprime en pantalla resultados recuperados en variable 'r'
print (r.json())
input("Presione cualquier tecla para continuar...")
