
import numpy as np

# Define the vector
x = np.array([1, 5, 4])  # Change to a single column vector
y = np.array([5, 9, 1])  # Change to a single column vector

# Outer product
r1 = np.outer(x, y)  # 3x3 matrix
# Dot product
r2 = np.dot(x.reshape(-1, 1), y.reshape(1, -1))  # Ensures shape is (3, 3)

# Now you can compare
result = np.array_equal(r1, r2)
print(result)  # This will print True
