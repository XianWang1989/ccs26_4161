
import numpy as N
import itertools

# Example lists (use your original lists here)
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))  # creating combinations

# Sample latitude/longitude arrays
lon = N.array([3.625, 4.625])  # example longitude array
lat = N.array([41.435, 42.435])  # example latitude array

# Iterate over the combinations without using an index variable
for (x_val, y_val) in xy:
    idx = N.where(lon == x_val)[0][0]  # accessing longitude directly
    idy = N.where(lat == y_val)[0][0]  # accessing latitude directly

    # Print or use idx and idy as needed
    print(f'Index for longitude {x_val}: {idx}, Index for latitude {y_val}: {idy}')
