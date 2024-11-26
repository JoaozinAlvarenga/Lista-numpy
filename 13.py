import numpy as np

np.random.seed(42)

array1 = np.random.randint(1, 10, 5)
array2 = np.random.randint(1, 10, 5)

resultado = np.square(array1) - array2

print("Array 1:", array1)
print("Array 2:", array2)
print("Resultado da operação (array1^2 - array2):", resultado)
