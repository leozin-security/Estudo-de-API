import requests
import json

URL_ALL = "https://restcountries.com/v3.1/all?fields=name,capital,currencies"
resposta = requests.get(URL_ALL)

#Pasing = É um termo tecnico para pegar uma string legivel para converter e transformar os dados que o computador possa enteder


print(resposta)
print()
print(type(resposta))
print(resposta.status_code)
##print(resposta.text)

paises = json.loads(resposta.text)# <---- Parsing de JSON PARA PYTHON

print(type(paises[0]["name"]))
print(paises[0]["name"])

print(len(paises))
for pais in paises:
    print(pais)
    print(pais["name"])