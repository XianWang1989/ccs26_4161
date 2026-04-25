
import numpy as np
import itertools

# Example lists
lx = [3.625, 4.625]  # Sample data
ly = [41.435, 42.435]

# Create a Cartesian product of lx and ly
xy = list(itertools.product(lx, ly))  # [(3.625, 41.435), (3.625, 42.435), (4.625, 41.435), (4.625, 42.435)]

# Initialize b and v
b = -1
v = 1

# Iterate over the cartesian product
for l in xy:
    b += 1
    # Correctly index the tuple l
    idx = np.where(lon == l[0])[0][0]  # Access the first element of tuple
    idy = np.where(lat == l[1])[0][0]  # Access the second element of tuple

    # Debug prints to check index values
    print("b:", b, "idx:", idx, "idy:", idy)
