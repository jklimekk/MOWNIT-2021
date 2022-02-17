import numpy as np

A = np.array([[0.1, 0.2, 0.3],
              [0.4, 0.5, 0.6],
              [0.7, 0.8, 0.9]])

B = np.array([0.1, 0.3, 0.5])

X = np.linalg.solve(A, B)
X2 = np.linalg.inv(A).dot(B)  # dodatkowa próba

# SPRAWDZENIE 1
print(X)
print(np.allclose(np.dot(A, X), B))

print(X2)
print(np.allclose(np.dot(A, X2), B))

# SPRAWDZENIE 2

x = X[0]
y = 1 - (2 * x)
z = x - (1 / 3)

X3 = B = np.array([x, y, z])

print(X3)
print(np.allclose(X, X3))