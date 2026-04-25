
import numpy as np
import itertools

# Sample data
lx = [3.625, 4.625]  # Shortened for example
ly = [41.435, 42.435]

# Create product of lists
xy = list(itertools.product(lx, ly))

# Sample longitude and latitude arrays
lon = np.array([3.625, 4.625])
lat = np.array([41.435, 42.435])

# Initialize index variable
b = -1

# Loop through the coordinate pairs
for l in xy:
    b += 1
    idx = np.where(lon == l[0])[0][0]  # Access first element of tuple
    idy = np.where(lat == l[1])[0][0]  # Access second element of tuple
    print(f"Index in lon: {idx}, Index in lat: {idy}")
