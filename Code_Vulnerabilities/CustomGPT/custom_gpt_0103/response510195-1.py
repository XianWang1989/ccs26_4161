
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

xylist = []

for angle_pair in angles:
    angle1, angle2 = angle_pair
    for value in r:
        x_value = value * math.cos(math.radians(angle1))
        y_value = value * math.sin(math.radians(angle2))
        xylist.append((x_value, y_value))

print(xylist)
