
import math
import numpy as np

# Your values
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

# Prepare the result list
xylist = []

# Iterate over each angle pair
for angle_pair in angles:
    for angle in angle_pair:
        # Create a list to store results for this specific angle
        meq = []
        # Multiply each r value by the cosine and sine of the angle
        for value in r:
            meq.append(value * math.cos(math.radians(angle)))
            meq.append(value * math.sin(math.radians(angle)))
        # Append the results for this pair of angles
        xylist.append(meq)

# Print the results
print(xylist)
