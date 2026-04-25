
import math
import numpy as np

# Your list of radius values
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
# Your list of angle pairs
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Convert angles to a numpy array (optional; you can keep them as a list)
angles = np.asarray(angles)
xylist = []

# Iterate over each angle pair
for angle_pair in angles:
    for angle in angle_pair:
        # Create a new list for the calculated x, y values
        meq = []
        for radius in r:  # Iterate over each value in r
            meq.append((radius * math.cos(math.radians(angle)), radius * math.sin(math.radians(angle))))
        xylist.extend(meq)  # Add the resulting pairs to xylist

print(xylist)
