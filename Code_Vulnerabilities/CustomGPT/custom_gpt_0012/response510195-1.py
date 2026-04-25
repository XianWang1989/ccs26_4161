
import math
import numpy as np

r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

xylist = []

# Iterate over each angle pair
for angle_pair in angles:
    for x in angle_pair:
        # Calculate the cosine and sine for each angle
        cos_val = math.cos(math.radians(x))
        sin_val = math.sin(math.radians(x))

        # Multiply each radius value by the cosine and sine
        for radius in r:
            meq = [radius * cos_val, radius * sin_val]
            xylist.append(meq)

print(xylist)
