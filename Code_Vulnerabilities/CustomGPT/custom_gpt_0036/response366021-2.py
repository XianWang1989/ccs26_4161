
import numpy as N
import itertools

# Sample lists (Replace these with your actual data)
lx = [3.625, 4.625]  # Example values
ly = [41.435, 42.435]  # Example values

xy = list(itertools.product(lx, ly))

# You would have read 'lon' and 'lat' from your netCDF before this loop
# Sample arrays for illustration (Replace these with the actual read data)
lon = N.array([3.625, 4.625, 5.00])
lat = N.array([41.435, 42.435, 43.0])

b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access the first element (longitude)
    idy = N.where(lat == l[1])[0][0]  # Access the second element (latitude)

    print(f'Index Lon: {idx}, Index Lat: {idy}')  # Print results for debugging
