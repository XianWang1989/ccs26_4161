
import numpy as N
import itertools

# Example data (replace with your real data)
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Creating the cartesian product of the lists
xy = list(itertools.product(lx, ly))

print(xy) 
# Output: [(3.625, 41.435), (3.625, 42.435), (4.625, 41.435), (4.625, 42.435)]

# Assuming lon and lat are numpy arrays read earlier in the script
# Example data for demonstration
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# Initialize index variables
for l in xy:
    # No need for 'b'; use 'l[0]' and 'l[1]' directly
    idx = N.where(lon == l[0])[0][0]  # Accessing the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Accessing the second element of the tuple
    print(f"Found indices: idx={idx}, idy={idy}")
