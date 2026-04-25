
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Convert angles to a numpy array
angles = np.asarray(angles)
xylist = []

# Iterate over angles and values of r
for angle_pair in angles:
    for r_value in r:
        # Calculate the x and y coordinates
        x = r_value * (math.cos(math.radians(angle_pair[0])))
        y = r_value * (math.sin(math.radians(angle_pair[1])))
        # Append the result as a tuple
        xylist.append((x, y))

print(xylist)
