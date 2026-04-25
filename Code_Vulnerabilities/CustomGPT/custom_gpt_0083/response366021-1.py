
import numpy as N
import itertools

# Example lists (they should contain actual values)
lx = [3.625, 4.625]  # Add your values
ly = [41.435, 42.435]  # Add your values

# Create a nice "table" of my lists
xy = list(itertools.product(lx, ly))

# Print the created list
print(xy)
# Access the first tuple elements correctly
print(xy[0][0])
print(xy[0][1])

b = -1
v = 1

# Assuming lon and lat are defined earlier in your script as numpy arrays
lon = N.array([3.625, 4.625])  # Sample data
lat = N.array([41.435, 42.435])  # Sample data

for l in xy:
    b += 1

    # Use the correct indexing
    idx = N.where(lon == l[0])[0][0]  # Access first value of the tuple
    idy = N.where(lat == l[1])[0][0]  # Access second value of the tuple

    print(f"Index in lon: {idx}, Index in lat: {idy}")
