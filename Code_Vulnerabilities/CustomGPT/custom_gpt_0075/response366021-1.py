
b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Correct indexing
    idy = N.where(lat == l[1])[0][0]
