
import numpy as np
import itertools

# Example lists (replace with your actual data)
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a grid of tuples
xy = list(itertools.product(lx, ly))

# Example longitude/latitude (replace with your actual data)
lon = np.array([3.625, 4.625])
lat = np.array([41.435, 42.435])

# Initialize index
b = -1

for l in xy:
    b += 1
    # Directly access the tuple elements
    idx = np.where(lon == l[0])[0][0]
    idy = np.where(lat == l[1])[0][0]

    print(f"Longitude Index: {idx}, Latitude Index: {idy}")
