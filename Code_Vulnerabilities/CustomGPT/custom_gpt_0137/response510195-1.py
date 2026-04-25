
import math
import numpy as np

# Define the radius list and the angles as tuples
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

# Initialize the xylist to hold the results
xylist = []

# Iterate over each angle pair and radius
for angle_pair in angles:
    for r_value in r:
        # Calculate x and y using cosine and sine for the given radius and angle
        x = r_value * math.cos(math.radians(angle_pair[0]))
        y = r_value * math.sin(math.radians(angle_pair[1]))
        # Append the results as a tuple
        xylist.append((x, y))

# Print the resulting xylist
print(xylist)
