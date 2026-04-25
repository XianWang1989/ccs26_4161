
import math
import numpy as np

# Your data
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Convert angles into a NumPy array
angles = np.asarray(angles)
xylist = []

# Iterate through angles
for angle_pair in angles:
    for r_value in r:
        # Calculate x and y for each angle with the current r_value
        x = r_value * math.cos(math.radians(angle_pair[0]))
        y = r_value * math.sin(math.radians(angle_pair[1]))
        xylist.append((x, y))

# Print the resulting list of (x, y) coordinates
print(xylist)
