import requests

URL_BASE = "https://swapi.dev/api/"

def buscar_dados(endpoint):
    resposta = requests.get(URL_BASE + endpoint)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None

def obter_todos_personagens():
    personagens = []
    pagina = 1
    while True:
        dados = buscar_dados(f"people/?page={pagina}")
        if dados and 'results' in dados:
            personagens.extend(dados['results'])
            if dados['next'] is None:  
                break
            pagina += 1
        else:
            break
    return personagens

def detalhes_personagem(id_personagem):
    return buscar_dados(f"people/{id_personagem}/")

def obter_naves():
    return buscar_dados("starships/")

def obter_filmes():
    return buscar_dados("films/")
