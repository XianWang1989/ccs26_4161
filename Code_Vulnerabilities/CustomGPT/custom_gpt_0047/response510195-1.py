
import math
import numpy as np

# Your lists
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)
xylist = []

# Iterate through each angle tuple
for angle_pair in angles:
    for angle in angle_pair:
        # Multiply each value in r by the cosine and sine of the angle
        for radius in r:
            meq = (radius * math.cos(math.radians(angle)), radius * math.sin(math.radians(angle)))
            xylist.append(meq)

print(xylist)
