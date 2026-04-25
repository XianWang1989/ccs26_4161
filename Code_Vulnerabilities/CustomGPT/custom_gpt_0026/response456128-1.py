
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Using np.outer on each row of X
outer_results = [np.outer(row, row) for row in X]

# To combine the results into a 3D array and view them
r1 = np.array(outer_results)

print("Result of np.outer for each row:\n", r1)

# Reshaping r1 to compare with np.dot
# np.dot(X, X.T) computes the matrix multiplication of X with its transpose
r2 = np.dot(X, X.T)

print("\nResult of np.dot:\n", r2)

# Check for equality
is_equal = np.array_equal(r1, r2)  # This will be False since they're not comparable directly
print("\nAre the two results equal?", is_equal)
