
import numpy as N
import itertools

# Example lists with floating-point numbers
lx = [3.625, 4.625]  # Extend with more numbers as needed
ly = [41.435, 42.435]  # Extend with more numbers as needed

xy = list(itertools.product(lx, ly))  # Create tuples of all combinations

# Check the generated tuples
print(xy) 
# Output: [(3.625, 41.435), (3.625, 42.435), (4.625, 41.435), (4.625, 42.435)]

b = -1
v = 1

# Assuming lon and lat are arrays filled with appropriate values:
lon = N.array([3.625, 4.625])  # Example longitude array
lat = N.array([41.435, 42.435])  # Example latitude array

for l in xy:
    b += 1  # Increment the index
    # Directly use l for indexing
    idx = N.where(lon == l[0])[0][0]  # Access first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Access second element of the tuple
    print(f"Index for lon: {idx}, Index for lat: {idy}")  # Output the indices
