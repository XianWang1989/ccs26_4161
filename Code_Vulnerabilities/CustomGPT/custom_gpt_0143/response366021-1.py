
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]  # The lists are not the same size!

# Create a cartesian product of the two lists
xy = list(itertools.product(lx, ly))

# Output the product
print(xy) 
# [(3.625, 41.435), (3.625, 42.435), (4.625, 41.435), (4.625, 42.435)]

# Initialize index variables
b = -1
v = 1

# Loop through the tuples in xy
for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Use l[0] for the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Use l[1] for the second element of the tuple
