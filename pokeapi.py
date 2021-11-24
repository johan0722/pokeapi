import requests
import json

url = 'http://pokeapi.co/api/v2/pokemon/'

def buscar(num):
	pedirDatos = requests.get(url +str(num))
	respuesta = json.loads(pedirDatos.content)
	print(respuesta['name'])

buscar(1)