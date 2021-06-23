#importacones
import requests

#definir variables
mercado = "xlmclp" # indicar mercado a consultar cadena de texto con nombres de cryptos definido por usuario

#cargar ticker desde API_REST
        
payload = {'market': mercado}        
r = requests.get("https://api.cryptomkt.com/v1/ticker", params=payload) #URL de consulta de ticker

#usa ticker_data para almacenas ticker desde json
ticker_data = (r.json())
               
#obtener valores desde JSON y los pone en cadenas distintas
data = (ticker_data['data'])
data_sin_corchetes = (data[0])

timestamp = (data_sin_corchetes['timestamp'])

bid = (data_sin_corchetes['bid'])
ask = (data_sin_corchetes['ask'])

#imprime valores obtenidos desde json TICKER
print ("")
print ("registro de tiempo: " + timestamp + " precio bid: " + bid + " precio ask: " + ask) 
print ("")
input("ha mostrado el ticker correctamente")

