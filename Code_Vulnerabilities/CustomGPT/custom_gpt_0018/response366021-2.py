
b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Access the second element of the tuple
