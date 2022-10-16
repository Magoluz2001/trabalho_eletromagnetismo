import numpy as np

# Variáveis
vetor1 = [4, 4, 4] #Vetor 1
vetor2 = [2, 2, 2] #Vetor 2

def distancia_entre_vetores (v1, v2):
    distancia = 0
    for i in range(3):
        distancia += ((v2[i]-v1[i])**2)
    return np.sqrt(distancia)

print(distancia_entre_vetores(vetor1, vetor2))


