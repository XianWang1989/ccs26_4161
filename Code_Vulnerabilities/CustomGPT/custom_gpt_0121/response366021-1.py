
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a Cartesian product
xy = list(itertools.product(lx, ly))

print(xy)  # Check the generated pairs

# Sample longitude/latitude arrays
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

b = -1

for l in xy:
    b += 1
    # Access the tuple values directly
    idx = N.where(lon == l[0])[0][0]
    idy = N.where(lat == l[1])[0][0]
    print(f'Index in lon: {idx}, Index in lat: {idy}')
