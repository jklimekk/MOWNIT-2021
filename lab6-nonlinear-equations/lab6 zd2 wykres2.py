import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: np.exp(-x) - x

x = np.linspace(-4, 4, 100)

fig, ax = plt.subplots()
ax.plot(x, fx(x), label="e^x - x")
ax.set_xlabel("x")
ax.set_ylabel("y")
#ax.set_aspect(0.1)
ax.legend()
ax.grid()
plt.show()