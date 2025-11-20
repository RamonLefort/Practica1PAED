import matplotlib.pyplot as plt
import numpy as np

# Valores de n
n_values = np.logspace(1, 6, num=100, base=10, dtype=int)

# Calculamos n log n y n^2
nlogn = n_values * np.log2(n_values)
n2 = n_values**2

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(n_values, nlogn, label=r"$O(n \log n)$")
plt.plot(n_values, n2, label=r"$O(n^2)$")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Número de operaciones")
plt.title("Crecimiento de $O(n \log n)$ vs $O(n^2)$")
plt.legend()
plt.grid(True)
plt.show()
