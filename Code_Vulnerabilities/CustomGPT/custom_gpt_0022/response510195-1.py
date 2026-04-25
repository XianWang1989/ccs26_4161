
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)
xylist = []

for angle_pair in angles:
    for angle in angle_pair:
        for r_value in r:
            x_value = r_value * math.cos(math.radians(angle))
            y_value = r_value * math.sin(math.radians(angle))
            xylist.append((x_value, y_value))

print(xylist)
