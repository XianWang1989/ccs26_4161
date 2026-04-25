
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

xylist = []

for radius in r:
    for angle in angles:
        x = radius * math.cos(math.radians(angle[0]))
        y = radius * math.sin(math.radians(angle[1]))
        xylist.append((x, y))

print(xylist)
