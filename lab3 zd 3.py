from math import sin
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

start = -4
end = 4

length = end - start

deg = [2, 5, 10]



for n in deg:
    dist = length / n
    i = 0

    result_x = []
    result_y = []

    print("\n\n======================================")
    print("\nstopien = ", n)

    while i <= n:

        x = round(start + (dist * i), 1)
        y = abs(sin(x))

        print(i + 1, ". x =", x, "y =", y)

        result_x.append(x)
        result_y.append(y)

        i += 1

    wynikowy_wielomian = Polynomial([0.])

    for i in range(n + 1):
        pierwiastki = []

        for j in range(n + 1):
            if j != i:
                pierwiastki.append(result_x[j])

        wielomian = Polynomial.fromroots(pierwiastki)

        mianownik = 1

        for j in range(n + 1):
            if j != i:
                mianownik *= (result_x[i] - result_x[j])

        wspolczynnik = result_y[i] / mianownik

        #print("\nwspolczynnik:", wspolczynnik)
        #print("wielomian:", wielomian)

        wielomian = wielomian * wspolczynnik
        wynikowy_wielomian = wynikowy_wielomian + wielomian

    print("\nwynikowy wielomian:")
    print(wynikowy_wielomian)


    x = np.linspace(-4, 4, 100)
    y = wynikowy_wielomian(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, label="w(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    plt.show()
