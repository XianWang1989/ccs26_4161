
import numpy as N
import itertools

# Sample lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))
print(xy)  # Display the generated pairs

# Example lon and lat arrays for demonstration
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# Loop over xy
for index, (lon_value, lat_value) in enumerate(xy):
    try:
        idx = N.where(lon == lon_value)[0][0]
        idy = N.where(lat == lat_value)[0][0]
        print(f'Index: {index}, lon index: {idx}, lat index: {idy}')
    except IndexError:
        print(f"Index error for value: {lon_value}, {lat_value}")
