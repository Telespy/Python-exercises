from requests import get,exceptions
import json


def info_movie(nome_filme, apikey):
    """
    Busca informações sobre o título de filme requisitado.
    """
    url = f"https://omdbapi.com/?t={nome_filme.lower().replace(" ","%20")}&apikey={apikey}"

    print(f"Buscando dados da URL > {url}\n")

    try:
        # 1. FAZENDO A REQUISIÇÃO PARA A API
        resposta = get(url)
        resposta.raise_for_status()  # Isso vai gerar um erro se a requisição falhar (ex: erro 404, 500)

        # 2. EXTRAINDO O JSON DA RESPOSTA
        # O método .json() já converte a resposta em um dicionário Python
        dados = resposta.json()

        # 3. Extraindo os dados para fora da função
        if dados.get("Response")=="True":
            return dados
        else:
            print("Esse filme não existe no banco de dados.")
            return None
    # verifica se houve algum problema ao requisitar o link
    except exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição HTTP: {e}")
        print("\nHouve um provável erro em sua API key, tente outra.")
        return None
    except json.JSONDecodeError:
        print("Erro ao decodificar a resposta JSON.")
        return None


# --- EXECUÇÃO PRINCIPAL DO SCRIPT ---
if __name__ == "__main__":
    print("If you don't have a API to request movies/series, go to this website > https://www.omdbapi.com/\n")
    apikey = input("Write you key API of OMDb API: ")
    nome_filme=input("Write the name of the movie/serie: ")

    # Pegando o json com suas informações
    movie = info_movie(nome_filme, apikey)

    if movie:
        # 4. UTILIZANDO AS INFORMAÇÕES EXTRAÍDAS DO JSON
        genero = movie.get("Genre")
        ano = movie.get("Year")
        tempo = movie.get("Runtime")

        if movie.get("Type")=="movie":
            print(f"--- Informações sobre o filme {nome_filme} ---")
        elif movie.get("Type")=="series":
            print(f"--- Informações sobre a série {nome_filme} ---")
        if genero:
            if movie.get("Type") == "movie":
                print(f"Gênero do filme > {genero}")
            elif movie.get("Type") == "series":
                print(f"Gênero da série > {genero}")

        if ano:
            print(f"Ano de lançamento > {ano}")
        if tempo:
            print(f"Tempo de duração > {tempo}")
