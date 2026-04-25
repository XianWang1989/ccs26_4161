
X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

r1 = np.outer(X, X)    # This will flatten X to create a vector for outer product.
r2 = np.dot(X, X.T)    # This will compute the matrix product of X and its transpose.
np.array_equal(r1, r2)  # This is expected to be False.
