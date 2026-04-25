
# Compute outer product directly with a single vector
r1 = np.outer(X.flatten(), X.flatten())
# You can adjust r2 to be the outer product of a specific vector
r2 = np.outer(X[0], X[0])  # Example using first row as the outer product

print("r1:\n", r1)
print("r2:\n", r2)
print("Are they equal?", np.array_equal(r1, r2))
