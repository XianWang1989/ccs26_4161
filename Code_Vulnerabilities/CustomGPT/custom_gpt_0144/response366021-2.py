for l in xy:
    x_val = l[0]
    y_val = l[1]
    idx = N.where(lon == x_val)[0][0]
    idy = N.where(lat == y_val)[0][0]
