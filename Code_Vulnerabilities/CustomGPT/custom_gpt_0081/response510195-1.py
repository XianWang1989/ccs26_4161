
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

xylist = []
for angle in angles:
    for value in r:
        # Multiply the current value of r with the cosine and sine of the first and second angle respectively
        meq = [value * math.cos(math.radians(angle[0])), value * math.sin(math.radians(angle[1]))]
        xylist.append(meq)

print(xylist)
