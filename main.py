from swapi_client import obter_todos_personagens, detalhes_personagem, obter_naves, obter_filmes
from utils import filtrar_personagens_por_genero, ordenar_naves, sugerir_ordem_filmes

def listar_personagens():
    print("\nLista de Personagens (Primeiros 10):")
    personagens = obter_todos_personagens()  
    if personagens:
        for i, pers in enumerate(personagens[:10], 1):  
            print(f"{i}. {pers['name']} - Altura: {pers['height']}cm, Peso: {pers['mass']}kg")
    else:
        print("Nenhum personagem encontrado.")

def detalhes_do_personagem(id_personagem):
    detalhes = detalhes_personagem(id_personagem)
    if detalhes:
        print(f"\nDetalhes de {detalhes['name']}:")
        for chave, valor in detalhes.items():
            print(f"{chave.capitalize()}: {valor}")

def filtrar_por_genero():
    genero = input("\nInforme o gênero para filtrar (male/female/unknown): ").lower()  
    personagens = obter_todos_personagens()  
    if personagens:
        filtrados = filtrar_personagens_por_genero(personagens, genero)
        if filtrados:
            print(f"\nPersonagens com gênero '{genero}':")
            for pers in filtrados:
                print(f"{pers['name']} - Gênero: {pers['gender']}")
        else:
            print(f"\nNenhum personagem encontrado com gênero '{genero}'.")
    else:
        print("Não foi possível obter os personagens.")


def listar_naves():
    naves = obter_naves()
    if naves and 'results' in naves:
        chave = input("\nOrdenar naves por (length/crew/passengers): ").lower()
        naves_ordenadas = ordenar_naves(naves['results'], chave)
        for nave in naves_ordenadas:
            print(f"{nave['name']} - {chave.capitalize()}: {nave.get(chave, 'N/A')}")
    else:
        print("Não foi possível obter as naves.")

def recomendar_filmes():
    filmes = obter_filmes()
    if filmes and 'results' in filmes:
        ordem = input("\nEscolha a ordem para assistir (lancamento/cronologica): ").lower()
        filmes_ordenados = sugerir_ordem_filmes(filmes['results'], ordem)
        print("\nOrdem Recomendável para Assistir:")
        for filme in filmes_ordenados:
            print(f"{filme['title']} - Data de Lançamento: {filme['release_date']}")
    else:
        print("Não foi possível obter os filmes.")

if __name__ == "__main__":
    print("Bem-vindo ao Explorador da API de Star Wars!")
    while True:
        print("\nOpções:")
        print("1. Listar Personagens")
        print("2. Detalhes de um Personagem")
        print("3. Filtrar Personagens por Gênero")
        print("4. Listar Naves")
        print("5. Recomendar Ordem de Assistir Filmes")
        print("0. Sair")
        opcao = input("\nEscolha sua opção: ")

        if opcao == "1":
            listar_personagens()
        elif opcao == "2":
            id_pers = input("Digite o ID do Personagem(0 a 10): ")
            detalhes_do_personagem(id_pers)
        elif opcao == "3":
            filtrar_por_genero()
        elif opcao == "4":
            listar_naves()
        elif opcao == "5":
            recomendar_filmes()
        elif opcao == "0":
            print("Até logo, e que a Força esteja com você!")
            break
        else:
            print("Opção inválida. Tente novamente.")
