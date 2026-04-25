
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

angles = np.asarray(angles)
xylist = []

for angle_tuple in angles:
    for angle in angle_tuple:
        for radius in r:
            # Calculate the x and y coordinates for each radius and angle
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            xylist.append((x, y))

print(xylist)
