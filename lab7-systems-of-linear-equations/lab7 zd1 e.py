import numpy as np

A = np.array([[0.1, 0.2, 0.3],
              [0.4, 0.5, 0.6],
              [0.7, 0.8, 0.9]])

condA = np.linalg.cond(A)

print("cond(A) = " + "{:.2f}".format(condA))

epsilon = 0.119209 / 1000000

condAeps = condA * epsilon

print("cond(A) * epsilon =", condAeps)

print("cond(A) * epsilon <= 0.5 * 10^(-m)")

m = condAeps * 0.5
m = np.log10(m)
m *= (-1)
m = np.floor(m)

print("m =", m)