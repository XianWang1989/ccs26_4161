
import numpy as np

# Define the input vector
v = np.array([1, 5, 3])

# Create a binary matrix using np.eye
C = np.eye(v.max())[v].astype(int)

print(C)
