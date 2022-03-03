import numpy as np

def newton_method(x, i):
    # badana funkcja
    fx = lambda x: (2 * x * x * x + 5) / (3 * x * x - 2)

    for i in range(0, i):
        x = fx(x)
        print(i + 1, ": x =", x)

# punkt startowy
startx = 1

# iteracje
iter = 10

newton_method(startx, iter)