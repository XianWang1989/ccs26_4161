
import math
import numpy as np

# Define your lists of floats
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

# Initialize xylist to store the results
xylist = []

# Iterate over each angle pair
for angle_pair in angles:
    for angle in angle_pair:
        # Now iterate over each r value
        for radius in r:
            # Calculate the x and y coordinates
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))

            # Append the result as a tuple to xylist
            xylist.append((x, y))

# Print the resulting xylist
print(xylist)
