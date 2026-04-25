
import numpy as np
import itertools

# Example data
lx = [3.625, 4.625]
ly = [41.435, 42.435]
lon = np.array([3.625, 4.625, 5.625])  # Sample lon array
lat = np.array([41.435, 42.435, 43.435])  # Sample lat array

xy = list(itertools.product(lx, ly))

# Printing the generated combinations
print(xy)

# Loop through xy
for l in xy:
    # Access the first and second elements directly
    idx = np.where(lon == l[0])[0][0]
    idy = np.where(lat == l[1])[0][0]

    # Print indices for debugging
    print(f"Indices for {l}: idx={idx}, idy={idy}")
