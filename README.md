# Explorador da API de Star Wars

Este é um projeto Python que explora a [Star Wars API (SWAPI)](https://swapi.dev/), permitindo acessar informações sobre personagens, naves espaciais e filmes do universo Star Wars. O programa interativo fornece diversas opções para navegar e filtrar os dados.

---

## Funcionalidades

- **Listar personagens**: Exibe os primeiros 10 personagens disponíveis na API, junto com informações básicas como altura e peso.
- **Detalhes de um personagem**: Permite consultar informações detalhadas de um personagem específico pelo seu ID.
- **Filtrar personagens por gênero**: Filtra personagens com base no gênero (male/female/unknown).
- **Listar naves**: Exibe informações sobre naves espaciais, com opção de ordenação por tamanho, número de tripulantes ou passageiros.
- **Recomendar ordem para assistir aos filmes**: Sugere uma ordem cronológica ou de lançamento para assistir aos filmes de Star Wars.

---

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

1. **`main.py`**: Arquivo principal do programa. Fornece o menu interativo para o usuário e gerencia a interação com o sistema.
2. **`swapi_client.py`**: Contém funções para realizar requisições à SWAPI, como buscar dados, obter personagens, naves e filmes.
3. **`utils.py`**: Inclui funções auxiliares para manipular e ordenar os dados, como filtrar personagens por gênero, ordenar naves e sugerir a ordem dos filmes.

---

## Requisitos

Certifique-se de que você tem o seguinte instalado em sua máquina:
- **Python 3.7 ou superior**
- Biblioteca `requests` para realizar as requisições HTTP.

### Instalando as dependências
Você pode instalar a biblioteca `requests` usando o `pip`:
**pip install requests**


## Como usar

-Clone ou baixe este repositório em sua máquina.
-Certifique-se de que os arquivos utils.py, swapi_client.py e main.py  estão no mesmo diretório do programa principal.
-Execute o programa principal:
   **python main.py**
-Siga o menu interativo para escolher as opções desejadas.




