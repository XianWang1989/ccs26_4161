
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)
xylist = []

# Iterate through each angle pair in angles
for angle_pair in angles:
    for angle in angle_pair:
        for radius in r:
            # Perform the calculations for each radius at this angle
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            xylist.append((x, y))

print(xylist)
