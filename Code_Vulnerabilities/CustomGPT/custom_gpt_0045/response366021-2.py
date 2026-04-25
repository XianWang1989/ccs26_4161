
b = -1
v = 1

for l in xy:
    b += 1  # If b is not necessary for tracking the index, consider removing it
    idx = N.where(lon == l[0])[0][0]  # Accessing the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Accessing the second element of the tuple
