import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-2, 2, 50)
Y = np.linspace(-2, 2, 50)

x, y = np.meshgrid(X, Y)

f1 = x ** 2 - 4 * x * y + y ** 2

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, f1, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

########################################

f2 = x ** 4 - 4 * x * y + y ** 4

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, f2, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

########################################

f3 = 2 * (x ** 3) - 3 * (x ** 2) - 6 * x * y * (x - y - 1)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, f3, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

########################################

f4 = (x - y) ** 4 + x ** 2 - y ** 2 - 2 * x + 2 * y + 1

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, f4, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
