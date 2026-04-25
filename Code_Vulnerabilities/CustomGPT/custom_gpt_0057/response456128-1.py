
X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

r1 = np.outer(X,X)  # This doesn't compute like you'd expect
r2 = np.dot(X, X.T)  # This computes the dot product with a transpose
