import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from timeit import default_timer as timer

# wymiary macierzy (N)
sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
index = -1

# tablica do zapisywania czasów
# times[nr_metody][rozmiar_N][nr_pomiaru]
times = [[[None for k in range(10)] for j in range(len(sizes))] for i in range(3)]

for size in sizes:
    n = size
    index += 1

    A = np.random.rand(n, n)   # macierz A
    u = np.random.rand(n, 1)   # wektor u
    v = np.random.rand(n, 1)   # wektor v

    inversed_A = np.linalg.inv(A)   # A^(-1)
    transposed_v = v.transpose()    # v^T

    rank_one_update_A = A + (u @ transposed_v)  # A + uv^T

    # METODA PIERWSZA
    method = 0

    for i in range(10):
        start = timer()
        inverse_A_1 = np.linalg.inv(rank_one_update_A)
        end = timer()

        times[method][index][i] = (end - start)


    # METODA DRUGA
    method = 1

    for i in range(10):
        start = timer()
        numerator = (((inversed_A @ u) @ transposed_v) @ inversed_A)
        denominator = 1 + (transposed_v @ inversed_A @ u)
        inverse_A_2 = inversed_A - (numerator / denominator)
        end = timer()

        times[method][index][i] = (end - start)


    # METODA TRZECIA
    method = 2

    for i in range(10):
        start = timer()
        numerator = ((inversed_A @ (u @ transposed_v)) @ inversed_A)
        denominator = 1 + (transposed_v @ inversed_A @ u)
        inverse_A_3 = inversed_A - (numerator / denominator)
        end = timer()

        times[method][index][i] = (end - start)

#--------------- PANDAS -----------------

rozmiary = []
for i in range(len(sizes)):
    rozmiary += ([sizes[i]] * 10)

for i in range(3):
    print("Metoda", i+1)

    czasy = []
    for j in range(len(sizes)):
        czasy += times[i][j]

    dict = {'Rozmiar': rozmiary, 'Czasy': czasy}

    dataFrame = pd.DataFrame(dict)
    print(dataFrame)

    print("\nSrednie czasy:")
    print(dataFrame.groupby('Rozmiar')['Czasy'].mean())

    print("\nOdchylenia standardowe:")
    print(dataFrame.groupby('Rozmiar')['Czasy'].std())
    print("\n\n")

    #dataFrame.groupby('Rozmiar')['Czasy'].mean().plot()
    plt.errorbar(sizes, dataFrame.groupby('Rozmiar')['Czasy'].mean(), yerr = dataFrame.groupby('Rozmiar')['Czasy'].std(), fmt = '-o')
    plt.xlabel("N", fontsize = 16)
    plt.ylabel("Mean time", fontsize = 16)
    plt.title("Method " + str(i+1), fontsize = 20)
    plt.show()