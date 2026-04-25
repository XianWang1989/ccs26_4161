
X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

r1 = np.outer(X, X)  # Outer product (higher dimension)
r2 = np.dot(X, X.T)  # Matrix multiplication
np.array_equal(r1, r2)  # Will return False
