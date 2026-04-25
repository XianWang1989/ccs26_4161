
import numpy as N
import itertools

# Example lists (replace ... with actual values)
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))  # Create combinations of lx and ly

# Example lon and lat arrays (replace with your actual data)
lon = N.array([3.625, 4.625, 3.500])
lat = N.array([41.435, 42.435, 41.000])

print(xy)  # Check the output
print(xy[0][0])  # Access first element
print(xy[0][1])  # Access second element

b = -1
v = 1

for l in xy:
    b += 1
    # Access values in the tuple directly
    idx = N.where(lon == l[0])[0][0]  # Access first element of tuple
    idy = N.where(lat == l[1])[0][0]  # Access second element of tuple
    print(f"Index in lon: {idx}, Index in lat: {idy}")
