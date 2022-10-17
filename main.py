import numpy as np

#np.dot() Produto escalar entre vetores
#np.sqrt Raiz quadrada

# Variáveis
vetor1 = [1, 2, 3] #Vetor 1
vetor2 = [4, 5, 6] #Vetor 2
vetor3 = [7, 8, 9]

def calcula_distancia_entre_pontos (v1, v2):
    distancia = 0
    for i in range(3):
        distancia += ((v2[i]-v1[i])**2)
    return np.sqrt(distancia)

def calcula_modulo (vetor):
    modulo = 0
    for i in range(3):
        modulo += vetor[i]**2
    return np.sqrt(modulo)

def calcula_vetor_unitario (vetor):
    vetor_unitario = []
    modulo = calcula_modulo(vetor)
    for i in range(3):
        vetor_unitario.append(vetor[i]/modulo)
    return vetor_unitario

def calcula_angulo_entre_vetores (v1, v2):
    v1 = calcula_vetor_unitario(v1)
    v2 = calcula_vetor_unitario(v2)
    return np.degrees(np.arccos(np.dot(v1, v2)))

def calcula_produtos (v1, v2):
    