
import numpy as N
import itertools

# Sample lists
lx = [3.625, 4.625]  # Add more values as needed
ly = [41.435, 42.435]  # Add more values as needed

# Create a Cartesian product of lx and ly
xy = list(itertools.product(lx, ly))

print(xy)  # Check the structure of xy

# Example lon and lat arrays (replace with your actual data)
lon = N.array([3.625, 4.625, 5.000])  # Sample longitude values
lat = N.array([41.435, 42.435, 43.000])  # Sample latitude values

b = -1
v = 1

for l in xy:
    b += 1
    # Accessing the tuple directly without indexing into l
    idx = N.where(lon == l[0])[0][0]  # Use l[0] instead of l[b][b]
    idy = N.where(lat == l[1])[0][0]  # Use l[1] instead of l[b][v]
    print(f"Indices for {l}: idx={idx}, idy={idy}")
