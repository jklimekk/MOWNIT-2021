import numpy as np
from numpy.linalg import inv

def newton_method(x, y, n):
    F = lambda x, y: np.array([[x*x + y*y - 1], [x*x - y]], dtype='float')
    dF = lambda x, y: np.array([[2*x, 2*y], [2*x, -1]], dtype='float')
    X = np.array([[x], [y]], dtype='float')

    for i in range(0, n):
        a, b = X[0][0], X[1][0]
        X = X - (inv(dF(a, b)) @ (F(a, b)))
        print(i + 1, ": (x, y) = (", X[0][0], ",", X[1][0], ")")

# punkt startowy
startx = 1
starty = 1

newton_method(startx, starty, 10)
