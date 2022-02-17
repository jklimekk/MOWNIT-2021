from numpy.polynomial.polynomial import Polynomial
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


nmax = 10

fx_odwr = Polynomial((1, 0, 25), domain=[-1.,  1.]) # odwrotność funkcji aproksymowanej

Tx = Polynomial((0, 1), domain=[-1.,  1.]) # wielomian R = x potrzebny do mnożenia z wielomianami Czebyszewa

T0 = Polynomial((1), domain=[-1.,  1.])
T1 = Polynomial((0, 1), domain=[-1.,  1.])

print("\n\n ======= WYZNACZONE WIELOMIANY =======\n")
print("\nT( 0 ) =", T0)
print("\nT( 1 ) =", T1)

polynomials = []
polynomials.append(T0)
polynomials.append(T1)

# wyznaczenie wielomianow Czebyszewa
for n in range(2, nmax+1):
    Tn = ((2 * Tx * polynomials[n-1]) - (polynomials[n-2]))
    print("\nT(", n, ") =", Tn)
    polynomials.append(Tn)


c_list = []

for n in range(0, nmax+1):

    # obliczenie calki lewej strony rownania
    L = polynomials[n] * polynomials[n]
    L = L.integ()
    calkaL = L(1) - L(-1)
    #print(calkaL)

    # obliczenie calki prawej strony rownania
    T = polynomials[n]

    T_func = lambda x: T(x) / ((1 + (x**2 * 25)) * (np.sqrt(1 - x**2)))
    calkaR = integrate.quad(T_func, -1, 1)
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
