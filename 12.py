# 12.Use numpy.linspace para criar um array com 50 valores igualmente espaçados entre 0 e 10. Use numpy.arange para criar um array com valores de 0 a 10, incrementando de 0.2.

import numpy as np

array_linspace = np.linspace(0, 10, 50)
array_arange = np.arange(0, 10.2, 0.2)

print("Array criado com numpy.linspace (50 valores entre 0 e 10):")
print(array_linspace)
print(f"\nTamanho do array: {len(array_linspace)}")

print("\nArray criado com numpy.arange (0 a 10, incremento de 0.2):")
print(array_arange)
print(f"\nTamanho do array: {len(array_arange)}")

print("\nComparação dos primeiros 5 elementos de cada array:")
print("linspace:", array_linspace[:5])
print("arange:", array_arange[:5])

print("\nComparação dos últimos 5 elementos de cada array:")
print("linspace:", array_linspace[-5:])
print("arange:", array_arange[-5:])
