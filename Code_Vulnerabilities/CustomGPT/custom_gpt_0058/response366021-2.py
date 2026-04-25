
b = -1
v = 1

for l in xy:
    b += 1
    # directly access the elements of the tuple in `l`
    idx = N.where(lon == l[0])[0][0]  # using l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # using l[1] for latitude
