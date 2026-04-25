
import math
import numpy as np

# Original list of r values
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Convert angles to a NumPy array (if necessary)
angles = np.asarray(angles)

xylist = []

# Iterate over each pair of angles
for angle_pair in angles:
    for angle in angle_pair:
        # Iterate over each radius value in r
        for radius in r:
            # Calculate the x and y coordinates
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            # Append the results as a tuple (x, y) to xylist
            xylist.append((x, y))

print(xylist)
