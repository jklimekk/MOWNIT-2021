import numpy as np

A = np.array([[1, 2, -1],
              [3, 4, 1],
              [2, -2, 3]])

B = np.array([5, 9, -1])


x = np.linalg.solve(A, B)
print("Wynik:", x)

condA = np.linalg.cond(A)
print("cond(A) =", condA)

#############################

D1 = np.array([[1, 0, 0],
               [0, 2/7, 0],
               [0, 0, 1/3]])

x1 = np.linalg.solve(np.dot(D1, A), np.dot(D1, B))
print("\nWynik:", x1)

condD1A = np.linalg.cond(np.dot(D1, A))
print("cond(D1*A) =", condD1A)

#############################

D2 = np.array([[20, 0, 0],
               [0, 40, 0],
               [0, 0, 80]])

x2 = np.linalg.solve(np.dot(D2, A), np.dot(D2, B))
print("\nWynik:", x2)

condD2A = np.linalg.cond(np.dot(D2, A))
print("cond(D2*A) =", condD2A)

#############################

D3 = np.array([[2, 0, 0],
               [0, -4048, 0],
               [0, 0, 1024]])

x3 = np.linalg.solve(np.dot(D3, A), np.dot(D3, B))
print("\nWynik:", x3)

condD3A = np.linalg.cond(np.dot(D3, A))
print("cond(D3*A) =", condD3A)

#############################

D4 = np.array([[0.00002, 0, 0],
               [0, 0.5, 0],
               [0, 0, 0.009]])

x4 = np.linalg.solve(np.dot(D4, A), np.dot(D4, B))
print("\nWynik:", x4)

condD4A = np.linalg.cond(np.dot(D4, A))
print("cond(D4*A) =", condD4A)