
import numpy as N
import itertools

# Sample data for illustration
lx = [3.625, 4.625]  # Your actual data would be much larger
ly = [41.435, 42.435]  # Same here for your actual data

# Create the Cartesian product of lx and ly
xy = list(itertools.product(lx, ly))

# Print the generated pairs
print(xy)  # [(3.625, 41.435), (3.625, 42.435), ...]

# Assuming lon and lat are defined as numpy arrays previously in your code
lon = N.array([3.625, 4.625])  # Example longitude array
lat = N.array([41.435, 42.435])  # Example latitude array

b = -1
v = 1

# Iterate directly over tuples and use fixed indices
for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Access second element of the tuple

    # Your further processing here
    print(f"Index in lon: {idx}, Index in lat: {idy}")
