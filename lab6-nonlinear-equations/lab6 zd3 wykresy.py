import numpy as np
import matplotlib.pyplot as plt

xlin = np.linspace(-2, 2, 100)
ylin = np.linspace(-2, 2, 100)

x, y = np.meshgrid(xlin, ylin)

f1 = x ** 2 + y ** 2 - 1
f2 = x ** 2 - y

figure, axes = plt.subplots()

axes.contour(x, y, f1, [0], )
axes.contour(x, y, f2, [0])
axes.set_aspect(1)
axes.grid()

plt.show()
