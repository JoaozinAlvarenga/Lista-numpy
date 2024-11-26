# 5. Crie uma matriz 4x4 preenchida com números de 1 a 16. Obtenha a transposta dessa matriz e multiplique a matriz original pela transposta.

import numpy as np

matriz_original = np.arange(1, 17).reshape(4, 4)

matriz_transposta = matriz_original.T

resultado_multiplicacao = np.dot(matriz_original, matriz_transposta)

print("Matriz original:")
print(matriz_original)

print("\nMatriz transposta:")
print(matriz_transposta)

print("\nResultado da multiplicação (matriz original * matriz transposta):")
print(resultado_multiplicacao)

print("\nVerificação das dimensões:")
print(f"Matriz original: {matriz_original.shape}")
print(f"Matriz transposta: {matriz_transposta.shape}")
print(f"Resultado da multiplicação: {resultado_multiplicacao.shape}")
