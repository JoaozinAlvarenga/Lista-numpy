# 1. Crie um array NumPy contendo os números de 1 a 10. Em seguida, transforme-o em um array bidimensional com 2 linhas e 5 colunas.

import numpy as np

array_1d = np.arange(1, 11)
array_2d = array_1d.reshape(2, 5)

print("Array 1D original:")
print(array_1d)

print("\nArray 2D transformado:")
print(array_2d)
