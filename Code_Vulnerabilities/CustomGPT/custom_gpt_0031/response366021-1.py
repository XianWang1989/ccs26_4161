
import numpy as N
import itertools

# Example lists (replace with your actual data)
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a list of tuples using itertools product
xy = list(itertools.product(lx, ly))

# Example lon and lat arrays (replace with your actual data)
lon = N.array([3.625, 4.625, 5.0])  # Example values
lat = N.array([41.435, 42.435, 43.0])  # Example values

b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Access the second element of the tuple
    print(f"Index for {l}: lon idx={idx}, lat idx={idy}")
