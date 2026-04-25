
import math
import numpy as np

# Define the lists
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Convert angles to a NumPy array (if needed)
angles = np.asarray(angles)

# Initialize xylist
xylist = []

# Iterate over each angle pair
for angle_pair in angles:
    for r_value in r:
        # Calculate x and y using the current r value and angle
        x = r_value * math.cos(math.radians(angle_pair[0]))
        y = r_value * math.sin(math.radians(angle_pair[1]))
        xylist.append((x, y))

# Print the results
print(xylist)
