
import numpy as np

# Define 1-D arrays
u = X[0, :]
v = X[1, :]

# Calculate outer product
r1 = np.outer(u, v)  # Correct outer product
