
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Compute the outer product for each row
outer_results = [np.outer(x, x) for x in X]

# Stack the outer results into a single array
r1 = np.vstack(outer_results)

# Calculate dot product with transposition
r2 = np.dot(X, X.T)

# Check if they are equal
result = np.array_equal(r1, r2)
print(result)  # This should print True
