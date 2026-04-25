
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)
xylist = []

for i in angles:
    for x in i:
        for value in r:
            # Calculate x and y using each value from r
            meq = [value * math.cos(math.radians(x)), value * math.sin(math.radians(x))]
            xylist.append(meq)

print(xylist)
