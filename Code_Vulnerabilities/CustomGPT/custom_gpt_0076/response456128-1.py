
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correct usage of np.outer
r1 = np.outer(X.flatten(), X.flatten())

# Adjust np.dot to create a similar structure as np.outer
r2 = np.dot(X, X.T).flatten()  # Flatten to compare with the outer product

# Reshaping to match the dimensions of np.outer
r2 = r2.reshape(X.shape[0], X.shape[0])

# Checking equality
result = np.array_equal(r1, r2)

print(f"Are the results equal? {result}")
