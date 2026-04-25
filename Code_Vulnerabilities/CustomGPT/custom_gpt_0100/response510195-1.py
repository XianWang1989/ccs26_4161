
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)
xylist = []

# Iterate over angles
for angle_tuple in angles:
    for r_value in r:
        x = r_value * math.cos(math.radians(angle_tuple[0]))
        y = r_value * math.sin(math.radians(angle_tuple[1]))
        xylist.append((x, y))

print(xylist)
