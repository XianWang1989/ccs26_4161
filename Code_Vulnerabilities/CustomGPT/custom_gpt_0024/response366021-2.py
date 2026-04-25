
import numpy as N
import itertools

# Sample data (replace with your actual numbers)
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create combinations of lists
xy = list(itertools.product(lx, ly))

# Print the combinations
print(xy)  # Example output: [(3.625, 41.435), (3.625, 42.435), (4.625, 41.435), (4.625, 42.435)]

# Sample lon and lat arrays (replace with your actual arrays)
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# Iterate over the combinations
for l in xy:
    # l is a tuple, so access it directly
    idx = N.where(lon == l[0])[0][0]  # l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # l[1] for latitude
    print(f"Index in lon: {idx}, Index in lat: {idy}")
