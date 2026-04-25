
import math
import numpy as np

# Define the lists
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]

# Convert angles to a numpy array
angles = np.asarray(angles)

# Initialize the list to store results
xylist = []

# Loop through each angle pair and each r value
for angle_pair in angles:
    for r_value in r:
        # Calculate the x and y components
        x = r_value * math.cos(math.radians(angle_pair[0]))
        y = r_value * math.sin(math.radians(angle_pair[1]))
        xylist.append((x, y))

# Print the results
print(xylist)
