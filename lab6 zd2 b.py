import numpy as np

def newton_method(x, i):
    # badana funkcja
    fx = lambda x: x - ((np.exp(-x) - x) / (- np.exp(-x) - 1))

    for i in range(0, i):
        x = fx(x)
        print(i + 1, ": x =", x)

# punkt startowy
startx = 1

# iteracje
iter = 10

newton_method(startx, iter)