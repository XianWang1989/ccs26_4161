
import numpy as N
import itertools

# Example lists, replace with your actual data
lx = [3.625, 4.625, ...]
ly = [41.435, 42.435, ...]  # The lists are not the same size!

xy = list(itertools.product(lx, ly))  # create a "table" of my lists

print(xy)  # Display the list of tuples

# Initialize b and v as indices
b = -1
v = 1

# Assuming lon and lat are defined earlier in your code
for l in xy:
    b += 1
    # l[0] and l[1] give the respective elements from the tuple
    idx = N.where(lon == l[0])[0][0]  # Access first element of tuple
    idy = N.where(lat == l[1])[0][0]  # Access second element of tuple

    # Add your processing logic here
