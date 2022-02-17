import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
h = 0.5

y1 = np.sin(x)
y2 = np.sin(x + h)
y3 = np.sin(x) - np.sin(x + h)
y4 = (np.sin(x) - np.sin(x + h)) / np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y1, label="sin(x)")
ax.plot(x, y2, label="sin(x + h)")
ax.plot(x, y3, label="sin(x) - sin(x + h)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.show()

fig, bx = plt.subplots()
bx.plot(x, y3, label="sin(x) - sin(x + h)")
bx.plot(x, y4, label="(sin(x) - sin(x + h)) / sin(x)")
bx.set_xlabel("x")
bx.set_ylabel("y")
bx.legend()
plt.show()

# x = np.linspace(-10, 10, 100)
#
# y3 = x / np.tan(x)
#
# fig, ax = plt.subplots()
# ax.plot(x, y3, label="ctg(x)")
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.legend()
# plt.show()
