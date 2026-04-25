
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

xylist = []
# Use enumerate to get index for r
for i, angle_pair in enumerate(angles):
    for angle in angle_pair:
        # Multiply each value in r[i] with the cosine and sine of the angle
        x = r[i] * math.cos(math.radians(angle))
        y = r[i] * math.sin(math.radians(angle))
        xylist.append((x, y))  # Append the tuple of (x, y) coordinates

print(xylist)
