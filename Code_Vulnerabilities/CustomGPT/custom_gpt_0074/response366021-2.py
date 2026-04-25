
b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Accessing longitude directly
    idy = N.where(lat == l[1])[0][0]  # Accessing latitude directly
