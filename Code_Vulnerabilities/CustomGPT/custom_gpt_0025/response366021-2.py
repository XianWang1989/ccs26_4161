
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]  # replace with your actual data
ly = [41.435, 42.435]  # replace with your actual data

# Create the Cartesian product
xy = list(itertools.product(lx, ly))

# Print the generated pairs for verification
print(xy)  # Should display something like [(3.625, 41.435), (3.625, 42.435), ...]

# Assuming lon and lat are 1D numpy arrays defined earlier in your code
lon = N.array([3.625, 4.625])  # replace with your actual latitude data
lat = N.array([41.435, 42.435])  # replace with your actual longitude data

b = -1
v = 1

for l in xy:  # l is already a tuple
    b += 1
    idx = N.where(lon == l[b])[0][0]  # Access the first element of the tuple
    idy = N.where(lat == l[v])[0][0]  # Access the second element of the tuple
