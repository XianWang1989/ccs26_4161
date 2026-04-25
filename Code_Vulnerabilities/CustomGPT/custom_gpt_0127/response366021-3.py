
while True:
    try:
        # Sample lon and lat arrays for demonstration
        lon = N.array([3.625, 4.625])
        lat = N.array([41.435, 42.435])

        for l in xy:
            idx = N.where(lon == l[0])[0][0]
            idy = N.where(lat == l[1])[0][0]

            print(f"Index for lon: {idx}, Index for lat: {idy}")

        break

    except IndexError as e:
        print(f"Error: {e}")
