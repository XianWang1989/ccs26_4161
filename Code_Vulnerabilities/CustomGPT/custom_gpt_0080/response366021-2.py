
import numpy as N
import itertools

# Example data
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create combinations
xy = list(itertools.product(lx, ly))

# Print the combinations
print(xy)

# Initialize b (not required since we're not using it this way)
b = -1

# Loop through each combination
for l in xy:
    # Access values directly from tuple l
    lon_val = l[0]
    lat_val = l[1]

    # Find indices using numpy
    idx = N.where(lon == lon_val)[0][0]  # Assuming lon is defined earlier 
    idy = N.where(lat == lat_val)[0][0]  # Assuming lat is defined earlier

    # You can then use idx and idy as needed
