
import numpy as N
import itertools

# Sample lists for demonstration
lx = [3.625, 4.625]
ly = [41.435, 42.435]  # The lists can be of different sizes

xy = list(itertools.product(lx, ly))

# Sample lon/lat values (replace these with your actual values)
lon = N.array([3.625, 4.625, 3.000])
lat = N.array([41.435, 42.435, 40.000])

# Looping through the product and fixing index access
for l in xy:
    # l is a tuple e.g., (3.625, 41.435)
    idx = N.where(lon == l[0])[0][0]  # Directly use l[0] for lon
    idy = N.where(lat == l[1])[0][0]  # Directly use l[1] for lat
    print(f'Indexes: lon index - {idx}, lat index - {idy}')
