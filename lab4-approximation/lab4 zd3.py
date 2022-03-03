from numpy.polynomial.polynomial import Polynomial
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


nmax = 10

fx_odwr = Polynomial((1, 0, 25), domain=[-1.,  1.]) # odwrotność funkcji aproksymowanej

Px = Polynomial((0, 1), domain=[-1.,  1.]) # wielomian R = x potrzebny do mnożenia z wielomianami Legendre’a

P0 = Polynomial((1), domain=[-1.,  1.])
P1 = Polynomial((0, 1), domain=[-1.,  1.])

print("\n\n ======= WYZNACZONE WIELOMIANY =======\n")
print("\nP( 0 ) =", P0)
print("\nP( 1 ) =", P1)

polynomials = []
polynomials.append(P0)
polynomials.append(P1)

# wyznaczenie wielomianow Legendre’a
for n in range(2, nmax+1):
    Pn = (((2 * n - 1) * Px * polynomials[n-1]) - ((n - 1) * polynomials[n-2])) / n
    print("\nP(", n, ") =", Pn)
    polynomials.append(Pn)


c_list = []

for n in range(0, nmax+1):

    # obliczenie calki lewej strony rownania
    L = polynomials[n] * polynomials[n]
    L = L.integ()
    calkaL = L(1) - L(-1)
    #print(calkaL)

    # obliczenie calki prawej strony rownania
    P = polynomials[n]
    P_func = lambda x: P(x) / (1 + (x**2 * 25))
    calkaR = integrate.quad(P_func, -1, 1)
    #print(calkaR)

    c_list.append(calkaR[0] / calkaL)

print("\n\n ======= WYZNACZONE Cn =======\n")
for i in range(len(c_list)):
    print("\nc" + str(i) + " =", c_list[i])

result = Polynomial(0)

for n in range(0, nmax+1):
    result = result + (polynomials[n] * c_list[n])

#print(result)

x = np.linspace(-1, 1, 100)

fig, ax = plt.subplots()
ax.plot(x, result(x), label="result")
ax.plot(x, 1/fx_odwr(x), label="function")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.show()
