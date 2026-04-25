
for l in xy:
    # No need for the b variable; we can just use the loop index for accessing l
    idx = N.where(lon == l[0])[0][0]  # Access the first item in the tuple
    idy = N.where(lat == l[1])[0][0]  # Access the second item in the tuple
