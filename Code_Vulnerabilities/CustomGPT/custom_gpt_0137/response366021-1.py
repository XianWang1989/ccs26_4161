
for l in xy:
    b += 1
    idx = N.where(lon==l[b][b])[0][0]  # This line may raise the error
    idy = N.where(lat==l[b][v])[0][0]
