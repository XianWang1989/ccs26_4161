
import numpy as np

X = np.matrix([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Use np.outer on the flattened versions of X's rows
# Assuming you want the outer product for each row in X
r1 = np.array([np.outer(X[i].A1, X[i].A1) for i in range(X.shape[0])]).reshape(X.shape[0] * X.shape[0], 2, 2)

# Using np.dot to get the product of X and its transpose
r2 = np.dot(X, X.T)

# This won't be equal but demonstrates an outer product as a sum of outer products
# Instead of element-wise comparison, you can check their structures
print(np.array_equal(r1, r2))  # This will return False

# To achieve true equivalence, we would adjust how we interpret outer products
# Therefore, to compare by considering the operations distinctly, we can display:
print(f"Outer products shaping differently:\n{r1}\n\nDot product:\n{r2}")
