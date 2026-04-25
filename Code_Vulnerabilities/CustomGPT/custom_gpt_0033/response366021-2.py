
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a list of tuples
xy = list(itertools.product(lx, ly))

# Print for verification
print(xy)
# [(3.625, 41.435), (3.625, 42.435), ...]

# Initialize values
b = -1
v = 1

# Iterate through the tuples
for l in xy:
    b += 1
    # Access values directly from the tuple
    idx = N.where(lon == l[0])[0][0]  # l[0] accesses the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # l[1] accesses the second element of the tuple

    # You can proceed with idx and idy
    print(f'Index values: idx = {idx}, idy = {idy}')
