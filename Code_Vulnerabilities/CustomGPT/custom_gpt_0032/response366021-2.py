
if len(N.where(lon == l[0])[0]) > 0:
    idx = N.where(lon == l[0])[0][0]
else:
    continue  # If not found, skip to the next iteration
