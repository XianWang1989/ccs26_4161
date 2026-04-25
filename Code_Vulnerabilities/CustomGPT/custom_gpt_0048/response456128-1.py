
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Calculate the outer product using np.outer
r1 = np.outer(X, X)

# To achieve a similar result with np.dot, stack X vertically or horizontally
r2 = np.dot(X.T, X)  # You may need to adjust dimensions based on desired output

# Check if the arrays are equal
result = np.array_equal(r1, r2)

print("Result of np.array_equal:", result)
print("Outer product (r1):\n", r1)
print("Dot product result (r2):\n", r2)
