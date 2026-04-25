
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

xylist = []

# Iterate over each angle pair
for angle_pair in angles:
    for r_val in r:
        x = r_val * math.cos(math.radians(angle_pair[0]))
        y = r_val * math.sin(math.radians(angle_pair[1]))
        xylist.append((x, y))

print(xylist)
