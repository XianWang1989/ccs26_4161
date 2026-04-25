
import math
import numpy as np

# Define radius list and angles
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Convert angles to a numpy array for easier indexing
angles = np.asarray(angles)

# Initialize result list
xylist = []

# Iterate over each radius and corresponding angle pair
for angle_pair in angles:
    for radius in r:
        # Calculate the x and y coordinates
        x = radius * math.cos(math.radians(angle_pair[0]))
        y = radius * math.sin(math.radians(angle_pair[1]))
        # Append the result as a tuple
        xylist.append((x, y))

print(xylist)
