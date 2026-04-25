for x_val, y_val in xy:
    idx = N.where(lon == x_val)[0][0]
    idy = N.where(lat == y_val)[0][0]
