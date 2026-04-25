
X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

r1 = np.outer(X, X)          # Outer product, results in 3D array
r2 = np.dot(X, X.T)          # Matrix multiplication, 3x3 result
np.array_equal(r1, r2)       # This returns False
