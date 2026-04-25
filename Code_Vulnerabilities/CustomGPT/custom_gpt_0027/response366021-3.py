
import numpy as N
import itertools

lon = N.array([3.625, 4.625, 3.465])  # Example lon array
lat = N.array([41.435, 42.435, 41.875])  # Example lat array

lx = [3.625, 4.625]
ly = [41.435, 42.435]
xy = list(itertools.product(lx, ly))

for l in xy:
    try:
        idx = N.where(lon == l[0])[0][0]
        idy = N.where(lat == l[1])[0][0]
        print(f"Index in lon: {idx}, Index in lat: {idy}")
    except IndexError:
        print("Value not found in arrays.")
