
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

xylist = []

# Iterate over angles and r
for angle_pair in angles:
    for r_value in r:
        for angle in angle_pair:
            x = r_value * math.cos(math.radians(angle))
            y = r_value * math.sin(math.radians(angle))
            xylist.append((x, y))

print(xylist)
