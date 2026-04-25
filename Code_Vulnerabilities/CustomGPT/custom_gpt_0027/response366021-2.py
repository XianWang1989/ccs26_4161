
b = 0  # Initialize b appropriately

for l in xy:
    idx = N.where(lon == l[0])[0][0]  # Access the first item directly
    idy = N.where(lat == l[1])[0][0]  # Access the second item directly
    b += 1  # Increment b if needed for other purposes, but not for indexing
