
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]
ly = [41.435, 42.435]  # Lists should not be empty or fewer than elements of lx

# Create combinations
xy = list(itertools.product(lx, ly))

# Assuming lat and lon are some numpy arrays defined earlier
lon = N.array(lx)  # For demonstration, convert lx to numpy array
lat = N.array(ly)  # For demonstration, convert ly to numpy array

b = -1  # index starts from -1, consider updating to start from 0
for l in xy:
    b += 1
    lon_value = l[0]  # Access first element of tuple
    lat_value = l[1]  # Access second element of tuple

    idx = N.where(lon == lon_value)[0][0]  # getting index based on values
    idy = N.where(lat == lat_value)[0][0]

    print(f"Index for lon: {idx}, Index for lat: {idy}")
