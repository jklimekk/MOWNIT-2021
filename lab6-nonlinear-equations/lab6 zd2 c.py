import numpy as np

def newton_method(x, i):
    # badana funkcja
    fx = lambda x: x - ((x * np.sin(x) - 1) / (x * np.cos(x) + np.sin(x)))

    for i in range(0, i):
        x = fx(x)
        print(i + 1, ": x =", x)

# punkt startowy
startx = 1
#startx = 3

# iteracje
iter = 10

newton_method(startx, iter)