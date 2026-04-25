
import math
import numpy as np

# Values for r and angles
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Convert angles to numpy array if necessary
angles = np.asarray(angles)

# List to store results
xylist = []

# Iterate over each angle pair
for angle_pair in angles:
    for angle in angle_pair:
        for radius in r:
            # Calculate coordinates for each radius and angle
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            xylist.append((x, y))

# Print the results
print(xylist)
