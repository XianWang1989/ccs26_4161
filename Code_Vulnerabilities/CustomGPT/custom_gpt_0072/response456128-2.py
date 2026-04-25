
import numpy as np

# Define your vectors
u = np.array([1, 5, 4])
v = np.array([1, 5, 4])  # Same as u for outer product comparison

# Calculate outer product using np.outer
r1 = np.outer(u, v)

# Calculate using np.dot on reshaped arrays
r2 = np.dot(u[:, np.newaxis], v[np.newaxis, :])

# Check equality
result = np.array_equal(r1, r2)

print("r1:\n", r1)
print("r2:\n", r2)
print("Arrays are equal:", result)
