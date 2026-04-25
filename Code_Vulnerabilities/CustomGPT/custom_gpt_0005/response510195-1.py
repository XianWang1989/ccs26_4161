
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

xylist = []
for angle_pair in angles:
    for r_value in r:
        for x in angle_pair:
            meq = (r_value * math.cos(math.radians(x)), r_value * math.sin(math.radians(x)))
            xylist.append(meq)

print(xylist)
