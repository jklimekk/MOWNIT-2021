import numpy as np

a = float(1)
b = np.float16(1)
c = np.float32(1)
d = np.float64(1)
e = np.longdouble(1)
f = np.double(1)
g = np.longfloat(1)

values = [a, b, c, d, e, f, g]

for elem in values:
    x = elem
    print('\nEpsilon maszynowy dla', type(x), ':')
    print(x)

    while (x + 1.0 > 1.0):
        x /= 2.0

    print(x * 2.0)
