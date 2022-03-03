import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: x**3 - (2*x) - 5

x = np.linspace(-4, 4, 100)

fig, ax = plt.subplots()
ax.plot(x, fx(x), label="x^3 - 2x - 5")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_aspect(0.1)
ax.legend()
ax.grid()
plt.show()