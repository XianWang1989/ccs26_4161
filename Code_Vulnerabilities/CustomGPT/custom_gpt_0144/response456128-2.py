X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Take one row as a and another as b
a = X[0]
b = X[1]

# Outer product
r1 = np.outer(a, b)

# Dot version
r2 = np.dot(a[:, np.newaxis], b[np.newaxis, :])

print(np.array_equal(r1, r2))  # True
