
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Correcting r1 to use outer on flattened versions of X
r1 = np.array([np.outer(X[i].A1, X[i].A1) for i in range(X.shape[0])]).reshape(X.shape[0], -1)

# Now using np.dot but we need flattening
r2 = np.dot(X, X.T)

# The two shapes of r1 and r2 will be different. To compare, we might need to change our approach.
# If you're looking for a true 2D outer product result you'd need to ensure both inputs are 1D.
r3 = np.outer(X.A1, X.A1)

# Now comparing shapes
equal_result = np.array_equal(r3, r2.flatten())

print(f"Are they equal? {equal_result}")
