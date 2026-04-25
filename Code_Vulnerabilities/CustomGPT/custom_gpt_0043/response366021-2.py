
import numpy as N
import itertools

# Sample lists for demonstration
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))  # Just like your code

# Assuming lon and lat are defined properly earlier
# Sample lon and lat arrays for demonstration
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# b is not needed as an index here
for l in xy:
    # Directly access the elements from the tuple l
    idx = N.where(lon == l[0])[0][0]  # Access the first value in l (x_value)
    idy = N.where(lat == l[1])[0][0]  # Access the second value in l (y_value)

    print(f'Coordinates: {l}, idx: {idx}, idy: {idy}')
