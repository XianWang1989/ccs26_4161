
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

xylist = []
for angle in angles:
    for value in r:
        # Calculate using only the current angle and current value of r
        meq = [value * math.cos(math.radians(angle[0])), value * math.sin(math.radians(angle[1]))]
        xylist.append(meq)

print(xylist)
