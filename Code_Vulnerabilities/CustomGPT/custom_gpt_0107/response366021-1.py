
import numpy as np
import itertools

# Sample data for demonstration
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create the Cartesian product of lx and ly
xy = list(itertools.product(lx, ly))

# Check the output format
print(xy)  # Example output: [(3.625, 41.435), (3.625, 42.435), ...]

# Indices to access the products
b = 0  # Starting index
v = 1  # Another index

# Assuming lon and lat are numpy arrays defined and populated earlier
lon = np.array([3.625, 4.625, 5.625])  # Example values
lat = np.array([41.435, 42.435, 43.435])  # Example values

# Loop over the Cartesian product
for l in xy:
    # Access elements directly without additional indexing
    idx = np.where(lon == l[0])[0][0]  # Using l[0] for longitude
    idy = np.where(lat == l[1])[0][0]  # Using l[1] for latitude

    print(f'Longitude index: {idx}, Latitude index: {idy}')
