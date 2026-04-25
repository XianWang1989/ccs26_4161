
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly)) 

lon = N.array([3.625, 4.625])  # Example longitude array
lat = N.array([41.435, 42.435]) # Example latitude array

# Iterate through xy without using b and v as indices
for l in xy:
    idx = N.where(lon == l[0])[0][0]  # Access first element directly
    idy = N.where(lat == l[1])[0][0]  # Access second element directly
    print(f"Index in lon: {idx}, Index in lat: {idy}")
