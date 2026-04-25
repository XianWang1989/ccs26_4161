
import numpy as N
import itertools

# Example lists (ensure they are defined properly)
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

print(xy)
# Example output: [(3.625, 41.435), (3.625, 42.435), (4.625, 41.435), (4.625, 42.435)]

# Manage indices correctly based on tuple structure
for b, l in enumerate(xy):
    lon_value = l[0]  # Accessing the first element (longitude)
    lat_value = l[1]  # Accessing the second element (latitude)

    # Ensure 'lon' and 'lat' are defined correctly as numpy arrays
    idx = N.where(lon == lon_value)[0]
    idy = N.where(lat == lat_value)[0]

    if idx.size > 0 and idy.size > 0:  # Check that indices were found
        idx = idx[0]
        idy = idy[0]
        print(f'Index for lon: {idx}, Index for lat: {idy}')
    else:
        print(f'Lon or lat value not found for {lon_value}, {lat_value}')
