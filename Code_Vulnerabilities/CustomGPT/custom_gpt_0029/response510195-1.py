
import math
import numpy as np

# Define the radius values and angles
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

xylist = []
# Iterate over each angle pair
for angle_pair in angles:
    for angle in angle_pair:
        # Create a temporary list to hold calculated values
        meq = []
        for radius in r:
            meq.append((radius * math.cos(math.radians(angle)), radius * math.sin(math.radians(angle))))
        xylist.extend(meq)

print(xylist)
