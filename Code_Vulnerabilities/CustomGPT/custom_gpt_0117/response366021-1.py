
import numpy as np
import itertools

# Example lists (replace with your actual data)
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create combinations of the lists
xy = list(itertools.product(lx, ly))

print(xy)  # Output: [(3.625, 41.435), (3.625, 42.435), ...]
print(xy[0][0])  # Accesses 3.625
print(xy[0][1])  # Accesses 41.435

# Assume lon and lat are defined, here's a mock example
lon = np.array([3.625, 4.625, 5.625])  # Replace with actual data
lat = np.array([41.435, 42.435, 43.435])  # Replace with actual data

b = -1
v = 1

for l in xy:
    b += 1
    idx = np.where(lon == l[0])[0][0]  # Access first element of the tuple
    idy = np.where(lat == l[1])[0][0]  # Access second element of the tuple
    print(f'Index in lon: {idx}, Index in lat: {idy}')
