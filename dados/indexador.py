import wikipediaapi
import json
import os
from unidecode import unidecode
import re

"""
wiki_wiki = wikipediaapi.Wikipedia('pt')
print("Pagina existe: %s" % pagina_inicial.exists())
"""

"""
def print_links(page):
        links = page.links
        for titulo in links.keys():
            print("%s: %s" % (titulo, links[titulo]))
print_links(pagina_inicial)
"""

def indexar_pagina(quantidade_pagina = 10000):
    wiki_wiki = wikipediaapi.Wikipedia('pt')
    paginas_encontrada = ['PageRank', 'Ficção', 'Natureza', 'Reta', 'Marte']
    paginas_visitadas = []
    paginas_error = []

    def gravar_pagina(pagina):
        links = list(pagina.links.keys())
        links = list(map(lambda p: p + ".json", links))
        dados = {
            "id": pagina.pageid,
            "titulo": pagina.title,
            "texto": pagina.text,
            "links": links,
            "url": pagina.fullurl,
        }
        
        json_objeto = json.dumps(dados, indent = 4, ensure_ascii=False)

        with open("./paginas/" + pagina.title + ".json", "w", encoding='utf8') as arquivo: 
            arquivo.write(json_objeto) 

    quantidade_paginas_salvas = 0

    while len(paginas_encontrada) > 0 and quantidade_paginas_salvas < quantidade_pagina:
        print(quantidade_paginas_salvas)
        titulo_pagina = paginas_encontrada.pop(0)

        def filtro(link, titulo_pagina=titulo_pagina, paginas_encontrada=paginas_encontrada, paginas_visitadas=paginas_visitadas, paginas_error=paginas_error):
            return not(link == titulo_pagina or link in paginas_encontrada or link in paginas_visitadas or link in paginas_error)

        try:
            pagina = wiki_wiki.page(titulo_pagina)
            
            gravar_pagina(pagina)
            quantidade_paginas_salvas = quantidade_paginas_salvas + 1

            lista_titulo_links = list(filter(filtro, pagina.links.keys()))
            paginas_encontrada = paginas_encontrada + lista_titulo_links
            paginas_visitadas = paginas_visitadas + [titulo_pagina]
            
        except:
            print("Erro pagina: %s" % (titulo_pagina))
            paginas_error = paginas_error + [paginas_error]


def formatar_palavra(palavra):
    palavra = palavra.lower()
    palavra = unidecode(palavra)
    palavra = re.sub(u'[^a-zA-Z0-9\-_]', '', palavra)
    return palavra

def obter_lista_palavras(nome_arquivo):
    with open("./paginas/" + nome_arquivo, "r", encoding='utf8') as arquivo:
        dados = json.load(arquivo)
        texto = dados["texto"]
        lista_palavra = texto.split()
        lista_palavra = list(filter(lambda p: len(p) > 4, lista_palavra))
        lista_palavra = list(map(formatar_palavra, lista_palavra))
        lista_palavra =  list(set(lista_palavra))
        return lista_palavra

def preencher_dicionario(dicionario, lista_palavra, nome_arquivo):
    for palavra in lista_palavra:
        if palavra in dicionario:
            dicionario[palavra] = dicionario[palavra] + [nome_arquivo]
        else:
            dicionario[palavra] = [nome_arquivo]


def criar_dicionario():
    dicionario = {}
    lista_nome_arquivo = os.listdir("./paginas")
    for nome_arquivo in lista_nome_arquivo:
        try:
            lista_palavra = obter_lista_palavras(nome_arquivo)
            preencher_dicionario(dicionario, lista_palavra, nome_arquivo)
        except:
            print("Erro no arquivo: %s" % (nome_arquivo))
    
    json_objeto = json.dumps(dicionario, indent = 4, ensure_ascii=False)
    with open("dicionario.json", "w", encoding='utf8') as arquivo: 
            arquivo.write(json_objeto)
            


#indexar_pagina()
criar_dicionario()