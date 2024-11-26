import numpy as np
import pandas as pd

np.random.seed(42)
dados = np.random.rand(50, 3)
df = pd.DataFrame(dados, columns=['A', 'B', 'C'])

print("Estatísticas:")
for coluna in df.columns:
    media = df[coluna].mean()
    desvio_padrao = df[coluna].std()
    valor_maximo = df[coluna].max()
    valor_minimo = df[coluna].min()
    
    print(f"\nColuna {coluna}:")
    print(f"Média: {media:.4f}")
    print(f"Desvio Padrão: {desvio_padrao:.4f}")
    print(f"Valor Máximo: {valor_maximo:.4f}")
    print(f"Valor Mínimo: {valor_minimo:.4f}")

df_normalizado = (df - df.min()) / (df.max() - df.min())

print("\nDados Normalizados (primeiras 5 linhas):")
print(df_normalizado.head())
print("\nVerificação da Normalização:")
print(df_normalizado.min())
print(df_normalizado.max())

