
import numpy as N
import itertools

# Sample data, replace with real values
lx = [3.625, 4.625, ...] 
ly = [41.435, 42.435, ...] 

xy = list(itertools.product(lx, ly))

# Assuming lon and lat have been defined and populated prior in the script
lon = N.array([...])
lat = N.array([...])

for b, l in enumerate(xy):  # Use enumerate to get index of loop
    idx = N.where(lon == l[0])[0][0]  # Access first element of tuple
    idy = N.where(lat == l[1])[0][0]  # Access second element of tuple
    # Further processing using idx and idy
