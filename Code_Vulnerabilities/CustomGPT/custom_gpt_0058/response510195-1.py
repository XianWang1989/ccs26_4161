
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)
xylist = []

# Iterate over each angle tuple
for angle_pair in angles:
    for angle in angle_pair:
        for radius in r:  # Iterate over each value in the list r
            meq = [
                radius * math.cos(math.radians(angle)), 
                radius * math.sin(math.radians(angle))
            ]
            xylist.append(meq)

print(xylist)
