
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

xylist = []
for angle_pair in angles:
    for radius in r:
        x = radius * math.cos(math.radians(angle_pair[0]))
        y = radius * math.sin(math.radians(angle_pair[1]))
        xylist.append((x, y))

print(xylist)
