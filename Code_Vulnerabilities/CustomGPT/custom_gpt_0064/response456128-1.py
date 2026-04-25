
X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

r1 = np.outer(X, X)  # This causes a shape issue since X is treated as a matrix
r2 = np.dot(X, X.T)  # This computes the matrix multiplication
