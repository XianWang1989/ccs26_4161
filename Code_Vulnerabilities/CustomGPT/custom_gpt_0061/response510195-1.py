
import math
import numpy as np

# Given lists
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Convert angles to a NumPy array for convenience
angles = np.asarray(angles)
xylist = []

# Loop through each angle pair
for angle_pair in angles:
    for angle in angle_pair:
        for radius in r:
            # Calculate the x and y coordinates
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            meq = (x, y)
            xylist.append(meq)

print(xylist)
