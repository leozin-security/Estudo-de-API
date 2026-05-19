import requests
import json


URL_ALL = "https://restcountries.com/v3.1/all?fields=name,capital,currencies"

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
        else:
            print(f"Erro na requisição. Código de status: {resposta.status_code}")
    except Exception as e:
        print("Erro ao fazer requisição em: ", url)
        print("Detalhe do erro:", e)

def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)
    except Exception as e:
        print("Erro ao fazer parsing:", e)

def contagem_de_paises(todos_os_paises):
    return len(todos_os_paises)

def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais["name"]["common"])

def mostrar_populacao(nome_do_pais):
    url_busca = f"https://restcountries.com/v3.1/name/{nome_do_pais}"
    texto_da_resposta = requisicao(url_busca)
    
    if texto_da_resposta:
        paises_encontrados = parsing(texto_da_resposta)
        
        if paises_encontrados:
            for pais in paises_encontrados:
                nome = pais["name"]["common"]
                populacao = pais.get("population", "Desconhecida") 
                print(f"{nome} tem {populacao} habitantes.")
        else:
            print("País não encontrado ou erro no JSON.")


if __name__ == "__main__":
    texto_da_resposta = requisicao(URL_ALL)
    
    if texto_da_resposta:
        texto_depois_do_parsing = parsing(texto_da_resposta)
        
        if texto_depois_do_parsing:
            total = contagem_de_paises(texto_depois_do_parsing)
            print(f"Total de países encontrados: {total}")
            
            

    print("\n--- Buscando país específico ---")
    mostrar_populacao("brazil")