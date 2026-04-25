
import math
import numpy as np

# Given lists of radii and angles
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

# Prepare a list to store the output
xylist = []

# Iterate over each angle pair
for angle_pair in angles:
    for angle in angle_pair:
        # Create an empty result list for current angles
        meq = []

        # Iterate over each radius
        for radius in r:
            meq.append((radius * math.cos(math.radians(angle)), radius * math.sin(math.radians(angle))))

        # Append the current angle's results to xylist
        xylist.extend(meq)

# Print the computed xylist
print(xylist)
