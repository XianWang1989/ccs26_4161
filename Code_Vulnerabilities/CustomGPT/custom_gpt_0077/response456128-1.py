
X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

r1 = np.outer(X, X)  # This will give a 3D array
r2 = np.dot(X, X.T)  # This will give a 2D array
