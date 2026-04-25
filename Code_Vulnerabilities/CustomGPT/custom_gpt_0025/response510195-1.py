
import math
import numpy as np

# Define the radius values and angles
r = [0.0, 0.01, 0.0, 0.35, 0.98, 0.001, 0.0]
angles = [(0.0, 0.01), (0.0, 0.35), (0.98, 0.001), (0.0, 0.0), (0.01, 0.0), (0.35, 0.98), (0.001, 0.0)]
angles = np.asarray(angles)

# Initialize list to hold results
xylist = []

# Iterate through each angle pair
for angle_pair in angles:
    for r_value in r:
        # Calculate the cosine and sine products
        x = r_value * math.cos(math.radians(angle_pair[0]))
        y = r_value * math.sin(math.radians(angle_pair[1]))
        # Append the results as a tuple
        xylist.append((x, y))

# Print the results
print(xylist)
