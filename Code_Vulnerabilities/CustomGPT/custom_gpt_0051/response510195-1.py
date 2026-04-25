
import math
import numpy as np

# Your original lists
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Convert angles to numpy array
angles = np.asarray(angles)
xylist = []

# Iterate through angles
for angle in angles:
    for radius in r:
        x = radius * math.cos(math.radians(angle[0]))
        y = radius * math.sin(math.radians(angle[1]))
        xylist.append((x, y))

print(xylist)
