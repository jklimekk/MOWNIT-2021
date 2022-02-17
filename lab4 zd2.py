from numpy.polynomial.polynomial import Polynomial
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


nmax = 10

fx_odwr = Polynomial((1, 0, 25), domain=[-1.,  1.]) # odwrotność funkcji aproksymowanej

Wx = Polynomial((0, 1), domain=[-1.,  1.]) # wielomian R = x potrzebny do mnożenia z wielomianami

W0 = Polynomial((1), domain=[-1.,  1.])
W1 = Polynomial((0, 1), domain=[-1.,  1.])

print("\n\n ======= WYZNACZONE WIELOMIANY =======\n")
print("\nW( 0 ) =", W0)
print("\nW( 1 ) =", W1)

polynomials = []
polynomials.append(W0)
polynomials.append(W1)

# wyznaczenie wielomianow
for n in range(2, nmax+1):
    Wn = polynomials[n-1] * Wx
    print("\nW(", n, ") =", Wn)
    polynomials.append(Wn)

"""
calki_lewastrona = [None] * (nmax+1)
for i in range(len(calki_lewastrona)):
    calki_lewastrona[i] = [None] * (nmax+1)

for i in range(0, nmax+1):
    for j in range(0, nmax + 1):
        if i <= j:
            P = polynomials[i]
            R = polynomials[j]
            P_func = lambda x: P(x) * R(x)
            calka = integrate.quad(P_func, -1, 1)
            # print(calka)
            calki_lewastrona[i][j] = calka[0]
"""

# macierz hilberta
calki_lewastrona = [None] * (nmax+1)
for i in range(len(calki_lewastrona)):
    calki_lewastrona[i] = [None] * (nmax+1)

for i in range(0, nmax+1):
    for j in range(0, nmax + 1):
        calki_lewastrona[i][j] = 1 / (i+1 + j+1 - 1)
#print(calki_lewastrona)

calki_prawastrona = [None] * (nmax+1)
for i in range(len(calki_prawastrona)):
    P = polynomials[i]
    P_func = lambda x: P(x) / (1 + (x**2 * 25))
    calki_prawastrona[i] = integrate.quad(P_func, -1, 1)[0]

a = np.array(calki_lewastrona)
b = np.array(calki_prawastrona)
c_list = np.linalg.solve(a, b)

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