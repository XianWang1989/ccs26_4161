
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

xylist = []
for angle_pair in angles:
    for angle in angle_pair:
        # Iterate over values in r
        for value in r:
            x = value * math.cos(math.radians(angle))
            y = value * math.sin(math.radians(angle))
            xylist.append((x, y))

print(xylist)
