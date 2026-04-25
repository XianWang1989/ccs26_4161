
import numpy as N
import itertools

# Sample lists (replace with your actual data)
lx = [3.625, 4.625]  # Example values
ly = [41.435, 42.435]  # Example values

xy = list(itertools.product(lx, ly))  # Create Cartesian product

# Example latitude and longitude arrays (replace with your actual data)
lon = N.array([3.625, 4.625])  # Example longitude array
lat = N.array([41.435, 42.435])  # Example latitude array

b = -1
v = 1

for l in xy:
    b += 1
    # Access the elements of l directly
    idx = N.where(lon == l[0])[0][0]  # Use l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # Use l[1] for latitude
    print("Index in lon:", idx)
    print("Index in lat:", idy)
