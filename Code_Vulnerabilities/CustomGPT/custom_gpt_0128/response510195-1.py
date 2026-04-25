
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)
xylist = []

# Iterate through angles and corresponding r values
for i in range(len(angles)):
    for x in angles[i]:
        meq = [r[i] * math.cos(math.radians(x)), r[i] * math.sin(math.radians(x))]
        xylist.append(meq)

print(xylist)
