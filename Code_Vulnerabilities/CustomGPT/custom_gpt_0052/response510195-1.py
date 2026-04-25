
import math
import numpy as np

# Define the radius list and angles
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Convert angles to a numpy array (though not strictly necessary here)
angles = np.asarray(angles)

xylist = []

# Iterate through each angle pair
for angle_pair in angles:
    for r_value in r:
        # Calculate x and y using the angle and corresponding radius
        x = r_value * math.cos(math.radians(angle_pair[0]))
        y = r_value * math.sin(math.radians(angle_pair[1]))
        xylist.append((x, y))

print(xylist)
