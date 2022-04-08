import numpy as np
from numpy import linalg as LA

def obter_vetor_inicial(n):
    vetor = np.zeros(n)
    vetor[0] = 1
    return vetor


def metodo_potencias(matriz = [], erro = 1e-5, interacao_maxima = 1000):
    (n, m) = matriz.shape
    vetor = obter_vetor_inicial(n)
    for i in range(interacao_maxima):
        print("%i %s" % (i, vetor))
        vetor_seguinte = np.matmul(matriz, vetor)
        vetor_seguinte = vetor_seguinte/LA.norm(vetor_seguinte, 1)
        vetor_dif = np.subtract(vetor_seguinte, vetor)

        if LA.norm(vetor_dif) < erro:
            return vetor_seguinte

        vetor = vetor_seguinte
    return vetor

def exemplo():
    matriz = np.array([[0.3,0.6],[0.7, 0.4]])
    metodo_potencias(matriz)

exemplo()

