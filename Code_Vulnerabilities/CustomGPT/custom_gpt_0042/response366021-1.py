
import numpy as np
import itertools

# Sample data for demonstration (use your actual data)
lx = [3.625, 4.625]  # Example longitude values
ly = [41.435, 42.435]  # Example latitude values

# Create a cartesian product of the two lists
xy = list(itertools.product(lx, ly))  # Generates pairs like [(3.625, 41.435), ...]

print(xy)  # Output the cartesian product

# Initialize b and v
b = -1
v = 1

# Assuming lon and lat are numpy arrays read from your netCDF file
lon = np.array([3.625, 4.625, ...])  # Example longitude array
lat = np.array([41.435, 42.435, ...])  # Example latitude array

for l in xy:
    b += 1
    # Instead of using l[b][b], just access indices directly
    idx = np.where(lon == l[0])[0][0]  # Access the first element
    idy = np.where(lat == l[1])[0][0]  # Access the second element

    print(f'Index for lon: {idx}, Index for lat: {idy}')
