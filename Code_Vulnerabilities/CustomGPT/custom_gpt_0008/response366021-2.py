
import numpy as N
import itertools

# Example lists, assuming these are your actual values
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))  # Create pairs of (lx, ly)

print(xy)  # Output: [(3.625, 41.435), (3.625, 42.435), ...]

# Initialize indices
b = -1
v = 1

# Assuming lon and lat are defined numpy arrays
lon = N.array([3.625, 4.625, 5.000])  # Example values for lon
lat = N.array([41.435, 42.435, 50.000])  # Example values for lat

for l in xy:
    b += 1
    # Correctly accessing the tuple elements
    idx = N.where(lon == l[0])[0][0]  # Access first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Access second element of the tuple

    # You can now use idx and idy as needed
    print(f"Index in lon: {idx}, Index in lat: {idy}")
