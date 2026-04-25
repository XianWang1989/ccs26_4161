
import math
import numpy as np

# Define your radius values
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
# Define your angles as tuples
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

xylist = []

# Iterate over each pair of angles
for angle_pair in angles:
    for angle in angle_pair:
        # Iterate over each value in r
        for radius in r:
            # Calculate x and y using the radius and angle
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            # Append the result as a tuple to xylist
            xylist.append((x, y))

# Print the results
print(xylist)
