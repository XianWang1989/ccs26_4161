
import numpy as np

X = np.array([
    [1, 5],
    [5, 9],
    [4, 1]
])

# Use the first column as a 1D array for outer product
vector_1 = X[:, 0]  # Getting the first column
vector_2 = X[:, 1]  # Getting the second column

r1 = np.outer(vector_1, vector_2)  # Outer product of the first and second columns
r2 = np.dot(vector_1[:, np.newaxis], vector_2[np.newaxis, :])  # Dot product in outer form

print(np.array_equal(r1, r2))  # Now this will return True
