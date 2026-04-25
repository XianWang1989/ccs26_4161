
import numpy as N
import itertools

# Example data for testing
lx = [3.625, 4.625]  # Sample longitude values
ly = [41.435, 42.435]  # Sample latitude values

# Creating Cartesian product of the two lists
xy = list(itertools.product(lx, ly))

# Dummy arrays for lon and lat, replace these with your actual arrays
lon = N.array([3.625, 4.625, 3.5])  # Example lon data
lat = N.array([41.435, 42.435, 41.5])  # Example lat data

# Iterate over the Cartesian product
for l in xy:
    # Each l is a tuple (longitude, latitude)
    lon_value = l[0]  # Extract longitude
    lat_value = l[1]  # Extract latitude

    # Find indices based on the extracted values
    idx = N.where(lon == lon_value)[0][0]  # Get index for corresponding lon
    idy = N.where(lat == lat_value)[0][0]  # Get index for corresponding lat

    print(f"Longitude: {lon_value}, Latitude: {lat_value} => idx: {idx}, idy: {idy}")
