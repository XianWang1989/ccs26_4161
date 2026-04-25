
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]  # Add your values here
ly = [41.435, 42.435]  # Add your values here

xy = list(itertools.product(lx, ly))  # Create cartesian product
print(xy)  # Check contents

# Replace b and v with fixed indices for access
for l in xy:
    # Directly access the elements of tuple l
    lon_value = l[0]  # First element of the tuple
    lat_value = l[1]  # Second element of the tuple

    # Use where on lon and lat arrays to find the index
    idx = N.where(lon == lon_value)[0][0]
    idy = N.where(lat == lat_value)[0][0]

    # Continue processing with idx and idy as needed
