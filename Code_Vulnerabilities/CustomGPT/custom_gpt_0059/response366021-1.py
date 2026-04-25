
import numpy as np
import itertools

# Sample lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Cartesian product of lx and ly
xy = list(itertools.product(lx, ly))

# Print the created list of tuples
print(xy)

# Initialize indices
b = -1
v = 1

# Assuming lon and lat are numpy arrays
lon = np.array([3.625, 4.625])  # Example lon values
lat = np.array([41.435, 42.435])  # Example lat values

for l in xy:
    b += 1
    # Correct index access
    idx = np.where(lon == l[0])[0][0]  # l[0] for first element of tuple
    idy = np.where(lat == l[1])[0][0]  # l[1] for second element of tuple
    print(f"Indices - idx: {idx}, idy: {idy}")
