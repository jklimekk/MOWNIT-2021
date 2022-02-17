import numpy as np
import matplotlib.pyplot as plt
import math

# całkowana funkcja
fx = lambda x: 2 / (x**2 + 1)

# przedzial
a = -1
b = 1
length = b - a

# liczby podzialow
ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def metoda_prostokatow(n):
    h = length / n
    x = np.linspace(a - (h/2), b - (h/2), num=n+1, endpoint=True)
    #print(x[1::])
    calka = sum(map(lambda x: fx(x) * length / n, x[1::]))
    return calka

def metoda_trapezow(n):
    h = length / n
    x = np.linspace(a, b, num=n+1, endpoint=True)
    #print(x)
    calka = sum(map(lambda x: (fx(x) + fx(x - h)) * h / 2, x[1::]))
    return calka

def metoda_simpsona(n):
    h = length / n
    x = np.linspace(a, b, num=n+1, endpoint=True)
    #print(x)
    calka = sum(map(lambda x: (fx(x) + 4 * fx(x - (h/2)) + fx(x-h)) * h / 6, x[1::]))
    return calka


x = np.linspace(min(ns), max(ns), len(ns))

fpi = [math.pi] * (len(ns))

fprostokatow = []
for n in ns:
    fprostokatow.append(metoda_prostokatow(n))

ftrapezow = []
for n in ns:
    ftrapezow.append(metoda_trapezow(n))

fsimpsona = []
for n in ns:
    fsimpsona.append(metoda_simpsona(n))


# porownanie wszystkich wykresow
fig, ax = plt.subplots()
ax.plot(x, fpi, label="prawdziwa wartosc", marker='o')
ax.plot(x, fprostokatow, label="metoda prostokatow", marker='o')
ax.plot(x, ftrapezow, label="metoda trapezow", marker='o')
ax.plot(x, fsimpsona, label="metoda simpsona", marker='o')
ax.set_xlabel("n")
ax.set_ylabel("obliczona wartosc calki")
ax.legend()
plt.show()


# porownanie metody prostokatow
print("\n====== METODA PROSTOKATOW ======\n")

blad_prostokaty = []
for i in range(len(ns)):
    blad_prostokaty.append(abs(fprostokatow[i] - fpi[i])/fpi[i])
    print("n =", ns[i], " blad =", round(blad_prostokaty[i], 10))

fig, ax = plt.subplots()
ax.plot(x, fpi, label="prawdziwa wartosc", marker='o')
ax.plot(x, fprostokatow, label="metoda prostokatow", marker='o')
ax.set_xlabel("n")
ax.set_ylabel("obliczona wartosc calki")
ax.legend()
plt.show()

fig, ax = plt.subplots()
ax.plot(x, blad_prostokaty, label="blad wzgledny", marker='o')
ax.set_xlabel("n")
ax.set_ylabel("blad wzgledny")
ax.legend()
plt.show()


# porownanie metody trapezow
print("\n====== METODA TRAPEZOW ======\n")

blad_trapezy = []
for i in range(len(ns)):
    blad_trapezy.append(abs(ftrapezow[i] - fpi[i])/fpi[i])
    print("n =", ns[i], " blad =", round(blad_trapezy[i], 10))

fig, ax = plt.subplots()
ax.plot(x, fpi, label="prawdziwa wartosc", marker='o')
ax.plot(x, ftrapezow, label="metoda trapezow", marker='o')
ax.set_xlabel("n")
ax.set_ylabel("obliczona wartosc calki")
ax.legend()
plt.show()

fig, ax = plt.subplots()
ax.plot(x, blad_trapezy, label="blad wzgledny", marker='o')
ax.set_xlabel("n")
ax.set_ylabel("blad wzgledny")
ax.legend()
plt.show()


# porownanie metody simpsona
print("\n====== METODA SIMPSONA ======\n")

blad_simpson = []
for i in range(len(ns)):
    blad_simpson.append(abs(fsimpsona[i] - fpi[i])/fpi[i])
    print("n =", ns[i], " blad =", round(blad_trapezy[i], 10))

fig, ax = plt.subplots()
ax.plot(x, fpi, label="prawdziwa wartosc", marker='o')
ax.plot(x, fsimpsona, label="metoda simpsona", marker='o')
ax.set_xlabel("n")
ax.set_ylabel("obliczona wartosc calki")
ax.legend()
plt.show()

fig, ax = plt.subplots()
ax.plot(x, blad_simpson, label="blad wzgledny", marker='o')
ax.set_xlabel("n")
ax.set_ylabel("blad wzgledny")
ax.legend()
plt.show()