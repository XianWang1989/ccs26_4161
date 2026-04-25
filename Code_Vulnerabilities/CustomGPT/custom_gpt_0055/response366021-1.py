
import numpy as N
import itertools

# Example lists with floating point numbers
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create all combinations of lx and ly
xy = list(itertools.product(lx, ly))

print(xy)  # Output: [(3.625, 41.435), (3.625, 42.435), (4.625, 41.435), (4.625, 42.435)]

b = -1
v = 1

# Assuming lon and lat are numpy arrays read earlier in the script:
# Example data for lon and lat
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

for l in xy:
    b += 1
    # Correctly access the elements of the tuple l
    idx = N.where(lon == l[0])[0][0]
    idy = N.where(lat == l[1])[0][0]
    print(f'Indices -> idx: {idx}, idy: {idy}')
