
import numpy as N
import itertools

# I created two lists, containing large amounts of numbers
lx = [3.625, 4.625, ...]
ly = [41.435, 42.435, ...]  # The lists are not the same size!

xy = list(itertools.product(lx, ly))  # Create a "table" of my lists

# Print the xy list to check its structure
print(xy)  # e.g. [(3.625, 41.435), (3.625, 42.435), ...]

# Initialize b and v for indexing
b = 0
v = 1

# Assume lon and lat are previously defined NumPy arrays
for l in xy:
    idx = N.where(lon == l[b])[0][0]  # Access the first element of the tuple
    idy = N.where(lat == l[v])[0][0]  # Access the second element of the tuple
    b += 1  # Increment b if needed for tracking iterations, but here it's not necessary

# Ensure lon and lat are adequately defined before this loop
