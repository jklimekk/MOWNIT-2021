import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: x * np.sin(x) - 1

x = np.linspace(-5, 20, 100)

fig, ax = plt.subplots()
ax.plot(x, fx(x), label="xsin(x) - 1")
ax.set_xlabel("x")
ax.set_ylabel("y")
#ax.set_aspect(0.1)
ax.legend()
ax.grid()
plt.show()


x = np.linspace(-3, 5, 100)

fig, ax = plt.subplots()
ax.plot(x, fx(x), label="xsin(x) - 1")
ax.set_xlabel("x")
ax.set_ylabel("y")
#ax.set_aspect(0.1)
ax.legend()
ax.grid()
plt.show()