def filtrar_personagens_por_genero(personagens, genero):
    return [pers for pers in personagens if pers['gender'].lower() == genero.lower()]

def ordenar_naves(naves, chave):
    return sorted(naves, key=lambda x: int(x.get(chave, 0)) if x.get(chave, 0).isdigit() else 0)

def sugerir_ordem_filmes(filmes, ordem="lancamento"):
    if ordem == "lancamento":
        return sorted(filmes, key=lambda x: x['release_date'])
    elif ordem == "cronologica":
        return sorted(filmes, key=lambda x: x['episode_id'])
    else:
        return filmes
