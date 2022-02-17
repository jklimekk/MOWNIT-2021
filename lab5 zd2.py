import numpy as np
import math
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt

# całkowana funkcja
fx = lambda x: 2 / (x**2 + 1)

# przedzial
a = -1
b = 1
length = b - a

# liczby podzialow
ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#nss = 10

# wyznaczenie wielomianow Legendre’a
def Legendre_polymonials(n):

    Px = Polynomial((0, 1)) # wielomian R = x potrzebny do mnożenia z wielomianami Legendre’a

    P0 = Polynomial((1))
    P1 = Polynomial((0, 1))

    polynomials = []
    polynomials.append(P0)
    polynomials.append(P1)

    for n in range(2, n+1):
        Pn = (((2 * n - 1) * Px * polynomials[n-1]) - ((n - 1) * polynomials[n-2])) / n
        polynomials.append(Pn)

    return polynomials

fgaussa = []

for n in ns:
    polymonials = Legendre_polymonials(n)
    xs = polymonials[n].roots()
    #print(xs)

    A = []

    for i in range(n):
        a = []
        Pi = polymonials[i]
        for j in range(n):
            x = xs[j]
            a.append(Pi(x))
        A.append(a)

    A = np.array(A)

    B = np.zeros(n)
    B[0] = 2

    cs = np.linalg.solve(A, B)
    #print(cs)

    result = 0
    for i in range(n):
        result += cs[i] * fx(xs[i])

    #print(result)
    fgaussa.append(result)


x = np.linspace(min(ns), max(ns), len(ns))

fpi = [math.pi] * (len(ns))

# porownanie wynikow
fig, ax = plt.subplots()
ax.plot(x, fpi, label="prawdziwa wartosc", marker='o')
ax.plot(x, fgaussa, label="metoda gaussa", marker='o')
ax.set_xlabel("n")
ax.set_ylabel("obliczona wartosc calki")
ax.legend()
plt.show()

# porownananie bledow
blad_gauss = []
for i in range(len(ns)):
    blad_gauss.append(abs(fgaussa[i] - fpi[i])/fpi[i])
    print("n =", ns[i], " blad =", round(blad_gauss[i], 10))

fig, ax = plt.subplots()
ax.plot(x, blad_gauss, label="blad wzgledny", marker='o')
ax.set_xlabel("n")
ax.set_ylabel("blad wzgledny")
ax.legend()
plt.show()