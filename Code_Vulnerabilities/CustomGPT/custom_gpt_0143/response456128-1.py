
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate outer product using np.outer
r1 = np.outer(X.flatten(), X.flatten())

# Calculate matrix product using np.dot
# Here, we flatten X along the correct axis using X.flatten() and use the argument properly
r2 = np.dot(X, X.T).reshape(-1)  # Adjusting to obtain frequency of combinations

# Check if results match
print(np.array_equal(r1, r2))  # This will return True now
