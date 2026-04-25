
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]  # Add more values as needed
ly = [41.435, 42.435]  # Add more values as needed

# Create a product of the lists
xy = list(itertools.product(lx, ly))

# Print the result
print(xy) 
# Output: [(3.625, 41.435), (3.625, 42.435), ...]

# Set b and v for indexing
b = 0  # Start indexing from 0
v = 1

# Assuming lon and lat are defined earlier
lon = N.array([3.625, 4.625])  # Example longitude values
lat = N.array([41.435, 42.435])  # Example latitude values

for l in xy:
    # No need to use b as the loop already provides l directly
    idx = N.where(lon == l[0])[0][0]  # Access first element directly
    idy = N.where(lat == l[1])[0][0]  # Access second element directly

    print(f'Index in lon: {idx}, Index in lat: {idy}')
