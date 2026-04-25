
import numpy as np
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a Cartesian product of two lists
xy = list(itertools.product(lx, ly))

print(xy)  # Output the Cartesian product

# Initialize latitude and longitude (example arrays)
lon = np.array([3.625, 4.625])
lat = np.array([41.435, 42.435])

# Down here is where we access elements
b = -1
v = 0  # Changed to index 0 for the second element of the tuple

for l in xy:
    b += 1
    # Correctly access elements of the tuple
    idx = np.where(lon == l[0])[0][0]  # Access first element of the tuple
    idy = np.where(lat == l[1])[0][0]  # Access second element of the tuple
    print(f'Index in lon: {idx}, Index in lat: {idy}')
