import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [1, 2, 0, 2, 1]

x_novo = np.arange(0, 4.1, 0.1)
y_novo = np.interp(x_novo, x, y)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'ro-', label='Dados originais')
plt.plot(x_novo, y_novo, 'b-', label='Dados interpolados')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Dados Originais vs Interpolados')
plt.legend()
plt.grid(True)

plt.show()

print("Primeiros 10 pares (x, y) interpolados:")
for i in range(10):
    print(f"({x_novo[i]:.1f}, {y_novo[i]:.2f})")