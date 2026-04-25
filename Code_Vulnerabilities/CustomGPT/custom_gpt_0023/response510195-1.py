
import math
import numpy as np

# Define variables
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

xylist = []

# Loop through angles and multiply by each value in r
for angle_pair in angles:
    for r_value in r:
        x = r_value * math.cos(math.radians(angle_pair[0]))
        y = r_value * math.sin(math.radians(angle_pair[1]))
        xylist.append((x, y))

# Print the result
print(xylist)
