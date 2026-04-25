
import numpy as N
import itertools

# Example lists (should contain your actual data)
lx = [3.625, 4.625]
ly = [41.435, 42.435]  # Ensure to replace these with your actual values

xy = list(itertools.product(lx, ly))  # Create a cartesian product of lists

# Assuming lon and lat are defined as NumPy arrays
lon = N.array([3.625, 4.625])  # Example lon array
lat = N.array([41.435, 42.435])  # Example lat array

# Iterate through the tuples in xy
for l in xy:
    # Directly access the values from the tuple without indexing
    idx = N.where(lon == l[0])[0][0]  # l[0] refers to the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # l[1] refers to the second element of the tuple

    print(f'Index of lon: {idx}, Index of lat: {idy}')
