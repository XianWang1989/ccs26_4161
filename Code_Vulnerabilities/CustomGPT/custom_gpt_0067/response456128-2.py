
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correctly using np.outer with flattened versions
r1 = np.outer(X.flatten(), X.flatten())

# Reshape result to compare to outer product
# Since np.dot will not produce the same output, we need another form to mimic outer product
r2 = np.zeros((X.shape[0] * X.shape[1], X.shape[0] * X.shape[1]))

for i in range(X.shape[0]):
    for j in range(X.shape[0]):
        # Fill corresponding outer product blocks
        r2[i * X.shape[1]:(i + 1) * X.shape[1], j * X.shape[1]:(j + 1) * X.shape[1]] = np.outer(X[i], X[j])

# Check if arrays are equal
result = np.array_equal(r1, r2)
print(result)  # Should return True
