
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

xylist = []
for angle_pair in angles:
    for x in angle_pair:
        for value in r:
            # Calculate the x and y coordinates based on the angle and radius
            x_coord = value * math.cos(math.radians(x))
            y_coord = value * math.sin(math.radians(x))
            xylist.append((x_coord, y_coord))

print(xylist)
