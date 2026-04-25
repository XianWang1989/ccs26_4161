
import math
import numpy as np

# Define r and angles
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Convert angles to a numpy array
angles = np.asarray(angles)
xylist = []

# Iterate through each angle and calculate products
for angle_pair in angles:
    for angle in angle_pair:
        for radius in r:
            # Calculate the x and y coordinates
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            xylist.append((x, y))

# Print the result
print(xylist)
