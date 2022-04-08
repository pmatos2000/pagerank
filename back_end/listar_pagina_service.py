import json
import numpy as np
import sys
  

sys.path.insert(0,'../pagerank/')
from pagerank import metodo_potencias

dicionario = {}

with open("../dados/dicionario.json", "r", encoding='utf8') as arquivo:
    dicionario = json.load(arquivo)

def obter_paginas(lista_nome_arquivos):
    paginas = {}
    for nome_arquivo in lista_nome_arquivos:
        try:
            with open("../dados/paginas/" + nome_arquivo, "r", encoding='utf8') as arquivo:
                paginas[nome_arquivo] = json.load(arquivo)
        except:
            print("Erro no arquivo: %s" % (nome_arquivo))
    return paginas

def remover_links_quebrado(paginas):
    for nome_arquivo in paginas:
        paginas_existentes = []
        for pagina in paginas[nome_arquivo]["links"]:
            if pagina in paginas:
                paginas_existentes = paginas_existentes + [pagina]
        paginas[nome_arquivo]["links"] = paginas_existentes


def criar_matriz(paginas, alpha = 0.25):
    quantidades = len(paginas)
    lista_nome_arquivo = list(paginas.keys())
    print(lista_nome_arquivo)

    matriz = np.zeros((quantidades, quantidades), dtype=np.float64)
    for i in range(quantidades):
        quantidade_link = 0
        for j in range(quantidades):
            nome_pagina = lista_nome_arquivo[i]
            link = lista_nome_arquivo[j]

            if link in paginas[nome_pagina]["links"]:
                quantidade_link = quantidade_link + 1
                matriz[j][i] = 1

        if quantidade_link > 0:
            for j in range(quantidades):
                if matriz[j][i] == 1:
                    matriz[j][i] = (1-alpha)/quantidade_link


    matriz_amortecimento = np.full((quantidades, quantidades), alpha/quantidades)
    return np.add(matriz, matriz_amortecimento)





def listar_pagina_service(texto_busca):
    if texto_busca in dicionario:
        lista_nome_arquivos = dicionario[texto_busca]
        paginas = obter_paginas(lista_nome_arquivos)
        remover_links_quebrado(paginas)
        # print(paginas)
        matriz = criar_matriz(paginas)
        print(matriz)
        metodo_potencias(matriz)
    return []

listar_pagina_service("marte")