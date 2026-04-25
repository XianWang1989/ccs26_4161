
for l in xy:
    b += 1
    lon_value = l[0]  # Access first element of the tuple
    lat_value = l[1]  # Access second element of the tuple

    idx = N.where(lon == lon_value)[0][0]
    idy = N.where(lat == lat_value)[0][0]
