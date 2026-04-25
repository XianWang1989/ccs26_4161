
import numpy as N
import itertools

# I created two lists, containing large amounts of numbers
lx = [3.625, 4.625]  # For the sake of example, I've limited the lists
ly = [41.435, 42.435]  # The lists should be of the same size in reality

xy = list(itertools.product(lx, ly))  # create a "table" of my lists

# that itertools gives me something like
print(xy) 
# Output: [(3.625, 41.435), (3.625, 42.435), (4.625, 41.435), (4.625, 42.435)]

# down here is where the processing occurs
b = -1
v = 1

lon = N.array([3.625, 4.625])  # Example longitude values
lat = N.array([41.435, 42.435])  # Example latitude values

for l in xy:
    b += 1
    # Now we use l directly without indexing
    idx = N.where(lon == l[0])[0][0]  # Accessing first element of tuple l
    idy = N.where(lat == l[1])[0][0]  # Accessing second element of tuple l

    print(f'Index for {l[0]} in lon is: {idx}, Index for {l[1]} in lat is: {idy}')
