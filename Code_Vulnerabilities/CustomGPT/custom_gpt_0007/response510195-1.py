
import math
import numpy as np

# Define the radii and angles
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

xylist = []

# Loop over each angle pair
for angle_pair in angles:
    for r_value in r:
        # Calculate the x and y coordinates based on the angle and radius
        x = r_value * math.cos(math.radians(angle_pair[0]))
        y = r_value * math.sin(math.radians(angle_pair[1]))
        xylist.append((x, y))

print(xylist)
