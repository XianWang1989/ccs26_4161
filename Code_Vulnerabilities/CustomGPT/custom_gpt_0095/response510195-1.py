
import math
import numpy as np

# Your data
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

xylist = []
for i in angles:
    for angle in i:
        for radius in r:
            meq = (radius * math.cos(math.radians(angle)), radius * math.sin(math.radians(angle)))
            xylist.append(meq)

print(xylist)
