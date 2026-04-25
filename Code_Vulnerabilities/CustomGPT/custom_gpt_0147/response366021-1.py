
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]  # Should be filled with actual numbers
ly = [41.435, 42.435]  # Should be filled with actual numbers

xy = list(itertools.product(lx, ly))  # Create combinations

# Print to check the combinations
print(xy)  # Should output something like [(3.625, 41.435), (3.625, 42.435), ...]

# Assuming lon and lat are numpy arrays previously defined
# Example: lon = N.array([3.625, 4.625, ...]), lat = N.array([41.435, 42.435, ...])
lon = N.array([3.625, 4.625])  # Dummy data for example
lat = N.array([41.435, 42.435])  # Dummy data for example

# Initialize counters
b = -1

# Iterate through the combinations
for l in xy:
    b += 1
    # Accessing directly instead of using an index
    idx = N.where(lon == l[0])[0][0]  # Accessing first value from tuple
    idy = N.where(lat == l[1])[0][0]  # Accessing second value from tuple
    print(f"Index of {l[0]} in lon is {idx}, Index of {l[1]} in lat is {idy}")
