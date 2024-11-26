# 27.Crie uma matriz 2×2 para representar uma transformação linear e um vetor v=[1,2]. Aplique a transformação ao vetor v multiplicando-o pela matriz.

import numpy as np
import matplotlib.pyplot as plt

matriz = np.array([[2, -1],
                   [1, 3]])

v = np.array([1, 2])

resultado = np.dot(matriz, v)

print(f"Matriz de transformação:\n{matriz}")
print(f"Vetor original: {v}")
print(f"Vetor transformado: {resultado}")

plt.figure(figsize=(8, 6))
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vetor Original')
plt.quiver(0, 0, resultado[0], resultado[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vetor Transformado')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(y=0, color='k', linestyle='--')
plt.axvline(x=0, color='k', linestyle='--')
plt.title('Transformação Linear')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
