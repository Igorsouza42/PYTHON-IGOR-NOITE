
import numpy as np

# Criando uma matriz 3x3 com valores de exemplo
matriz = np.array([[12, 5, 7],
                   [9, 14, 11],
                   [6, 8, 15]])

# Selecionando os valores maiores que 10
valores_maiores_que_10 = matriz[matriz > 10]

# Imprimindo os valores maiores que 10
print("Valores maiores que 10:", valores_maiores_que_10)
