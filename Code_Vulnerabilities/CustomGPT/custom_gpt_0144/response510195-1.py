import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

xylist = []

for i in angles:
    for x in i:
        # Multiply each value of r with the cosine and sine of the angle
        meq = [(val * math.cos(math.radians(x)), val * math.sin(math.radians(x))) for val in r]
        xylist.append(meq)

print(xylist)
