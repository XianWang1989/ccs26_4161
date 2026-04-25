
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]  # The lists should have a matching number of elements when creating pairs.

# Create a product of the two lists
xy = list(itertools.product(lx, ly))

# Print the generated pairs
print(xy) 
# Output example: [(3.625, 41.435), (3.625, 42.435), (4.625, 41.435), (4.625, 42.435)]

# Replace with your actual lon and lat arrays
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# Iteration over the product pairs
for l in xy:
    # Directly access the float values in the tuple
    idx = N.where(lon == l[0])[0][0]  # Use l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # Use l[1] for latitude
    print(f"Index in lon: {idx}, Index in lat: {idy}")
