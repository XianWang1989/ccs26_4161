
import numpy as N
import itertools

# Sample lists of longitude and latitude
lx = [3.625, 4.625]  # Example values for lx
ly = [41.435, 42.435]  # Example values for ly

# Create a product of the two lists
xy = list(itertools.product(lx, ly))  # This creates pairs of all combinations

# Print the result of the product
print(xy)  # Example output: [(3.625, 41.435), (3.625, 42.435), (4.625, 41.435), (4.625, 42.435)]

# Latitude and Longitude arrays
lon = N.array([3.625, 4.625, 5.500])  # Sample data for lon
lat = N.array([41.435, 42.435, 43.500])  # Sample data for lat

# Initialization of b and v
b = -1
v = 1

# Loop through the list of tuples
for l in xy:
    b += 1
    # Accessing the values directly from l
    idx = N.where(lon == l[0])[0][0]  # l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # l[1] for latitude
    print(f"Longitude Index: {idx}, Latitude Index: {idy}")
