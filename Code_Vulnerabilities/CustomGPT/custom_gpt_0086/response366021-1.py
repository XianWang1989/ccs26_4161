
import numpy as N
import itertools

# Example lists (replace with your data)
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create pairs
xy = list(itertools.product(lx, ly))

# Latitude and longitude arrays (example values, replace with your data)
lon = N.array([3.625, 4.625]) 
lat = N.array([41.435, 42.435])

for l in xy:
    # Directly access the elements of l
    idx = N.where(lon == l[0])[0][0]  # l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # l[1] for latitude

    print(f"Longitude index: {idx}, Latitude index: {idy}")
