
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

xylist = []

# Iterate over angles
for angle_pair in angles:
    # For each angle in the pair
    for angle in angle_pair:
        # Calculate the products for each value of r
        for radius in r:
            meq = [radius * math.cos(math.radians(angle)), radius * math.sin(math.radians(angle))]
            xylist.append(meq)

print(xylist)
