
import numpy as N
import itertools

# I created two lists, containing large amounts of numbers, i.e. 3.465
lx = [3.625, 4.625, ...]
ly = [41.435, 42.435, ...]  # The lists are not the same size!

xy = list(itertools.product(lx, ly))  # Create a nice "table" of my lists

# That itertools gives me something like
print(xy)  # [(3.625, 41.435), (3.625, 42.435), (... , ..), ...]

print(xy[0][0])  # Accessing first element (longitude)
print(xy[0][1])  # Accessing second element (latitude)

# Down here is where the error occurs
b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Directly access longitude
    idy = N.where(lat == l[1])[0][0]  # Directly access latitude
